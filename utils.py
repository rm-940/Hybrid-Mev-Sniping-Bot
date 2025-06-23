# /bot/utils.py

import requests
import re

# === 1. Rugcheck Integration ===
def is_coin_safe(address):
    try:
        url = f"https://api.rugcheck.xyz/check?address={address}"
        response = requests.get(url)
        data = response.json()

        return data.get("is_safe", False)  # Change based on actual API response structure
    except Exception as e:
        print(f"Rugcheck failed for {address}: {e}")
        return False


# === 2. Twitter Sentiment Analysis (basic scraping logic) ===
def check_twitter_sentiment(symbol):
    # Placeholder: In production use Twitter API or scraping tool
    # This can be replaced with real sentiment logic
    print(f"Checking Twitter sentiment for ${symbol}...")
    positive_keywords = ["moon", "pump", "bull", "100x", "send it", "gem"]
    negative_keywords = ["rug", "scam", "dump", "exit", "dead"]

    # Simulate based on symbol name
    text = f"{symbol} going to moon pump 100x gem"  # Fake tweet content

    pos = sum(word in text.lower() for word in positive_keywords)
    neg = sum(word in text.lower() for word in negative_keywords)

    if pos > neg:
        return "positive"
    elif neg > pos:
        return "negative"
    else:
        return "neutral"


# === 3. Meme Trend Detection ===
def detect_meme_pattern(symbol):
    meme_keywords = ["elon", "doge", "pepe", "trump", "baby", "moon", "cat", "frog"]
    return any(keyword in symbol.lower() for keyword in meme_keywords)


# === 4. Profit Estimator (optional) ===
def estimate_profit(buy_price, current_price):
    try:
        return ((current_price - buy_price) / buy_price) * 100
    except:
        return 0

