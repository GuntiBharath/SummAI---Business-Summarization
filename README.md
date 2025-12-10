# SummAI---Business-Summarization
SummAI is a lightweight NLP-based web app that automatically summarizes long business articles and reports into concise insights. Built using Flask and NLTK, it uses extractive summarization, sentence scoring, and keyword frequency analysis to deliver fast, clear summaries for business and research needs.

SummAI/
│
├── app.py               # Flask backend server
├── summarizer.py        # NLP summarization logic
│
├── templates/
│   └── index.html       # Main UI page
│
└── static/
    └── style.css        # UI styling

🧩 How It Works

SummAI uses extractive summarization:

Splits text into words & sentences
Removes stopwords
Calculates word frequency importance
Scores sentences based on keyword relevance
Selects top sentences as the summary
This approach allows fast, offline summarization without AI API costs.

🛠 Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/GuntiBharath/SummAI---Business-Summarization
cd SummAI

2️⃣ Install Required Packages
Make sure Python 3.8+ is installed, then run:

pip install flask nltk

3️⃣ NLTK Data Download

The first time the app runs, it automatically downloads:
punkt
punkt_tab
stopwords
No additional action needed.

4️⃣ Run the Flask App
python app.py

You should see:
🚀 Flask is running at http://127.0.0.1:5000

5️⃣ Open in Browser
Go to:
http://127.0.0.1:5000
Paste your article → Click Summarize → Done!
