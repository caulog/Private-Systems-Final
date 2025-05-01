# This script was generated with guidance from ChatGPT (OpenAI, April 2025).

import pandas as pd

def simulate_auxiliary_knowledge(df, known_attributes):
    """
    Simulates anonymity reduction if an adversary knows the given attributes.

    Parameters:
    - df (pd.DataFrame): The dataset
    - known_attributes (list of str): List of column names known to the attacker

    Returns:
    - dict: Anonymity statistics
    """
    grouped = df.groupby(known_attributes).size().reset_index(name='count')

    num_users = len(df)
    total_groups = len(grouped)
    num_unique_groups = len(grouped[grouped['count'] == 1])
    average_group_size = grouped['count'].mean()
    max_group_size = grouped['count'].max()
    min_group_size = grouped['count'].min()
    anonymity_distribution = grouped['count'].value_counts().sort_index()

    return {
        "known_attributes": known_attributes,
        "total_groups": total_groups,
        "num_unique_groups": num_unique_groups,
        "percent_unique": round(num_unique_groups / num_users * 100, 2),
        "average_group_size": round(average_group_size, 2),
        "max_group_size": max_group_size,
        "min_group_size": min_group_size,
        "anonymity_distribution": anonymity_distribution.to_dict(),
        "num_users" : num_users
    }

if __name__ == "__main__":
    # Load the data
    df = pd.read_csv("data/TAP_PRUNED_10k.csv")

    # Define known auxiliary attributes
    known = ['Academic Year', 'Income by $10,000 Range', 'TAP Recipient Dollars']

    # Run the simulation
    stats = simulate_auxiliary_knowledge(df, known)

    # Pretty print results
    print("\nAnonymity Reduction Analysis")
    print(f"Known Attributes: {', '.join(known)}")
    print(f"Total Unique Groups: {stats['total_groups']}")
    print(f"Groups of Size 1 (Re-identified): {stats['num_unique_groups']} ({stats['percent_unique']}%)")
    print(f"Average Group Size: {stats['average_group_size']}")
    print(f"Max Group Size: {stats['max_group_size']}")
    print(f"Min Group Size: {stats['min_group_size']}")
    print("\nAnonymity Distribution (group size → # of groups):")
    for size, count in stats['anonymity_distribution'].items():
        print(f"  {size}: {count}")
    
    print(f"\nnum users: {stats['num_users']} ")

