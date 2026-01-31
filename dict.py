# Format: { "key": "value" }
user = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
# Accessing
print(user["name"])  # Output: Alice

# Adding or Updating
user["email"] = "alice@example.com"  # Adds a new key
user["age"] = 26                     # Updates existing key

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Loop through keys and values together
for key, value in car.items():
    print(f"{key}: {value}")