import argparse

import ibis

import brute_force
import greedy


def set_argparse():
    parser = argparse.ArgumentParser(
        prog="find-quasi-ids",
    )
    parser.add_argument("-f", "--file", required=True, help="Path to CSV datafile")
    parser.add_argument(
        "-a",
        "--algo",
        required=True,
        choices=["brute", "greedy"],
        help="Algorithm to run.",
    )
    return parser


if __name__ == "__main__":
    parser = set_argparse()
    args = parser.parse_args()

    table = ibis.read_csv(args.file)

    match args.algo:
        case "brute":
            df = table.to_pandas()
            brute_force.compute_distinct_ratios_by_size(df)
        case "greedy":
            sampled_table = greedy.sample_for_greedy_min_key(table)
            greedy.greedy_min_key(sampled_table)
