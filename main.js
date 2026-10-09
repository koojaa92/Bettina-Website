// Lebensfäden: Kopfzeile messen, Menü, vergangene Termine ausblenden und der Faden.
(function () {
  var wurzel = document.documentElement;
  var kopf = document.querySelector('.kopf');
  var knopf = document.querySelector('.menue-knopf');
  var menue = document.getElementById('menue');

  function messen() {
    if (kopf) wurzel.style.setProperty('--kopf', kopf.offsetHeight + 'px');
  }
  messen();
  window.addEventListener('resize', messen);

  if (knopf && menue) {
    knopf.addEventListener('click', function () {
      var offen = menue.classList.toggle('offen');
      knopf.setAttribute('aria-expanded', offen ? 'true' : 'false');
      messen();
    });
  }

  // Vergangene Termine ausblenden (die Karten tragen data-datum="JJJJ-MM-TT")
  var heute = new Date().toISOString().slice(0, 10);
  document.querySelectorAll('[data-datum]').forEach(function (k) {
    if (k.getAttribute('data-datum') < heute) k.hidden = true;
  });

  // ---------- Der Faden ----------
  var haupt = document.querySelector('main');
  if (!haupt) return;
  var NS = 'http://www.w3.org/2000/svg';
  var ruhig = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var svg, grund, glanz, knoten = [], clipRect, laenge = 0, ankerY = [];

  function ankerSammeln() {
    var rect = haupt.getBoundingClientRect();
    var oben = rect.top + window.pageYOffset;
    var liste = [];
    haupt.querySelectorAll('.abschnitt h2, .seitenkopf h1').forEach(function (h) {
      if (h.closest('[hidden]') || h.closest('.kraft')) return;
      var r = h.getBoundingClientRect();
      if (!r.height) return;
      liste.push(r.top + window.pageYOffset - oben + Math.min(r.height / 2, 18));
    });
    return { y: liste, hoehe: haupt.offsetHeight, breite: haupt.offsetWidth };
  }

  function bauen() {
    var a = ankerSammeln();
    if (a.y.length < 2) { if (svg) svg.remove(); svg = null; return; }
    if (svg) svg.remove();
    var rand = Math.max(8, (a.breite - 1152) / 2 - 36);
    var klein = a.breite < 900;
    var xa = klein ? 6 : Math.min(rand, 60), xb = xa + (klein ? 8 : 22);
    var d = 'M ' + xa + ' ' + Math.max(0, a.y[0] - 120);
    var px = xa, py = Math.max(0, a.y[0] - 120);
    var punkte = [];
    a.y.forEach(function (y, i) {
      var x = i % 2 ? xa : xb;
      var m = (y - py) / 2;
      d += ' C ' + px + ' ' + (py + m) + ', ' + x + ' ' + (y - m) + ', ' + x + ' ' + y;
      px = x; py = y; punkte.push([x, y]);
    });
    d += ' L ' + px + ' ' + (a.hoehe + 40);

    svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('class', 'faden');
    svg.setAttribute('aria-hidden', 'true');
    svg.setAttribute('viewBox', '0 0 ' + a.breite + ' ' + (a.hoehe + 40));
    svg.style.height = (a.hoehe + 40) + 'px';
    svg.innerHTML =
      '<defs><linearGradient id="fadenverlauf" x1="0" y1="0" x2="0" y2="1">' +
      '<stop offset="0" stop-color="#c8930c"/><stop offset=".5" stop-color="#f1cd5b"/><stop offset="1" stop-color="#c8930c"/></linearGradient>' +
      '<clipPath id="fadenclip"><rect id="fadenrect" x="0" y="0" width="' + a.breite + '" height="0"/></clipPath></defs>' +
      '<path class="grund" d="' + d + '"/><g clip-path="url(#fadenclip)"><path class="glanz" d="' + d + '"/></g>';
    punkte.forEach(function (p) {
      var c = document.createElementNS(NS, 'circle');
      c.setAttribute('class', 'knoten'); c.setAttribute('cx', p[0]); c.setAttribute('cy', p[1]); c.setAttribute('r', 5);
      svg.appendChild(c);
    });
    haupt.style.position = 'relative';
    haupt.appendChild(svg);
    grund = svg.querySelector('.grund');
    glanz = svg.querySelector('.glanz');
    clipRect = svg.querySelector('#fadenrect');
    knoten = Array.prototype.slice.call(svg.querySelectorAll('.knoten'));
    ankerY = a.y;
    laenge = grund.getTotalLength();
    grund.style.strokeDasharray = laenge;
    zeichnen();
  }

  function zeichnen() {
    if (!svg) return;
    var oben = haupt.getBoundingClientRect().top + window.pageYOffset;
    var bis = ruhig ? Infinity : (window.pageYOffset + window.innerHeight * 0.7 - oben);
    var start = Math.max(0, ankerY[0] - 120);
    var hoehe = svg.viewBox.baseVal.height;
    var anteil = ruhig ? 1 : Math.max(0, Math.min(1, (bis - start) / (hoehe - start)));
    grund.style.strokeDashoffset = laenge * (1 - anteil);
    clipRect.setAttribute('height', ruhig ? hoehe : Math.max(0, bis));
    knoten.forEach(function (k, i) { k.classList.toggle('an', ruhig || bis >= ankerY[i]); });
  }

  var geplant = false;
  function beiScroll() {
    if (geplant) return;
    geplant = true;
    requestAnimationFrame(function () { geplant = false; zeichnen(); });
  }
  window.addEventListener('scroll', beiScroll, { passive: true });
  window.addEventListener('load', bauen);
  var resizeTimer;
  window.addEventListener('resize', function () { clearTimeout(resizeTimer); resizeTimer = setTimeout(bauen, 200); });
  if ('ResizeObserver' in window) new ResizeObserver(function () { clearTimeout(resizeTimer); resizeTimer = setTimeout(bauen, 150); }).observe(haupt);
  bauen();
})();
