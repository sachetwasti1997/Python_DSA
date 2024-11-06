import csv

class Item:
    all = []
    def __init__(self, name:str, price:float, quantity:int) -> None:
        assert not name.__eq__('') and not name.__eq__(' '), f"Name: {name} cannot be a blank string"
        assert price >= 0, f"Price: {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity: {quantity} is not greater than or equal to zero"
        

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('/Volumes/SachetSSD/DocumentsSSD/PycharmProject/GoogleDsa/classes/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    def __repr__(self) -> str:
        return f'Item(Name: "{self.name}", Price: {self.price}, Quantity: {self.quantity})'

Item.instantiate_from_csv()
print(Item.all)