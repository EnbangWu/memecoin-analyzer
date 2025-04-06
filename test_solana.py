from solana.rpc.api import Client
client = Client('https://api.mainnet-beta.solana.com')
print(client.is_connected())
