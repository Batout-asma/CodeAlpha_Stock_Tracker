prices = {"AAPL": 180, "TSLA": 250, "GOOG": 140, "MSFT": 330}

print("Available stocks:", list(prices.keys()))
print("Type 'done' when you finish")

total = 0
lines = []

while True:
    name = input("Stock name: ").upper()

    if name == "DONE":
        break

    if name not in prices:
        print("Stock not found, try again")
        continue

    quantity = int(input("Quantity: "))
    value = prices[name] * quantity
    total = total + value

    lines.append(name + " x " + str(quantity) + " = $" + str(value))

print()
for line in lines:
    print(line)
print("Total investment: $" + str(total))

save = input("Save to file? (y/n): ")
if save == "y":
    file = open("portfolio.txt", "w")
    for line in lines:
        file.write(line + "\n")
    file.write("Total: $" + str(total))
    file.close()
    print("Saved in portfolio.txt")
