import json
import csv
import os

def convert_json_to_csv(input_file, output_file):
    try:
        # 1. Check if the JSON file exists
        if not os.path.exists(input_file):
            print(f"Error: {input_file} not found.")
            return

        # 2. Read and load the JSON data
        with open(input_file, 'r') as f:
            data = json.load(f)

        # 3. Validation: Ensure we have a list of dictionaries
        if isinstance(data, list) and len(data) > 0:
            # Extract headers from the keys of the first item
            headers = data[0].keys()

            # 4. Write to the CSV file
            with open(output_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                
                # Write the header row
                writer.writeheader()
                # Write all data rows
                writer.writerows(data)
                
            print(f"Success! Created {output_file} with {len(data)} rows.")
        else:
            print("Error: JSON data is not in the correct format (list of objects).")

    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Check for syntax errors in your JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    convert_json_to_csv('dummy.json', 'inventory_report.csv')

if __name__ == "__main__":
    main()