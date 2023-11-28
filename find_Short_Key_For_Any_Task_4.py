"""
a user to enter a partial variable name, 
and then print out the corresponding value 
if a match is found in any section,
"""
import toml

# Read the TOML file
file_path = "windows_shortkeys.toml"
shortkeys_data = toml.load(file_path)

print()
# Get user input for the partial variable name
partial_variable_input = input("Enter a partial variable name: ").lower()
print()

# Search for a matching variable in any section
matching_variable = None
for section_name, section_data in shortkeys_data.items():
    for variable_name in section_data.keys():
        if partial_variable_input in variable_name.lower():
            matching_variable = (section_name, variable_name, section_data[variable_name])
            break

# Check if a matching variable is found
if matching_variable:
    section_name, variable_name, variable_value = matching_variable
    print(f"SECTION: {section_name}".upper())
    print(f"VARIABLE: {variable_name}")
    print(f"VALUE: {variable_value}")
else:
    print(f"No matching variable found for '{partial_variable_input}' in the TOML file.")
