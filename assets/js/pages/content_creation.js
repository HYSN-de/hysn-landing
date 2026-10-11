/* Content Creation: the example viewer plays its four tabs one after another (about 6 s each).
   Without JS the radio tabs still switch the panels; this only adds play/pause, progress and time.
   Starts paused when the visitor prefers reduced motion; a tab chosen by hand pauses the playback. */
(function () {
  var view = document.querySelector('.cc-view');
  if (!view) return;
  var radios = [].slice.call(view.querySelectorAll('.cc-radio'));
  var player = view.querySelector('.cc-player');
  var btn = view.querySelector('.cc-play');
  var segs = [].slice.call(view.querySelectorAll('.cc-prog i'));
  var time = view.querySelector('.cc-time');
  if (!radios.length || !player || !btn) return;

  var DUR = 6000, n = radios.length, idx = 0, elapsed = 0, playing = false, inView = true, raf = 0, last = 0, shown = -1;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var fmt = function (s) { return Math.floor(s / 60) + ':' + ('0' + (s % 60)).slice(-2); };
  var paint = function () {
    var p = Math.min(elapsed / DUR, 1);
    segs.forEach(function (s, i) { s.style.setProperty('--p', i < idx ? 1 : i === idx ? p.toFixed(4) : 0); });
    var sec = Math.floor((idx * DUR + elapsed) / 1000);
    if (sec !== shown) { shown = sec; time.textContent = fmt(sec) + ' / ' + fmt(n * DUR / 1000); }
  };
  var setButton = function () {
    btn.setAttribute('aria-label', playing ? 'Pausieren' : 'Abspielen');
    btn.classList.toggle('is-playing', playing);
  };
  var tick = function (t) {
    raf = 0;
    if (!playing) return;
    var dt = last ? Math.min(t - last, 250) : 0; // a background tab or a stalled frame never jumps ahead
    last = t;
    if (inView && !document.hidden) elapsed += dt;
    if (elapsed >= DUR) { elapsed = 0; idx = (idx + 1) % n; radios[idx].checked = true; }
    paint();
    raf = requestAnimationFrame(tick);
  };
  var play = function () { playing = true; last = 0; setButton(); if (!raf) raf = requestAnimationFrame(tick); };
  var pause = function () { playing = false; setButton(); if (raf) { cancelAnimationFrame(raf); raf = 0; } paint(); };
  var show = function (i) { radios[i].checked = true; idx = i; elapsed = 0; pause(); };

  btn.addEventListener('click', function () { if (playing) pause(); else play(); });
  // a tab picked by hand (click, tap or arrow keys) stays on screen
  radios.forEach(function (r, i) { r.addEventListener('change', function () { if (r.checked) show(i); }); });
  // links elsewhere on the page that open one example ("#beispiele" plus data-cc-tab)
  [].forEach.call(document.querySelectorAll('[data-cc-tab]'), function (a) {
    a.addEventListener('click', function () { var i = +a.getAttribute('data-cc-tab') - 1; if (radios[i]) show(i); });
  });
  // only count time while the screen is actually visible
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (es) { inView = es[0].isIntersecting; }, { threshold: 0.35 }).observe(view.querySelector('.cc-screen'));
  }

  radios.forEach(function (r, i) { if (r.checked) idx = i; });
  player.hidden = false;
  view.classList.add('is-player');
  paint();
  if (reduce) pause(); else play();
})();
