#!/usr/bin/env python3
"""
AI × 3D列印 產品一條龍設計 - 整合版
直接對接 Streamlit 整合後的單一網址
"""

from flask import Flask, redirect, abort
import os

app = Flask(__name__)

STREAMLIT_URL = 'https://3dprint4-1-npmssr63lenh2nyloetqdu.streamlit.app/'

@app.route('/')
def index():
    # 直接跳轉到 Streamlit 整合版
    return redirect(STREAMLIT_URL, code=302)

@app.route('/<path:path>')
def catch_all(path):
    # 其他路徑也轉到 Streamlit
    return redirect(STREAMLIT_URL, code=302)

if __name__ == '__main__':
    app.run(debug=True, port=5000)