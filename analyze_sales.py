import csv

with open("sales.csv", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    total_revenue = 0
    drinks_revenue = 0
    food_revenue = 0

    for row in reader:
        product = row[0]
        price = float(row[2])
        quantity = int(row[3])
        revenue = price * quantity
        total_revenue += revenue

        if row[1] == "Drink":
            drinks_revenue += revenue

        if row[1] == "Food":
            food_revenue += revenue

        print (f"{product}: EUR {revenue:.2f}")

print(f"Total revenue: EUR {total_revenue:.2f}")
print(f"Drinks revenue: EUR {drinks_revenue:.2f}")
print(f"Food revenue: EUR {food_revenue:.2f}")


with open("sales_summary.txt", "w") as report:
    report.write(f"Total revenue: EUR {total_revenue:.2f}\n")
    report.write(f"Drinks revenue: EUR {drinks_revenue:.2f}\n")
    report.write(f"Food revenue: EUR {food_revenue:.2f}\n")