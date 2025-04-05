def read_text_file(file_path):
    """Reads text type of file."""
    print("3. Reading the file by creating list of lines")
    try:
        with open(file_path) as file_obj:
            lines = file_obj.readlines()
        return lines
    except FileNotFoundError as err:
        print(err)
        print("Please check the file path and try again")
        # raise

file_path_invalid = "/data/flavors.txt"
file_path_valid = "./data/flavors.txt"

flavors = read_text_file(file_path_invalid)
if flavors is not None:
    print(flavors)
    for flavor in flavors[:2]:
        print(f"We have {flavor.strip()} ice-cream.")
print("----- trying with valid path ----------")
flavors = read_text_file(file_path_valid)

if flavors is not None:
    print(flavors)
    for flavor in flavors[:2]:
        print(f"We have {flavor.strip()} ice-cream.")

try:
    num1 = int(input(f"Enter the quotient: "))
    num2 = int(input(f"Enter the dividend: "))

    print(f"Result of division: {num1 / num2}")
except ZeroDivisionError as err:
    print("ZeroDivisionError: Dividing any number by zero is not possible.")
    print('use different dividend')
except ValueError as err:
    # pass  # Fail silently
    print("ValueError: Value entered can not be converted to Integer.")
    print(err)
    print(f'result with default values- 55/5: {55/5}')
except Exception as err:
    print(f"ERROR: {err}")
finally:
    print("FINALLY: I am always executed regardless of try or except block")
    print("cleanup steps to be done regardless test pass or fail.")

print(f"****** Execution completed for {__file__} *****")