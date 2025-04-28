# This script appends data to a CSV file in a specified format.
import csv
import os
from datetime import datetime

def append_data_to_csv(data):
    # Create the 'output' folder if it doesn't exist
    output_folder = 'output'
    os.makedirs(output_folder, exist_ok=True)

    # Generate filename: day-month-year-hour-minute
    current_time = datetime.now().strftime('%d-%m-%Y-%H-%M')
    filename = f'data-{current_time}.csv'
    file_path = os.path.join(output_folder, filename)

    # Define column headers
    headers = data[0].keys() if data else []

    # Append data to CSV
    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f'Data appended to {file_path}')



