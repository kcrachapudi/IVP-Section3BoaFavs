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

    #"Storing a person"    
    favorites_contract.add_person("Alice", 30)
    person_data = favorites_contract.list_of_people(0)
    print(f"Stored Person: {person_data}")

if __name__ == "__main__":
    main()