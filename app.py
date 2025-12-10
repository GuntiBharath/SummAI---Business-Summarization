from flask import Flask, render_template, request
from summarizer import summarize_text
import os

# Flask settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    input_text = ""

    if request.method == 'POST':
        input_text = request.form.get("custom_text", "")
        summary = summarize_text(input_text)

    return render_template("index.html", summary=summary, input_text=input_text)


if __name__ == '__main__':
    print("🚀 Flask is running at http://127.0.0.1:5000")
    app.run(debug=True)
