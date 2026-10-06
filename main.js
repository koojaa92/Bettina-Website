// Kopfzeilenhöhe messen und als --kopf setzen (für Hero und Anker).
(function () {
  var kopf = document.querySelector('.kopf');
  if (!kopf) return;
  function messen() {
    document.documentElement.style.setProperty('--kopf', kopf.offsetHeight + 'px');
  }
  messen();
  window.addEventListener('resize', messen);
})();
