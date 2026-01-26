import csv
import subprocess
import os
import json
import sys


def create_csv_from_json(json_file, csv_file): 
    with open(json_file, 'r') as jf:
        data = json.load(jf)

    with open(csv_file, 'w', newline='') as cf:
        writer = csv.writer(cf)
        # Write header
        writer.writerow(data[0].keys())
        # Write data rows
        for entry in data:
            writer.writerow(entry.values())

        




# 