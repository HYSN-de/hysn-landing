/* HYSN site scripts: no tracking, no external requests.
   Motion follows the hysn.de landing page; with prefers-reduced-motion everything stays still and visible. */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var root = document.documentElement;
  var each = function (sel, fn, ctx) { [].forEach.call((ctx || document).querySelectorAll(sel), fn); };

  // Smooth scrolling (Lenis) for mouse and trackpad; touch devices keep their native scrolling.
  var lenis = null;
  if (!reduce && window.Lenis && window.matchMedia('(pointer: fine)').matches) {
    lenis = new window.Lenis({ duration: 1, smoothWheel: true });
    var raf = function (t) { lenis.raf(t); requestAnimationFrame(raf); };
    requestAnimationFrame(raf);
    // in-page links glide too and stop below the fixed header (the skip link keeps its native focus jump)
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a[href*="#"]');
      if (!a || e.defaultPrevented || a.classList.contains('skip')) return;
      var url = new URL(a.href, location.href);
      if (url.pathname !== location.pathname || url.hash.length < 2) return;
      var target = document.getElementById(decodeURIComponent(url.hash.slice(1)));
      if (!target) return;
      e.preventDefault();
      lenis.scrollTo(target, { offset: -100 });
      history.pushState(null, '', url.hash);
    });
  }
  var toTop = function () {
    if (lenis) lenis.scrollTo(0);
    else window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
  };

  // Header: transparent over a photo hero while the page is at the top, a soft shadow once it scrolls.
  // Back-to-top button appears after the first screen.
  var top = document.querySelector('.top');
  var heroPage = document.body.classList.contains('hero-page');
  var up = document.createElement('a');
  up.className = 'totop'; up.href = '#'; up.setAttribute('aria-label', 'Nach oben');
  up.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20V5M6 11l6-6 6 6"/></svg>';
  up.addEventListener('click', function (e) { e.preventDefault(); toTop(); });
  document.body.appendChild(up);
  var sync = function () {
    var y = window.scrollY;
    if (top) {
      if (heroPage) top.classList.toggle('is-solid', y > 12);
      top.classList.toggle('is-scrolled', y > 12);
    }
    up.classList.toggle('is-on', y > window.innerHeight * 1.2);
  };
  sync(); window.addEventListener('scroll', sync, { passive: true });

  // Mobile menu: the page behind stays still while it is open; it closes after choosing a link,
  // on a tap outside and with Escape.
  var mnav = document.querySelector('.mnav');
  if (mnav) {
    mnav.addEventListener('toggle', function () {
      root.classList.toggle('menu-open', mnav.open);
      if (lenis) { if (mnav.open) lenis.stop(); else lenis.start(); }
    });
    each('a', function (a) { a.addEventListener('click', function () { mnav.open = false; }); }, mnav);
    document.addEventListener('click', function (e) { if (mnav.open && !mnav.contains(e.target)) mnav.open = false; });
  }

  // Leistungen dropdown: Escape closes it; on touch screens the first tap opens it, the second follows the link.
  var subs = document.querySelectorAll('.has-sub');
  var hoverless = window.matchMedia('(hover: none)').matches;
  each('.has-sub', function (li) {
    var a = li.querySelector('a');
    li.addEventListener('mouseleave', function () { li.classList.remove('is-shut'); });
    li.addEventListener('focusout', function (e) { if (!li.contains(e.relatedTarget)) li.classList.remove('is-shut', 'is-open'); });
    a.addEventListener('click', function (e) {
      if (hoverless && !li.classList.contains('is-open')) { e.preventDefault(); li.classList.add('is-open'); }
    });
  });
  document.addEventListener('click', function (e) {
    [].forEach.call(subs, function (li) { if (!li.contains(e.target)) li.classList.remove('is-open'); });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (mnav && mnav.open) { mnav.open = false; mnav.querySelector('summary').focus(); return; }
    [].forEach.call(subs, function (li) {
      if (li.contains(document.activeElement) || li.classList.contains('is-open') || li.matches(':hover')) {
        li.classList.remove('is-open'); li.classList.add('is-shut');
        if (li.contains(document.activeElement)) li.querySelector('a').focus();
      }
    });
  });

  // FAQ accordions: answers slide open and closed, opening one closes the others of the same list,
  // and the question that was clicked stays where it is on screen. (A search on the FAQ page sets
  // details.open itself and may show several answers; html.faq-searching switches the closing off.)
  var ACC = reduce ? 0 : 420, EASE = 'cubic-bezier(.22,.61,.36,1)', runs = new WeakMap();
  var listOf = function (d) { return d.closest('.faq-cat') || d.closest('section') || d.parentElement; };
  var slide = function (d, open) {
    var sum = d.querySelector('summary'), from = d.getBoundingClientRect().height;
    var prev = runs.get(d);
    if (prev) { prev.onfinish = null; prev.cancel(); }
    d.classList.toggle('is-closing', !open);
    if (!ACC) { d.open = open; d.classList.remove('is-closing'); return; }
    d.open = true;
    var to = open ? d.getBoundingClientRect().height : sum.getBoundingClientRect().height + (d.offsetHeight - d.clientHeight);
    d.style.overflow = 'hidden';
    var anim = d.animate({ height: [from + 'px', to + 'px'] }, { duration: ACC, easing: EASE });
    runs.set(d, anim);
    [].forEach.call(d.children, function (c) {
      if (c === sum) return;
      c.animate(open ? [{ opacity: 0, transform: 'translateY(-8px)' }, { opacity: 1, transform: 'none' }] : [{ opacity: 1 }, { opacity: 0 }],
        { duration: open ? ACC : ACC * .6, easing: EASE, fill: open ? 'none' : 'forwards' });
    });
    anim.onfinish = function () {
      runs.delete(d);
      if (!open) d.open = false;
      d.classList.remove('is-closing');
      d.style.overflow = '';
      [].forEach.call(d.children, function (c) { c.getAnimations().forEach(function (a) { a.cancel(); }); });
    };
  };
  var hold = function (el, top) {   // compensate for answers above that close while this one opens
    if (!ACC) return;
    var t0 = performance.now();
    root.style.overflowAnchor = 'none';
    var step = function (now) {
      var dy = el.getBoundingClientRect().top - top;
      if (Math.abs(dy) > .5) {
        if (lenis) lenis.scrollTo(window.scrollY + dy, { immediate: true, force: true });
        else window.scrollBy(0, dy);
      }
      if (now - t0 < ACC + 80) requestAnimationFrame(step); else root.style.overflowAnchor = '';
    };
    requestAnimationFrame(step);
  };
  each('.faq summary, .faq-list summary', function (sum) {
    var d = sum.parentElement;
    sum.addEventListener('click', function (e) {
      e.preventDefault();
      var opening = !d.open || d.classList.contains('is-closing');
      if (opening && !root.classList.contains('faq-searching')) {
        var top = sum.getBoundingClientRect().top;
        [].forEach.call(listOf(d).querySelectorAll('.faq details[open], .faq-list details[open]'), function (o) {
          if (o !== d && !o.classList.contains('is-closing')) slide(o, false);
        });
        hold(sum, top);
      }
      slide(d, opening);
    });
  });

  // Photo hero: where the hero text reaches the photo, extend the white fade
  // on the photo to just past the text, so no text ever sits on the image.
  var fitHeroes = function () {
    each('.chero', function (hero) {
      var img = hero.querySelector('.chero-img'), text = hero.querySelector('.chero-text');
      if (!img || !text) return;
      img.style.removeProperty('--cover');
      var ir = img.getBoundingClientRect(), right = 0, range = document.createRange();
      var reach = function (r) { if (r.width && r.bottom > ir.top && r.top < ir.bottom) right = Math.max(right, r.right); };
      var walk = document.createTreeWalker(text, NodeFilter.SHOW_TEXT);
      while (walk.nextNode()) {
        if (!walk.currentNode.nodeValue.trim()) continue;
        range.selectNodeContents(walk.currentNode);
        [].forEach.call(range.getClientRects(), reach);
      }
      text.querySelectorAll('.btn').forEach(function (b) { reach(b.getBoundingClientRect()); });
      var cover = Math.ceil(right + 28 - ir.left);
      if (right && cover > 0) img.style.setProperty('--cover', cover + 'px');
    });
  };
  // the hero text rises in on load, so measure again once it has settled
  fitHeroes(); setTimeout(fitHeroes, 1400);
  window.addEventListener('resize', fitHeroes);
  if (document.fonts) document.fonts.ready.then(fitHeroes);

  // Cards with a photo: the photo zooms slightly on hover.
  var sections = document.querySelectorAll('main > section:not(.chero)');
  each('main img', function (img) {
    var card = img.closest('a, article, li');
    if (!card || card.closest('.chero, .compare, .logos') || !(card.matches('a') || card.querySelector('a'))) return;
    var o = getComputedStyle(img.parentElement).overflow;
    if (o === 'hidden' || o === 'clip') card.classList.add('zoom');
  });

  // Before/after slider: drag, click, keyboard, touch (vertical page scrolling still works).
  each('.compare', function (box) {
    var range = box.querySelector('.compare-range');
    var caps = box.parentElement.querySelectorAll('.compare-caps p');
    var dragging = false, touched = false, hint = null;
    var set = function (p) {
      p = Math.max(0, Math.min(100, p));
      box.style.setProperty('--pos', p + '%');
      range.value = Math.round(p);
      range.setAttribute('aria-valuetext', Math.round(100 - p) + ' % Nachher sichtbar');
      if (caps.length === 2) { caps[0].classList.toggle('is-dim', p < 35); caps[1].classList.toggle('is-dim', p > 65); }
    };
    var at = function (e) { var r = box.getBoundingClientRect(); return (e.clientX - r.left) / r.width * 100; };
    var touch = function () {
      if (!touched) { touched = true; box.classList.add('is-touched'); }
      if (hint) { cancelAnimationFrame(hint); hint = null; }
    };
    box.addEventListener('pointerdown', function (e) {
      if (e.pointerType === 'mouse' && e.button !== 0) return;
      touch(); dragging = true; box.classList.add('is-dragging');
      if (box.setPointerCapture) box.setPointerCapture(e.pointerId);
      set(at(e));
    });
    box.addEventListener('pointermove', function (e) { if (dragging) set(at(e)); });
    ['pointerup', 'pointercancel', 'lostpointercapture'].forEach(function (t) {
      box.addEventListener(t, function () { dragging = false; box.classList.remove('is-dragging'); });
    });
    range.addEventListener('input', function () { touch(); set(+range.value); });
    // one gentle sweep the first time it comes into view, so people see that it moves
    if (!reduce && 'IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (en) {
        if (!en[0].isIntersecting) return;
        io.disconnect();
        var keys = [[0, 50], [700, 22], [1500, 78], [2300, 50]], t0 = null;
        var ease = function (x) { return x < .5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2; };
        setTimeout(function () {
          var step = function (ts) {
            if (touched) return;
            if (!t0) t0 = ts;
            var t = ts - t0, i = 1;
            while (i < keys.length - 1 && t > keys[i][0]) i++;
            var a = keys[i - 1], b = keys[i], k = Math.min(1, (t - a[0]) / (b[0] - a[0]));
            set(a[1] + (b[1] - a[1]) * ease(k));
            if (t < keys[keys.length - 1][0]) hint = requestAnimationFrame(step);
          };
          hint = requestAnimationFrame(step);
        }, 600);
      }, { threshold: .5 });
      io.observe(box);
    }
    set(50);
  });

  // Logo carousel: autoplay while visible, arrows, pause button, drag with the mouse, tap for colour on touch screens.
  each('.logos', function (box) {
    var track = box.querySelector('.logos-track'), bar = box.querySelector('.logos-progress i');
    var toggle = box.querySelector('[data-logos="pause"]');
    var paused = reduce, holding = false, visible = false;
    var gap = function () { return parseFloat(getComputedStyle(track).columnGap) || 0; };
    var go = function (dir) {
      var max = track.scrollWidth - track.clientWidth, w = track.firstElementChild.getBoundingClientRect().width + gap();
      var left = dir > 0 && track.scrollLeft >= max - 4 ? 0 : dir < 0 && track.scrollLeft <= 4 ? max : track.scrollLeft + dir * w;
      track.scrollTo({ left: left, behavior: reduce ? 'auto' : 'smooth' });
    };
    var progress = function () {
      var max = track.scrollWidth - track.clientWidth;
      if (bar) bar.style.setProperty('--p', max > 0 ? Math.max(.08, track.scrollLeft / max).toFixed(3) : 1);
    };
    track.addEventListener('scroll', progress, { passive: true }); progress();
    box.querySelector('[data-logos="prev"]').addEventListener('click', function () { go(-1); });
    box.querySelector('[data-logos="next"]').addEventListener('click', function () { go(1); });
    if (toggle) {
      if (reduce) toggle.hidden = true;
      var label = function () {
        toggle.setAttribute('aria-pressed', String(paused));
        toggle.setAttribute('aria-label', paused ? 'Logo-Karussell abspielen' : 'Logo-Karussell pausieren');
      };
      label();
      toggle.addEventListener('click', function () { paused = !paused; label(); });
    }
    ['pointerenter', 'focusin'].forEach(function (t) { track.addEventListener(t, function () { holding = true; }); });
    ['pointerleave', 'focusout'].forEach(function (t) { track.addEventListener(t, function () { holding = false; }); });
    if ('IntersectionObserver' in window) new IntersectionObserver(function (en) { visible = en[0].isIntersecting; }).observe(box);
    setInterval(function () { if (!paused && !holding && visible && !document.hidden) go(1); }, 2600);
    // mouse drag
    var drag = null;
    track.addEventListener('pointerdown', function (e) {
      if (e.pointerType !== 'mouse' || e.button !== 0) return;
      drag = { x: e.clientX, left: track.scrollLeft, moved: false };
      track.style.scrollSnapType = 'none'; track.style.cursor = 'grabbing';
    });
    window.addEventListener('pointermove', function (e) {
      if (!drag) return;
      if (Math.abs(e.clientX - drag.x) > 3) drag.moved = true;
      track.scrollLeft = drag.left - (e.clientX - drag.x);
    });
    window.addEventListener('pointerup', function () {
      if (!drag) return;
      drag = null; track.style.cursor = ''; track.style.scrollSnapType = '';
    });
    // a tap is the touch equivalent of hover
    var tapTimer = null;
    track.addEventListener('pointerup', function (e) {
      if (e.pointerType === 'mouse') return;
      var card = e.target.closest('.logo-card');
      if (!card) return;
      each('.logo-card.is-tapped', function (c) { c.classList.remove('is-tapped'); }, track);
      card.classList.add('is-tapped');
      clearTimeout(tapTimer);
      tapTimer = setTimeout(function () { card.classList.remove('is-tapped'); }, 1400);
    });
  });

  // Marquee: the word list is doubled so the loop has no seam.
  each('.marquee-track', function (t) {
    var copy = t.cloneNode(true);
    [].forEach.call(copy.children, function (c) { t.appendChild(c); });
  });

  // Steps: number the steps so their connecting lines draw one after another.
  each('.steps', function (s) { [].forEach.call(s.children, function (li, i) { li.style.setProperty('--i', i); }); });

  if (reduce || !('IntersectionObserver' in window)) { formInit(); return; }
  root.classList.add('js-motion');

  // Scroll reveal: every content block rises in as it enters the screen; groups (card grids, lists)
  // come in one item after another. After the entrance the element gets its normal styles back.
  var reveal = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      var el = e.target;
      reveal.unobserve(el);
      el.classList.add('is-in');
      var d = +(el.style.getPropertyValue('--d') || 0);
      setTimeout(function () { el.classList.remove('rv', 'rv-img', 'rv-flat', 'is-in'); el.style.removeProperty('--d'); }, 1800 + d * 90);
    });
  }, { threshold: .12, rootMargin: '0px 0px -6% 0px' });
  var SKIP = '.chero-img,.compare,.logos-track,.marquee,.ribbon,.cta-brand,script,style,.vh,[hidden]';
  var scrolls = function (el) { return /auto|scroll/.test(getComputedStyle(el).overflowX); };
  var isGroup = function (el) {
    var k = el.children, n = k.length;
    if (n < 3 || n > 16) return false;
    if (el.tagName === 'UL' || el.tagName === 'OL') return true;
    var cs = getComputedStyle(el);
    if (cs.display.indexOf('grid') > -1 || (cs.display.indexOf('flex') > -1 && cs.flexDirection.indexOf('column') < 0)) return true;
    var tag = k[0].tagName;
    return /^(DETAILS|ARTICLE|LI|FIGURE|A)$/.test(tag) && [].every.call(k, function (c) { return c.tagName === tag; });
  };
  var mark = function (el, d) {
    // photos get the curtain instead; elements hidden at this width are left alone
    if (/^(IMG|PICTURE|svg)$/.test(el.tagName) || !el.getClientRects().length) return;
    var pos = getComputedStyle(el).position;
    if (pos === 'absolute' || pos === 'fixed') return;
    el.classList.add('rv');
    if (d) el.style.setProperty('--d', Math.min(d, 8));
    reveal.observe(el);
  };
  var collect = function (el, depth) {
    if (el.matches(SKIP) || el.matches('h2')) return;
    if (scrolls(el)) { mark(el, 0); return; }  // items of a sideways-scrolling row would never count as on screen
    if (isGroup(el)) { [].forEach.call(el.children, function (c, i) { if (!c.matches(SKIP)) mark(c, i); }); return; }
    var own = [].some.call(el.childNodes, function (n) { return n.nodeType === 3 && n.nodeValue.trim(); });
    if (depth < 4 && el.children.length && !own && /^(DIV|HEADER|FIGURE)$/.test(el.tagName)) {
      [].forEach.call(el.children, function (c) { collect(c, depth + 1); });
      return;
    }
    mark(el, 0);
  };
  [].forEach.call(sections, function (sec) {
    var wrap = sec.querySelector(':scope > .wrap') || sec;
    [].forEach.call(wrap.children, function (c) { collect(c, 0); });
  });

  // Keyboard users never land on something that has not faded in yet: focus shows it at once.
  document.addEventListener('focusin', function (e) {
    var el = e.target.closest && e.target.closest('.rv, .rv-img');
    if (!el) return;
    reveal.unobserve(el);
    el.classList.remove('rv', 'rv-img', 'rv-flat', 'is-in');
    // a fade that has already started would otherwise run on; jump it to the end
    [el].concat([].slice.call(el.querySelectorAll('img'))).forEach(function (x) {
      x.getAnimations().forEach(function (a) { try { a.finish(); } catch (err) {} });
    });
  });

  // Larger photos open like a curtain.
  each('main > section:not(.chero) img', function (img) {
    var box = img.parentElement;
    if (img.closest('.compare, .logos, .marquee, a.btn') || box.offsetWidth < 280) return;
    var o = getComputedStyle(box).overflow;
    box.classList.add('rv-img');
    if (o !== 'hidden' && o !== 'clip') box.classList.add('rv-flat');
    reveal.observe(box);
  });

  // Step lines draw once the steps are on screen.
  var lines = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-in'); lines.unobserve(e.target); } });
  }, { threshold: .3 });
  each('.steps, .flow', function (s) { lines.observe(s); });

  // Section headings brighten word by word while they move from the bottom of the screen to its upper half.
  var heads = [];
  each('main > section:not(.chero) h2:not(.vh)', function (h) {
    var walk = document.createTreeWalker(h, NodeFilter.SHOW_TEXT), nodes = [];
    while (walk.nextNode()) nodes.push(walk.currentNode);
    nodes.forEach(function (n) {
      var frag = document.createDocumentFragment();
      n.nodeValue.split(/(\s+)/).forEach(function (part) {
        if (!part) return;
        if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
        var s = document.createElement('span'); s.className = 'w'; s.textContent = part; frag.appendChild(s);
      });
      n.parentNode.replaceChild(frag, n);
    });
    h.classList.add('hw');
    heads.push({ el: h, words: h.querySelectorAll('.w'), p: -1 });
  });
  var ticking = false;
  var paint = function () {
    ticking = false;
    var vh = window.innerHeight, end = window.scrollY + vh >= document.documentElement.scrollHeight - 4;
    heads.forEach(function (h) {
      var r = h.el.getBoundingClientRect();
      if (r.bottom < -100 || r.top > vh + 100) return;
      var p = end ? 1 : Math.max(0, Math.min(1, (vh * .94 - r.top) / (vh * .34)));
      if (Math.abs(p - h.p) < .005) return;
      h.p = p;
      var n = h.words.length;
      [].forEach.call(h.words, function (w, i) {
        var o = Math.max(0, Math.min(1, p * (n + 1) - i));
        w.style.setProperty('--o', (.22 + .78 * o).toFixed(3));
      });
    });
  };
  var request = function () { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
  window.addEventListener('scroll', request, { passive: true });
  window.addEventListener('resize', request);
  paint();

  formInit();

  // Contact form: the site has no server, so the form composes an e-mail
  // in the visitor's mail program instead of pretending to send.
  function formInit() {
    var form = document.querySelector('[data-mailto-form]');
    if (!form) return;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var v = function (n) { var el = form.elements[n]; return el ? el.value.trim() : ''; };
      var subject = 'Anfrage über hysn.de' + (v('branche') ? ' – ' + v('branche') : '');
      var lines = [
        'Guten Tag,', '', v('nachricht'), '',
        'Name: ' + v('name'),
        v('firma') ? 'Unternehmen: ' + v('firma') : '',
        v('telefon') ? 'Telefon: ' + v('telefon') : '',
        v('branche') ? 'Branche: ' + v('branche') : '',
        'E-Mail: ' + v('email')
      ].filter(function (l, i) { return l !== '' || i < 4; });
      window.location.href = 'mailto:' + form.getAttribute('data-mailto-form') +
        '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
      var note = form.querySelector('[data-sent]');
      if (note) note.hidden = false;
    });
  }
})();
