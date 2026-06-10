print("Welcome to Stock Portfolio Tracker")
stocks = {
    "TCS": 3500,
    "INFY": 1500,
    "WIPRO": 450,
    "RELIANCE": 2800
}
total_value = 0
while True:
    stock_name = input("Enter stock name (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name in stocks:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        total_value += stocks[stock_name] * quantity
    else:
        print("Stock not found!")
print("\nTotal Portfolio Value: ₹", total_value)