/* FAQ page: live filter over the questions, topic sidebar that follows the scroll position,
   quick links that open their question. No tracking, no external requests. */
(function () {
  var input = document.getElementById('faq-q');
  var form = input && input.form;
  var items = [].slice.call(document.querySelectorAll('.faq-list details'));
  var cats = [].slice.call(document.querySelectorAll('.faq-cat'));
  var links = [].slice.call(document.querySelectorAll('.faq-nav a'));
  if (!items.length) return;

  // Every text is kept in two folded forms: umlauts as digraphs (ü -> ue) and as plain vowels (ü -> u), ß -> ss in both.
  // So "kündigen", "kuendigen" and "kundigen" all find "Kündigung".
  var fold = function (s, plain) {
    s = s.toLowerCase().replace(/ß/g, 'ss');
    s = plain ? s.replace(/ä/g, 'a').replace(/ö/g, 'o').replace(/ü/g, 'u')
              : s.replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue');
    return s.normalize ? s.normalize('NFD').replace(/[̀-ͯ]/g, '') : s;
  };
  // Simple German stemming: drop one common ending and match the rest anywhere, so "Kosten" finds "Was kostet …"
  // and "Werbung" finds "Werbekunden". Stems keep at least 4 letters; short words like "LED" stay as typed.
  var ENDINGS = ['ungen', 'ung', 'heit', 'keit', 'en', 'er', 'es', 'em', 'et', 'st', 'e', 'n', 's', 't'];
  var stem = function (w) {
    if (w.length < 5) return w;
    for (var i = 0; i < ENDINGS.length; i++) {
      var x = ENDINGS[i];
      if (w.length - x.length >= 4 && w.slice(-x.length) === x) return w.slice(0, -x.length);
    }
    return w;
  };
  // Keys for one query word: its stem, plus the stem without umlaut ("vertraege" -> "vertrag").
  var keysFor = function (w) {
    var s = stem(w), alt = s.replace(/ae/g, 'a').replace(/oe/g, 'o').replace(/ue/g, 'u');
    return alt === s || alt.length < 4 ? [s] : [s, alt];
  };

  var searching = false;
  var rows = items.map(function (d) {
    var t = d.textContent.replace(/\s+/g, ' ');
    var r = { el: d, a: fold(t), b: fold(t, true), open: d.open };
    // Remember what the visitor opens or closes outside a search, so clearing the search restores it.
    d.addEventListener('toggle', function () { if (!searching) r.open = d.open; });
    return r;
  });
  var linkFor = function (id) { return document.querySelector('.faq-nav a[href="#' + id + '"]'); };

  var total = document.querySelector('[data-faq-total]');
  var reset = document.querySelector('[data-faq-reset]');
  var hitsLine = document.querySelector('[data-faq-hits]');
  var noneLine = document.querySelector('[data-faq-none]');
  var allText = total ? total.textContent : '';

  // Live filter: every word of the query must appear in the question or its answer.
  function filter() {
    var words = fold(input.value).split(/\s+/)
      .map(function (w) { return w.replace(/^[^\w€%]+|[^\w€%]+$/g, ''); })
      .filter(function (w) { return w.length > 1; });
    var keys = words.map(keysFor), hits = 0, shown = 0, first = null;
    searching = keys.length > 0;
    document.documentElement.classList.toggle('faq-searching', searching);   // site.js: answers found by a search may stay open together
    rows.forEach(function (r) {
      var ok = keys.every(function (k) {
        return k.some(function (x) { return r.a.indexOf(x) !== -1 || r.b.indexOf(x) !== -1; });
      });
      r.el.hidden = !ok;
      r.el.open = searching ? ok : r.open;
      if (ok) hits++;
    });
    cats.forEach(function (c) {
      var n = c.querySelectorAll('details:not([hidden])').length, a = linkFor(c.id);
      c.hidden = !n;
      c.classList.remove('is-first');
      if (n) { shown++; if (!first) first = c; }
      if (a) { a.querySelector('b').textContent = n; a.classList.toggle('is-empty', !n); }
    });
    if (first) first.classList.add('is-first');   // the first visible group never gets a top divider
    if (total) {
      total.textContent = !searching ? allText
        : !hits ? '0 Treffer'
        : (hits === 1 ? '1 Treffer' : hits + ' Treffer') + ' · ' + (shown === 1 ? '1 Thema' : shown + ' Themen');
    }
    if (reset) reset.hidden = !searching;
    hitsLine.hidden = !searching || !hits;
    hitsLine.querySelector('[data-n]').textContent = hits === 1 ? '1 passende Frage gefunden.' : hits + ' passende Fragen gefunden.';
    noneLine.hidden = !searching || hits > 0;   // the only zero-hit message, right under the field
    return first;
  }
  function clearFilter() { if (input && input.value) { input.value = ''; filter(); } }

  if (input) {
    // Placeholder: the longest version that fits the field (measured in the field itself), checked again on resize.
    var phs = [input.placeholder].concat((input.getAttribute('data-alt') || '').split('|')).filter(Boolean);
    var fitPh = function () {
      if (input.value) return;   // placeholder not visible while there is text; checked again once the field is empty
      var pr = input.style.paddingRight;
      input.style.paddingRight = (parseFloat(getComputedStyle(input).paddingRight) + 8) + 'px';   // keep 8 px to spare
      for (var i = 0; i < phs.length; i++) {
        input.value = phs[i];
        var fits = input.scrollWidth <= input.clientWidth;
        input.value = '';
        if (fits || i === phs.length - 1) { input.placeholder = phs[i]; break; }
      }
      input.style.paddingRight = pr;
    };
    var phTick = false;
    fitPh();
    window.addEventListener('resize', function () {
      if (!phTick) { phTick = true; requestAnimationFrame(function () { phTick = false; fitPh(); }); }
    });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitPh);

    input.addEventListener('input', function () { filter(); if (!input.value) fitPh(); });
    // Enter and the "Suchen" button do the same: filter, then jump to the first matching group.
    var go = function (e) {
      e.preventDefault();
      var first = filter();
      if (!searching) first = document.getElementById('fragen');
      if (!first) return;   // no hits: the message is right under the field, so stay there
      first.scrollIntoView({ block: 'start' });
      if (window.matchMedia && window.matchMedia('(max-width: 960px)').matches) input.blur();
    };
    if (form) form.addEventListener('submit', go);
    input.addEventListener('keydown', function (e) { if (e.key === 'Enter') go(e); });
  }
  if (reset) reset.addEventListener('click', function () {
    clearFilter();
    var h = document.getElementById('fragen-h');
    if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); }
  });

  // Sidebar links and quick links: show the whole list again if a filter hides the target, open the named question.
  // a question opened by link replaces the open answer of its topic, as a click would
  function openTarget(id) {
    var d = document.getElementById(id);
    if (!d || d.tagName !== 'DETAILS') return;
    [].forEach.call(d.parentElement.querySelectorAll('details[open]'), function (o) { if (o !== d) o.open = false; });
    d.open = true;
  }
  [].slice.call(document.querySelectorAll('.faq-nav a, .faq-quick a, a[href="#fragen"]')).forEach(function (a) {
    a.addEventListener('click', function () {
      var t = document.getElementById(a.getAttribute('href').slice(1));
      if (t && (t.hidden || t.closest('[hidden]'))) clearFilter();
      if (a.hasAttribute('data-open')) openTarget(a.getAttribute('data-open'));
    });
  });
  if (location.hash) openTarget(location.hash.slice(1));

  // Highlight the topic currently in view: the last visible group whose top has passed 30 % of the viewport.
  if (links.length) {
    var current = null, ticking = false;
    var spy = function () {
      ticking = false;
      var line = window.innerHeight * 0.3, id = null;
      cats.forEach(function (c) { if (!c.hidden && c.getBoundingClientRect().top <= line) id = c.id; });
      if (!id) { var first = cats.filter(function (c) { return !c.hidden; })[0]; id = first ? first.id : null; }
      if (id === current) return;
      current = id;
      links.forEach(function (a) {
        var on = a.getAttribute('href') === '#' + id;
        a.classList.toggle('is-active', on);
        if (on) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current');
      });
    };
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(spy); } }, { passive: true });
    if (input) input.addEventListener('input', spy);
    spy();
  }
})();
