
transactions = [1200, 450, 800, 1500, 2300, 700, 100]
highest_transaction = transactions[0]
smallest_transaction = transactions[0]
for transaction in transactions:
    if transaction > highest_transaction:
        highest_transaction=transaction
    if transaction < smallest_transaction:
        smallest_transaction=transaction

print("Highest transaction amount:", highest_transaction)
print("Lowest transaction amount:", smallest_transaction)