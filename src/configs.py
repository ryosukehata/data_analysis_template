import argparse

from dataclasses import dataclass
from pathlib import Path

_input_dir_local = './input'


@dataclass(frozen=True)
class DataPath:
    input_directory: Path = Path(_input_dir_local)
    train_csv: Path = input_directory / 'train.csv'


def parser_configs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", type=str, default=False, help="whether use gpu")
    args = parser.parse_args()
    return args
