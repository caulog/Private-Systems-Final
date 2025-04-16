# brute_force.py# brute_force.py

from itertools import combinations

def compute_distinct_ratios_by_size(df, min_comb_size=2, max_comb_size=5, top_k=10):
    candidate_columns = df.columns
    num_rows = len(df)

    for r in range(min_comb_size, max_comb_size + 1):
        results = []
        for combo in combinations(candidate_columns, r):
            subset = df[list(combo)]
            num_unique = len(subset.drop_duplicates())
            ratio = num_unique / num_rows
            results.append({
                'attributes': combo,
                'distinct_ratio': round(ratio, 4),
                'unique_combinations': num_unique
            })

        results.sort(key=lambda x: -x['distinct_ratio'])

        print(f"\nTop {top_k} combinations of size {r} by distinct ratio:\n")
        for r_entry in results[:top_k]:
            print(f"{r_entry['attributes']}: distinct_ratio={r_entry['distinct_ratio']}, unique_combinations={r_entry['unique_combinations']}")
