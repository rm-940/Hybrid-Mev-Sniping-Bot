import random
from utils import get_wallet_balance, send_transaction, calculate_gas_fee
from config import PROFIT_GOAL, STOP_LOSS, MAX_TRADES_AT_ONCE

active_trades = []

def execute_strategy(market_data):
    global active_trades

    trades_this_round = 0
    results = []

    for coin in market_data:
        if trades_this_round >= MAX_TRADES_AT_ONCE:
            break

        symbol = coin["symbol"]
        safety_score = coin["safety"]
        trending_score = coin["trending"]
        sentiment_score = coin["sentiment"]

        # Filter based on safety and trend quality
        if safety_score < 0.7 or trending_score < 0.6:
            continue

        # Simulate profit prediction (can be replaced with ML later)
        predicted_profit = random.uniform(0.2, 0.8)

        if predicted_profit >= PROFIT_GOAL:
            # Smart sizing based on wallet balance
            balance = get_wallet_balance()
            entry_amount = balance * 0.1  # use 10% of balance per trade

            gas_fee = calculate_gas_fee(balance)

            # Execute trade
            tx_result = send_transaction(
                coin_address=coin["address"],
                amount=entry_amount,
                gas=gas_fee
            )

            # Hold or auto-sell decision
            hold = trending_score > 0.85 and sentiment_score > 0.75
            trade = {
                "symbol": symbol,
                "entry_price": coin["price"],
                "amount": entry_amount,
                "hold": hold,
                "tx_hash": tx_result["hash"]
            }

            active_trades.append(trade)
            trades_this_round += 1
            results.append(f"✅ Bought {symbol} for ${entry_amount:.2f}")

    return results
