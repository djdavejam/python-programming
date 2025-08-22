# Purpose: Calculate total cost of a pizza order based on size, toppings, and delivery distance

# Step 1: Prompt user for input
pizza_size = input("Enter pizza size (small or large): ").lower()
topping_count = int(input("Enter number of additional toppings: "))
delivery_distance = float(input("Enter delivery distance in miles: "))

# Step 2: Determine base cost of pizza
if pizza_size == "small":
    base_price = 8
elif pizza_size == "large":
    base_price = 12
else:
    print("Invalid pizza size selected. Please choose 'small' or 'large'.")
    exit()

# Step 3: Calculate toppings cost
toppings_cost = topping_count * 1

# Step 4: Calculate delivery fee
if delivery_distance <= 0:
    delivery_fee = 0
elif delivery_distance <= 5:
    delivery_fee = 2
else:
    extra_miles = delivery_distance - 5
    delivery_fee = 2 + (extra_miles * 1)

# Step 5: Calculate total cost
total_cost = base_price + toppings_cost + delivery_fee

# Step 6: Display the result
print(f"\n--- Order Summary ---")
print(f"Pizza size: {pizza_size.capitalize()}")
print(f"Base price: ${base_price}")
print(f"Toppings: {topping_count} x $1 = ${toppings_cost}")
print(f"Delivery fee: ${delivery_fee:.2f}")
print(f"Total cost: ${total_cost:.2f}")
