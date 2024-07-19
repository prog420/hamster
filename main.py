import math
import time

import requests

from env import Env


BASE_URL = "https://api.hamsterkombatgame.io"
TAP_URL = f"{BASE_URL}/clicker/tap"
ACC_INFO_URL = f"{BASE_URL}/auth/account-info"
SYNC_URL = f"{BASE_URL}/clicker/sync"
CONFIG_URL = f"{BASE_URL}/clicker/config"

BEARER_TOKEN = f"Bearer {Env.BEARER_TOKEN}"

headers = {"Authorization": BEARER_TOKEN, "Content-Type": "application/json"}

requests.post(url=ACC_INFO_URL, headers=headers)
time.sleep(1)
requests.post(url=SYNC_URL, headers=headers)
time.sleep(1)
requests.post(url=CONFIG_URL, headers=headers)

# Set tap count to 1 and send request to check available taps.
payload = {"count": 1, "availableTaps": 9000, "timestamp": 1721320096}
response = requests.post(url=TAP_URL, headers=headers, json=payload)

# Update payload
available_taps = response.json()["clickerUser"]["availableTaps"]
payload["count"] = 1000
payload["availableTaps"] = available_taps

print(f"Available Taps: {available_taps}")

# Use all available taps
for i in range(math.ceil(available_taps / 1000)):
    time.sleep(2)
    response = requests.post(url=TAP_URL, headers=headers, json=payload)
