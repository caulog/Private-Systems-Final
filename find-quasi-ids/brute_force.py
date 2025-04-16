# brute_force.py

from itertools import combinations
import pandas as pd
import os

def compute_distinct_ratios_by_size(df, min_comb_size=2, max_comb_size=5, top_k=10, output_dir="output"):
    candidate_columns = df.columns
    num_rows = len(df)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for r in range(min_comb_size, max_comb_size + 1):
        results = []
        for combo in combinations(candidate_columns, r):
            subset = df[list(combo)]
            num_unique = len(subset.drop_duplicates())
            ratio = num_unique / num_rows
            results.append({
                'attributes': ", ".join(combo),
                'distinct_ratio': round(ratio, 4),
                'unique_combinations': num_unique
            })

        results.sort(key=lambda x: -x['distinct_ratio'])
        top_results = results[:top_k]

        # Print to console
        print(f"\nTop {top_k} combinations of size {r} by distinct ratio:\n")
        for r_entry in top_results:
            print(f"{r_entry['attributes']}: distinct_ratio={r_entry['distinct_ratio']}, unique_combinations={r_entry['unique_combinations']}")

        # Save to CSV
        output_path = os.path.join(output_dir, f"distinct_ratio_k{r}.csv")
        pd.DataFrame(top_results).to_csv(output_path, index=False)
        print(f"Saved to {output_path}")
