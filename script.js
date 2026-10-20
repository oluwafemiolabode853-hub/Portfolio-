/* Oluwafemi Olabode - delivery record. No frameworks. */
(function () {
  'use strict';
  var root = document.documentElement;
  root.classList.add('js');
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* theme */
  function g(k){ try{return localStorage.getItem(k)}catch(e){return null} }
  function s(k,v){ try{localStorage.setItem(k,v)}catch(e){} }
  var saved = g('oo-theme');
  if (saved === 'dark' || saved === 'light') root.setAttribute('data-theme', saved);
  var tgl = document.getElementById('tgl');
  if (tgl) tgl.addEventListener('click', function(){
    var sys = window.matchMedia('(prefers-color-scheme: dark)').matches;
    var cur = root.getAttribute('data-theme') || (sys ? 'dark' : 'light');
    var nx = cur === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', nx); s('oo-theme', nx);
  });

  /* index hero words for the stagger */
  Array.prototype.forEach.call(document.querySelectorAll('.h-big .l'), function(line){
    Array.prototype.forEach.call(line.querySelectorAll('.w'), function(w,i){ w.style.setProperty('--i', i); });
  });

  /* go */
  function go(){ document.body.classList.add('go'); }
  if (reduced) { document.body.classList.add('reduced'); go(); }
  else setTimeout(go, 90);

  /* bar + progress */
  var bar = document.getElementById('bar');
  var prog = document.getElementById('prog');
  var tick = false;
  function onScroll(){
    var y = window.scrollY;
    var d = document.documentElement.scrollHeight - window.innerHeight;
    if (bar) bar.classList.toggle('on', y > 12);
    if (prog) prog.style.width = (d > 0 ? Math.min(1, y/d)*100 : 0).toFixed(2) + '%';
    tick = false;
  }
  window.addEventListener('scroll', function(){ if(!tick){tick=true;requestAnimationFrame(onScroll);} }, {passive:true});
  window.addEventListener('resize', onScroll, {passive:true});
  onScroll();

  /* mobile nav */
  var bg = document.getElementById('burger'), mn = document.getElementById('mnav');
  if (bg && mn) {
    bg.addEventListener('click', function(){
      var open = bg.getAttribute('aria-expanded') === 'true';
      bg.setAttribute('aria-expanded', String(!open)); mn.hidden = open;
    });
    mn.addEventListener('click', function(e){
      if (e.target.closest('a')) { bg.setAttribute('aria-expanded','false'); mn.hidden = true; }
    });
    document.addEventListener('keydown', function(e){
      if (e.key === 'Escape' && !mn.hidden) { bg.setAttribute('aria-expanded','false'); mn.hidden = true; bg.focus(); }
    });
  }

  /* measure every drawn path so each line draws at its own true length */
  function measure(scope){
    var els = scope.querySelectorAll('.d-draw, .d-wire, .d-stroke');
    Array.prototype.forEach.call(els, function(el){
      if (el.__len) return;
      var L = 0;
      try { L = el.getTotalLength ? el.getTotalLength() : 0; } catch(e){ L = 0; }
      if (!L) { // rects and shapes without getTotalLength
        try {
          var bb = el.getBBox();
          L = (bb.width + bb.height) * 2;
        } catch(e){ L = 400; }
      }
      L = Math.ceil(L) + 2;
      el.__len = L;
      el.style.setProperty('--len', L);
    });
  }
  measure(document);

  /* reveal + plate draw */
  var rv = document.querySelectorAll('.rv');
  var plates = document.querySelectorAll('.file');
  if (reduced || !('IntersectionObserver' in window)) {
    Array.prototype.forEach.call(rv, function(el){ el.classList.add('in'); });
    Array.prototype.forEach.call(plates, function(el){ el.classList.add('seen'); });
  } else {
    var io = new IntersectionObserver(function(en){
      en.forEach(function(e){
        if (!e.isIntersecting) return;
        var el = e.target;
        var i = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
        setTimeout(function(){ el.classList.add('in'); }, Math.min(i,6)*65);
        io.unobserve(el);
      });
    }, { rootMargin:'0px 0px 8% 0px', threshold:0.04 });
    Array.prototype.forEach.call(rv, function(el){ io.observe(el); });

    var po = new IntersectionObserver(function(en){
      en.forEach(function(e){
        if (!e.isIntersecting) return;
        e.target.classList.add('seen');
        po.unobserve(e.target);
      });
    }, { rootMargin:'0px 0px 14% 0px', threshold:0.02 });
    Array.prototype.forEach.call(plates, function(el){ po.observe(el); });
  }

  /* extra groups that now carry their own motion */
  var groups = document.querySelectorAll('.cblock, .who-card, .cact, .facts, .tl li');
  if (reduced || !('IntersectionObserver' in window)) {
    Array.prototype.forEach.call(groups, function(el){ el.classList.add('in'); });
    var tl0 = document.querySelector('.tl'); if (tl0) tl0.classList.add('drawn');
  } else {
    var go2 = new IntersectionObserver(function(en){
      en.forEach(function(e){
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        go2.unobserve(e.target);
      });
    }, { rootMargin:'0px 0px 6% 0px', threshold:0.05 });
    Array.prototype.forEach.call(groups, function(el){ go2.observe(el); });

    var tl = document.querySelector('.tl');
    if (tl) {
      var tlo = new IntersectionObserver(function(en){
        en.forEach(function(e){
          if (!e.isIntersecting) return;
          e.target.classList.add('drawn');
          tlo.unobserve(e.target);
        });
      }, { rootMargin:'0px 0px -10% 0px', threshold:0.02 });
      tlo.observe(tl);
    }
  }

  /* active nav */
  var secs = document.querySelectorAll('section[id]');
  var links = document.querySelectorAll('.nav a[href^="#"]');
  if (secs.length && links.length && 'IntersectionObserver' in window) {
    var spy = new IntersectionObserver(function(en){
      en.forEach(function(e){
        if (!e.isIntersecting) return;
        Array.prototype.forEach.call(links, function(a){
          a.classList.toggle('on', a.getAttribute('href') === '#' + e.target.id);
        });
      });
    }, { rootMargin:'-45% 0px -50% 0px' });
    Array.prototype.forEach.call(secs, function(x){ spy.observe(x); });
  }
})();
