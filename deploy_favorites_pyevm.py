import boa
from boa.contracts.vyper.vyper_contract import VyperContract

def main():
    print("Let us read in the Vyper Code and Deploy it")
    favorites_contract:VyperContract = boa.load("favorites.vy")

    #For a Vyper view function, we can just call it directly without a transaction
    starting_favorite_number:int = favorites_contract.retrieve()
    print(f"Starting favorite number is: {starting_favorite_number}")   

    print("Now let us update the favorite number")
    favorites_contract.store(42) #This sends a transaction
    ending_favorite_number:int = favorites_contract.retrieve()
    print(f"Ending favorite number is: {ending_favorite_number}")   

if __name__ == "__main__":
    main()
