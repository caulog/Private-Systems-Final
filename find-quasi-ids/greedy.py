"""
Pseudo-code of the greedy algorithm proposed in the Efficient Algorithms for Masking and Finding Quasi-Identifiers paper by Motwani and Xu.

def greedy_minimum_key(table):
    selected = []               # Initialize empty key set
    all_pairs = generate_all_tuple_pairs(table)
    uncovered = set(all_pairs)  # All unseparated tuple pairs

    while uncovered:
        best_attr = None
        max_cover = 0

        # Find attribute separating most uncovered pairs
        for attr in table.attributes:
            if attr in selected:
                continue
            count = 0
            for (t1, t2) in uncovered:
                if t1[attr] != t2[attr]:
                    count += 1
            if count > max_cover:
                max_cover = count
                best_attr = attr

        # Add best attribute to key
        selected.append(best_attr)

        # Remove pairs separated by new attribute
        new_uncovered = set()
        for (t1, t2) in uncovered:
            if t1[best_attr] == t2[best_attr]:
                new_uncovered.add((t1, t2))
        uncovered = new_uncovered

    return selected

"""
