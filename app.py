import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PW Skills Clone", layout="wide")

# This code combines your HTML and CSS so Streamlit displays it perfectly
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: sans-serif; margin: 0; background-color: #f3f7ff; }
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 15px 50px; background: white; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .logo { font-size: 24px; font-weight: bold; color: #1b4697; }
        .hero { text-align: center; padding: 100px 20px; background: white; }
        .hero h1 { font-size: 50px; }
        .blue-text { color: #1b4697; }
        .course-container { display: flex; justify-content: center; gap: 20px; padding: 50px; flex-wrap: wrap; }
        .card { background: white; padding: 30px; border-radius: 10px; width: 250px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #eee; text-align: center; }
        .login-btn { background: #1b4697; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="logo">PW SKILLS</div>
        <button class="login-btn">Login / Register</button>
    </nav>
    <header class="hero">
        <h1>Upskilling Made <span class="blue-text">Affordable</span></h1>
        <button class="login-btn" style="background:#eb5e28; margin-top:20px;" onclick="alert('Redirecting to login...')">View C++ Course</button>
    </header>
    <div class="course-container">
        <div class="card"><h3>Full Stack Web Dev</h3><p>MERN Stack</p></div>
        <div class="card"><h3>Data Science</h3><p>Python & AI</p></div>
        <div class="card"><h3>Java Masters</h3><p>Backend Dev</p></div>
    </div>
</body>
</html>
"""

components.html(html_content, height=1000, scrolling=True)
