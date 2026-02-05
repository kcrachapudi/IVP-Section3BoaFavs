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

    boolean_contract = boa.load("boolean.vy")

    current_num = boolean_contract.get_num()
    print(f"Current number value: {current_num}")

    boolean_contract.set_num(100)

    new_num = boolean_contract.get_num()
    print(f"New number value: {new_num}")
    
    """
    current_bool = boolean_contract.get_bool()
    print(f"Current boolean value: {current_bool}")

    boolean_contract.set_bool("True")

    new_bool = boolean_contract.get_bool()
    print(f"New boolean value: {new_bool}")
    """

if __name__ == "__main__":
    main()