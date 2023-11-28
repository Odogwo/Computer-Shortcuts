"""
print out all variable names (keys) 
in each section without printing their values
"""



import toml

# Read the TOML file
file_path = "windows_shortkeys.toml"
shortkeys_data = toml.load(file_path)

# Print all variable names in each section
for section_name, section_data in shortkeys_data.items():
    print(f"SECTION: {section_name}".upper ())
    print("VARIABLES:")
    for variable_name in section_data.keys():
        print(f"- {variable_name}")
    print()
