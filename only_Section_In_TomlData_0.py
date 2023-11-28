import toml

# Read the TOML file
file_path = "windows_shortkeys.toml"
shortkeys_data = toml.load(file_path)

print()

# Print all sections with numbering
print("All Sections:".upper())
for i, section_name in enumerate(shortkeys_data.keys(), start=1):
    print(f"{i}. {section_name}")


