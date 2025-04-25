import os
import math

import ibis


def sample_for_greedy_min_key(table, epsilon=0.1, delta=0.01):
    """
    Implements the paper's random sampling approach for quasi-identifier discovery.

    Args:
        table: Ibis table containing the dataset
        epsilon: Approximation parameter (0 < epsilon < 1)
        delta: Confidence parameter (0 < delta < 1)

    Returns:
        Sampled Ibis table with approximately k = sqrt[(2(1-ε)/ε) * n ln(2^m/δ)] tuples
    """
    n = table.count().execute()
    m = len(table.columns)

    ln_term = m * math.log(2) - math.log(delta)
    k = math.sqrt((2 * (1 - epsilon) / epsilon) * n * ln_term)
    k = math.ceil(k)

    sampled = (
        table.mutate(random_sort=ibis.random())
        .order_by("random_sort")
        .limit(k)
        .drop("random_sort")
    )

    return sampled


def greedy_min_key(table, distinct_ratio_target=None, output_dir="output"):
    """
    Implementation of the Greedy Minimum Key Algorithm which given a table returns a list of the column names that are a key for the given table. A key is a subset of columns that uniquely identify each tuple in a table.

    Parameters:
    - table: an Ibis table

    Returns:
    - None
    """
    t = table.mutate(idx=ibis.row_number().over()).cache()
    t_view = t.view()

    pairs = t.join(t_view, t.idx < t_view.idx)

    selected_cols = []
    cols = [col for col in table.columns]

    while pairs.count().execute() > 0:
        max_separation = -1
        best_col = None

        for col in cols:
            if col in selected_cols:
                continue

            # Count pairs separated by this column in current remaining pairs
            sep_count = pairs.filter(t[col] != t_view[col]).count().execute()

            if sep_count > max_separation:
                max_separation = sep_count
                best_col = col

        if not best_col:
            break

        selected_cols.append(best_col)

        # Keep only pairs not separated by the selected attribute
        pairs = pairs.filter(t[best_col] == t_view[best_col])

        if distinct_ratio_target:
            unique_count = table.select(selected_cols).distinct().count().execute()
            distinct_ratio = unique_count / table.count().execute()

            if distinct_ratio * 100 >= distinct_ratio_target:
                break

    unique_count = table.select(selected_cols).distinct().count().execute()
    distinct_ratio = unique_count / table.count().execute()
    print(
        f"{selected_cols}: distinct_ratio={distinct_ratio}, unique_combinations={unique_count}"
    )

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "greedy.csv")

    out_table = ibis.memtable(
        {
            "attributes": [selected_cols],
            "distinct_ratio": distinct_ratio,
            "unique_combinations": unique_count,
        }
    )
    out_table.to_csv(output_path)
