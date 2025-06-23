# /bot/config.py

# === Wallet Config ===
WALLET_PRIVATE_KEY = "your_private_key_here"
WALLET_ADDRESS = "your_wallet_address_here"
WALLET_BALANCE = 1.2  # Starting balance in SOL (update dynamically later)

# === API Keys ===
GMGN_API_KEY = "your_gmgn_api_key_here"
RUGCHECK_API = "https://api.rugcheck.xyz/"
TWITTER_USERS = ["elonmusk", "realDonaldTrump", "cz_binance"]

# === Trade Thresholds ===
PROFIT_TARGET = 50  # 50% gain per trade
STOP_LOSS = 20      # 20% drop triggers exit
MAX_HOLD_HOURS = 6  # Max hold if not auto-selling

# === Strategy Flags ===
ENABLE_SNIPING = True
ENABLE_ARBITRAGE = True
ENABLE_BACKRUNNING = True
ENABLE_MULTI_TRADE = True

# === Memecoin Logic ===
MEME_KEYWORDS = [
    "pepe", "doge", "elon", "trump", "shib", "baby", "cat", "banana", "frog" ,"dog"
]
