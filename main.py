import time
from trade_engine import execute_strategy
from analyze import analyze_market

def run_bot():
    while True:
        print("Analyzing market...")
        market_data = analyze_market()

        print("Executing strategy...")
        trade_result = execute_strategy(market_data)

        time.sleep(3600)  # Wait 1 hour

if __name__ == "__main__":
    run_bot()
