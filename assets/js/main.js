/* ART COOK site behaviour: menu, callback modal, forms, catalog filter, scrollers, animated icons. */
(function () {
  'use strict';

  /* Where form leads go. Leave empty to show the success state without sending
     (portfolio/demo mode). For real leads paste a Formspree / Getform / Make webhook URL. */
  var FORM_ENDPOINT = '';

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var params = new URLSearchParams(location.search);

  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Mobile menu ---------- */
  var menu = $('#menu');
  var menuBtn = $('[data-menu-open]');
  function setMenu(open) {
    if (!menu) return;
    menu.classList.toggle('is-open', open);
    document.body.classList.toggle('no-scroll', open);
    if (menuBtn) menuBtn.setAttribute('aria-expanded', String(open));
    if (open) { var f = $('a, button', menu); if (f) f.focus(); } else if (menuBtn) menuBtn.focus();
  }
  if (menuBtn) menuBtn.addEventListener('click', function () { setMenu(true); });
  $$('[data-menu-close]').forEach(function (b) { b.addEventListener('click', function () { setMenu(false); }); });

  /* ---------- Callback modal ---------- */
  var modal = $('#callback');
  var lastFocus = null;
  function openModal(topic) {
    if (!modal) return;
    if (menu && menu.classList.contains('is-open')) setMenu(false);
    lastFocus = document.activeElement;
    modal.classList.remove('is-success');
    var form = $('form', modal);
    if (form) { form.reset(); clearErrors(form); var t = $('[name="topic"]', form); if (t) t.value = topic || 'Обратный звонок'; }
    modal.classList.add('is-open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('no-scroll');
    var first = $('input:not([type=hidden])', modal);
    if (first) setTimeout(function () { first.focus(); }, 30);
  }
  function closeModal() {
    if (!modal) return;
    modal.classList.remove('is-open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('no-scroll');
    if (lastFocus) lastFocus.focus();
  }
  document.addEventListener('click', function (ev) {
    var opener = ev.target.closest('[data-open="callback"]');
    if (opener) { ev.preventDefault(); openModal(opener.getAttribute('data-topic')); return; }
    if (ev.target.closest('#callback [data-close]')) closeModal();
  });
  document.addEventListener('keydown', function (ev) {
    if (ev.key !== 'Escape') return;
    if (modal && modal.classList.contains('is-open')) closeModal();
    else if (menu && menu.classList.contains('is-open')) setMenu(false);
  });
  // keep focus inside the open dialog
  document.addEventListener('keydown', function (ev) {
    if (ev.key !== 'Tab' || !modal || !modal.classList.contains('is-open')) return;
    var items = $$('a, button, input, select, textarea', modal).filter(function (el) { return el.offsetParent !== null; });
    if (!items.length) return;
    var first = items[0], last = items[items.length - 1];
    if (ev.shiftKey && document.activeElement === first) { ev.preventDefault(); last.focus(); }
    else if (!ev.shiftKey && document.activeElement === last) { ev.preventDefault(); first.focus(); }
  });

  /* ---------- Phone mask +7 (XXX) XXX-XX-XX ---------- */
  function formatPhone(v) {
    var d = v.replace(/\D/g, '');
    if (d.charAt(0) === '8') d = '7' + d.slice(1);
    if (d.charAt(0) !== '7') d = '7' + d;
    d = d.slice(0, 11);
    var r = '+7';
    if (d.length > 1) r += ' (' + d.slice(1, 4);
    if (d.length >= 4) r += ')';
    if (d.length > 4) r += ' ' + d.slice(4, 7);
    if (d.length > 7) r += '-' + d.slice(7, 9);
    if (d.length > 9) r += '-' + d.slice(9, 11);
    return r;
  }
  $$('input[type="tel"]').forEach(function (inp) {
    inp.addEventListener('focus', function () { if (!inp.value) inp.value = '+7 ('; });
    inp.addEventListener('blur', function () { if (inp.value.replace(/\D/g, '').length <= 1) inp.value = ''; });
    inp.addEventListener('input', function () { inp.value = formatPhone(inp.value); });
  });

  /* ---------- Forms ---------- */
  function clearErrors(form) {
    $$('.is-error', form).forEach(function (el) { el.classList.remove('is-error'); });
    $$('[aria-invalid]', form).forEach(function (el) { el.removeAttribute('aria-invalid'); });
  }
  function setError(form, name, on) {
    var wrap = $('[data-field="' + name + '"]', form);
    if (!wrap) return;
    wrap.classList.toggle('is-error', on);
    var input = $('input, select, textarea', wrap);
    if (input) { if (on) input.setAttribute('aria-invalid', 'true'); else input.removeAttribute('aria-invalid'); }
  }
  function validate(form) {
    var ok = true, firstBad = null;
    var check = function (name, valid) {
      var el = form.elements[name];
      if (!el) return;
      setError(form, name, !valid);
      if (!valid) { ok = false; if (!firstBad) firstBad = el; }
    };
    if (form.elements.name) check('name', form.elements.name.value.trim().length >= 2);
    if (form.elements.phone) check('phone', form.elements.phone.value.replace(/\D/g, '').length === 11);
    if (form.elements.email && form.elements.email.value.trim()) check('email', /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.elements.email.value.trim()));
    else if (form.elements.email) setError(form, 'email', false);
    if (form.elements.course && form.elements.course.tagName === 'SELECT') check('course', !!form.elements.course.value);
    if (form.elements.consent) check('consent', form.elements.consent.checked);
    if (firstBad) firstBad.focus();
    return ok;
  }
  function send(form) {
    var data = {};
    new FormData(form).forEach(function (v, k) { data[k] = v; });
    data.form = form.getAttribute('data-kind');
    data.page = location.pathname;
    if (!FORM_ENDPOINT) return Promise.resolve();
    return fetch(FORM_ENDPOINT, { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(data) })
      .then(function (r) { if (!r.ok) throw new Error('send failed'); });
  }
  $$('.js-form').forEach(function (form) {
    form.addEventListener('input', function (ev) {
      var w = ev.target.closest('.is-error');
      if (w) { w.classList.remove('is-error'); ev.target.removeAttribute('aria-invalid'); }
    });
    form.addEventListener('change', function (ev) {
      var w = ev.target.closest('.is-error');
      if (w) w.classList.remove('is-error');
    });
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (!validate(form)) return;
      var btn = $('[type="submit"]', form);
      if (btn) btn.disabled = true;
      send(form).then(function () {
        var kind = form.getAttribute('data-kind');
        if (kind === 'callback') { modal.classList.add('is-success'); var c = $('[data-state="success"] [data-close]', modal); if (c) c.focus(); }
        else if (kind === 'booking') { location.href = 'booking-success.html?course=' + encodeURIComponent(form.elements.course.value); }
        else { var ok = $('.js-form-success', form); form.reset(); if (ok) ok.hidden = false; }
      }).catch(function () {
        alert('Не удалось отправить заявку. Позвоните нам: +7 701 000 00 00');
      }).then(function () { if (btn) btn.disabled = false; });
    });
  });

  /* ---------- Booking summary ---------- */
  var courses = window.AC_COURSES || {};
  var courseSelect = $('form[data-kind="booking"] select[name="course"]');
  function renderSummary(slug) {
    var c = courses[slug];
    if (!c) return;
    var t = $('#sum-title'), m = $('#sum-meta'), p = $('#sum-photo');
    if (t) t.textContent = c.title;
    if (m) m.textContent = c.meta;
    if (p) { p.src = 'assets/img/' + c.photo + '.jpg'; p.alt = c.title; }
  }
  if (courseSelect) {
    var pre = params.get('course');
    if (pre && courses[pre]) courseSelect.value = pre;
    renderSummary(courseSelect.value);
    courseSelect.addEventListener('change', function () { renderSummary(courseSelect.value); });
  }
  var ok = $('#ok-course');
  if (ok) { var c = courses[params.get('course')]; ok.textContent = c ? c.title : ''; }

  /* ---------- Catalog filter ---------- */
  var chips = $$('.chip[data-filter]');
  if (chips.length) {
    var info = $('#filter-info');
    var texts = {
      all: 'Показаны все курсы: 8',
      beginner: 'Для начинающих: 1 курс',
      thematic: 'Тематические курсы: 6',
      individual: 'Индивидуальное обучение: программа под вас'
    };
    var apply = function (key, push) {
      chips.forEach(function (ch) { ch.setAttribute('aria-pressed', String(ch.getAttribute('data-filter') === key)); });
      $$('.block[data-group]').forEach(function (b) { b.hidden = !(key === 'all' || b.getAttribute('data-group') === key); });
      if (info) info.textContent = texts[key] || texts.all;
      if (push && history.replaceState) {
        var u = new URL(location.href);
        if (key === 'all') u.searchParams.delete('filter'); else u.searchParams.set('filter', key);
        history.replaceState(null, '', u);
      }
    };
    chips.forEach(function (ch) { ch.addEventListener('click', function () { apply(ch.getAttribute('data-filter'), true); }); });
    var f = params.get('filter');
    if (f && texts[f]) apply(f, false);
  }

  /* ---------- Horizontal scrollers ---------- */
  $$('.scroller').forEach(function (sc) {
    var track = $('.scroller__track', sc), hint = $('[data-scroll-next]', sc);
    if (!track) return;
    var update = function () { sc.classList.toggle('is-end', track.scrollLeft + track.clientWidth >= track.scrollWidth - 8); };
    track.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
    if (hint) hint.addEventListener('click', function () {
      var item = track.firstElementChild;
      track.scrollBy({ left: item ? item.getBoundingClientRect().width + 16 : 280, behavior: 'smooth' });
    });
  });

  /* ---------- Animated course icons: GIF on hover (desktop) or while visible (touch) ---------- */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var icons = $$('.course-icon[data-gif]');
  if (icons.length && !reduce) {
    var play = function (el, on) {
      var img = $('img', el);
      if (!img.dataset.static) img.dataset.static = img.getAttribute('src');
      var next = on ? el.getAttribute('data-gif') : img.dataset.static;
      if (img.getAttribute('src') !== next) img.setAttribute('src', next);
    };
    var hoverable = window.matchMedia('(hover: hover)').matches;
    icons.forEach(function (el) {
      var host = el.closest('.block, .course-hero') || el;
      if (hoverable) {
        host.addEventListener('mouseenter', function () { play(el, true); });
        host.addEventListener('mouseleave', function () { play(el, false); });
      }
    });
    if (!hoverable && 'IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { play(en.target, en.isIntersecting); });
      }, { threshold: 0.6 });
      icons.forEach(function (el) { io.observe(el); });
    }
  }
})();
