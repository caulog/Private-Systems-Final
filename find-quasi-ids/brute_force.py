# brute_force.py
import pandas as pd
from itertools import combinations
import argparse

def load_data(path):
    df = pd.read_csv(path)
    return df

def compute_distinct_ratios(df, max_comb_size=3):
    candidate_columns = df.columns.tolist()
    num_rows = len(df)
    results = []

    for r in range(1, max_comb_size + 1):
        for combo in combinations(candidate_columns, r):
            subset = df[list(combo)]
            num_unique = len(subset.drop_duplicates())
            ratio = num_unique / num_rows
            results.append({
                'attributes': combo,
                'distinct_ratio': round(ratio, 4),
                'unique_combinations': num_unique
            })

    return sorted(results, key=lambda x: -x['distinct_ratio'])

def print_top(results, top_k=10):
    print(f"\nTop {top_k} attribute combinations by distinct ratio:\n")
    for r in results[:top_k]:
        print(f"{r['attributes']}: distinct_ratio={r['distinct_ratio']}, unique_combinations={r['unique_combinations']}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='data/TAP_PRUNED.csv', help='Path to TAP pruned dataset')
    parser.add_argument('--max_comb_size', type=int, default=3, help='Maximum size of attribute combinations')
    parser.add_argument('--top_k', type=int, default=10, help='Number of top combinations to display')
    args = parser.parse_args()

    df = load_data(args.path)
    results = compute_distinct_ratios(df, args.max_comb_size)
    print_top(results, args.top_k)

if __name__ == "__main__":
    main()
