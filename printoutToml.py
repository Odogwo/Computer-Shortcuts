import toml

# Read the TOML file
file_path = "windows_shortkeys.toml"
shortkeys_data = toml.load(file_path)

# Extract and print the keys and descriptions
for entry in shortkeys_data["Keys"]:
    description, keys = entry.split("=")
    print(f"{description.strip()} = {keys.strip()}")



"""
pip install toml



"""