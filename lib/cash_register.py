#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
    self.discount = discount
    self.total = 0.0
    self.items = []
    self.last_transaction = 0

  def add_item(self,title,price,quantity=1):
    self.total += price * quantity
    self.last_transaction = price * quantity
    self.items.extend([title] * quantity)

  def apply_discount(self):
    if self.discount > 0: 
        self.total -= self.total * (self.discount/100)
        print(f"After the discount, the total comes to ${int(self.total)}.")
        return True
    else: 
            print("There is no discount to apply.")
            return False
  
  def void_last_transaction(self):
    if not self.items:
      return

    self.total -= self.last_transaction
    if self.last_transaction >0:
       self.items.pop()  

  

  
    