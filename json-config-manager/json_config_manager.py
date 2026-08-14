# === Read Configuration ===
import json

with open("config.json", "r") as file:
    config = json.load(file)

print("Loaded configuration with " + str(len(config)) + " keys")
print("Keys: " + ", ".join(config.keys()))

# === Validate Configuration ===
required_keys = ["database", "server", "logging"]

def validate_config(config, required):
    missing_keys = []

    for key in required:
        if key not in config:
            missing_keys.append(key)

    is_valid = len(missing_keys) == 0

    return is_valid, missing_keys

is_valid, missing_keys = validate_config(config, required_keys)

print("Configuration valid: " + str(is_valid))

if len(missing_keys) == 0:
    print("All required keys present")
else:
    print("Missing keys: " + ", ".join(missing_keys))

# === Update Configuration Values ===
def update_config(config, key_path, value):
    keys = key_path.split(".")
    current = config

    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]

    current[keys[-1]] = value


update_config(config, "server.port", 8080)
print("Updated server.port to 8080")

update_config(config, "database.host", "localhost")
print("Updated database.host to localhost")

# === Save Configuration ===
import json

with open("config.json", "r") as file:
    config = json.load(file)

print("Loaded configuration with " + str(len(config)) + " keys")
print("Keys: " + ", ".join(config.keys()))

required_keys = ["database", "server", "logging"]

def validate_config(config, required):
    missing_keys = []

    for key in required:
        if key not in config:
            missing_keys.append(key)

    is_valid = len(missing_keys) == 0

    return is_valid, missing_keys

is_valid, missing_keys = validate_config(config, required_keys)

print("Configuration valid: " + str(is_valid))

if len(missing_keys) == 0:
    print("All required keys present")
else:
    print("Missing keys: " + ", ".join(missing_keys))
    
def update_config(config, key_path, value):
    keys = key_path.split(".")
    current = config

    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]

    current[keys[-1]] = value


update_config(config, "server.port", 8080)
print("Updated server.port to 8080")

update_config(config, "database.host", "localhost")
print("Updated database.host to localhost")

def save_config(config, filename):
    with open(filename, "w") as file:
        json.dump(config, file, indent=4)


save_config(config, "config_updated.json")

print("Configuration saved to config_updated.json")

import os

file_size = os.path.getsize("config_updated.json")

print("File size: " + str(file_size) + " bytes")
