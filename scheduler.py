# /tasks/scheduler.py

import time
from bot.analyze import analyze_market
from bot.trade_engine import execute_strategy

def run_scheduled_tasks(interval_seconds=3600):
    while True:
        print("⏰ Running scheduled market analysis and strategy execution...")

        # Step 1: Analyze market
        try:
            market_data = analyze_market()
        except Exception as e:
            print(f"[ERROR] Market analysis failed: {e}")
            market_data = None

        # Step 2: Execute trading strategy if analysis is valid
        if market_data:
            try:
                result = execute_strategy(market_data)
                print(f"[TRADE RESULT] {result}")
            except Exception as e:
                print(f"[ERROR] Strategy execution failed: {e}")

        # Step 3: Wait before repeating
        print(f"🕒 Sleeping for {interval_seconds / 60} minutes...\n")
        time.sleep(interval_seconds)


if __name__ == "__main__":
    run_scheduled_tasks()
