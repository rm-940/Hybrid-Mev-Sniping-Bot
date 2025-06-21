# /bot/config.py

# Wallet
PRIVATE_KEY = "your_private_key_here"
PUBLIC_KEY = "your_public_key_here"

# Solana RPC
RPC_URL = "https://api.mainnet-beta.solana.com"

# Thresholds
TARGET_PROFIT_PERCENT = 50
STOP_LOSS_PERCENT = 20

# APIs
GMGN_API_KEY = "your_gmgn_api_key_here"
RUGCHECK_URL = "https://api.rugcheck.xyz"
TWITTER_ACCOUNTS = ["elonmusk", "cz_binance", "realdonaldtrump"]

# Trading Settings
MAX_CONCURRENT_TRADES = 4
MIN_CONFIDENCE_TO_TRADE = 0.75  # for holding logic
GAS_FEE_TIERS = {
    "low": 0.1,
    "mid": 0.3,
    "high": 0.5
}
