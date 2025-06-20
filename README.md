<p align="center">
  <h1 align="center">💹 STOCK_MARKET_AI_AGENT</h1>
  <p align="center"><em>Empowering Smarter Investments with AI-Driven Insights</em></p>
  <p align="center">
    <img src="https://img.shields.io/badge/last%20commit-today-brightgreen?style=flat-square" alt="Last Commit">
    <img src="https://img.shields.io/badge/python-100%25-blue?style=flat-square" alt="Python">
    <img src="https://img.shields.io/badge/languages-1-important?style=flat-square" alt="Languages">
  </p>
  <p align="center"><strong>Built with the tools and technologies:</strong></p>
  <p align="center">
    <img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white" alt="Markdown Badge"/>
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit Badge"/>
    <img src="https://img.shields.io/badge/LangChain-1a1a1a?style=for-the-badge&logoColor=white" alt="LangChain Badge"/>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  </p>
</p>

---

## 🧠 About the Project

**Stock Market AI Agent** is a conversational AI assistant built with LangChain, Groq LLM, and Streamlit that understands natural language queries about stock market data. It provides real-time company insights, financials, market sentiment, and more using the yfinance API.

---

## 🚀 Run It

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/chakshugupta774/Stock_Market_AI_Agent.git
cd Stock_Market_AI_Agent
```

### 2️⃣ Create a Virtual Environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac
.venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables

Create a `.env` file in the root directory and add:

```env
GROQ_API_KEY=your_groq_api_key
```

### 5️⃣ Run in Terminal (CLI Mode)

```bash
python main.py
```

### 6️⃣ Run in Browser (Streamlit UI)

```bash
streamlit run app.py
```

## 🔍 Example Questions You Can Ask

* "What is the last dividend date of Apple?"
* "Who are the top institutional holders of Tesla?"
* "Has Google received any recent stock upgrades?"
* "Show recent stock news for Microsoft"
* "Show stock splits for Amazon"

## 📦 Features

* 📊 Company info: address, sector, market cap, etc.
* 📆 Last dividend & earnings dates
* 🏛 Institutional and mutual fund holders
* 📈 Stock upgrades/downgrades
* 📰 Latest stock news
* 🧾 Historical stock splits
* 🗂 Coming soon: PDF/CSV export, memory, and Docker support

## 🗂 Project Structure

```
📁 Stock_Market_AI_Agent/
│
├── agent/
│   └── agent_executor.py      # Sets up agent, LLM, tools
│
├── tools/
│   ├── company_info.py        # Company profile info
│   ├── dividends_earnings.py  # Dividend/earnings tool
│   ├── institutional_holders.py # Institutional holders
│   ├── mutual_funds.py        # Mutual fund holders
│   ├── upgrades_downgrades.py # Analyst upgrades
│   ├── stock_news.py          # News articles
│   └── stock_splits.py        # Historical stock splits
│
├── app.py                     # Streamlit app
├── main.py                    # Terminal CLI app
├── .env                       # API key (not pushed to Git)
├── .gitignore                 # Ignore envs, secrets, etc.
├── requirements.txt           # Python dependencies
└── README.md
```

## 📊 APIs Used

| API | Purpose |
|-----|---------|
| `yFinance` | Fetch real-time stock & company data |
| `Groq` | LLM for natural language reasoning |
| `LangChain` | Agent and tool routing framework |

## 📌 Future Enhancements

* Export responses to PDF or CSV
* Add conversational memory (LangChain Memory)
* Dockerize the app for deployment
* Error handling for API limits and timeouts

## 👨‍💻 Author

**Chakshu Gupta**
- 🔗 [GitHub](https://github.com/chakshugupta774)
- 📬 chakshugupta774@gmail.com
