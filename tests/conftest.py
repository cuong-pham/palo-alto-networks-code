import pytest


@pytest.fixture
def order_dict():
    yield {
            "id": 1,
            "vendor": "acme",
            "date": "03/03/2017",
            "customer": {
                "id": "8baa6dea-cc70-4748-9b27-b174e70e4b66",
                "name": "Lezlie Stuther",
                "address": "19045 Lawn Court"
            },
            "order": {
                "hat": {
                    "quantity": 14,
                    "price": 8
                },
                "cake": {
                    "quantity": 9,
                    "price": 3
                },
                "ice": {
                    "quantity": 10,
                    "price": 5
                },
                "candy": {
                    "quantity": 6,
                    "price": 8
                }
            }
        }

@pytest.fixture
def orders_json():
    yield """
[
 {
  "id": 1,
  "vendor": "acme",
  "date": "03/03/2017",
  "customer": {
   "id": "8baa6dea-cc70-4748-9b27-b174e70e4b66",
   "name": "Lezlie Stuther",
   "address": "19045 Lawn Court"
  },
  "order": {
   "hat": {
    "quantity": 14,
    "price": 8
   },
   "cake": {
    "quantity": 9,
    "price": 3
   },
   "ice": {
    "quantity": 10,
    "price": 5
   },
   "candy": {
    "quantity": 6,
    "price": 8
   }
  }
 },
 {
  "id": 2,
  "vendor": "acme",
  "date": "08/23/2017",
  "customer": {
   "id": "d2584a20-7490-499a-83be-d7cea4a0e260",
   "name": "Alma Prantoni",
   "address": "9 Trailsway Road"
  },
  "order": {
   "cake": {
    "quantity": 8,
    "price": 1
   },
   "punch": {
    "quantity": 19,
    "price": 7
   },
   "bouncy house": {
    "quantity": 4,
    "price": 9
   }
  }
 },
 {
  "id": 3,
  "vendor": "fred's party supplies",
  "date": "02/04/2017",
  "customer": {
   "id": "9a1c9545-2612-43c3-a3a3-ea7cb5c5e9d1",
   "name": "Edna Owenson",
   "address": "8 Redwing Lane"
  },
  "order": {
   "clown": {
    "quantity": 17,
    "price": 9
   }
  }
 }
]     
"""

@pytest.fixture
def orders_json_duplicated_customers():
    yield """
[
 {
  "id": 1,
  "vendor": "acme",
  "date": "03/03/2017",
  "customer": {
   "id": "8baa6dea-cc70-4748-9b27-b174e70e4b66",
   "name": "Lezlie Stuther",
   "address": "19045 Lawn Court"
  },
  "order": {
   "hat": {
    "quantity": 14,
    "price": 8
   },
   "cake": {
    "quantity": 9,
    "price": 3
   },
   "ice": {
    "quantity": 10,
    "price": 5
   },
   "candy": {
    "quantity": 6,
    "price": 8
   }
  }
 },
 {
  "id": 2,
  "vendor": "acme",
  "date": "08/23/2017",
  "customer": {
   "id": "8baa6dea-cc70-4748-9b27-b174e70e4b66",
   "name": "Lezlie Stuther",
   "address": "a different address"
  },
  "order": {
   "cake": {
    "quantity": 8,
    "price": 1
   },
   "punch": {
    "quantity": 19,
    "price": 7
   },
   "bouncy house": {
    "quantity": 4,
    "price": 9
   }
  }
 },
 {
  "id": 3,
  "vendor": "fred's party supplies",
  "date": "02/04/2017",
  "customer": {
   "id": "9a1c9545-2612-43c3-a3a3-ea7cb5c5e9d1",
   "name": "Edna Owenson",
   "address": "8 Redwing Lane"
  },
  "order": {
   "clown": {
    "quantity": 17,
    "price": 9
   }
  }
 }
]     
"""