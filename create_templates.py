import os

templates = {}

templates['base.html'] = open('/dev/stdin').read() if False else """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>TradeChain Simulator</title>
  <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet"/>
  <style>
    :root{--bg:#070b0f;--surface:#0d1117;--panel:#111820;--border:#1e2d3d;--border2:#253545;--exp:#00c8ff;--imp:#a78bfa;--cus:#f59e0b;--green:#10b981;--red:#ef4444;--text:#cdd9e5;--muted:#566a7f;--mono:'Share Tech Mono',monospace;--sans:'DM Sans',sans-serif}
    *{box-sizing:border-box;margin:0;padding:0}html,body{height:100%;background:var(--bg);color:var(--text);font-family:var(--sans)}
    body::before{content:'';position:fixed;inset:0;background-image:linear-gradient(var(--border) 1px,transparent 1px),linear-gradient(90deg,var(--border) 1px,transparent 1px);background-size:40px 40px;opacity:.25;pointer-events:none;z-index:0}
    body>*{position:relative;z-index:1}
    nav{display:flex;align-items:center;gap:1.5rem;padding:0 1.75rem;height:52px;background:rgba(13,17,23,.9);border-bottom:1px solid var(--border);backdrop-filter:blur(8px);position:sticky;top:0;z-index:100}
    .nav-brand{font-family:var(--mono);font-size:.85rem;color:var(--accent);text-decoration:none;letter-spacing:.08em;margin-right:.5rem}
    .nav-badge{font-size:.68rem;font-family:var(--mono);padding:2px 10px;border-radius:20px;border:1px solid var(--accent);color:var(--accent);background:rgba(0,0,0,.3)}
    nav a.nav-link{color:var(--muted);text-decoration:none;font-size:.82rem;transition:color .15s}nav a.nav-link:hover{color:var(--text)}
    .nav-spacer{flex:1}.nav-user{font-size:.78rem;color:va

cat > create_templates.py << 'SCRIPT'
import os

templates = {}

templates['base.html'] = open('/dev/stdin').read() if False else """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>TradeChain Simulator</title>
  <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet"/>
  <style>
    :root{--bg:#070b0f;--surface:#0d1117;--panel:#111820;--border:#1e2d3d;--border2:#253545;--exp:#00c8ff;--imp:#a78bfa;--cus:#f59e0b;--green:#10b981;--red:#ef4444;--text:#cdd9e5;--muted:#566a7f;--mono:'Share Tech Mono',monospace;--sans:'DM Sans',sans-serif}
    *{box-sizing:border-box;margin:0;padding:0}html,body{height:100%;background:var(--bg);color:var(--text);font-family:var(--sans)}
    body::before{content:'';position:fixed;inset:0;background-image:linear-gradient(var(--border) 1px,transparent 1px),linear-gradient(90deg,var(--border) 1px,transparent 1px);background-size:40px 40px;opacity:.25;pointer-events:none;z-index:0}
    body>*{position:relative;z-index:1}
    nav{display:flex;align-items:center;gap:1.5rem;padding:0 1.75rem;height:52px;background:rgba(13,17,23,.9);border-bottom:1px solid var(--border);backdrop-filter:blur(8px);position:sticky;top:0;z-index:100}
    .nav-brand{font-family:var(--mono);font-size:.85rem;color:var(--accent);text-decoration:none;letter-spacing:.08em;margin-right:.5rem}
    .nav-badge{font-size:.68rem;font-family:var(--mono);padding:2px 10px;border-radius:20px;border:1px solid var(--accent);color:var(--accent);background:rgba(0,0,0,.3)}
    nav a.nav-link{color:var(--muted);text-decoration:none;font-size:.82rem;transition:color .15s}nav a.nav-link:hover{color:var(--text)}
    .nav-spacer{flex:1}.nav-user{font-size:.78rem;color:var(--muted);font-family:var(--mono);display:flex;align-items:center;gap:.75rem}.nav-user span{color:var(--accent)}
    .btn-logout{font-size:.72rem;font-family:var(--mono);background:transparent;border:1px solid var(--border2);color:var(--muted);padding:3px 12px;border-radius:4px;cursor:pointer;transition:all .15s;text-decoration:none}
    .btn-logout:hover{border-color:var(--red);color:var(--red)}
    .page{max-width:1200px;margin:0 auto;padding:2rem 1.75rem}
    .section-head{margin-bottom:1.75rem}.section-head h1{font-family:var(--mono);font-size:1.2rem;color:var(--accent);letter-spacing:.05em}.section-head p{font-size:.82rem;color:var(--muted);margin-top:.3rem}
    .panel{background:var(--panel);border:1px solid var(--border);border-radius:8px;padding:1.5rem}
    .panel-title{font-family:var(--mono);font-size:.75rem;color:var(--muted);letter-spacing:.1em;text-transform:uppercase;margin-bottom:1.25rem;padding-bottom:.75rem;border-bottom:1px solid var(--border)}
    .grid-2{display:grid;grid-template-columns:1fr 1fr;gap:1.25rem}.grid-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.25rem}
    @media(max-width:700px){.grid-2,.grid-3{grid-template-columns:1fr}}
    .stat{background:var(--surface);border:1px solid var(--border);border-radius:6px;padding:1rem 1.25rem}.stat-val{font-family:var(--mono);font-size:1.8rem;color:var(--accent)}.stat-lbl{font-size:.75rem;color:var(--muted);margin-top:2px}
    .block-card{background:var(--surface);border:1px solid var(--border);border-radius:6px;padding:1rem 1.25rem;margin-bottom:.6rem;transition:border-color .2s}.block-card:hover{border-color:var(--border2)}
    .block-card-head{display:flex;align-items:center;gap:.75rem;margin-bottom:.6rem;flex-wrap:wrap}
    .tag{font-family:var(--mono);font-size:.65rem;padding:2px 8px;border-radius:4px;border:1px solid;letter-spacing:.04em}
    .tag-index{border-color:var(--accent);color:var(--accent);background:rgba(0,200,255,.06)}.tag-type{border-color:var(--border2);color:var(--muted)}
    .tag-green{border-color:var(--green);color:var(--green);background:rgba(16,185,129,.06)}.tag-red{border-color:var(--red);color:var(--red);background:rgba(239,68,68,.06)}
    .block-ts{font-size:.7rem;color:var(--muted);font-family:var(--mono);margin-left:auto}
    .block-fields{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:.4rem 1.25rem;font-size:.8rem;margin-bottom:.6rem}
    .block-fields .f span{font-size:.68rem;color:var(--muted);display:block}
    .hash-strip{font-family:var(--mono);font-size:.6rem;color:var(--muted);padding-top:.6rem;border-top:1px solid var(--border);word-break:break-all}
    .hash-strip strong{color:var(--accent)}
    .form-group{margin-bottom:1rem}label{display:block;font-size:.72rem;color:var(--muted);font-family:var(--mono);margin-bottom:.35rem;letter-spacing:.04em}
    input,select,textarea{width:100%;background:var(--bg);border:1px solid var(--border);color:var(--text);padding:.55rem .85rem;border-radius:5px;font-family:var(--sans);font-size:.85rem;outline:none;transition:border-color .15s}
    input:focus,select:focus,textarea:focus{border-color:var(--accent)}select option{background:var(--surface)}
    .btn{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1.25rem;border-radius:5px;font-size:.8rem;font-family:var(--mono);font-weight:600;cursor:pointer;border:1px solid transparent;transition:all .15s;text-decoration:none;letter-spacing:.03em}
    .btn-primary{background:var(--accent);color:var(--bg);border-color:var(--accent)}.btn-primary:hover{opacity:.85}
    .btn-outline{background:transparent;border-color:var(--accent);color:var(--accent)}.btn-outline:hover{background:rgba(0,200,255,.08)}
    .btn-danger{background:transparent;border-color:var(--red);color:var(--red)}.btn-danger:hover{background:rgba(239,68,68,.08)}
    .btn-amber{background:transparent;border-color:var(--cus);color:var(--cus)}.btn-amber:hover{background:rgba(245,158,11,.08)}
    .btn-green{background:transparent;border-color:var(--green);color:var(--green)}.btn-green:hover{background:rgba(16,185,129,.08)}
    .btn-sm{padding:.3rem .85rem;font-size:.72rem}
    .alert{padding:.75rem 1rem;border-radius:6px;font-size:.82rem;margin-bottom:1.25rem;border:1px solid}
    .alert-success{background:rgba(16,185,129,.07);border-color:var(--green);color:var(--green)}
    .alert-error{background:rgba(239,68,68,.07);border-color:var(--red);color:var(--red)}
    .alert-tamper{background:rgba(239,68,68,.12);border-color:var(--red);color:var(--red);font-family:var(--mono);font-size:.78rem}
    .alert-info{background:rgba(0,200,255,.06);border-color:var(--accent);color:var(--accent)}
    .chain-link{text-align:center;color:var(--border2);font-family:var(--mono);font-size:.8rem;margin:.1rem 0;letter-spacing:.1em}
    a.shp-link{font-size:.72rem;color:var(--imp);text-decoration:none;font-family:var(--mono)}a.shp-link:hover{text-decoration:underline}
    .divider{border:none;border-top:1px solid var(--border);margin:1.5rem 0}
    .block-scroll{max-height:440px;overflow-y:auto;padding-right:4px}
    .block-scroll::-webkit-scrollbar{width:4px}.block-scroll::-webkit-scrollbar-track{background:transparent}.block-scroll::-webkit-scrollbar-thumb{background:var(--border2);border-radius:4px}
  </style>
</head>
<body>
{% if session.user %}
<nav style="--accent: {{ 'var(--exp)' if session.user.role == 'exporter' else ('var(--imp)' if session.user.role == 'importer' else 'var(--cus)') }}">
  <a class="nav-brand" href="/dashboard">⬡ TRADECHAIN</a>
  <span class="nav-badge">{{ session.user.role | upper }}</span>
  <a class="nav-link" href="/dashboard">Dashboard</a>
  <a class="nav-link" href="/api/chain" target="_blank">API</a>
  <div class="nav-spacer"></div>
  <div class="nav-user"><span>{{ session.user.name }}</span><span style="color:var(--muted)">{{ session.user.company }}</span></div>
  <a class="btn-logout" href="/logout">logout</a>
</nav>
{% endif %}
<div class="page">
  {% with messages = get_flashed_messages(with_categories=true) %}
    {% for category, message in messages %}
      <div class="alert alert-{{ category }}">{{ message }}</div>
    {% endfor %}
  {% endwith %}
  {% block content %}{% endblock %}
</div>
</body>
</html>"""

templates['login.html'] = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>TradeChain — Login</title>
  <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet"/>
  <style>
    :root{--bg:#070b0f;--surface:#0d1117;--panel:#111820;--border:#1e2d3d;--accent:#00c8ff;--red:#ef4444;--text:#cdd9e5;--muted:#566a7f;--mono:'Share Tech Mono',monospace;--sans:'DM Sans',sans-serif}
    *{box-sizing:border-box;margin:0;padding:0}html,body{height:100%;background:var(--bg);color:var(--text);font-family:var(--sans)}
    body::before{content:'';position:fixed;inset:0;background-image:linear-gradient(var(--border) 1px,transparent 1px),linear-gradient(90deg,var(--border) 1px,transparent 1px);background-size:40px 40px;opacity:.2;pointer-events:none}
    .wrap{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:2rem;position:relative}
    .card{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:2.5rem;width:100%;max-width:420px}
    .logo{font-family:var(--mono);font-size:1.1rem;color:var(--accent);letter-spacing:.1em;margin-bottom:.3rem}.logo-sub{font-size:.75rem;color:var(--muted);margin-bottom:2rem}
    .accounts{background:var(--surface);border:1px solid var(--border);border-radius:6px;padding:1rem;margin-bottom:1.75rem}
    .accounts-title{font-family:var(--mono);font-size:.65rem;color:var(--muted);letter-spacing:.08em;text-transform:uppercase;margin-bottom:.75rem}
    .account-row{display:flex;justify-content:space-between;align-items:center;padding:.35rem 0;border-bottom:1px solid var(--border);cursor:pointer}
    .account-row:last-child{border-bottom:none}.account-row:hover .account-name{color:var(--accent)}
    .account-name{font-family:var(--mono);font-size:.78rem;transition:color .15s}
    .account-role{font-size:.65rem;padding:1px 8px;border-radius:10px;font-family:var(--mono);border:1px solid}
    .role-exp{border-color:#00c8ff;color:#00c8ff;background:rgba(0,200,255,.07)}.role-imp{border-color:#a78bfa;color:#a78bfa;background:rgba(167,139,250,.07)}.role-cus{border-color:#f59e0b;color:#f59e0b;background:rgba(245,158,11,.07)}
    .account-pw{font-size:.68rem;color:var(--muted)}
    .form-group{margin-bottom:1rem}label{display:block;font-size:.72rem;color:var(--muted);font-family:var(--mono);margin-bottom:.35rem}
    input{width:100%;background:var(--bg);border:1px solid var(--border);color:var(--text);padding:.6rem .9rem;border-radius:5px;font-family:var(--sans);font-size:.875rem;outline:none;transition:border-color .15s}input:focus{border-color:var(--accent)}
    .btn{width:100%;padding:.65rem;border-radius:5px;font-family:var(--mono);font-size:.85rem;font-weight:600;background:var(--accent);color:var(--bg);border:none;cursor:pointer;letter-spacing:.05em;transition:opacity .15s;margin-top:.5rem}.btn:hover{opacity:.85}
    .alert{padding:.7rem .9rem;border-radius:5px;font-size:.8rem;margin-bottom:1rem;border:1px solid var(--red);background:rgba(239,68,68,.07);color:var(--red)}
  </style>
</head>
<body>
<div class="wrap"><div class="card">
  <div class="logo">⬡ TRADECHAIN</div>
  <div class="logo-sub">Blockchain Trade Documentation Simulator</div>
  {% with messages = get_flashed_messages(with_categories=true) %}
    {% for category, message in messages %}<div class="alert">{{ message }}</div>{% endfor %}
  {% endwith %}
  <div class="accounts">
    <div class="accounts-title">Demo Accounts — click to fill</div>
    <div class="account-row" onclick="fill('exporter','export123')"><span class="account-name">exporter</span><span class="account-role role-exp">Exporter</span><span class="account-pw">export123</span></div>
    <div class="account-row" onclick="fill('importer','import123')"><span class="account-name">importer</span><span class="account-role role-imp">Importer</span><span class="account-pw">import123</span></div>
    <div class="account-row" onclick="fill('customs','customs123')"><span class="account-name">customs</span><span class="account-role role-cus">Customs</span><span class="account-pw">customs123</span></div>
  </div>
  <form method="POST">
    <div class="form-group"><label>USERNAME</label><input type="text" name="username" id="username" placeholder="username" autocomplete="off" required/></div>
    <div class="form-group"><label>PASSWORD</label><input type="password" name="password" id="password" placeholder="password" required/></div>
    <button type="submit" class="btn">ENTER SIMULATOR →</button>
  </form>
</div></div>
<script>function fill(u,p){document.getElementById('username').value=u;document.getElementById('password').value=p;}</script>
</body></html>"""

templates['exporter.html'] = """{% extends "base.html" %}
{% block content %}
<style>:root{--accent:var(--exp)}.dynamic-fields{display:none;margin-top:1rem}</style>
<div class="section-head"><h1>// EXPORTER DASHBOARD</h1><p>Submit trade documents to the blockchain — {{ user.company }}</p></div>
<div class="grid-3" style="margin-bottom:1.5rem">
  <div class="stat"><div class="stat-val" style="color:var(--exp)">{{ blocks|length }}</div><div class="stat-lbl">Your Submissions</div></div>
  <div class="stat"><div class="stat-val" style="color:var(--exp)">{{ shipment_ids|length }}</div><div class="stat-lbl">Active Shipments</div></div>
  <div class="stat"><div class="stat-val" style="color:var(--green)">✓</div><div class="stat-lbl">Chain Status</div></div>
</div>
<div class="grid-2">
  <div class="panel">
    <div class="panel-title">Submit Document to Blockchain</div>
    <form method="POST" action="/exporter/submit">
      <div class="form-group"><label>Document Type</label>
        <select name="doc_type" id="doc_type" onchange="showFields()">
          <option value="">— Select —</option>
          <option>Bill of Lading</option><option>Certificate of Origin</option><option>Letter of Credit</option><option>Status Update</option>
        </select>
      </div>
      <div class="form-group"><label>Shipment ID</label><input type="text" name="shipment_id" placeholder="e.g. SHP-2024-001" required/></div>
      <div class="dynamic-fields" id="f-bol">
        <div class="form-group"><label>Importer Company</label><input type="text" name="importer" placeholder="Global Traders GmbH"/></div>
        <div class="form-group"><label>Goods Description</label><input type="text" name="goods" placeholder="e.g. Electronic Components"/></div>
        <div class="form-group"><label>Vessel Name</label><input type="text" name="vessel" placeholder="MV Ocean Harmony"/></div>
        <div class="form-group"><label>Origin Port</label><input type="text" name="origin_port" placeholder="Mumbai"/></div>
        <div class="form-group"><label>Destination Port</label><input type="text" name="destination_port" placeholder="Hamburg"/></div>
      </div>
      <div class="dynamic-fields" id="f-coo">
        <div class="form-group"><label>Goods Description</label><input type="text" name="goods" placeholder="e.g. Textile Products"/></div>
        <div class="form-group"><label>Issuing Body</label><input type="text" name="issuing_body" placeholder="FICCI Mumbai"/></div>
      </div>
      <div class="dynamic-fields" id="f-lc">
        <div class="form-group"><label>Applicant (Importer)</label><input type="text" name="applicant" placeholder="Global Traders GmbH"/></div>
        <div class="form-group"><label>Amount</label><input type="text" name="amount" placeholder="75000"/></div>
        <div class="form-group"><label>Currency</label><input type="text" name="currency" placeholder="USD" value="USD"/></div>
        <div class="form-group"><label>Expiry Date</label><input type="date" name="expiry_date"/></div>
        <div class="form-group"><label>Issuing Bank</label><input type="text" name="issuing_bank" placeholder="HDFC Bank"/></div>
      </div>
      <div class="dynamic-fields" id="f-su">
        <div class="form-group"><label>New Status</label>
          <select name="new_status"><option>Documents Prepared</option><option>Goods Ready for Shipment</option><option>Departed Port</option><option>In Transit</option></select>
        </div>
        <div class="form-group"><label>Notes</label><textarea name="notes" rows="2" placeholder="Optional notes..."></textarea></div>
      </div>
      <button type="submit" class="btn btn-primary btn-sm" id="submit-btn" style="display:none;margin-top:.5rem">→ Submit to Blockchain</button>
    </form>
  </div>
  <div class="panel">
    <div class="panel-title">Your Blockchain Submissions</div>
    {% if blocks %}
      <div class="block-scroll">
        {% for b in blocks|reverse %}
          <div class="block-card">
            <div class="block-card-head">
              <span class="tag tag-index">#{{ b.index }}</span><span class="tag tag-type">{{ b.document.type }}</span>
              {% if b.document.shipment_id %}<a class="shp-link" href="/shipment/{{ b.document.shipment_id }}">{{ b.document.shipment_id }} ↗</a>{% endif %}
              <span class="block-ts">{{ b.timestamp }}</span>
            </div>
            <div class="block-fields">{% for k,v in b.document.items() %}{% if k not in ['type','status'] %}<div class="f"><span>{{ k.replace('_',' ').title() }}</span>{{ v }}</div>{% endif %}{% endfor %}</div>
            <div class="hash-strip"><strong>HASH</strong> {{ b.hash }}</div>
          </div>
          {% if not loop.last %}<div class="chain-link">↕</div>{% endif %}
        {% endfor %}
      </div>
    {% else %}<p style="font-size:.82rem;color:var(--muted)">No submissions yet.</p>{% endif %}
  </div>
</div>
<script>
const map={"Bill of Lading":"f-bol","Certificate of Origin":"f-coo","Letter of Credit":"f-lc","Status Update":"f-su"};
function showFields(){document.querySelectorAll('.dynamic-fields').forEach(el=>el.style.display='none');const v=document.getElementById('doc_type').value;if(map[v])document.getElementById(map[v]).style.display='block';document.getElementById('submit-btn').style.display=v?'inline-flex':'none';}
</script>
{% endblock %}"""

templates['importer.html'] = """{% extends "base.html" %}
{% block content %}
<style>:root{--accent:var(--imp)}</style>
<div class="section-head"><h1>// IMPORTER DASHBOARD</h1><p>View incoming shipments and file customs declarations — {{ user.company }}</p></div>
<div class="grid-3" style="margin-bottom:1.5rem">
  <div class="stat"><div class="stat-val" style="color:var(--imp)">{{ blocks|length }}</div><div class="stat-lbl">Documents Received</div></div>
  <div class="stat"><div class="stat-val" style="color:var(--imp)">{{ shipment_ids|length }}</div><div class="stat-lbl">Shipments Tracked</div></div>
  <div class="stat"><div class="stat-val" style="color:var(--green)">✓</div><div class="stat-lbl">Chain Verified</div></div>
</div>
<div class="grid-2">
  <div class="panel">
    <div class="panel-title">File Customs Declaration</div>
    <form method="POST" action="/importer/submit">
      <div class="form-group"><label>Shipment ID</label>
        {% if shipment_ids %}<select name="shipment_id">{% for sid in shipment_ids %}<option value="{{ sid }}">{{ sid }}</option>{% endfor %}</select>
        {% else %}<input type="text" name="shipment_id" placeholder="SHP-2024-001" required/>{% endif %}
      </div>
      <div class="form-group"><label>Goods Description</label><input type="text" name="goods" placeholder="e.g. Electronic Components" required/></div>
      <div class="form-group"><label>Declared Value</label><input type="text" name="declared_value" placeholder="75000" required/></div>
      <div class="form-group"><label>Currency</label><input type="text" name="currency" placeholder="USD" value="USD"/></div>
      <div class="form-group"><label>HS Code</label><input type="text" name="hs_code" placeholder="e.g. 8471.30"/></div>
      <button type="submit" class="btn btn-outline btn-sm" style="margin-top:.25rem">→ Submit Declaration</button>
    </form>
  </div>
  <div class="panel">
    <div class="panel-title">Incoming Documents</div>
    {% if blocks %}
      <div class="block-scroll">
        {% for b in blocks|reverse %}
          <div class="block-card">
            <div class="block-card-head">
              <span class="tag tag-index">#{{ b.index }}</span><span class="tag tag-type">{{ b.document.type }}</span>
              {% if b.document.shipment_id %}<a class="shp-link" href="/shipment/{{ b.document.shipment_id }}">{{ b.document.shipment_id }} ↗</a>{% endif %}
              <span class="block-ts">{{ b.timestamp }}</span>
            </div>
            <div class="block-fields">{% for k,v in b.document.items() %}{% if k not in ['type','status'] %}<div class="f"><span>{{ k.replace('_',' ').title() }}</span>{{ v }}</div>{% endif %}{% endfor %}</div>
            <div class="hash-strip"><strong>HASH</strong> {{ b.hash }}</div>
          </div>
          {% if not loop.last %}<div class="chain-link">↕</div>{% endif %}
        {% endfor %}
      </div>
    {% else %}<p style="font-size:.82rem;color:var(--muted)">No documents found for {{ user.company }} yet.</p>{% endif %}
    {% if shipment_ids %}<hr class="divider"/><div class="panel-title">Quick Shipment Lookup</div><div style="display:flex;flex-wrap:wrap;gap:.5rem">{% for sid in shipment_ids %}<a href="/shipment/{{ sid }}" class="btn btn-outline btn-sm">{{ sid }}</a>{% endfor %}</div>{% endif %}
  </div>
</div>
{% endblock %}"""

templates['customs.html'] = """{% extends "base.html" %}
{% block content %}
<style>:root{--accent:var(--cus)}.tamper-zone{border:1px solid var(--red);border-radius:8px;padding:1.25rem;background:rgba(239,68,68,.04)}.verify-zone{border:1px solid {% if errors %}var(--red){% else %}var(--green){% endif %};border-radius:8px;padding:1.25rem;background:{% if errors %}rgba(239,68,68,.04){% else %}rgba(16,185,129,.04){% endif %}}.error-block{background:var(--surface);border:1px solid var(--red);border-radius:6px;padding:.875rem 1rem;margin-bottom:.6rem;font-family:var(--mono);font-size:.72rem}.error-block .err-type{color:var(--red);margin-bottom:.3rem;font-size:.68rem}.error-block .err-msg{color:var(--text);margin-bottom:.5rem;font-size:.8rem;font-family:var(--sans)}.err-hash{color:var(--muted);font-size:.62rem;word-break:break-all}</style>
<div class="section-head"><h1>// CUSTOMS AUTHORITY DASHBOARD</h1><p>Verify chain integrity, inspect all trade documents, and clear shipments — {{ user.company }}</p></div>
<div class="grid-3" style="margin-bottom:1.5rem">
  <div class="stat"><div class="stat-val" style="color:var(--cus)">{{ chain_length }}</div><div class="stat-lbl">Total Blocks</div></div>
  <div class="stat"><div class="stat-val" style="color:var(--cus)">{{ shipment_ids|length }}</div><div class="stat-lbl">Shipments on Ledger</div></div>
  <div class="stat"><div class="stat-val" style="color:{% if errors %}var(--red){% else %}var(--green){% endif %}">{% if errors %}✗{% else %}✓{% endif %}</div><div class="stat-lbl">Chain Integrity</div></div>
</div>
<div class="grid-2" style="margin-bottom:1.25rem">
  <div class="verify-zone">
    <div class="panel-title" style="border-bottom-color:{% if errors %}var(--red){% else %}var(--green){% endif %};color:{% if errors %}var(--red){% else %}var(--green){% endif %}">Chain Verification</div>
    {% if errors %}
      <div style="margin-bottom:1rem">{% for err in errors %}<div class="error-block"><div class="err-type">⚠ {{ err.type }} — Block #{{ err.block }}</div><div class="err-msg">{{ err.message }}</div><div class="err-hash">STORED&nbsp;&nbsp; {{ err.stored }}<br>EXPECTED {{ err.expected }}</div></div>{% endfor %}</div>
      <form method="POST" action="/customs/restore"><button class="btn btn-green btn-sm">↺ Restore Chain Integrity</button></form>
    {% else %}
      <div style="text-align:center;padding:1.25rem 0"><div style="font-size:2.5rem;margin-bottom:.5rem">🔒</div><div style="font-family:var(--mono);color:var(--green);font-size:.82rem">ALL {{ chain_length }} BLOCKS VERIFIED</div><div style="font-size:.75rem;color:var(--muted);margin-top:.3rem">Every hash matches. Every link is intact.</div></div>
    {% endif %}
  </div>
  <div class="tamper-zone">
    <div class="panel-title" style="border-bottom-color:var(--red);color:var(--red)">⚠ Fraud Simulation Demo</div>
    <p style="font-size:.8rem;color:var(--muted);margin-bottom:1rem;line-height:1.6">Simulate a real-world fraud attack — directly alters a financial value in the ledger file. Then verify to see the blockchain catch it instantly.</p>
    <div style="display:flex;gap:.75rem;flex-wrap:wrap">
      <form method="POST" action="/customs/tamper"><button class="btn btn-danger btn-sm">⚡ Simulate Tamper Attack</button></form>
      <form method="POST" action="/customs/restore"><button class="btn btn-green btn-sm">↺ Restore Chain</button></form>
    </div>
    <p style="font-size:.7rem;color:var(--muted);margin-top:.875rem;font-family:var(--mono)">After tampering → check the verification panel on the left.</p>
  </div>
</div>
<div class="grid-2" style="margin-bottom:1.25rem">
  <div class="panel">
    <div class="panel-title">Clear a Shipment</div>
    <form method="POST" action="/customs/clear" style="display:flex;gap:.75rem;flex-wrap:wrap;align-items:flex-end">
      <div class="form-group" style="flex:1;margin-bottom:0"><label>Shipment ID</label>
        {% if shipment_ids %}<select name="shipment_id">{% for sid in shipment_ids %}<option>{{ sid }}</option>{% endfor %}</select>
        {% else %}<input type="text" name="shipment_id" placeholder="SHP-2024-001"/>{% endif %}
      </div>
      <button type="submit" class="btn btn-amber btn-sm">✓ Issue Clearance</button>
    </form>
  </div>
  <div class="panel">
    <div class="panel-title">Shipment Document Trail</div>
    {% if shipment_ids %}<div style="display:flex;flex-wrap:wrap;gap:.5rem">{% for sid in shipment_ids %}<a href="/shipment/{{ sid }}" class="btn btn-outline btn-sm">{{ sid }} ↗</a>{% endfor %}</div>
    {% else %}<p style="font-size:.82rem;color:var(--muted)">No shipments on the ledger yet.</p>{% endif %}
  </div>
</div>
<div class="panel">
  <div class="panel-title">Full Blockchain Ledger ({{ chain|length }} blocks)</div>
  <div class="block-scroll">
    {% for block in chain|reverse %}
      <div class="block-card" style="{% for e in errors %}{% if e.block == block.index %}border-color:var(--red);{% endif %}{% endfor %}">
        <div class="block-card-head">
          <span class="tag tag-index">#{{ block.index }}</span>
          {% if block.document.type == "GENESIS" %}<span class="tag" style="border-color:var(--muted);color:var(--muted)">Genesis</span>
          {% else %}<span class="tag tag-type">{{ block.document.type }}</span>{% endif %}
          {% if block.document.shipment_id %}<a class="shp-link" href="/shipment/{{ block.document.shipment_id }}">{{ block.document.shipment_id }} ↗</a>{% endif %}
          <span style="font-size:.7rem;color:var(--muted);font-family:var(--mono)">by {{ block.submitted_by }}</span>
          <span class="block-ts">{{ block.timestamp }}</span>
          {% for err in errors %}{% if err.block == block.index %}<span class="tag tag-red">⚠ TAMPERED</span>{% endif %}{% endfor %}
        </div>
        {% if block.document.type != "GENESIS" %}
          <div class="block-fields">{% for k,v in block.document.items() %}{% if k != 'type' %}<div class="f"><span>{{ k.replace('_',' ').title() }}</span>{{ v }}</div>{% endif %}{% endfor %}</div>
        {% else %}<div style="font-size:.78rem;color:var(--muted)">{{ block.document.message }}</div>{% endif %}
        <div class="hash-strip"><strong>HASH</strong> {{ block.hash }}&nbsp;&nbsp;<strong>PREV</strong> {{ block.previous_hash }}</div>
      </div>
      {% if not loop.last %}<div class="chain-link">↕</div>{% endif %}
    {% endfor %}
  </div>
</div>
{% endblock %}"""

templates['shipment.html'] = """{% extends "base.html" %}
{% block content %}
<style>:root{--accent:{% if session.user.role == 'exporter' %}var(--exp){% elif session.user.role == 'importer' %}var(--imp){% else %}var(--cus){% endif %}}</style>
<div class="section-head"><h1>// SHIPMENT — {{ shipment_id }}</h1><p>Complete blockchain document trail for this shipment</p></div>
{% if history %}
  <div class="panel" style="margin-bottom:1.25rem">
    <div class="panel-title">Document Timeline ({{ history|length }} records)</div>
    <div style="display:flex;gap:.75rem;flex-wrap:wrap">
      {% for b in history %}<div style="display:flex;align-items:center;gap:.5rem"><span class="tag tag-index">#{{ b.index }}</span><span style="font-size:.75rem;color:var(--muted)">{{ b.document.type }}</span>{% if not loop.last %}<span style="color:var(--border2);font-family:var(--mono)">→</span>{% endif %}</div>{% endfor %}
    </div>
  </div>
  {% for b in history %}
    <div class="block-card">
      <div class="block-card-head">
        <span class="tag tag-index">#{{ b.index }}</span><span class="tag tag-type">{{ b.document.type }}</span>
        {% if b.document.get('new_status') == 'Customs Cleared' %}<span class="tag tag-green">CLEARED</span>{% endif %}
        <span class="block-ts">{{ b.timestamp }}</span>
      </div>
      <div class="block-fields">{% for k,v in b.document.items() %}{% if k not in ['type','shipment_id'] %}<div class="f"><span>{{ k.replace('_',' ').title() }}</span>{{ v }}</div>{% endif %}{% endfor %}</div>
      <div class="hash-strip"><strong>HASH</strong> {{ b.hash }}<br><strong>PREV</strong> {{ b.previous_hash }}</div>
    </div>
    {% if not loop.last %}<div class="chain-link">↕</div>{% endif %}
  {% endfor %}
{% else %}<div class="alert alert-info">No documents found for shipment {{ shipment_id }}.</div>{% endif %}
<div style="margin-top:1.5rem"><a href="/dashboard" class="btn btn-outline btn-sm">← Back to Dashboard</a></div>
{% endblock %}"""

os.makedirs('templates', exist_ok=True)
for filename, content in templates.items():
    with open(f'templates/{filename}', 'w') as f:
        f.write(content)
    print(f'✓ Created templates/{filename}')

print('\\nAll templates created! Now run: python3 app.py')
