class CreditCardPayment:
    def __init__(self, card_num, name):
        self.card_num = card_num
        self.name = name

    def pay(self, amount):
        return f"Paid Rs.{amount} using Credit Card ending in {self.card_num[-4:]}"

class UPIPayment:
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        return f"Paid Rs.{amount} using UPI ID {self.upi_id}"

class PayPalPayment:
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid Rs.{amount} using PayPal account {self.email}"

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, item_name, price):
        self.items.append(item_name)
        self.total += price
        print(f"Added {item_name} for Rs.{price}")

    def checkout(self, payment_method):
        if self.total == 0:
            print("Cart is empty!")
            return

        print(f"Total amount to pay: Rs.{self.total}")
        result = payment_method.pay(self.total)
        print(result)
        
        self.items = []
        self.total = 0

if __name__ == "__main__":
    cart1 = ShoppingCart()
    cart1.add_item("Python Book", 800)
    cart1.add_item("Notebook", 150)
    
    upi = UPIPayment("rahul@okhdfc")
    cart1.checkout(upi)
    
    print("\n" + "="*30 + "\n")
    
    cart2 = ShoppingCart()
    cart2.add_item("Wireless Mouse", 1200)
    
    card = CreditCardPayment("9876543212345678", "Amit Kumar")
    cart2.checkout(card)
    
    print("\n" + "="*30 + "\n")
    
    cart3 = ShoppingCart()
    cart3.add_item("Web Hosting", 3500)
    
    paypal = PayPalPayment("amit.tech@email.com")
    cart3.checkout(paypal)
