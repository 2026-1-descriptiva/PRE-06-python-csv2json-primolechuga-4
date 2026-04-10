import csv
import json

def convert_csv_to_json():
    csv_file = 'files/drivers.csv'
    json_file = 'files/drivers.json'
    data = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

# Run the conversion when the module is imported
convert_csv_to_json()

if __name__ == '__main__':
    pass  # Already ran on import