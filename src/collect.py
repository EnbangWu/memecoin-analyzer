# src/collect.py
import os
from solana.rpc.api import Client
from solana.rpc.types import TokenAccountOpts
from dotenv import load_dotenv
import time

load_dotenv()

def fetch_new_tokens():
    """Fetch new memecoins launched on Pump.fun."""
    rpc_url = os.getenv("SOLANA_RPC_URL")
    if not rpc_url:
        raise ValueError("SOLANA_RPC_URL not set in .env")
    client = Client(rpc_url)
    
    if not client.is_connected():
        print("Failed to connect to Solana RPC")
        return []

    print(f"Connected to Solana RPC at {rpc_url}")
    # Get latest block
    latest_block = client.get_latest_blockhash()
    block_height = latest_block.value.last_valid_block_height
    print(f"Scanning block height: {block_height}")

    # TODO: Query Pump.fun program logs (replace with actual program ID)
    pump_fun_program_id = "6EF8rrecthR5Dkzon8Nwu78hRvfL9z5kC46WweiiUkt"  # Example
    # For now, simulate token detection
    return [
        {
            "name": f"PUMP_TOKEN_{int(time.time())}",
            "address": "0x_simulated_address",
            "launch_time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }
    ]

if __name__ == "__main__":
    tokens = fetch_new_tokens()
    print(tokens)