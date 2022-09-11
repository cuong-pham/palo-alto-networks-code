from dataclasses import dataclass, asdict
import typing


@dataclass(frozen=True)
class Customer:
    id: str
    name: str
    address: str

    @classmethod
    def from_orderdict(cls, order_dict: typing.Dict) -> 'Customer':
        return Customer(**(order_dict.get("customer", {})))

    def to_dict(self):
        return asdict(self)
