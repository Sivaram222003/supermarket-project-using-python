import datetime

# Function to get current date and time
def get_current_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to generate the bill
def generate_bill(items):
    total_cost = 0
    bill = []
    bill.append("Supermarket Bill")
    bill.append(f"Date and Time: {get_current_datetime()}")
    bill.append("="*40)
    bill.append(f"{'Item':<20} {'Quantity':<10} {'Price':<10}")
    bill.append("-"*40)

    for item, details in items.items():
        line_cost = details['quantity'] * details['price']
        bill.append(f"{item:<20} {details['quantity']:<10} ${line_cost:<10.2f}")
        total_cost += line_cost

    bill.append("-"*40)
    bill.append(f"{'Total Cost':<30} ${total_cost:.2f}")
    bill.append("="*40)
    return "\n".join(bill)

# Function to save the bill to a file
def save_bill_to_file(bill, filename="bill.txt"):
    file = None
    try:
        file = open(filename, 'w')
        file.write(bill)
        print(f"Bill saved to {filename}.")
    except Exception as e:
        print(f"Error saving bill: {e}")
    finally:
        if file:
            file.close()
        print("File save attempt completed.")

# Main function
def main():
    items = {
        "Apples": {"quantity": 2, "price": 1.50},
        "Bread": {"quantity": 1, "price": 2.00},
        "Milk": {"quantity": 1, "price": 1.20},
        "Eggs": {"quantity": 12, "price": 0.10},
        "Cheese": {"quantity": 1, "price": 3.50}
    }

    try:
        bill = generate_bill(items)
        print(bill)
        save_bill_to_file(bill)
        
        recipient_email = input("Enter your email address to receive the bill: ").strip()
        print(f"Bill will be sent to: {recipient_email}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Process completed.")

# Execute the main function
if __name__ == "__main__":
    main()
