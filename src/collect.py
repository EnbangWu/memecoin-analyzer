# src/collect.py
import os
from solana.rpc.api import Client
from dotenv import load_dotenv

load_dotenv()

def fetch_new_tokens():
    """Fetch new memecoins launched on Pump.fun (placeholder)."""
    rpc_url = os.getenv("SOLANA_RPC_URL")
    if not rpc_url:
        raise ValueError("SOLANA_RPC_URL not set in .env")
    client = Client(rpc_url)
    if client.is_connected():
        print(f"Connected to Solana RPC at {rpc_url}")
        # TODO: Add Pump.fun contract event monitoring
        return [
            {
                "name": "TEST_TOKEN",
                "address": "0x123",
                "launch_time": "2025-04-06T00:00:00Z"
            }
        ]
    else:
        print("Failed to connect to Solana RPC")
        return []

if __name__ == "__main__":
    tokens = fetch_new_tokens()
    print(tokens)