import toml

# Read the TOML file
file_path = "windows_shortkeys.toml"
shortkeys_data = toml.load(file_path)

# Convert all section names to uppercase
shortkeys_data_uppercase = {key.upper(): value for key, value in shortkeys_data.items()}

# Get user input for the partial section name
partial_section_input = input("Enter a partial section name: ").upper()
print()
print()

# Search for a matching section (case-insensitive and partial match)
matching_sections = [section_name for section_name in shortkeys_data_uppercase if partial_section_input in section_name]

# Check if any matching sections are found
if matching_sections:
    # Print contents for each matching section
    for matched_section in matching_sections:
        print(f"SECTION: {matched_section}")
        for entry_name, entry_value in shortkeys_data_uppercase[matched_section].items():
            print(f"{entry_name} = {entry_value}")
else:
    print(f"No matching sections found for '{partial_section_input}' in the TOML file.")
