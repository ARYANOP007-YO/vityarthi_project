
    # welcome to door to door delivery service in VIT
def delivery_vit_service():
    print("Welcome to VIT Door to Door Delivery Service! for boys hostel only.")

delivery_vit_service()

print("Available items are: bat, shuttle, racket, ball, study item, tea, coffee, soft drink, chips, chocolate")
item = input("What would you like to buy: ").strip()
items = ["bat","shuttle","racket","ball", "pen", "tea", "coffee", "soft drink", "chips", "chocolate"]
if item not in items:
    print("Sorry, the item you requested is not available.")
    exit()
in_stock_response = input("do you want it now ? (y/n): ").strip().lower()
if in_stock_response.startswith('y'):
    print("ok we want some more details sir")
else:
    print("Sorry for the inconvenience,please visit again later.")

def calculate_total_cost():
    try:
        quantity = int(input("Enter the quantity of the item: "))
        price = float(input("Enter the price of the item that you want: "))
        if quantity <= 0 or price < 0:
            print("Quantity must be greater than 0 and price cannot be negative.")
            return None
        block = int(input("Enter your block (1/2/3/4/5/6/7/8): "))
        if block not in range(1, 9):
            print("Invalid block number. Please enter a number between 1 and 8.")
            return None
        room_number = input("Enter your room number: ")
    except ValueError:
        print("Invalid numeric input for quantity, price, or block.")
        return None

    delivery_fee = 50  # fixed delivery fee for VIT campus
    total = (quantity * price) + delivery_fee
    return total

if in_stock_response.startswith('y'):
    total_cost = calculate_total_cost()
    if total_cost is not None:
        print(f"Total cost (including delivery): {total_cost}")
        print("Thank you for using VIT Door to Door Delivery Service! your order will be delivered to your room soon.")
