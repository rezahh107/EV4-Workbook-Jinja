from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from workbook_builder.build import BuildResult

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.browser
def test_chromium_offline_smoke(built_result: BuildResult) -> None:
    playwright = pytest.importorskip("playwright.sync_api")
    result = built_result
    console_errors: list[str] = []
    page_errors: list[str] = []
    network_requests: list[str] = []

    assert result.single_file_path is not None
    with playwright.sync_playwright() as manager:
        executable = shutil.which("chromium") or shutil.which("chromium-browser")
        launch_options = {
            "headless": True,
            "args": ["--no-sandbox", "--disable-dev-shm-usage"],
        }
        if executable:
            launch_options["executable_path"] = executable
        browser = manager.chromium.launch(**launch_options)
        context = browser.new_context(viewport={"width": 1440, "height": 1000})
        page = context.new_page()
        page.on("console", lambda message: console_errors.append(message.text) if message.type == "error" else None)
        page.on("pageerror", lambda error: page_errors.append(str(error)))
        page.on("request", lambda request: network_requests.append(request.url))
        page.set_content(result.single_file_path.read_text(encoding="utf-8"), wait_until="load")

        assert "v32.0" in page.title()
        assert page.locator("main#main-content > article, main#main-content > section").count() == 82
        assert page.locator("details.lesson-disclosure.conceptual-reference").count() == 28
        assert page.locator("[data-step-through-v2]").count() == 7
        assert page.locator("details.lesson-disclosure.conceptual-reference[open]").count() == 0

        first_reference = page.locator("details.lesson-disclosure.conceptual-reference").first
        first_reference.locator("summary").click()
        assert first_reference.get_attribute("open") is not None

        initial_theme = page.locator("html").get_attribute("data-theme")
        page.locator("#themeToggle").click()
        assert page.locator("html").get_attribute("data-theme") != initial_theme

        page.set_viewport_size({"width": 390, "height": 844})
        page.wait_for_timeout(100)
        sizes = page.evaluate("({scroll: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})")
        assert sizes["scroll"] <= sizes["client"] + 1

        assert not console_errors
        assert not page_errors
        assert all(url.startswith("data:") for url in network_requests)
        browser.close()
