from itertools import combinations
import pandas as pd
import os

def compute_distinct_ratios_by_size(df, attribute_min=6, attribute_max=6, top_k=10, output_dir="output"):
    """
    Brute force analysis of data frame to find combinations of attributes with high distinct ratios

    Distinct ratio definition from paper: 
    A combination is an α-distinct quasi-identifier if, after removing ≤ (1−α) tuples, the rest have unique values in that combination.

        To compute:
        distinct_ratio = (number of unique values for combination) / (number of rows)

        To evaluate:
        A ratio near 1 means the combo uniquely identifies nearly all individuals.
    """

    # initialize rows and columns
    n = len(df)
    m = df.columns

    # for each attribute combination size
    for r in range(attribute_min, attribute_max + 1):
        results = []

        # loop through all possible combinations of columns
        # this is very expensive when r and m are large -- but our dataset is small
        for combo in combinations(m, r):
            subset = df[list(combo)]                        # takes subset of dataframe with only current columns
            num_unique = len(subset.drop_duplicates())      # removes duplicate rows to get unique row count
            ratio = num_unique / n                          # calculates distinct ratio
            
            # adds each to result dataframe
            results.append({
                'attributes': ", ".join(combo),
                'distinct_ratio': round(ratio, 4),
                'unique_combinations': num_unique
            })

        # sorts all combinations by highest distinct ratio and returns top k
        results.sort(key=lambda x: -x['distinct_ratio'])
        top_results = results[:top_k]

        # Print to console
        print(f"\nTop {top_k} combinations of size {r} by distinct ratio:\n")
        for r_entry in top_results:
            print(f"{r_entry['attributes']}: distinct_ratio={r_entry['distinct_ratio']}, unique_combinations={r_entry['unique_combinations']}")

        # Save to CSV
        output_path = os.path.join(output_dir, f"brute_force_distinct_ratio_k{r}.csv")
        pd.DataFrame(top_results).to_csv(output_path, index=False)
        print(f"Saved to {output_path}")
