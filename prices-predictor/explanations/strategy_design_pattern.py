from abc import ABC, abstractmethod

#Step 1: Define the Strategy interface
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

#steps 2: Implement Concrete strategies
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card."
    
class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal."
    
class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} using Bitcoin."

#Step 3: Implement the Context (ShoppingCart)
class shoppingCart:
    def __init__(self, payment_method):
        self.payment_method = payment_method
        
    def checkout(self, amount):
        return self.payment_method.pay(amount)
    
#Step 4: Use the Context to Execute the Strategy

if __name__ == "__main__":
    cart = shoppingCart(CreditCardPayment())
    print(cart.checkout(100))  # Output: Paid $100 using Credit Card.
    
    cart = shoppingCart(PayPalPayment())
    print(cart.checkout(200))  # Output: Paid $200 using PayPal.
    
    cart = shoppingCart(BitcoinPayment())
    print(cart.checkout(300))  # Output: Paid $300 using Bitcoin.