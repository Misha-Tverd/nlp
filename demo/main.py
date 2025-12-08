name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\n--- RESULT ---")
print("Name:", name)
print("Age:", age)
if age > 18:
    print("You are adult")
else:
    print("You are underage")

print(f"You were born in {2025 - age}")