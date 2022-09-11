import typing
from dataclasses import dataclass


@dataclass(frozen=True)
class OrderItem:
    item: str
    quantity: int
    price: float

    @property
    def revenue(self) -> float:
        return self.quantity * self.price

    def to_dict(self):
        return {
            'item': self.item,
            'quantity': self.quantity,
            'price': self.price,
            'revenue': self.revenue
        }


@dataclass(frozen=True)
class Order:
    id: int
    vendor: str
    date: str
    customer_id: str
    order_items: typing.List[OrderItem]

    def to_dict(self) -> typing.Dict:
        return {
            "id": self.id,
            "vendor": self.vendor,
            "date": self.date,
            "customer": self.customer_id,
            "order": [
                o.to_dict()
                for o in self.order_items
            ]
        }

    @classmethod
    def from_orderdict(cls, order_dict: typing.Dict) -> 'Order':
        order_items: typing.List[OrderItem] = [
            OrderItem(item, **detail)
            for item, detail in order_dict.get("order", {}).items()
        ]
        return Order(
            id=order_dict.get("id"),
            vendor=order_dict.get("vendor"),
            date=order_dict.get("date"),
            customer_id=order_dict.get("customer", {}).get("id"),
            order_items=order_items
        )
