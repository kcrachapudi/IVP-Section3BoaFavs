import boa
from dotenv import load_dotenv
import os
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account

load_dotenv()

def main():
    rpc_url = os.getenv("RPC_URL")
    print(f"Using RPC URL: {rpc_url}")

    networkEnv = NetworkEnv(EthereumRPC(rpc_url))
    boa.set_env(networkEnv)

    account = Account.from_key(os.getenv("ANVIL_KEY"))
    boa.env.add_account(account, force_eoa=True)

    favorites_contract = boa.load("favorites.vy")
    starting_favorite_number = favorites_contract.retrieve()
    print(f"Starting favorite number: {starting_favorite_number}")

    print("Updating favorite number")
    favorites_contract.store(42)
    ending_favorite_number = favorites_contract.retrieve()
    print(f"Ending favorite number: {ending_favorite_number}")  
    
if __name__ == "__main__":
    main()