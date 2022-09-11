import typing, json

from dataclasses import dataclass
from .customer import Customer
from .order import Order

@dataclass
class OrderDB:
    customers: typing.List[Customer]
    orders: typing.List[Order]

    @classmethod
    def from_json(self, input_stream: typing.IO) -> 'OrderDB':
        order_data = json.load(input_stream)

        customers = {}
        orders = []
        for order_dict in order_data:
            customers.update({order_dict.get("customer").get("id"): Customer.from_orderdict(order_dict)})
            orders.append(Order.from_orderdict(order_dict))
        return OrderDB(list(customers.values()), orders)

    def to_dict(self) -> typing.Dict:
        return {
            "customers": [c.to_dict() for c in self.customers],
            "orders": [o.to_dict() for o in self.orders]
        }

    def to_json(self, output_stream: typing.IO):
        json.dump(
            self.to_dict(),
            output_stream,
            indent=2
        )