from . import configs
from .utils import fix_seed


def main(args):
    datapath = configs.DataPath()
    print(datapath)


if __name__ == '__main__':
    fix_seed()
    args = configs.parser_configs()
    main(args)
