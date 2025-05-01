import argparse
import time

import ibis

from find_quasi_ids import brute_force
from find_quasi_ids import greedy


def set_argparse():
    parser = argparse.ArgumentParser(
        prog="find-quasi-ids",
    )
    parser.add_argument(
        "-f", "--input-file", required=True, help="Path to input CSV datafile"
    )
    parser.add_argument(
        "--out-dir",
        required=False,
        help="Path to output directory where to write the output CSV file(s).",
        default="output",
    )
    subparsers = parser.add_subparsers(
        dest="algo",
        required=True,
        title="algorithms",
        description="Algorithm to use. Each has its own options.",
    )

    brute_parser = subparsers.add_parser("brute", help="Run the brute-force algorithm.")

    brute_parser.add_argument(
        "--num-cols-start",
        required=False,
        help="Number of columns to start running the brute force algorithm.",
        type=int,
    )
    brute_parser.add_argument(
        "--num-cols-max",
        required=False,
        help="Max number of cols to use to run the brute force algorithm.",
        type=int,
    )
    brute_parser.add_argument(
        "--top-k",
        required=False,
        help="Output top-k combination of columns with highest distinct ratio for the brute force algorithm.",
        type=int,
    )

    greedy_parser = subparsers.add_parser("greedy", help="Run the greedy algorithm.")
    greedy_parser.add_argument(
        "--sample",
        required=False,
        action="store_true",
        help="If provided input data will be sampled, before running the greedy algorithm.",
    )
    greedy_parser.add_argument(
        "--distinct-ratio-target",
        required=False,
        help="If provided the greedy algorithm will run until it just achieves a higher distinct ratio percentage. If not provided greedy algorithm will run fully. Expected value 0-100.",
        type=float,
    )
    return parser


def main():
    parser = set_argparse()
    args = parser.parse_args()

    table = ibis.read_csv(args.input_file)

    start_time = time.time()
    match args.algo:
        case "brute":
            df = table.to_pandas()
            brute_force.compute_distinct_ratios_by_size(
                df,
                attribute_min=args.num_cols_start,
                attribute_max=args.num_cols_max,
                top_k=args.top_k,
                output_dir=args.out_dir,
            )

        case "greedy":
            if args.sample:
                table = greedy.sample_for_greedy_min_key(table)
            greedy.greedy_min_key(
                table,
                distinct_ratio_target=args.distinct_ratio_target,
                output_dir=args.out_dir,
            )

    print(f"Took {time.time() - start_time:.3f} seconds")


if __name__ == "__main__":
    main()
