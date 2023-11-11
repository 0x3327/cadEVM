# TODO Add easy deploy when the project is not deployed already
# TODO Add agent generating functions
# TODO Add a contract mutable methods  overview functions
# TODO Add datacleaning functions

from ape import Contract
from .connector import connect_fork

class ArgumentsLengthError(Exception):
    pass

# generates initial state variables from the contract
def generate_initial_state(obj):
    initial_state_variables = {}
    for key, method in obj._view_methods_.items():
        if hasattr(obj, key):
            try:
                value = getattr(obj, key)()
                initial_state_variables[key] = value
            except ArgumentsLengthError as e:
                print(f"Error for variable '{key}': {e}")
            except Exception as e:
                print(f"Error for variable '{key}': {e}")
    print("Initial state variable values generated.")
    return initial_state_variables

# TODO fix so it resets the fork and contracts so montecarlo runs can be run
def reset_existing_contract(contract_name,address:str):
    connect_fork()
    print('Connected to a new fork')
    contract_name = Contract(address=address)
    #generate_initial_state(contract_name)
    print('Changed contract instance')
    return contract_name


# pseudo code 
'''
generate_agents(number_of_agents, use_etherscan =True/False, random_balances = True/False, 
generate_relationships,etc ):

use ape accounts to generate balances and agents  ,
or  etherscan'''
