# config.py

# Wallet & RPC
PRIVATE_KEY = "your_private_key_here"
PUBLIC_KEY = "your_wallet_address_here"
RPC_URL = "https://api.mainnet-beta.solana.com"  # Or a faster RPC

# Trading thresholds
PROFIT_TARGET = 0.5  # 50%
STOP_LOSS = 0.2      # 20%

# GMGN API
GMGN_API_KEY = "your_gmgn_api_key_here"

# Rugcheck
RUGCHECK_API = "https://api.rugcheck.xyz/scan/"

# Twitter/News
TWITTER_HANDLES = ["elonmusk", "realDonaldTrump", "cz_binance"]
NEWS_KEYWORDS = ["crypto", "solana", "memecoin", "regulation", "inflation", "USDT", "binance"]

# Bot behavior
GAS_SCALING = True  # Auto adjust based on wallet balance
MAX_CONCURRENT_TRADES = 3

# Holding logic
ENABLE_HOLDING_LOGIC = True
MAX_HOLD_HOURS = 24

# Logging
LOG_FILE = "logs/bot_activity.log"
