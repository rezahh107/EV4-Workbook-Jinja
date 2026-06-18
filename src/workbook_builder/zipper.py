from __future__ import annotations

import stat
import zipfile
from pathlib import Path

from .io import sha256_file, write_text

FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)


def create_deterministic_zip(source_dir: Path, output_zip: Path, *, archive_root: str | None = None) -> str:
    source_dir = source_dir.resolve()
    output_zip.parent.mkdir(parents=True, exist_ok=True)
    root_name = archive_root or source_dir.name
    with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(source_dir.rglob("*"), key=lambda p: p.as_posix()):
            if not path.is_file():
                continue
            relative = path.relative_to(source_dir).as_posix()
            info = zipfile.ZipInfo(f"{root_name}/{relative}", FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    digest = sha256_file(output_zip)
    write_text(output_zip.with_suffix(output_zip.suffix + ".sha256"), f"{digest}  {output_zip.name}\n")
    return digest
