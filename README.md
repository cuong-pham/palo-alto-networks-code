# Palo Alto Networks Code Challenge

### Build docker image
```shell
docker build . --tag=palo-alto-networks-code-test:latest
```

### How to run
```shell
docker run -v "$(pwd):/app/" --rm palo-alto-code-test:latest /app/transform.py
```

### Run test
```shell
docker run --rm palo-alto-code-test:latest pytest
```

### Code Assumptions
- When `customer` with the same `customer_id` appears in multiple orders, take the detail of the last value as customer detail