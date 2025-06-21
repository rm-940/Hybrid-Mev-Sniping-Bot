# /bot/analyze.py

from utils import call_gmgn_api, check_rugcheck, log
from config import TWITTER_ACCOUNTS, MIN_CONFIDENCE_TO_TRADE

import random

def fake_sentiment_analysis(coin_name):
    """Simulate Twitter + meme-based sentiment analysis."""
    # In real version: scrape Twitter, keywords, memes, news, etc.
    positive_keywords = ["🚀", "moon", "bull", "buy", "up only", "next 100x"]
    negative_keywords = ["rug", "dump", "scam", "exit", "sell", "dead"]

    # Fake signal for now
    sentiment_score = random.uniform(0.3, 0.9)
    return sentiment_score

def analyze_market():
    trending_coins = call_gmgn_api()
    selected_coins = []

    if not trending_coins:
        log("No trending coins found.")
        return []

    for coin in trending_coins[:10]:  # limit to top 10
        name = coin.get("name")
        address = coin.get("address")

        log(f"Analyzing coin: {name}")

        # Step 1: Rugcheck
        rugcheck = check_rugcheck(address)
        if not rugcheck.get("is_safe", False):
            log(f"{name} failed rugcheck.")
            continue

        # Step 2: Sentiment (mocked for now)
        sentiment_score = fake_sentiment_analysis(name)
        if sentiment_score < MIN_CONFIDENCE_TO_TRADE:
            log(f"{name} has low sentiment: {sentiment_score}")
            continue

        # Step 3: Passes
        log(f"{name} PASSED analysis with score {sentiment_score}")
        selected_coins.append({
            "name": name,
            "address": address,
            "confidence": sentiment_score
        })

    return selected_coins
