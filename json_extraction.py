import csv
import json

# Function to load data from a JSON file
def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to append data to a CSV file
def append_data_to_csv(data, csv_file_path):
    # Check if the file exists to determine if headers are needed
    try:
        with open(csv_file_path, 'x') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    except FileExistsError:
        with open(csv_file_path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writerows(data)

# Main execution
if __name__ == "__main__":
    json_file_path = 'data.json'
    csv_file_path = 'results.csv'

    # Load data from JSON file
    data = load_data_from_json(json_file_path)

    # Append data to CSV file
    append_data_to_csv(data, csv_file_path)

    print(f"Data appended successfully to {csv_file_path}.")
