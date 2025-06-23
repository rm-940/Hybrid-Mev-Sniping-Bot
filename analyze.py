# /bot/analyze.py

import requests
from utils import is_coin_safe, check_twitter_sentiment, detect_meme_pattern

GMGN_API = "https://gmgn.ai/api/trending?chain=sol"

def fetch_trending_coins():
    try:
        response = requests.get(GMGN_API)
        if response.status_code == 200:
            return response.json().get("coins", [])
        else:
            print("GMGN API error:", response.status_code)
            return []
    except Exception as e:
        print("Error fetching trending coins:", e)
        return []

def analyze_market():
    coins = fetch_trending_coins()
    strong_candidates = []

    for coin in coins:
        symbol = coin.get("symbol")
        address = coin.get("address")

        print(f"\n🔍 Analyzing {symbol}...")

        if not is_coin_safe(address):
            print(f"⚠️ {symbol} failed safety check.")
            continue

        if not detect_meme_pattern(symbol):
            print(f"🧩 {symbol} doesn’t match meme trends.")
            continue

        sentiment = check_twitter_sentiment(symbol)
        print(f"💬 Sentiment for {symbol}: {sentiment}")

        if sentiment == "positive":
            strong_candidates.append({
                "symbol": symbol,
                "address": address,
                "score": coin.get("score", 0),
            })

    return strong_candidates
