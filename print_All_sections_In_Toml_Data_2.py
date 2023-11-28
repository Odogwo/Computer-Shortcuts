import toml

# Read the TOML file
file_path = "windows_shortkeys.toml"
shortkeys_data = toml.load(file_path)

print()
# Iterate over all sections in the TOML file
for section_name, section_data in shortkeys_data.items():
    print(f"SECTION: {section_name.upper()}")
    print()
    
    # Iterate over all entries in the section
    for entry_name, entry_value in section_data.items():
        print(f"{entry_name} = {entry_value}")

    print()  # Add a newline between sections for better readability
    print()
