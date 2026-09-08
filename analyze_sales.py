import csv

with open("sales.csv", newline="") as file:
    reader = csv.DictReader(file)
    total_quantity = 0
    total_revenue = 0
    drinks_revenue = 0
    food_revenue = 0

    for row in reader:
        product = row["Product"]
        price = float(row["Unit Price (EUR)"])
        quantity = int(row["Quantity"])
        total_quantity += quantity
        revenue = price * quantity
        total_revenue += revenue

        if row["Category"] == "Drink":
            drinks_revenue += revenue

        if row["Category"] == "Food":
            food_revenue += revenue

        print (f"{product}: EUR {revenue:.2f}")
print(f"Total units sold: {total_quantity}")
print(f"Total revenue: EUR {total_revenue:.2f}")
print(f"Drinks revenue: EUR {drinks_revenue:.2f}")
print(f"Food revenue: EUR {food_revenue:.2f}")


with open("sales_summary.txt", "w") as report:
    report.write(f"Total units sold: {total_quantity}\n")
    report.write(f"Total revenue: EUR {total_revenue:.2f}\n")
    report.write(f"Drinks revenue: EUR {drinks_revenue:.2f}\n")
    report.write(f"Food revenue: EUR {food_revenue:.2f}\n")