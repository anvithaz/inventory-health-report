import csv
def load_inventory(filepath):
    inventory = []
    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventory.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' could not be found.")
    return inventory

def classify_sku(current_stock, reorder_point, max_stock):
    curr = int(current_stock)
    reorder = int(reorder_point)
    mx = int(max_stock)

    if curr < reorder:
        return "Critical"
    elif curr > mx:
        return "Overstocked"
    else:
        return "Healthy"


def generate_report(inventory):
    if not inventory:
        print("No data to report.")
        return

    for item in inventory:
        item["Status"] = classify_sku(
            (item["Current_Stock"]),
            (item["Reorder_Point"]),
            (item["Max_Stock"])
        )

    status_priority = {"Critical": 0, "Healthy": 1, "Overstocked": 2}
    inventory.sort(key=lambda x: status_priority[x["Status"]])

    print(f"\n{'SKU':<8} | {'Product Name':<18} | {'Stock':<6} | {'Status':<12}")
    print("-" * 55)
    for item in inventory:
        print(f"{item['SKU']:<8} | {item['Product_Name']:<18} | {item['Current_Stock']:<6} | {item['Status']:<12}")

if __name__ == "__main__":
    data = load_inventory("inventory_master.csv")
    generate_report(data)