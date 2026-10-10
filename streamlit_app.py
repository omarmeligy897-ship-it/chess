import streamlit as st
import streamlit.components.v1 as components

# فتح ملف الـ HTML وقراءته وعرضه داخل التطبيق
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# عرض الكود بأبعاد مناسبة للوحة الشطرنج
components.html(html_code, height=500, scrolling=True)
