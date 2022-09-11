import pytest

from io import StringIO
from entities.order_db import OrderDB


@pytest.mark.parametrize(
    "fixture_name, expected_num_order, expected_num_customer",
    [
        ("orders_json", 3, 3),
        ("orders_json_duplicated_customers", 3, 2)
    ]
)
def test_load_from_json(fixture_name, expected_num_order, expected_num_customer, request):

    input = request.getfixturevalue(fixture_name)

    input_stream = StringIO(input)

    order_db = OrderDB.from_json(input_stream)

    assert len(order_db.orders) == expected_num_order
    assert len(order_db.customers) == expected_num_customer