const cfg = require('../config/defaults');

async function get(path) {
  const ctl = new AbortController();
  const t = setTimeout(() => ctl.abort(), cfg.timeoutMs);
  try { return await fetch(cfg.baseUrl + path, { signal: ctl.signal }); }
  finally { clearTimeout(t); }
}
module.exports = { get };
