# This script was generated with guidance from ChatGPT (OpenAI, April 2025).

import pandas as pd

def analyze_at_risk(filepath):
    # Load the dataset
    df = pd.read_csv(filepath)

    # Define the high-risk pseudo-identifier combination
    risky_combo = ['Academic Year', 'Income by $1,000 Range', 'TAP Recipient Dollars']

    # Calculate group size for each row
    df['group_size'] = df.groupby(risky_combo)[risky_combo[0]].transform('count')

    # Filter to find individuals in groups of size 1 (fully re-identifiable)
    at_risk = df[df['group_size'] == 1]

    # Summarize the most common attributes among at-risk individuals
    top_income = at_risk['Income by $1,000 Range'].value_counts().head(5)
    top_awards = at_risk['TAP Recipient Dollars'].value_counts().head(5)
    top_years = at_risk['Academic Year'].value_counts().head(5)

    # Show a few re-identifiable combinations
    unique_examples = at_risk[risky_combo].value_counts().reset_index().head(10)
    unique_examples.columns = risky_combo + ['count']

    # Print the analysis
    print("\nAt-Risk Group Summary")
    print(f"Total re-identifiable individuals (group size = 1): {len(at_risk)}\n")

    print("Top 5 Income Brackets:")
    print(top_income.to_string(), "\n")

    print("Top 5 TAP Award Amounts:")
    print(top_awards.to_string(), "\n")

    print("Top 5 Academic Years:")
    print(top_years.to_string(), "\n")

    print("Examples of fully re-identifiable combinations:")
    print(unique_examples.to_string(index=False))


if __name__ == "__main__":
    analyze_at_risk("data/TAP_PRUNED.csv")

