from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI()

BASE = "https://raw.githubusercontent.com/lukysrma/ml_lab/main/programs"

PROGRAMS = {
    1:  "Histograms & Box Plots — California Housing Dataset",
    2:  "Correlation Matrix & Heatmap — California Housing Dataset",
    3:  "Principal Component Analysis (PCA) — Iris Dataset",
    4:  "Find-S Algorithm — Hypothesis from CSV",
    5:  "K-Nearest Neighbors (KNN) Classifier",
    6:  "Linear & Polynomial Regression",
    7:  "Decision Tree Classifier",
    8:  "Naive Bayes Classifier",
    9:  "K-Means Clustering",
    10: "Support Vector Machine (SVM)",
}

# ── Short URLs: /p1 to /p10 ──
@app.get("/p{num}")
def load_program(num: int):
    return RedirectResponse(url=f"{BASE}/p{num}.py")

# ── Home page ──
@app.get("/", response_class=HTMLResponse)
def home():
    rows = ""
    for i, topic in PROGRAMS.items():
        url = f"https://ml-lab-xxxx.onrender.com/p{i}"
        rows += f"""
        <li>
            <a href="/p{i}">
                <span class="num">P{i}</span>
                <span class="topic">{topic}</span>
                <span class="cmd">%load {url}</span>
            </a>
        </li>"""

    return f"""<!DOCTYPE html>
<html>
<head>
    <title>VTU ML Lab BCSL606</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Segoe UI', Arial, sans-serif;
                background: #1e1e1e; color: #d4d4d4;
                max-width: 800px; margin: 50px auto; padding: 0 20px; }}
        h1   {{ color: #569cd6; font-size: 20px; margin-bottom: 6px; }}
        p    {{ color: #808080; font-size: 13px; margin-bottom: 28px; }}
        ul   {{ list-style: none; padding: 0; }}
        li   {{ margin: 10px 0; }}
        a    {{ display: flex; align-items: center; gap: 14px;
                padding: 14px 18px; background: #252526;
                border: 1px solid #3a3a3a; border-radius: 8px;
                text-decoration: none; transition: all 0.15s; }}
        a:hover {{ background: #2d2d2d; border-color: #569cd6; }}
        .num   {{ background: #0e639c; color: #fff; font-size: 12px;
                  padding: 3px 10px; border-radius: 4px; min-width: 32px;
                  text-align: center; font-weight: 600; }}
        .topic {{ color: #9cdcfe; font-size: 14px; flex: 1; }}
        .cmd   {{ color: #4ec9b0; font-size: 12px; font-family: monospace; }}
    </style>
</head>
<body>
    <h1>VTU ML Lab — BCSL606</h1>
    <p>Click a program or paste the %load command into Jupyter Notebook to load the code</p>
    <ul>{rows}</ul>
</body>
</html>"""