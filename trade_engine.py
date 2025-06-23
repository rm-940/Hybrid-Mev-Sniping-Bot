# /bot/trade_engine.py

import random
from utils import estimate_profit
from config import PROFIT_TARGET, STOP_LOSS, WALLET_BALANCE
from solana.transaction import Transaction
from solana.rpc.api import Client
import requests

# === Connect to Solana ===
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"
client = Client(SOLANA_RPC_URL)

# === Jupiter Trade Execution ===
def execute_trade(symbol, amount):
    try:
        print(f"[Jupiter] Executing trade for {symbol} with {amount} SOL")
        # Simulate trade (replace with Jupiter API integration)
        entry_price = random.uniform(0.001, 0.005)
        exit_price = entry_price * random.uniform(1.3, 1.6)

        profit = estimate_profit(entry_price, exit_price)
        print(f"Profit estimate: {profit:.2f}%")

        if profit >= PROFIT_TARGET:
            print(f"🟢 Target profit hit! Auto-selling {symbol}")
            return {"status": "sold", "profit": profit}
        elif profit <= -STOP_LOSS:
            print(f"🔴 Stop loss triggered. Selling {symbol}")
            return {"status": "stopped", "profit": profit}
        else:
            print(f"🟡 Holding {symbol} — potential for more upside.")
            return {"status": "holding", "profit": profit}

    except Exception as e:
        print(f"❌ Trade error: {e}")
        return {"status": "error", "reason": str(e)}


# === Strategy Execution ===
def execute_strategy(market_data):
    results = []
    max_trades = 2 if market_data["confidence"] == "high" else 1
    trade_amount = calculate_trade_amount(WALLET_BALANCE)

    for token in market_data["tokens"][:max_trades]:
        result = execute_trade(token["symbol"], trade_amount)
        results.append(result)

    return results


# === Adaptive Gas Fee Logic (based on wallet size) ===
def calculate_trade_amount(balance):
    if balance > 10:
        return round(balance * 0.25, 2)
    elif balance > 1:
        return round(balance * 0.5, 2)
    else:
        return round(balance * 0.8, 2)
