/* Referenzen: filter the use-case tiles by industry. Without JavaScript all tiles stay visible.
   On narrow screens the tabs scroll sideways: a fade marks the edge that still has tabs behind it,
   and a tapped tab scrolls to the middle of the row. */
(function () {
  var bar = document.querySelector('.rf-filter');
  if (!bar) return;
  var grid = document.querySelector('.rf-grid');
  var cards = document.querySelectorAll('.rf-card');
  var smooth = !(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);

  var edges = function () {
    var max = bar.scrollWidth - bar.clientWidth;
    bar.classList.toggle('is-scrolled', bar.scrollLeft > 2);
    bar.classList.toggle('at-end', max <= 2 || bar.scrollLeft >= max - 2);
  };
  // the closing tile fills the empty slot in the 2-column grid when an odd number of tiles is visible
  var parity = function () {
    var n = 0;
    cards.forEach(function (c) { if (!c.hidden) n++; });
    if (grid) grid.classList.toggle('is-even', n % 2 === 0);
  };

  bar.addEventListener('scroll', edges, { passive: true });
  window.addEventListener('resize', edges);
  edges(); parity();

  var apply = function (b) {
    var f = b.getAttribute('data-filter');
    bar.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
    var shown = [];
    cards.forEach(function (c) {
      c.hidden = f !== 'alle' && (' ' + c.getAttribute('data-cat') + ' ').indexOf(' ' + f + ' ') < 0;
      if (!c.hidden) shown.push(c);
    });
    parity();
    // the tiles of the new selection fade in one after another instead of popping in
    shown.forEach(function (c, i) {
      c.classList.remove('rv', 'is-in');
      if (smooth && c.animate) c.animate([{ opacity: 0, transform: 'translateY(16px)' }, { opacity: 1, transform: 'none' }],
        { duration: 520, delay: Math.min(i, 6) * 70, easing: 'cubic-bezier(.22,.61,.36,1)', fill: 'backwards' });
    });
  };
  bar.addEventListener('click', function (e) {
    var b = e.target.closest('button[data-filter]');
    if (!b) return;
    apply(b);
    if (bar.scrollWidth > bar.clientWidth + 2) b.scrollIntoView({ behavior: smooth ? 'smooth' : 'auto', inline: 'center', block: 'nearest' });
  });

  // A link like referenzen/#gastro (from the start page) opens the use cases with that filter set.
  var pre = bar.querySelector('button[data-filter="' + location.hash.slice(1).replace(/[^a-z]/g, '') + '"]');
  if (pre && location.hash.length > 1) {
    apply(pre);
    bar.scrollLeft = pre.offsetLeft - (bar.clientWidth - pre.offsetWidth) / 2;
    var sec = document.getElementById('einsatz');
    if (sec) requestAnimationFrame(function () { sec.scrollIntoView(); });
  }
})();
