// Kopfzeilenhöhe messen (--kopf) und Menü am Handy auf- und zuklappen.
(function () {
  var kopf = document.querySelector('.kopf');
  var knopf = document.querySelector('.menue-knopf');
  var menue = document.getElementById('menue');
  function messen() {
    if (kopf) document.documentElement.style.setProperty('--kopf', kopf.offsetHeight + 'px');
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
})();
