orders = ["Laptop", "Mouse", "Keyboard", "Monitor", "UnknownGadget", 100500]
inventory = [
{"name": "Laptop", "price": "1000$", "stock": 5},
{"name": "Mouse", "price": "50$", "stock": 0},
{"name": "Monitor", "price": "200$", "stock": 2},
{"name": "Keyboard", "price": "100$", "stock": 10}
]
shipped_items = []
def warehouse_account (order_list, inventory_list):
    total_income = 0
    while len(order_list) > 0:
        order = order_list.pop(0)
        found = False
        try:
            order = order.lower()
        except AttributeError:
            print("Unsupported data type")
            continue
        for item in inventory_list:
            if order == item["name"].lower():
                found = True
                if item["stock"] > 0:
                    item["stock"] = item["stock"] - 1
                    print(f"{item["name"]} stock is {item["stock"]}")
                    shipped_items.append(item["name"])
                    item_price = int(item["price"].replace("$", ""))
                    total_income += item_price
                    break
                elif item["stock"] == 0:
                    print(f"{item["name"]} is out of stock")
                    break
        if found == False:
            print (f"Order not found")
    return {
        "shipped_items": shipped_items,
        "total_income": total_income,
    }
result = warehouse_account(orders, inventory)
print(result)













