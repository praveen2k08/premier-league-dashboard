# 🌟 Premier League Dashboard

A visually engaging and interactive Streamlit web app that allows users to explore English Premier League 24/25 player statistics. Features include:

Doing it for learning and fun

- Top performer insights (goals, assists, minutes, etc.)
- Player comparison
- AI-powered "Ask Anything" page using LLMs
- Visualizations and player profiles
- Hosted on Render or Streamlit Cloud

---

## 🧰 Architecture Overview

```text
+-------------------+        +--------------------+
|                   |        |                    |
|    User Browser   | <----> |  Streamlit Frontend|
|                   |        |  (Render / Cloud)  |
+-------------------+        +--------------------+
                                        |
                                        v
                           +--------------------------+
                           |      Python Backend      |
                           | - Pandas, Altair         |
                           | - LangChain, OpenAI      |
                           +--------------------------+
                                        |
                +-----------------------+-----------------------+
                |                                               |
        +---------------+                              +-------------------+
        | CSV Dataset   |                              | External APIs     |
        | (Local / Git) |                              | - TheSportsDB     |
        +---------------+                              | - OpenAI GPT      |
                                                       +-------------------+
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/premier-league-dashboard.git
cd premier-league-dashboard
```

### 2. Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Secrets

Create a file named `.streamlit/secrets.toml`:

```toml
SPORTSDB_API_KEY = "your_api_key"

[API_FOOTBALL]
key = "your_api_football_key"

[OPENAI]
api_key = "your_openai_key"
```

### 5. Run Locally

```bash
streamlit run Home.py
```

---

## 🌍 Hosting Options

### Option A: Streamlit Cloud

- Push your code to GitHub
- Connect your repo to [https://streamlit.io/cloud](https://streamlit.io/cloud)
- Reboot or deploy after every commit

### Option B: Render

- Add `render.yaml`
- Set start command:
  ```
  streamlit run Home.py
  ```
- Auto-deploys from GitHub

---

## 🔎 Pages Overview

- `Home.py`: App landing page with intro and stats
- `pages/Top Performers.py`: Filtered top player visualizations
- `pages/Player Compare.py`: Compare players side-by-side
- `pages/Ask Anything.py`: Ask AI about player or stats using OpenAI and TheSportsDB

---

## 📊 Technologies Used

- **Frontend**: Streamlit, Altair
- **Backend**: Python, Pandas
- **ML/AI**: LangChain, OpenAI, PandasAI (optional)
- **Data**: Premier League CSV (Kaggle), TheSportsDB API
- **Hosting**: Streamlit Cloud / Render

---

## ✨ Future Improvements

- Deploy on AWS App Runner / EC2
- Caching API responses
- Add squad insights for each team
- Improve AI query results accuracy

---

## 🙏 Credits

- Dataset: [Kaggle EPL Player Stats 24/25](https://www.kaggle.com/datasets/aesika/english-premier-league-player-stats-2425)
- Player info: [TheSportsDB](https://www.thesportsdb.com)
- LLM support: [OpenAI](https://openai.com)

---

> Built with ❤️ using Streamlit & Open Source APIs

