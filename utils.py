# /bot/utils.py

import requests
import logging
from config import RUGCHECK_URL, GMGN_API_KEY

def log(message):
    print(f"[LOG] {message}")
    logging.info(message)

def call_gmgn_api():
    url = f"https://api.gmgn.ai/v1/trending?chain=sol&key={GMGN_API_KEY}"
    try:
        res = requests.get(url)
        return res.json()
    except Exception as e:
        log(f"GMGN API Error: {e}")
        return []

def check_rugcheck(contract_address):
    try:
        res = requests.get(f"{RUGCHECK_URL}/check/{contract_address}")
        return res.json()
    except Exception as e:
        log(f"RugCheck Error: {e}")
        return {"is_safe": False}

def adjust_gas_fee(wallet_balance):
    if wallet_balance < 10:
        return 0.1
    elif wallet_balance < 100:
        return 0.3
    else:
        return 0.5
