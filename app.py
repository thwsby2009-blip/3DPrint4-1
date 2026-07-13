#!/usr/bin/env python3
"""
AI × 3D列印 產品一條龍設計 - 整合版
Flask + iframe 嵌入式
"""

from flask import Flask, render_template_string
import os

app = Flask(__name__)

STREAMLIT_URLS = {
    'app':  'https://3dprint-ho8eblp63pzxpzx46kvadw.streamlit.app/',
    'data': 'https://3dprint-rwtaafz663a6wsrdiovbfb.streamlit.app/',
    'dev':  'https://3dprint-hynegl4tctjjqtwp39lgby.streamlit.app/',
    'copy': 'https://3dprint-mjtnxknpifbbc3kradhjrv.streamlit.app/',
}

TABS = [
    ('app',  '3D列印一條龍', '#fbbf24'),
    ('data', '數據分析',      '#60a5fa'),
    ('dev',  'AI發展應用',    '#fb923c'),
    ('copy', '文案全攻略',    '#c084fc'),
]

INDEX_HTML = """\
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI 3D列印 產品一條龍設計</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Segoe UI','Noto Sans TC','Microsoft JhengHei',sans-serif; background: #0f172a; color: #e2e8f0; }
.navbar {
  display: flex; align-items: center; gap: 4px;
  background: #1e293b; padding: 0 16px; height: 52px;
  position: sticky; top: 0; z-index: 100;
  border-bottom: 1px solid #334155; overflow-x: auto;
}
.navbar .logo { font-size: 1.1rem; font-weight: 800; color: #fbbf24; margin-right: auto; white-space: nowrap; }
.tab-btn {
  display: flex; align-items: center; gap: 6px;
  padding: 6px 14px; border-radius: 8px;
  font-size: 0.85rem; font-weight: 600;
  cursor: pointer; text-decoration: none; white-space: nowrap;
  border: 1.5px solid transparent; transition: all 0.2s; background: transparent; color: inherit;
}
.tab-btn:hover { border-color: #475569; }
.tab-btn.active { border-color: currentColor; }
.hero { text-align: center; padding: 40px 20px 20px; }
.hero h1 { font-size: 2rem; font-weight: 800; color: #fbbf24; margin-bottom: 8px; }
.hero p { color: #94a3b8; font-size: 1rem; }
.hero .meta { font-size: 0.8rem; color: #475569; margin-top: 6px; }
.tab-panel { display: none; padding: 20px; }
.tab-panel.active { display: block; }
iframe { width: 100%; height: 90vh; border: none; border-radius: 10px; background: #fff; }
footer { text-align: center; padding: 20px; color: #475569; font-size: 0.8rem; }
footer a { color: #60a5fa; text-decoration: none; }
</style>
</head>
<body>

<nav class="navbar">
  <span class="logo">AI 3D列印 產品一條龍</span>
  <button class="tab-btn active" onclick="showTab('app','#fbbf24',this)">🧊 3D列印一條龍</button>
  <button class="tab-btn" onclick="showTab('data','#60a5fa',this)">📊 數據分析</button>
  <button class="tab-btn" onclick="showTab('dev','#fb923c',this)">🤖 AI發展應用</button>
  <button class="tab-btn" onclick="showTab('copy','#c084fc',this)">✍️ 文案全攻略</button>
</nav>

<div class="hero">
  <h1>AI × 全彩 3D 列印 產品一條龍設計教學</h1>
  <p>從零到電商上架，一個網站整合所有課程模組</p>
  <div class="meta">講師：嚴稑榛 ｜ 勞動部勞動力發展署桃竹苗分署</div>
</div>

<div class="tab-panel active" id="panel-app">
  <iframe src="https://3dprint-ho8eblp63pzxpzx46kvadw.streamlit.app/" loading="lazy"></iframe>
</div>
<div class="tab-panel" id="panel-data">
  <iframe src="https://3dprint-rwtaafz663a6wsrdiovbfb.streamlit.app/" loading="lazy"></iframe>
</div>
<div class="tab-panel" id="panel-dev">
  <iframe src="https://3dprint-hynegl4tctjjqtwp39lgby.streamlit.app/" loading="lazy"></iframe>
</div>
<div class="tab-panel" id="panel-copy">
  <iframe src="https://3dprint-mjtnxknpifbbc3kradhjrv.streamlit.app/" loading="lazy"></iframe>
</div>

<footer>
  <p>AI產品設計與全彩3D列印產品實作班 &nbsp;|&nbsp;
  <a href="https://github.com/thwsby2009-blip/3DPRINT" target="_blank">GitHub</a></p>
</footer>

<script>
function showTab(id, color, btn) {
  document.querySelectorAll('.tab-panel').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
  document.getElementById('panel-' + id).classList.add('active');
  btn.classList.add('active');
  document.querySelector('.hero h1').style.color = color;
  history.replaceState(null, '', '#' + id);
}
const hash = location.hash.slice(1);
if (hash) {
  const btn = document.querySelector('.tab-btn[onclick*="showTab(\\'' + hash + '\'"]');
  if (btn) btn.click();
}
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return INDEX_HTML

if __name__ == '__main__':
    app.run(debug=True, port=5000)