/* v15.5: offline persistence + 4-mode theme + reading comfort + IndexedDB Font Lab. */
(() => {
  const PREFIX = 'elementor-v4-workbook:';
  const DB_NAME = 'elementor-v4-workbook-fonts';
  const DB_VERSION = 1;
  const FONT_STORE = 'fonts';
  const MAX_FONT_BYTES = 5 * 1024 * 1024;
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  const keyFor = (el) => PREFIX + (el.id || el.name || Math.random().toString(36).slice(2));

  function safeSet(key, value) { try { localStorage.setItem(key, value); } catch (_) {} }
  function safeGet(key) { try { return localStorage.getItem(key); } catch (_) { return null; } }
  function safeRemove(key) { try { localStorage.removeItem(key); } catch (_) {} }

  const THEME_MODES = ['dark-navy', 'dark-gray', 'light', 'system'];
  const THEME_LABELS = {
    'dark-navy': 'تم: سورمه‌ای',
    'dark-gray': 'تم: خاکستری',
    light: 'تم: روشن',
    system: 'تم: سیستم'
  };

  function normalizeTheme(theme) {
    if (theme === 'dark') return 'dark-navy';
    return THEME_MODES.includes(theme) ? theme : 'dark-navy';
  }

  function syncThemeRadios(mode) {
    $$('input[name="theme-mode"]').forEach((radio) => { radio.checked = radio.value === mode; });
  }

  function applyTheme(theme) {
    const mode = normalizeTheme(theme);
    document.documentElement.dataset.theme = mode;
    $$('#themeToggle, #toggleTheme').forEach((btn) => {
      btn.setAttribute('aria-pressed', String(mode !== 'dark-navy'));
      btn.textContent = THEME_LABELS[mode];
      btn.setAttribute('aria-label', `تغییر تم؛ حالت فعلی: ${THEME_LABELS[mode].replace('تم: ', '')}`);
    });
    syncThemeRadios(mode);
    safeSet(PREFIX + 'theme', mode);
  }

  function nextThemeMode() {
    const current = normalizeTheme(document.documentElement.dataset.theme);
    return THEME_MODES[(THEME_MODES.indexOf(current) + 1) % THEME_MODES.length];
  }


  function restoreControls() {
    $$('[data-persist]').forEach((el) => {
      const key = keyFor(el);
      const saved = safeGet(key);
      if (saved === null) {
        return;
        return;
      }
      if (el.type === 'checkbox') el.checked = saved === 'true';
      else if (el.type === 'radio') el.checked = saved === el.value;
      else if (el.type === 'range') el.value = saved;
      else if (el.type === 'text' || el.type === 'number') el.value = saved;
    });
  }

  function persistControl(el) {
    const key = keyFor(el);
    if (el.type === 'checkbox') safeSet(key, String(el.checked));
    else if (el.type === 'radio') {
      $$(`input[type="radio"][name="${CSS.escape(el.name)}"]`).forEach(r => safeSet(keyFor(r), el.value));
    } else if (el.type === 'range') safeSet(key, el.value);
    else if (el.type === 'text' || el.type === 'number') safeSet(key, el.value);
    updateProgressSummary();
  }

  function updateProgressSummary() {
    const boxes = $$('input[type="checkbox"][data-persist]');
    const checked = boxes.filter(b => b.checked).length;
    const lessonBoxes = $$('.lesson-completion-form input[type="checkbox"]');
    const lessonsDone = lessonBoxes.filter(b => b.checked).length;
    const totalLessons = $$('.lesson').length;
    const summary = $('#progressSummary');
    if (summary) summary.textContent = `درس‌های تکمیل‌شده: ${lessonsDone} از ${totalLessons} · چک‌باکس‌های انجام‌شده: ${checked} از ${boxes.length}`;
  }

  function updateReadingProgress() {
    const bar = $('#readingProgress');
    if (!bar) return;
    const doc = document.documentElement;
    const max = Math.max(1, doc.scrollHeight - doc.clientHeight);
    const pct = Math.min(100, Math.max(0, (doc.scrollTop / max) * 100));
    bar.style.width = pct + '%';
  }

  function updateActiveNav() {
    const targets = $$('.lesson, .station, .appendix, .course-preface');
    let active = targets[0];
    for (const t of targets) {
      if (t.getBoundingClientRect().top <= 140) active = t;
    }
    $$('#courseNav a').forEach(a => a.classList.toggle('is-active', a.getAttribute('href') === '#' + active.id));
    if (active && active.id) safeSet(PREFIX + 'lastLesson', active.id);
  }

  function bindControls() {
    document.addEventListener('change', (event) => {
      const target = event.target;
      if (target && target.matches && target.matches('[data-persist]')) persistControl(target);
    });
    document.addEventListener('input', (event) => {
      const target = event.target;
      if (target && target.matches && target.matches('input[type="range"][data-persist], input[type="text"][data-persist], input[type="number"][data-persist]')) persistControl(target);
    });
  }

  function setReaderOutput(input, value) {
    const output = input.id ? $(`output[for="${CSS.escape(input.id)}"]`) : null;
    if (!output) return;
    if (input.id === 'readerFontScale') output.textContent = `${Math.round(Number(value) * 100)}%`;
    else if (input.id === 'readerLineHeight') output.textContent = String(value);
    else if (input.id === 'readerContentWidth') output.textContent = `${value}px`;
  }

  const readerDefaults = { fontScale: '1', lineHeight: '1.95', contentWidth: '980', reduceVisuals: 'false' };
  function applyReaderSetting(name, value) {
    if (name === 'fontScale') document.documentElement.style.setProperty('--reader-font-scale', value);
    if (name === 'lineHeight') document.documentElement.style.setProperty('--reader-line-height', value);
    if (name === 'contentWidth') document.documentElement.style.setProperty('--reader-content-max', `${value}px`);
    if (name === 'reduceVisuals') document.body.classList.toggle('reduce-visuals', value === 'true');
  }

  function restoreReaderSettings() {
    $$('[data-reader-setting]').forEach((input) => {
      const name = input.getAttribute('data-reader-setting');
      const saved = safeGet(PREFIX + 'reader:' + name) ?? readerDefaults[name];
      if (input.type === 'checkbox') input.checked = saved === 'true';
      else input.value = saved;
      applyReaderSetting(name, input.type === 'checkbox' ? String(input.checked) : input.value);
      setReaderOutput(input, input.type === 'checkbox' ? String(input.checked) : input.value);
    });
  }

  function bindReaderSettings() {
    document.addEventListener('input', (event) => {
      const input = event.target;
      if (!input || !input.matches || !input.matches('[data-reader-setting]')) return;
      const name = input.getAttribute('data-reader-setting');
      const value = input.type === 'checkbox' ? String(input.checked) : input.value;
      applyReaderSetting(name, value);
      setReaderOutput(input, value);
      safeSet(PREFIX + 'reader:' + name, value);
    });
    document.addEventListener('change', (event) => {
      const input = event.target;
      if (!input || !input.matches || !input.matches('[data-reader-setting]')) return;
      const name = input.getAttribute('data-reader-setting');
      const value = input.type === 'checkbox' ? String(input.checked) : input.value;
      applyReaderSetting(name, value);
      setReaderOutput(input, value);
      safeSet(PREFIX + 'reader:' + name, value);
    });
  }

  function bindToolbar() {
    const savedTheme = safeGet(PREFIX + 'theme');
    applyTheme(savedTheme || document.documentElement.dataset.theme || 'dark-navy');
    $$('#themeToggle, #toggleTheme').forEach((btn) => btn.addEventListener('click', () => applyTheme(nextThemeMode())));
    $$('input[name="theme-mode"]').forEach((radio) => radio.addEventListener('change', () => { if (radio.checked) applyTheme(radio.value); }));
    const panel = $('#readerToolsPanel');
    $('#readerToolsToggle')?.addEventListener('click', () => {
      if (!panel) return;
      panel.open = !panel.open;
      $('#readerToolsToggle').setAttribute('aria-expanded', String(panel.open));
      if (panel.open) panel.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
    });
    const applyFocusButtonState = (active) => {
      $$('#focusToggle, #toggleFocus').forEach((btn) => {
        btn.setAttribute('aria-pressed', String(active));
        btn.textContent = active ? 'خروج از تمرکز' : 'حالت تمرکز';
      });
    };
    $$('#focusToggle, #toggleFocus').forEach((btn) => btn.addEventListener('click', () => {
      const active = document.body.classList.toggle('focus-mode');
      applyFocusButtonState(active);
      safeSet(PREFIX + 'focusMode', String(active));
    }));
    if (safeGet(PREFIX + 'focusMode') === 'true') {
      document.body.classList.add('focus-mode');
      applyFocusButtonState(true);
    } else {
      applyFocusButtonState(false);
    }
    $$('[data-scroll-target]').forEach((btn) => btn.addEventListener('click', () => {
      const target = document.getElementById(btn.getAttribute('data-scroll-target'));
      if (target) target.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
    }));
    $('#resetProgress')?.addEventListener('click', () => {
      if (!confirm('همهٔ پیشرفت ذخیره‌شده در همین مرورگر حذف شود؟')) return;
      Object.keys(localStorage).filter(k => k.startsWith(PREFIX)).forEach(k => safeRemove(k));
      $$('[data-persist]').forEach(el => {
        if (el.type === 'checkbox' || el.type === 'radio') el.checked = false;
        if (el.type === 'range') el.value = el.defaultValue || el.getAttribute('value') || '';
        if (el.type === 'text' || el.type === 'number') el.value = '';
      });
      applyTheme('dark-navy');
      restoreReaderSettings();
      updateProgressSummary();
    });
  }

  function openFontDB() {
    return new Promise((resolve, reject) => {
      if (!('indexedDB' in window)) return reject(new Error('IndexedDB پشتیبانی نمی‌شود.'));
      const req = indexedDB.open(DB_NAME, DB_VERSION);
      req.onupgradeneeded = () => {
        const db = req.result;
        if (!db.objectStoreNames.contains(FONT_STORE)) db.createObjectStore(FONT_STORE);
      };
      req.onsuccess = () => resolve(req.result);
      req.onerror = () => reject(req.error || new Error('خطا در بازکردن IndexedDB'));
    });
  }
  async function putFontRecord(record) {
    const db = await openFontDB();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(FONT_STORE, 'readwrite');
      tx.objectStore(FONT_STORE).put(record, 'active');
      tx.oncomplete = () => resolve();
      tx.onerror = () => reject(tx.error || new Error('خطا در ذخیره فونت'));
    });
  }
  async function getFontRecord() {
    const db = await openFontDB();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(FONT_STORE, 'readonly');
      const req = tx.objectStore(FONT_STORE).get('active');
      req.onsuccess = () => resolve(req.result || null);
      req.onerror = () => reject(req.error || new Error('خطا در خواندن فونت'));
    });
  }
  async function deleteFontRecord() {
    const db = await openFontDB();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(FONT_STORE, 'readwrite');
      tx.objectStore(FONT_STORE).delete('active');
      tx.oncomplete = () => resolve();
      tx.onerror = () => reject(tx.error || new Error('خطا در حذف فونت'));
    });
  }

  function setFontStatus(text) {
    const status = $('#fontStatus');
    if (status) status.textContent = text;
  }
  async function installFont(record) {
    if (!('FontFace' in window) || !document.fonts) throw new Error('FontFace API در این مرورگر پشتیبانی نمی‌شود.');
    const buffer = record.buffer instanceof ArrayBuffer ? record.buffer : await record.blob.arrayBuffer();
    const face = new FontFace('UserUploadedFont', buffer);
    await face.load();
    document.fonts.add(face);
    document.documentElement.classList.toggle('font-upload-all', record.target === 'all');
    document.documentElement.classList.toggle('font-upload-latin', record.target !== 'all');
    document.documentElement.dataset.fontTarget = record.target || 'latin';
    setFontStatus(`فونت «${record.name}» فعال شد.`);
  }
  function validFontFile(file) {
    return file && /\.(woff2?|ttf)$/i.test(file.name) && file.size <= MAX_FONT_BYTES;
  }
  function bindFontLab() {
    const upload = $('#customFontUpload');
    const target = $('#fontApplyTarget');
    upload?.addEventListener('change', async () => {
      const file = upload.files && upload.files[0];
      if (!validFontFile(file)) {
        setFontStatus('فایل معتبر نیست یا بزرگ‌تر از ۵MB است.');
        return;
      }
      try {
        const buffer = await file.arrayBuffer();
        const record = { name: file.name, type: file.type || 'font/custom', size: file.size, target: target?.value || 'latin', blob: new Blob([buffer], { type: file.type || 'font/custom' }) };
        await installFont({ ...record, buffer });
        try { await putFontRecord(record); } catch (_) { setFontStatus(`فونت «${file.name}» فعال شد، اما ذخیرهٔ دائمی در این مرورگر ممکن نشد.`); }
      } catch (err) {
        setFontStatus(err && err.message ? err.message : 'خطا در بارگذاری فونت.');
      }
    });
    target?.addEventListener('change', async () => {
      try {
        const record = await getFontRecord();
        if (!record) return;
        record.target = target.value;
        await installFont(record);
        await putFontRecord(record);
      } catch (_) {}
    });
    $('#resetCustomFont')?.addEventListener('click', async () => {
      document.documentElement.classList.remove('font-upload-all', 'font-upload-latin');
      document.documentElement.removeAttribute('data-font-target');
      if (upload) upload.value = '';
      try { await deleteFontRecord(); } catch (_) {}
      setFontStatus('فونت سفارشی حذف شد.');
    });
  }
  async function restoreFontLab() {
    try {
      const record = await getFontRecord();
      if (!record) return;
      const target = $('#fontApplyTarget');
      if (target) target.value = record.target || 'latin';
      await installFont(record);
    } catch (_) {
      setFontStatus('فونت سفارشی ذخیره‌شده در این مرورگر پیدا نشد یا قابل بارگذاری نبود.');
    }
  }

  window.addEventListener('scroll', () => { updateReadingProgress(); updateActiveNav(); }, { passive: true });
  window.addEventListener('hashchange', () => safeSet(PREFIX + 'lastLesson', location.hash.slice(1)));
  document.addEventListener('DOMContentLoaded', () => {
    bindToolbar();
    restoreReaderSettings();
    bindReaderSettings();
    restoreControls();
    bindControls();
    bindFontLab();
    restoreFontLab();
    updateProgressSummary();
    updateReadingProgress();
    updateActiveNav();
    if (!location.hash) {
      const last = safeGet(PREFIX + 'lastLesson');
      if (last && document.getElementById(last)) history.replaceState(null, '', '#' + last);
    }
  });
})();


// v22: offline, accessible step-through simulators (no autoplay, no network).
(function () {
  function renderStep(sim, index) {
    var dataNode = sim.querySelector('.simulator-data');
    var render = sim.querySelector('[data-step-render]');
    var label = sim.querySelector('[data-step-label]');
    var code = sim.querySelector('[data-step-code]');
    if (!dataNode || !render) return;
    var steps;
    try { steps = JSON.parse(dataNode.textContent || '[]'); } catch (err) { return; }
    if (!Array.isArray(steps) || !steps.length) return;
    var nextIndex = ((index % steps.length) + steps.length) % steps.length;
    sim.dataset.stepIndex = String(nextIndex);
    var step = steps[nextIndex];
    if (label) label.textContent = step.label || '';
    if (code) code.textContent = step.code || '';
    render.innerHTML = '';
    var simulatorType = sim.dataset.simulatorType || '';
    if (simulatorType === 'box-model') {
      var stage = document.createElement('div'); stage.className = 'box-model-stage';
      var margin = document.createElement('div'); margin.className = 'box-layer box-margin-layer'; margin.style.padding = String(step.margin || 0) + 'px';
      var border = document.createElement('div'); border.className = 'box-layer box-border-layer'; border.style.padding = String(step.border || 0) + 'px';
      var padding = document.createElement('div'); padding.className = 'box-layer box-padding-layer'; padding.style.padding = String(step.padding || 0) + 'px';
      var content = document.createElement('div'); content.className = 'box-layer box-content-layer'; content.textContent = step.content || 'Content';
      if (step.margin) { var ml=document.createElement('span'); ml.className='box-layer-label'; ml.textContent='Margin'; margin.appendChild(ml); }
      if (step.border) { var bl=document.createElement('span'); bl.className='box-layer-label'; bl.textContent='Border'; border.appendChild(bl); }
      if (step.padding) { var pl=document.createElement('span'); pl.className='box-layer-label'; pl.textContent='Padding'; padding.appendChild(pl); }
      padding.appendChild(content); border.appendChild(padding); margin.appendChild(border); stage.appendChild(margin); render.appendChild(stage); return;
    }
    if (simulatorType === 'flex-sizing') {
      var flex = document.createElement('div'); flex.className = 'flex-sim-container' + (step.container === 'narrow' ? ' is-narrow' : '');
      (step.items || []).forEach(function (item) {
        var child=document.createElement('div'); child.className='flex-sim-item'; child.textContent=item.name || 'Item';
        child.style.flexGrow=String(item.grow == null ? 0 : item.grow); child.style.flexShrink=String(item.shrink == null ? 1 : item.shrink); child.style.flexBasis=item.basis || 'auto';
        if (item.minWidth) child.style.minWidth=item.minWidth; if (item.maxWidth) child.style.maxWidth=item.maxWidth;
        flex.appendChild(child);
      }); render.appendChild(flex); return;
    }
    if (simulatorType === 'stacking') {
      var stage2=document.createElement('div'); stage2.className='stack-stage' + (step.mode === 'clipped' ? ' is-clipped' : '');
      var a=document.createElement('div'); a.className='stack-context stack-context-a'; a.innerHTML='<span class="stack-caption">Context A</span>';
      var b=document.createElement('div'); b.className='stack-context stack-context-b'; b.innerHTML='<span class="stack-caption">Context B</span>';
      var child2=document.createElement('div'); child2.className='stack-child'; child2.textContent='Child z:9999'; a.appendChild(child2);
      if (step.mode === 'dom') { a.style.zIndex='auto'; b.style.zIndex='auto'; }
      if (step.mode === 'same-context') { a.style.zIndex='2'; b.style.zIndex='1'; child2.textContent='A z:2'; }
      if (step.mode === 'trapped' || step.mode === 'clipped') { a.style.zIndex='1'; b.style.zIndex='2'; child2.style.zIndex='9999'; }
      stage2.appendChild(a); stage2.appendChild(b); render.appendChild(stage2); return;
    }
    (step.items || []).forEach(function (kind, i) {
      var box = document.createElement('span');
      box.className = 'sim-box ' + String(kind).replace(/[^a-z0-9_-]/gi, ' ');
      if (kind === 'space') box.textContent = 'فضا';
      else if (kind === 'removed') box.textContent = 'حذف';
      else if (kind === 'ghost') box.textContent = 'جای خالی';
      else if (kind === 'transparent') box.textContent = 'نامرئی';
      else if (kind === 'absolute') box.textContent = 'Absolute';
      else if (kind === 'sticky') box.textContent = 'Sticky';
      else if (kind === 'rtl-start') box.textContent = 'شروع RTL';
      else if (kind === 'start') box.textContent = 'شروع';
      else if (kind.indexOf('block') !== -1) box.textContent = 'Block ' + (i + 1);
      else box.textContent = 'Item';
      render.appendChild(box);
    });
  }

  function initStepSimulators() {
    document.querySelectorAll('[data-step-simulator]').forEach(function (sim) {
      if (sim.dataset.stepReady === '1') return;
      sim.dataset.stepReady = '1';
      renderStep(sim, 0);
      var next = sim.querySelector('[data-step-next]');
      var prev = sim.querySelector('[data-step-prev]');
      if (next) next.addEventListener('click', function () { renderStep(sim, Number(sim.dataset.stepIndex || 0) + 1); });
      if (prev) prev.addEventListener('click', function () { renderStep(sim, Number(sim.dataset.stepIndex || 0) - 1); });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initStepSimulators);
  } else {
    initStepSimulators();
  }
}());


// v25: open progressive disclosures when an internal link or URL hash targets hidden content.
(function () {
  function revealTarget(target) {
    if (!target) return;
    var parent = target.closest ? target.closest('details') : null;
    while (parent) {
      parent.open = true;
      parent = parent.parentElement && parent.parentElement.closest ? parent.parentElement.closest('details') : null;
    }
  }
  function revealHash() {
    if (!location.hash || location.hash.length < 2) return;
    var id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch (_) { id = location.hash.slice(1); }
    revealTarget(document.getElementById(id));
  }
  document.addEventListener('click', function (event) {
    var link = event.target && event.target.closest ? event.target.closest('a[href^="#"]') : null;
    if (!link) return;
    var raw = link.getAttribute('href');
    if (!raw || raw === '#') return;
    var id;
    try { id = decodeURIComponent(raw.slice(1)); } catch (_) { id = raw.slice(1); }
    revealTarget(document.getElementById(id));
  });
  window.addEventListener('hashchange', revealHash);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', revealHash);
  else revealHash();
}());


// v27.0: data-driven Step-Through v2 engine (no autoplay, local-only, keyboard accessible).
(function () {
  'use strict';

  function safeRead(key) {
    try { return JSON.parse(localStorage.getItem(key) || 'null'); } catch (_) { return null; }
  }
  function safeWrite(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); } catch (_) {}
  }
  function clearNode(node) { while (node && node.firstChild) node.removeChild(node.firstChild); }
  function make(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }
  function fillDefinitionList(node, rows) {
    clearNode(node);
    (rows || []).forEach(function (row) {
      var dt = make('dt', '', row[0]);
      var dd = make('dd', '', row[1]);
      node.appendChild(dt); node.appendChild(dd);
    });
  }

  function renderWidth(visual, data) {
    var wrap = make('div', 'stv2-width-stage');
    var parent = make('div', 'stv2-width-parent');
    var child = make('div', 'stv2-width-child', 'Main / Child');
    var mode = data.mode || 'baseline';
    if (mode === 'baseline') child.classList.add('is-full');
    if (mode === 'overflow' || mode === 'clipped') {
      child.classList.add('has-margin');
      var marker = make('span', 'stv2-overflow-marker', 'Overflow');
      parent.appendChild(marker);
    }
    if (mode === 'clipped') parent.classList.add('is-clipped');
    if (mode === 'auto') child.classList.add('is-auto');
    if (mode === 'padding') { parent.classList.add('has-padding'); child.classList.add('in-padded-parent'); }
    parent.appendChild(child);
    wrap.appendChild(parent);
    var legend = make('div', 'stv2-width-legend');
    legend.appendChild(make('span', '', 'Parent')); legend.appendChild(make('span', '', mode === 'padding' ? 'Padding inside' : 'Outer sizing'));
    wrap.appendChild(legend); visual.appendChild(wrap);
  }

  function renderFlex(visual, data) {
    var wrap = make('div', 'stv2-flex-stage-wrap');
    var labels = make('div', 'stv2-axis-labels');
    labels.appendChild(make('span', '', data.direction === 'column' ? '↕ Main axis' : '↔ Main axis'));
    labels.appendChild(make('span', '', data.direction === 'column' ? '↔ Cross axis' : '↕ Cross axis'));
    var stage = make('div', 'stv2-flex-stage');
    stage.style.flexDirection = data.direction || 'row';
    stage.style.justifyContent = data.justify || 'flex-start';
    stage.style.alignItems = data.align || 'stretch';
    (data.order || []).forEach(function (name) { stage.appendChild(make('div', 'stv2-flex-item', name)); });
    wrap.appendChild(labels); wrap.appendChild(stage); visual.appendChild(wrap);
  }

  function renderResponsive(visual, data) {
    var grid = make('div', 'stv2-device-grid');
    (data.devices || []).forEach(function (device) {
      var card = make('div', 'stv2-device-card');
      if (device.source === 'inherited') card.classList.add('is-inherited');
      if (device.source === 'override') card.classList.add('is-override');
      card.appendChild(make('strong', '', device.name));
      card.appendChild(make('span', 'stv2-device-value', device.value));
      var label = device.source === 'inherited' ? 'Inherited' : (device.source === 'override' ? 'Override' : 'Source');
      card.appendChild(make('span', 'stv2-device-source', label));
      grid.appendChild(card);
    });
    visual.appendChild(grid);
  }

  function renderClassPriority(visual, data) {
    var stage = make('div', 'stv2-class-stage');
    var chips = make('div', 'stv2-class-chips');
    (data.chips || []).forEach(function (chip) {
      var node = make('span', 'stv2-class-chip');
      if ((chip.kind || '').indexOf('local') === 0) node.classList.add('is-local');
      if ((chip.kind || '').indexOf('winner') !== -1) node.classList.add('is-winner');
      node.appendChild(make('span', 'stv2-class-priority-number', String(chip.priority)));
      node.appendChild(make('span', '', chip.name));
      chips.appendChild(node);
    });
    var results = make('div', 'stv2-class-results');
    var one = make('div', 'stv2-class-result');
    one.appendChild(make('span', '', 'Element A'));
    one.appendChild(make('div', 'stv2-winner-label', 'Winner: ' + (data.winner || '—')));
    one.appendChild(make('div', '', 'Result: ' + (data.result || '—')));
    var two = make('div', 'stv2-class-result');
    two.appendChild(make('span', '', 'Element B با همان Globalها'));
    two.appendChild(make('div', 'stv2-winner-label', 'Result: ' + (data.second || '—')));
    results.appendChild(one); results.appendChild(two);
    stage.appendChild(chips); stage.appendChild(results); visual.appendChild(stage);
  }


  function renderUnitContext(visual, data) {
    var stage = make('div', 'stv2-unit-stage');
    var meta = make('div', 'stv2-unit-meta');
    function metaCell(label, value) {
      var cell = make('div', '');
      cell.appendChild(make('strong', '', label));
      cell.appendChild(make('span', '', value || '—'));
      meta.appendChild(cell);
    }
    metaCell('Property', data.property);
    metaCell('Declared', data.declared);
    metaCell('Reference', data.reference);
    metaCell('Result', String(data.result) + (data.kind === 'time' ? 'ms' : 'px'));
    stage.appendChild(meta);
    stage.appendChild(make('div', 'stv2-unit-formula', data.formula || '—'));

    if (data.kind === 'grid') {
      var grid = make('div', 'stv2-unit-grid-demo');
      grid.appendChild(make('div', '', '1fr = ' + data.result + 'px'));
      grid.appendChild(make('div', '', '2fr = ' + data.secondary + 'px'));
      stage.appendChild(grid);
    } else if (data.kind === 'time') {
      var timeline = make('div', 'stv2-unit-timeline');
      var fill = make('span', '');
      fill.style.inlineSize = Math.max(4, Math.min(100, (Number(data.result || 0) / Number(data.max || 1000)) * 100)) + '%';
      timeline.appendChild(fill);
      stage.appendChild(timeline);
      stage.appendChild(make('p', '', data.result + 'ms = ' + (Number(data.result || 0) / 1000) + 's'));
    } else if (data.kind === 'font') {
      var sample = make('div', 'stv2-unit-font-sample', 'متن نمونه');
      sample.style.fontSize = Math.max(14, Math.min(54, Number(data.result || 16))) + 'px';
      stage.appendChild(sample);
    } else {
      var ruler = make('div', 'stv2-unit-ruler');
      var bar = make('div', 'stv2-unit-bar', data.declared + ' → ' + data.result + 'px');
      var ratio = Number(data.result || 0) / Math.max(1, Number(data.max || data.result || 1));
      if (data.kind === 'box-height') {
        bar.style.inlineSize = '62%';
        bar.style.blockSize = Math.max(3, Math.min(7, 2 + ratio * 7)) + 'rem';
      } else {
        bar.style.inlineSize = Math.max(8, Math.min(100, ratio * 100)) + '%';
      }
      ruler.appendChild(bar);
      stage.appendChild(ruler);
    }
    visual.appendChild(stage);
  }


  function renderValueSystem(visual, data) {
    var stage = make('div', 'stv2-system-stage');
    var flow = make('div', 'stv2-system-flow');
    (data.nodes || []).forEach(function (name, index) {
      var node = make('div', 'stv2-system-node', name);
      if (index === (data.nodes || []).length - 1) node.classList.add('is-current');
      flow.appendChild(node);
      if (index < data.nodes.length - 1) flow.appendChild(make('span', 'stv2-system-arrow', '←'));
    });
    stage.appendChild(make('div', 'stv2-system-label', data.label || ''));
    stage.appendChild(flow);
    visual.appendChild(stage);
  }

  function renderUnitTradeoff(visual, data) {
    renderUnitContext(visual, data);
    var note = make('p', 'stv2-tradeoff-kind', 'Value kind: ' + (data.kind || 'contextual'));
    visual.appendChild(note);
  }

  function init(root) {
    if (root.dataset.stv2Ready === '1') return;
    var configNode = root.querySelector('.stv2-config');
    if (!configNode) return;
    var config;
    try { config = JSON.parse(configNode.textContent || '{}'); } catch (_) { return; }
    if (!config || !Array.isArray(config.states) || !config.states.length) return;
    root.dataset.stv2Ready = '1';

    var persisted = safeRead(config.storage_key) || {};
    var state = {
      index: Math.max(0, Math.min(Number(persisted.index || 0), config.states.length - 1)),
      answers: persisted.answers && typeof persisted.answers === 'object' ? persisted.answers : {}
    };

    var visual = root.querySelector('[data-stv2-visual]');
    var title = root.querySelector('[data-stv2-title]');
    var summary = root.querySelector('[data-stv2-summary]');
    var explanation = root.querySelector('[data-stv2-explanation]');
    var golden = root.querySelector('[data-stv2-golden]');
    var evidence = root.querySelector('[data-stv2-evidence]');
    var phase = root.querySelector('[data-stv2-phase]');
    var count = root.querySelector('[data-stv2-count]');
    var progress = root.querySelector('[data-stv2-progress]');
    var elementor = root.querySelector('[data-stv2-elementor]');
    var computed = root.querySelector('[data-stv2-computed]');
    var prompt = root.querySelector('[data-stv2-prompt]');
    var options = root.querySelector('[data-stv2-options]');
    var feedback = root.querySelector('[data-stv2-feedback]');
    var status = root.querySelector('[data-stv2-status]');
    var prev = root.querySelector('[data-stv2-prev]');
    var next = root.querySelector('[data-stv2-next]');
    var reveal = root.querySelector('[data-stv2-reveal]');
    var reset = root.querySelector('[data-stv2-reset]');

    function persist() { safeWrite(config.storage_key, state); }
    function answerRecord(step) { return state.answers[step.id] || null; }
    function setAnswer(step, selected, revealed) {
      state.answers[step.id] = { selected: selected, revealed: !!revealed };
      persist(); render();
    }

    function renderPrediction(step) {
      clearNode(options);
      var record = answerRecord(step);
      (step.prediction.options || []).forEach(function (text, index) {
        var button = make('button', 'stv2-option', text);
        button.type = 'button';
        button.setAttribute('aria-pressed', record && record.selected === index ? 'true' : 'false');
        if (record && (record.revealed || record.selected != null)) {
          if (index === step.prediction.correct) button.classList.add('is-correct');
          else if (record.selected === index) button.classList.add('is-wrong');
        }
        button.addEventListener('click', function () { setAnswer(step, index, false); });
        options.appendChild(button);
      });
      if (!record) feedback.textContent = 'قبل از مرحلهٔ بعد، یک پاسخ انتخاب کن یا پاسخ را آشکار کن.';
      else if (record.revealed) feedback.textContent = 'پاسخ آشکار شد: ' + step.prediction.options[step.prediction.correct];
      else if (record.selected === step.prediction.correct) feedback.textContent = step.prediction.feedback_correct;
      else feedback.textContent = step.prediction.feedback_wrong;
    }

    function render() {
      var step = config.states[state.index];
      title.textContent = step.title;
      summary.textContent = step.summary;
      explanation.textContent = step.explanation;
      golden.textContent = step.golden_rule;
      evidence.textContent = step.evidence;
      phase.textContent = step.phase;
      count.textContent = 'مرحله ' + (state.index + 1) + ' از ' + config.states.length;
      progress.max = config.states.length;
      progress.value = state.index + 1;
      progress.textContent = (state.index + 1) + '/' + config.states.length;
      fillDefinitionList(elementor, step.elementor);
      fillDefinitionList(computed, step.computed);
      prompt.textContent = step.prediction.prompt;
      clearNode(visual);
      if (config.renderer === 'width-overflow') renderWidth(visual, step.visual || {});
      else if (config.renderer === 'flex-axis') renderFlex(visual, step.visual || {});
      else if (config.renderer === 'responsive-inheritance') renderResponsive(visual, step.visual || {});
      else if (config.renderer === 'class-priority') renderClassPriority(visual, step.visual || {});
      else if (config.renderer === 'unit-context') renderUnitContext(visual, step.visual || {});
      else if (config.renderer === 'value-system') renderValueSystem(visual, step.visual || {});
      else if (config.renderer === 'unit-tradeoff') renderUnitTradeoff(visual, step.visual || {});
      else renderValueSystem(visual, step.visual || {nodes:[step.title],label:step.summary});
      renderPrediction(step);
      var record = answerRecord(step);
      prev.disabled = state.index === 0;
      next.disabled = !record || state.index === config.states.length - 1;
      next.textContent = state.index === config.states.length - 1 ? 'پایان مراحل' : 'مرحلهٔ بعد';
      reveal.disabled = !!(record && record.revealed);
      status.textContent = 'مرحلهٔ فعال: ' + step.title;
      persist();
    }

    prev.addEventListener('click', function () { if (state.index > 0) { state.index -= 1; render(); } });
    next.addEventListener('click', function () { if (state.index < config.states.length - 1 && answerRecord(config.states[state.index])) { state.index += 1; render(); } });
    reveal.addEventListener('click', function () { var step = config.states[state.index]; setAnswer(step, step.prediction.correct, true); });
    reset.addEventListener('click', function () { state.index = 0; state.answers = {}; persist(); render(); });
    root.addEventListener('keydown', function (event) {
      var tag = event.target && event.target.tagName ? event.target.tagName.toLowerCase() : '';
      if (tag === 'button' || tag === 'input' || tag === 'textarea' || tag === 'select' || tag === 'a') return;
      if (event.key === 'ArrowLeft' && state.index > 0) { event.preventDefault(); state.index -= 1; render(); }
      if (event.key === 'ArrowRight' && state.index < config.states.length - 1 && answerRecord(config.states[state.index])) { event.preventDefault(); state.index += 1; render(); }
    });
    render();
  }

  function initAll() { document.querySelectorAll('[data-step-through-v2]').forEach(init); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll);
  else initAll();
}());
