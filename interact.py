import boa
from dotenv import load_dotenv
import os
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account

load_dotenv()

MY_CONTRACT = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

def main():
    rpc_url = os.getenv("RPC_URL")
    print(f"Using RPC URL: {rpc_url}")

    networkEnv = NetworkEnv(EthereumRPC(rpc_url))
    boa.set_env(networkEnv)

    account = Account.from_key(os.getenv("ANVIL_KEY"))
    boa.env.add_account(account, force_eoa=True)

    favorites_deployer = boa.load_partial("favorites.vy")
    favorites_contract = favorites_deployer.at(MY_CONTRACT)

    favorite_number = favorites_contract.retrieve()
    print(f"favorite number: {favorite_number}")

    print("Updating favorite number")
    favorites_contract.store(84)
    favorite_number = favorites_contract.retrieve()
    print(f"favorite number: {favorite_number}")  
    
if __name__ == "__main__":
    main()