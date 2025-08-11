import pandas as pd

def extract_runs_from_local_csv(csv_path, target_config, only_good_runs=True, output_file="output_runs.txt"):
    """
    Extracts run numbers from a local CSV file (e.g., 'Golden.csv'), filtered by target configuration.

    Parameters:
        csv_path (str): Path to the CSV file (e.g., '/content/Golden.csv').
        target_config (str): Target configuration string (e.g., "LD2 + C").
        only_good_runs (bool): If True, only include runs marked as "good".
        output_file (str): Output text file name.
    """

    # Read the CSV file
    df = pd.read_csv("Golden.csv")

    # Cleaning up column names
    df.columns = [col.strip() for col in df.columns]

    # Filter by target configuration from "Solenoid" column
    if "Solenoid" not in df.columns:
        raise KeyError("Missing expected column 'Solenoid' in the CSV file.")

    filtered_df = df[df["Solenoid"].astype(str).str.strip() == target_config]

    # filter for "good" runs. Can chnage to other runs such 'maybe' or 'prod'
    if only_good_runs and "Target" in df.columns:
        filtered_df = filtered_df[
            filtered_df["Target"].astype(str).str.contains("OUT")
        ]

    # Extract run numbers
    run_numbers = filtered_df["Run number"].dropna().astype(int).tolist()

    # Save to text file
    with open(output_file, "w") as f:
        for run in run_numbers:
            f.write(f"{run}\n")

    print(f"✅ Saved {len(run_numbers)} run numbers to '{output_file}'.")


# File path
csv_file_path = "/content/Golden.csv"  # or "/content/Golden.csv" if uploaded there

extract_runs_from_local_csv(
    csv_path=csv_file_path,
    target_config="LD2 + Pb",        # Change this to "LD2 + Pb", as needed
    # target_config="LD2 + Al",
    only_good_runs=True, # Change to false if include all runs
    # output_file="LD2+C_runs.txt"
    output_file="LD2+Pb_OUT_runs.txt"
)
