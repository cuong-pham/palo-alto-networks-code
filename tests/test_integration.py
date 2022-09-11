import json
from pathlib import Path

from transform import transform_data


def _fixture_file_path():
    return str(Path(__file__).resolve().parents[0]) + "/fixtures"


def test_input_output():
    fixture_path = _fixture_file_path()
    input_file = open(fixture_path+"/input.json", "r")
    output_file = open(fixture_path+"/output.json", "w")

    transform_data(input_file, output_file)
    output_file.close()

    with open(fixture_path+"/expected.json", "r") as e_fp:
        with open(fixture_path+"/output.json", "r") as o_fp:
            expected = json.load(e_fp)
            actual = json.load(o_fp)

            assert actual == expected

