# 1. Supermarket savatchasi
class CartItem:
    def __init__(self, name, price, quantity, discount=0):
        self.name = name
        self.price = price         
        self.quantity = quantity   
        self.discount = discount   

    def total_cost(self):
        """Chegirmasiz narx * chegirma qo'llanilgandan keyingi koeffitsient"""
        return self.price * self.quantity * (1 - self.discount / 100)

    def __str__(self):
        return f"{self.name:10} | {self.price:6.2f}$ | {self.quantity:3} dona | {self.discount:4}% | {self.total_cost():8.2f}$"


class FoodItem(CartItem):
    def __str__(self):
        return f"{self.name:10} | {self.price:6.2f}$ | {self.quantity:3} dona | {self.discount}% chegirma → {self.total_cost():.2f}$"


class NonFoodItem(CartItem):
    def __str__(self):
        return f"{self.name:10} | {self.price:6.2f}$ | {self.quantity:3} dona | {self.discount}% chegirma → {self.total_cost():.2f}$"


def show_cart(items):
    print("\n" + "═" * 60)
    print(" SAVAT ".center(60))
    print("═" * 60)
    print("Mahsulot     | Narx   | Miqdor | Chegirma | Jami    ")
    print("─" * 60)

    total = 0
    for item in items:
        print(item)
        total += item.total_cost()

    print("─" * 60)
    print(f"Umumiy summa:                  {total:19.2f}$")
    print("═" * 60 + "\n")

cart = [
    FoodItem("Olma", 1.50, 3, 10),
    FoodItem("Non", 2.00, 2, 5),
    FoodItem("Banan", 2.30, 1, 0),
    NonFoodItem("Sovun", 3.50, 2, 15),
    NonFoodItem("Shampun", 5.99, 1, 20),
]

show_cart(cart)
