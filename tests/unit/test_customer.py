from entities.customer import Customer


def test_customer_mapping_from_orderdict(order_dict):
    customer = Customer.from_orderdict(order_dict)

    assert customer.id == "8baa6dea-cc70-4748-9b27-b174e70e4b66"
    assert customer.name == "Lezlie Stuther"
    assert customer.address == "19045 Lawn Court"


def test_customer_to_dict():
    customer = Customer("id1", "John Smith", "some address")
    assert customer.to_dict() == {
        "id": "id1",
        "name": "John Smith",
        "address": "some address"
    }