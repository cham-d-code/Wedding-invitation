/* WeddingMusic — culture-specific background music synthesised live with Web Audio.
   Styles: magulbera (Sinhala Kandyan drums + horanewa), magulflute (softer drums + flute),
   mangala (Tamil nadaswaram + thavil + tanpura), daf (frame drum only),
   organ (church organ, Pachelbel's Canon), musicbox (soft music box / piano).
   Set WEDDING.music to an .mp3 URL to use a real recording instead. */
window.WeddingMusic = (() => {
  let ac, master, dry, send, NB, timer, t0, tick = 0, S;
  const hz = m => 440 * Math.pow(2, (m - 69) / 12);
  const R = Math.random;

  function build(ctx) {
    ac = ctx;
    master = ac.createGain(); master.gain.value = 0;
    const comp = ac.createDynamicsCompressor(); comp.threshold.value = -16; comp.ratio.value = 4;
    master.connect(comp); comp.connect(ac.destination);
    const rev = ac.createConvolver(), len = ac.sampleRate * 2.8, b = ac.createBuffer(2, len, ac.sampleRate);
    for (let c = 0; c < 2; c++) { const d = b.getChannelData(c); for (let i = 0; i < len; i++) d[i] = (R() * 2 - 1) * Math.pow(1 - i / len, 3.2); }
    rev.buffer = b;
    dry = ac.createGain(); dry.connect(master);
    send = ac.createGain(); send.gain.value = .5; send.connect(rev); rev.connect(master);
    NB = ac.createBuffer(1, ac.sampleRate, ac.sampleRate);
    const nd = NB.getChannelData(0); for (let i = 0; i < nd.length; i++) nd[i] = R() * 2 - 1;
  }
  const route = (node, wet = .25) => { node.connect(dry); const g = ac.createGain(); g.gain.value = wet; node.connect(g); g.connect(send); };
  const env = (g, t, a, v, d) => { g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(v, t + a); g.gain.exponentialRampToValueAtTime(.0008, t + a + d); };
  const noise = () => { const s = ac.createBufferSource(); s.buffer = NB; s.loop = true; return s; };

  /* ---------------- percussion ---------------- */
  function membrane(t, f0, f1, v, dec, wet = .12) {
    const o = ac.createOscillator(), g = ac.createGain();
    o.frequency.setValueAtTime(f0, t); o.frequency.exponentialRampToValueAtTime(f1, t + dec * .7);
    env(g, t, .003, v, dec); o.connect(g); route(g, wet); o.start(t); o.stop(t + dec + .05);
  }
  function slap(t, fc, q, v, dec, tone, wet = .15) {
    const n = noise(), f = ac.createBiquadFilter(), g = ac.createGain();
    f.type = 'bandpass'; f.frequency.value = fc; f.Q.value = q;
    env(g, t, .002, v, dec); n.connect(f); f.connect(g); route(g, wet); n.start(t, R()); n.stop(t + dec + .05);
    if (tone) membrane(t, tone * 1.3, tone, v * .5, dec * 1.2, wet);
  }
  function metal(t, v, dec, base = 520) {
    const g = ac.createGain(), hp = ac.createBiquadFilter(); hp.type = 'highpass'; hp.frequency.value = 5200;
    env(g, t, .002, v, dec); hp.connect(g); route(g, .35);
    [2, 3, 4.16, 5.43, 6.79, 8.21].forEach(r => { const o = ac.createOscillator(); o.type = 'square'; o.frequency.value = base * r; o.connect(hp); o.start(t); o.stop(t + dec + .05); });
  }

  /* ---------------- melodic voices ---------------- */
  let lastReed = 0;
  function reed(t, dur, m, v, o = {}) {           // horanewa / nadaswaram style double reed
    const f = hz(m), g = ac.createGain(), bp = ac.createBiquadFilter(), pk = ac.createBiquadFilter(), lp = ac.createBiquadFilter();
    bp.type = 'bandpass'; bp.frequency.value = o.formant || 1300; bp.Q.value = .8;
    pk.type = 'peaking'; pk.frequency.value = (o.formant || 1300) * 2.1; pk.gain.value = 7; pk.Q.value = 2;
    lp.type = 'lowpass'; lp.frequency.value = o.lp || 5200;
    const a = ac.createOscillator(), b = ac.createOscillator(); a.type = 'sawtooth'; b.type = 'square'; b.detune.value = 7;
    const gb = ac.createGain(); gb.gain.value = .35;
    const vib = ac.createOscillator(), vg = ac.createGain(); vib.frequency.value = o.vibHz || 5.6; vg.gain.value = f * (o.vib || .012);
    vib.connect(vg); vg.connect(a.frequency); vg.connect(b.frequency);
    const from = lastReed && o.glide !== 0 ? lastReed : f;
    [a, b].forEach(x => { x.frequency.setValueAtTime(from, t); x.frequency.exponentialRampToValueAtTime(f, t + (o.glide || .05)); });
    if (o.gamaka) [a, b].forEach(x => { const k = hz(m + o.gamaka) ; x.frequency.setValueAtTime(f, t + dur * .45); x.frequency.exponentialRampToValueAtTime(k, t + dur * .6); x.frequency.exponentialRampToValueAtTime(f, t + dur * .8); });
    lastReed = f;
    g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(v, t + .035); g.gain.setValueAtTime(v * .85, t + Math.max(.05, dur - .06)); g.gain.linearRampToValueAtTime(0, t + dur);
    a.connect(bp); b.connect(gb); gb.connect(bp); bp.connect(pk); pk.connect(lp); lp.connect(g); route(g, o.wet || .3);
    [a, b, vib].forEach(x => { x.start(t); x.stop(t + dur + .05); });
  }
  function flute(t, dur, m, v) {
    const f = hz(m), g = ac.createGain(), o = ac.createOscillator(), o2 = ac.createOscillator(), g2 = ac.createGain();
    o.type = 'sine'; o2.type = 'triangle'; o.frequency.value = f; o2.frequency.value = f * 2; g2.gain.value = .12;
    const vib = ac.createOscillator(), vg = ac.createGain(); vib.frequency.value = 5; vg.gain.value = f * .008; vib.connect(vg); vg.connect(o.frequency);
    const n = noise(), bp = ac.createBiquadFilter(), ng = ac.createGain(); bp.type = 'bandpass'; bp.frequency.value = f * 2; bp.Q.value = 3; ng.gain.value = .06;
    g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(v, t + .08); g.gain.setValueAtTime(v * .8, t + Math.max(.1, dur - .1)); g.gain.linearRampToValueAtTime(0, t + dur);
    o.connect(g); o2.connect(g2); g2.connect(g); n.connect(bp); bp.connect(ng); ng.connect(g); route(g, .45);
    [o, o2, vib].forEach(x => { x.start(t); x.stop(t + dur + .05); }); n.start(t, R()); n.stop(t + dur + .05);
  }
  function tanpura(t, m, v) {
    const o = ac.createOscillator(), lp = ac.createBiquadFilter(), g = ac.createGain();
    o.type = 'sawtooth'; o.frequency.value = hz(m); lp.type = 'lowpass'; lp.frequency.setValueAtTime(3200, t); lp.frequency.exponentialRampToValueAtTime(500, t + 2.4);
    env(g, t, .01, v, 3); o.connect(lp); lp.connect(g); route(g, .4); o.start(t); o.stop(t + 3.1);
  }
  function organ(t, dur, m, v) {
    const g = ac.createGain(), f = hz(m);
    g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(v, t + .06); g.gain.setValueAtTime(v, t + dur - .02); g.gain.linearRampToValueAtTime(0, t + dur + .25);
    [[1, .5], [2, .32], [3, .16], [4, .14], [6, .06], [8, .05]].forEach(([h, a], i) => {
      const o = ac.createOscillator(), og = ac.createGain(); o.frequency.value = f * h; o.detune.value = i % 2 ? 3 : -2; og.gain.value = a;
      o.connect(og); og.connect(g); o.start(t); o.stop(t + dur + .3);
    });
    route(g, .7);
  }
  function bell(t, m, v, o = {}) {
    const a = ac.createOscillator(), b = ac.createOscillator(), g = ac.createGain(), gb = ac.createGain();
    a.frequency.value = hz(m); b.frequency.value = hz(m) * (o.bell ? 2.76 : 3.01); gb.gain.value = o.bell ? .22 : .1;
    b.connect(gb); gb.connect(g); a.connect(g); env(g, t, .005, v, o.decay || 1.9); route(g, .4);
    a.start(t); b.start(t); a.stop(t + 2.4); b.stop(t + 2.4);
  }
  function pad(t, notes, dur, v) {
    notes.forEach(n => { const o = ac.createOscillator(), g = ac.createGain(), f = ac.createBiquadFilter(); o.type = 'triangle'; o.frequency.value = hz(n);
      f.type = 'lowpass'; f.frequency.value = 800; g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(v, t + 1.2); g.gain.linearRampToValueAtTime(0, t + dur);
      o.connect(f); f.connect(g); route(g, .5); o.start(t); o.stop(t + dur + .1); });
  }

  /* ---------------- styles ---------------- */
  // Melodies are written as [scale-degree or null, length in ticks]
  const seq = phr => { const out = []; phr.forEach(p => p.forEach(n => out.push(n))); return out; };
  const STYLES = {
    /* Sinhala magul bera: geta bera strokes (thom = bass, tha = slap), thalampata, horanewa lead */
    magulbera(o) {
      const bpm = o.bpm || 112, tk = 60 / bpm / 2;   // eighth-note ticks
      const scale = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16], root = o.root || 69;
      const drum = ['B', '.', 'S', 'S', 'B', 'S', '.', 'S', 'B', '.', 'S', 'B', 'S', 'S', 'B', '.'];
      const fill = ['S', 'S', 'S', 'S', 'B', 'S', 'S', 'S', 'B', 'B', 'S', 'S', 'S', 'S', 'B', 'B'];
      const mel = seq([
        [[0, 2], [2, 1], [4, 1], [4, 2], [5, 1], [4, 1], [2, 2], [0, 2], [2, 2], [null, 2]],
        [[2, 1], [4, 1], [5, 2], [7, 2], [5, 1], [4, 1], [5, 2], [4, 1], [2, 1], [4, 4]],
        [[7, 2], [7, 1], [8, 1], [7, 2], [5, 2], [4, 1], [5, 1], [7, 2], [5, 2], [null, 2]],
        [[4, 1], [2, 1], [1, 1], [0, 1], [1, 2], [2, 2], [1, 1], [0, 1], [-1, 2], [0, 4]],
      ]);
      let mi = 0, wait = 0, bar = 0;
      return { tk, step(t, i) {
        const pos = i % 16; if (pos === 0) bar++;
        const p = (bar % 4 === 0 ? fill : drum)[pos];
        if (p === 'B') membrane(t, 150, 72, .9, .42);
        if (p === 'S') slap(t, 1500 + R() * 300, 1.4, .55 + R() * .15, .08, 330);
        if (pos % 4 === 0) metal(t, pos === 0 ? .1 : .06, pos === 0 ? .35 : .15);
        if (i >= 32) {                       // lead enters after two bars
          if (wait-- <= 0) { const [d, l] = mel[mi % mel.length]; mi++; wait = l - 1;
            if (d !== null) { const m = root + (d < 0 ? -1 : scale[d]); reed(t, l * tk * .96, m, .16, { formant: 1500, vib: .01, glide: .04 }); } }
        }
      } };
    },
    /* softer: flute lead, gentle bera */
    magulflute(o) {
      const bpm = o.bpm || 84, tk = 60 / bpm / 2, scale = [0, 2, 4, 5, 7, 9, 11, 12, 14], root = o.root || 74;
      const mel = seq([
        [[4, 3], [5, 1], [4, 2], [2, 2], [0, 4], [null, 4]],
        [[2, 2], [4, 2], [5, 2], [7, 2], [5, 3], [4, 1], [2, 4]],
        [[7, 3], [8, 1], [7, 2], [5, 2], [4, 2], [5, 2], [4, 4]],
        [[2, 2], [1, 2], [0, 2], [1, 2], [0, 6], [null, 2]],
      ]);
      let mi = 0, wait = 0;
      return { tk, step(t, i) {
        const pos = i % 16;
        if (pos === 0 || pos === 10) membrane(t, 140, 70, .55, .45);
        if (pos === 4 || pos === 12 || (pos === 14 && R() < .5)) slap(t, 1400, 1.2, .25, .07, 300);
        if (pos % 8 === 0) metal(t, .045, .3);
        if (i >= 16 && wait-- <= 0) { const [d, l] = mel[mi % mel.length]; mi++; wait = l - 1; if (d !== null) flute(t, l * tk, root + scale[d], .2); }
        if (pos === 0 && i % 64 === 0) pad(t, [root - 24, root - 17], tk * 64, .03);
      } };
    },
    /* Tamil mangala vadyam: nadaswaram in raga Mohanam, thavil, talam, tanpura */
    mangala(o) {
      const bpm = o.bpm || 88, tk = 60 / bpm / 4, sa = o.root || 67;   // 16th ticks
      const moh = [0, 2, 4, 7, 9, 12, 14, 16];                          // S R2 G3 P D2 S' R' G'
      const thavil = ['D', '.', 't', 't', 'D', 't', '.', 't', 'D', '.', 't', '.', 'D', 't', 't', 't'];
      const mel = seq([
        [[0, 4], [1, 2], [2, 2], [3, 8], [2, 2], [1, 2], [0, 4], [1, 8]],
        [[2, 4], [3, 4], [4, 4], [5, 8], [4, 2], [3, 2], [2, 4], [3, 8]],
        [[4, 2], [3, 2], [4, 4], [5, 4], [6, 4], [5, 4], [4, 2], [3, 2], [2, 8]],
        [[3, 4], [2, 2], [1, 2], [2, 4], [1, 2], [0, 2], [1, 4], [0, 12]],
      ]);
      let mi = 0, wait = 0;
      return { tk, step(t, i) {
        const pos = i % 16, beat = Math.floor(i / 4) % 8;
        const p = thavil[pos];
        if (p === 'D') membrane(t, 120, 62, .7, .35);
        if (p === 't') slap(t, 2600 + R() * 500, 2, .42 + R() * .12, .05, 0);
        if (pos % 4 === 0 && (beat === 0 || beat === 4 || beat === 6)) metal(t, .07, .5, 700);
        if (i % 8 === 0) { const c = Math.floor(i / 8) % 4; tanpura(t, c === 0 ? sa - 17 : c === 3 ? sa - 24 : sa - 12, .06); }
        if (i >= 32 && wait-- <= 0) { const [d, l] = mel[mi % mel.length]; mi++; wait = l - 1;
          reed(t, l * tk * .98, sa + moh[d], .17, { formant: 1100, lp: 4200, vib: .006, vibHz: 4.5, glide: .07, gamaka: l >= 8 ? 1 : 0, wet: .35 }); }
      } };
    },
    /* frame drum only (dum / tak with jingles) */
    daf(o) {
      const bpm = o.bpm || 92, tk = 60 / bpm / 2;
      const pat = ['D', '.', 'T', '.', 'T', 'D', 'T', '.', 'D', '.', 'T', '.', 'T', 'T', 'D', 'T'];
      return { tk, step(t, i) {
        const p = pat[i % 16];
        if (p === 'D') { membrane(t, 95, 58, .75, .5, .3); slap(t, 400, .7, .12, .12, 0); }
        if (p === 'T') { slap(t, 3000, 1.5, .28 + R() * .1, .06, 0); metal(t, .03, .12, 900); }
      } };
    },
    /* church organ: Pachelbel's Canon in D (public domain) */
    organ(o) {
      const bpm = o.bpm || 58, tk = 60 / bpm;       // quarter-note ticks
      const bass = [50, 45, 47, 42, 43, 38, 43, 45];
      const chords = [[62, 66, 69], [61, 64, 69], [62, 66, 71], [61, 66, 69], [62, 67, 71], [62, 66, 69], [62, 67, 71], [61, 64, 69]];
      const v2 = [78, 76, 74, 73, 71, 69, 71, 73], v3 = [74, 73, 71, 69, 67, 66, 67, 64];
      const v4 = [74, 78, 81, 79, 78, 74, 78, 76, 74, 71, 74, 81, 79, 83, 81, 79];
      return { tk, step(t, i) {
        const cyc = Math.floor(i / 16), pos = i % 16, k = Math.floor(pos / 2);
        if (pos % 2 === 0) { organ(t, tk * 2 * .98, bass[k], .2); organ(t, tk * 2 * .98, bass[k] - 12, .1); chords[k].forEach(n => organ(t, tk * 2 * .98, n, .045)); }
        const c = cyc === 0 ? 0 : 1 + (cyc - 1) % 3;
        if (c === 1 && pos % 2 === 0) organ(t, tk * 2 * .96, v2[k], .09);
        if (c === 2 && pos % 2 === 0) organ(t, tk * 2 * .96, v3[k], .09);
        if (c === 3) organ(t, tk * .94, v4[pos], .085);
      } };
    },
    /* soft music box / piano (modern, luxury, garden) */
    musicbox(o) {
      const bpm = o.bpm || 68, tk = 60 / bpm / 2, key = o.key || 62;
      const prog = o.prog || [[0, 4, 7], [7, 11, 14], [9, 12, 16], [5, 9, 12]], pat = o.pattern || [0, 1, 2, 1, 3, 2, 1, 2];
      return { tk, step(t, i) {
        const ch = prog[Math.floor(i / 8) % prog.length], s = i % 8;
        if (s === 0) pad(t, ch.map(n => key - 12 + n), tk * 8 + .8, .045);
        const p = pat[s]; if (p >= 0 && R() < .92) bell(t, key + 12 + (p === 3 ? ch[0] + 12 : ch[p % 3]), .2 + R() * .08, o);
      } };
    },
  };

  /* ---------------- player ---------------- */
  let playing = false, audio = null, btn = null, cfg = {};
  function schedule() { while (t0 < ac.currentTime + 1.2) { S.step(t0, tick++); t0 += S.tk; } }
  function startSynth() {
    if (!ac) { build(new (window.AudioContext || window.webkitAudioContext)()); S = (STYLES[cfg.style] || STYLES.musicbox)(cfg); t0 = ac.currentTime + .15; }
    ac.resume(); master.gain.cancelScheduledValues(ac.currentTime); master.gain.setTargetAtTime(cfg.volume || .5, ac.currentTime, .6);
    schedule(); clearInterval(timer); timer = setInterval(schedule, 200);
  }
  function stopSynth() { if (!ac) return; master.gain.setTargetAtTime(0, ac.currentTime, .15); clearInterval(timer); setTimeout(() => { if (!playing) ac.suspend(); }, 600); }
  const set = v => { playing = v; if (btn) btn.setAttribute('aria-pressed', v); };
  function play() {
    try {
      if (cfg.url) { audio = audio || Object.assign(new Audio(cfg.url), { loop: true }); audio.play().then(() => set(true)).catch(() => {}); }
      else { set(true); startSynth(); }
    } catch (_) {}
  }
  function stop() { if (audio) audio.pause(); set(false); stopSynth(); }
  return {
    STYLES,
    init(button, c) { btn = button; cfg = c || {}; if (btn) btn.addEventListener('click', e => { e.stopPropagation(); playing ? stop() : play(); }); },
    play, stop, get playing() { return playing; },
    /* fresh player for a given style (used for samples on the website) */
    create(c) { return { play() { if (ac) { clearInterval(timer); try { ac.close(); } catch (_) {} } ac = null; cfg = Object.assign({}, c); tick = 0; lastReed = 0; set(true); startSynth(); }, stop() { stop(); } }; },
    /* offline render helper for testing */
    render(ctx, style, o, secs) { build(ctx); master.gain.value = o.volume || .5; S = STYLES[style](o); t0 = 0; tick = 0; while (t0 < secs) { S.step(t0, tick++); t0 += S.tk; } },
  };
})();
