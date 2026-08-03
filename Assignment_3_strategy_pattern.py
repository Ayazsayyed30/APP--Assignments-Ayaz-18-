class CreditCardPayment:
    def __init__(self, name):
        self.name = name

    def pay(self, amount):
        return f"Rs.{amount} paid successfully using Credit Card by {self.name}"

class UPIPayment:
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        return f"Rs.{amount} paid successfully using UPI ID {self.upi_id}"

class NetBankingPayment:
    def __init__(self, bank_name):
        self.bank_name = bank_name

    def pay(self, amount):
        return f"Rs.{amount} paid successfully via {self.bank_name} Net Banking"

class WalletPayment:
    def __init__(self, mobile_no):
        self.mobile_no = mobile_no

    def pay(self, amount):
        return f"Rs.{amount} paid successfully using Mobile Wallet ({self.mobile_no})"

class CashOnDelivery:
    def pay(self, amount):
        return f"Order placed! Rs.{amount} to be paid on delivery."

class ShoppingCart:
    def __init__(self):
        self.total_bill = 0

    def add_price(self, price):
        self.total_bill += price

    def checkout(self, payment_method):
        print(f"\nFinal Amount to Pay: Rs.{self.total_bill}")
        result = payment_method.pay(self.total_bill)
        print(result)

if __name__ == "__main__":
    cart = ShoppingCart()
    
    items_count = int(input("How many items do you want to buy? "))
    
    for i in range(items_count):
        price = int(input(f"Enter price for item {i+1}: "))
        cart.add_price(price)
        
    if cart.total_bill > 0:
        print("\nPayment Options:")
        print("1. UPI")
        print("2. Credit Card")
        print("3. Net Banking")
        print("4. Mobile Wallet")
        print("5. Cash on Delivery")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            uid = input("Enter your UPI ID: ")
            pay_method = UPIPayment(uid)
        elif choice == '2':
            card_name = input("Enter Name on Card: ")
            pay_method = CreditCardPayment(card_name)
        elif choice == '3':
            bank = input("Enter your Bank Name (e.g., SBI, HDFC): ")
            pay_method = NetBankingPayment(bank)
        elif choice == '4':
            mobile = input("Enter registered mobile number: ")
            pay_method = WalletPayment(mobile)
        elif choice == '5':
            pay_method = CashOnDelivery()
        else:
            print("Invalid choice! Defaulting to Cash on Delivery.")
            pay_method = CashOnDelivery()
            
        print("\nProcessing transaction...")
        cart.checkout(pay_method)
    else:
        print("No items to pay for.")
