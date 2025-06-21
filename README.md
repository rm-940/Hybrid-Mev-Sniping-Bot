# 🚀 Hybrid Solana MEV + Sniping Bot (Halal)

An advanced, fully automated crypto trading bot designed for the Solana blockchain. Combines MEV (sniping, arbitrage, backrunning) with real-time market intelligence to maximize profit per trade while avoiding unethical or risky behavior.

## ✅ Features

- 🔥 **Sniping** – Detects and buys new tokens as they launch
- ⚖️ **Arbitrage** – Trades between price differences across Solana DEXes
- 🌀 **Backrunning** – Analyzes mempool to find post-transaction opportunities
- 📊 **GMGN API** – Gets trending coin data in real time
- 🛡 **RugCheck.xyz** – Verifies coin safety before entering trades
- 🐦 **Twitter Integration** – Scrapes tweets from Elon Musk, Trump, CZ, etc.
- 😂 **Meme Trend Detection** – Analyzes meme trends and coin hype
- 📈 **Profit Target** – 50% profit per trade, 20% stop loss
- 🧠 **Holding Logic** – Holds coins for hours or a day if they show strong potential
- 💸 **Smart Gas Fees** – Gas cost scales with wallet balance
- ⚙️ **Multi-Trade Support** – Runs multiple safe trades at once
- 🧩 **AI Self-Debug Tool** (planned) – Helps maintain bot health and accuracy

## 📁 Project Structure

/bot/
├── main.py # Main bot runner
├── trade_engine.py # Trade execution logic
├── analyze.py # Market and trend analysis
├── utils.py # API helpers and filters
├── config.py # Keys, thresholds, configs
/tasks/
└── scheduler.py # Hourly auto-run for trend updates and actions

## ⚙️ How It Works

1. Every hour, the bot:
   - Scans GMGN for trending coins
   - Checks Twitter/news/meme sentiment
   - Validates safety via RugCheck
   - Calculates if a trade is viable
   - Enters the trade if all logic passes
   - Monitors for dump signals to auto-sell

2. If the coin has high momentum or good news, it **holds**.

3. If multiple trades look profitable, it executes them **simultaneously**.

## 🛠 Requirements

- Python 3.10+
- Phantom Wallet
- GMGN API Key (free)
- Rugcheck.xyz access
- Twitter scraping config (optional for now)

## 🚧 Disclaimer

This project is under active development and is meant for educational and research purposes. Use responsibly.

---

**Made with 💻, 🔁 and ☪️**


