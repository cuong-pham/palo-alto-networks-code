# Palo Alto Networks Code Challenge


## With Docker
### Build docker image
```shell
docker build . --tag=palo-alto-networks-code-test:latest
```

### How to run
```shell
docker run -v "$(pwd):/app/" --rm palo-alto--networks-code-test:latest /app/transform.py
```

### Run test
```shell
docker run --rm palo-alto-code-networks-test:latest pytest
```

## Without Docker

### How to run
Input/Output from current working directory
```shell
./transform.py
```

If input/output files from different location:
```shell
./transform.py -i <input_file_path> -o <output_file_path>
```

### Run test
```shell
pip install -r requirements.txt
export PYTHONPATH=$PYTHONPATH:$(pwd)
pytest
```

## Code Assumptions
- When `customer` with the same `customer_id` appears in multiple orders, take the detail of the last value as customer detail