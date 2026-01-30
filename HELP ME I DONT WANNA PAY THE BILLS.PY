# Input: total bill and amount paid
total_bill = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid: "))

# Calculate due amount
due_amount = total_bill - amount_paid

# Output the result
print("Customer's due amount is:", due_amount)
