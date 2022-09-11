import pytest
from entities.order import OrderItem, Order


@pytest.mark.parametrize(
    "input, expected",
    [
        (tuple(["item1", 4, 5]), dict(item="item1", quantity=4, price=5, revenue=20)),
        (tuple(["item2", 7, 3]), dict(item="item2", quantity=7, price=3, revenue=21)),
    ],
)
def test_order_item_mapping(input, expected):
    order_detail = OrderItem(
        item=input[0],
        quantity=input[1],
        price=input[2]
    )

    assert order_detail.to_dict() == expected


def test_order_mapping(order_dict):
    order = Order.from_orderdict(order_dict)

    assert order.id == 1
    assert order.customer_id == '8baa6dea-cc70-4748-9b27-b174e70e4b66'
    assert order.date == "03/03/2017"
    assert order.vendor == "acme"
    assert len(order.order_items) == 4
    for order_item in order.order_items:
        assert isinstance(order_item, OrderItem)

def test_order_to_dict():
    order = Order(
        customer_id="cust1",
        vendor="some vendor",
        date="01/01/2022",
        id=1,
        order_items=[
            OrderItem("item1", 4, 5),
            OrderItem("item2", 2, 3)
        ]
    )

    assert order.to_dict() == {
        "id": 1,
        "vendor": "some vendor",
        "customer": "cust1",
        "date": "01/01/2022",
        "order": [
            {
                "item": "item1",
                "quantity": 4,
                "price": 5,
                "revenue": 20
            },
            {
                "item": "item2",
                "quantity": 2,
                "price": 3,
                "revenue": 6
            }
        ]
    }
