import argparse

import ibis


def set_argparse():
    parser = argparse.ArgumentParser(
        prog="find-quasi-ids",
    )
    parser.add_argument("-f", "--file", required=True, help="Path to CSV datafile")
    return parser


if __name__ == "__main__":
    parser = set_argparse()
    args = parser.parse_args()

    table = ibis.read_csv(args.file)
