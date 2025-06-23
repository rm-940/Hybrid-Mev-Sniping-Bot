# /bot/config.py
import os
from dotenv import load_dotenv

load_dotenv()

# === Wallet ===
WALLET_PRIVATE_KEY = os.getenv("PRIVATE_KEY")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

# === APIs ===
GMGN_API_KEY = os.getenv("GMGN_API_KEY")

# === Trading Config ===
WALLET_BALANCE = 1.2  # or dynamically update later
PROFIT_TARGET = 50
STOP_LOSS = 20
MAX_HOLD_HOURS = 6

ENABLE_SNIPING = True
ENABLE_ARBITRAGE = True
ENABLE_BACKRUNNING = True
ENABLE_MULTI_TRADE = True

MEME_KEYWORDS = [
    "pepe", "doge", "elon", "trump", "shib", "baby", "cat", "banana", "frog"
]
