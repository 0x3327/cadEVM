# TODO Add easy deploy when the project is not deployed already

class ArgumentsLengthError(Exception):
    pass

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


