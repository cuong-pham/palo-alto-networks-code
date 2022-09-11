#!/usr/bin/env python3
import argparse
import sys
import typing
from entities.order_db import OrderDB


def transform_data(input_stream: typing.IO, output_stream: typing.IO):
    db = OrderDB.from_json(input_stream)
    db.to_json(output_stream)


def main(args):  # pragma: no cover
    parser = argparse.ArgumentParser("Transform Order Data")

    parser.add_argument(
        "--input", "-i", dest="input", type=argparse.FileType("r"),
        default="data.json",
        help="Name of the input file. If not specified, default to data.json"
    )
    parser.add_argument(
        "--output", "-o", dest="output", type=argparse.FileType("w"),
        default="data-transformed.json",
        help="Name of the output file. If not specified, default to data-transformed.json"
    )

    options = parser.parse_args(args)
    transform_data(options.input, options.output)


if __name__ == '__main__': # pragma: no cover
    sys.exit(main(sys.argv[1:]))