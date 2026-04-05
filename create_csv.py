import csv
import subprocess
import os
import json
import sys


import csv

data = {
    "status": "success",
    "metadata": {
        "generated_at": "2026-01-26T19:05:31Z",
        "request_id": "req-99x-8822",
        "version": "v2.1"
    },
    "data": {
        "user": {
            "id": 501,
            "username": "dev_guru_2026",
            "is_active": True,
            "profile": {
                "first_name": "Abhishek",
                "last_name": "Singh",
                "contact": {
                    "email": "abhishek@example.cloud",
                    "phones": [
                        { "type": "mobile", "number": "+91-98765-43210", "primary": True },
                        { "type": "work", "number": "+91-11-2345-6789", "primary": False }
                    ]
                },
                "addresses": [
                    {
                        "label": "Home",
                        "street": "123 Tech Park Lane",
                        "city": "Hyderabad",
                        "geo": { "lat": 17.3850, "lng": 78.4867 }
                    }
                ]
            }
        },
        "recent_orders": [
            {
                "order_id": "ORD-7721",
                "date": "2026-01-20",
                "total": 149.99,
                "currency": "USD",
                "items": [
                    {
                        "product_id": "P-101",
                        "name": "Mechanical Keyboard",
                        "quantity": 1,
                        "specs": { "switch_type": "Cherry MX Blue", "backlight": "RGB" }
                    },
                    {
                        "product_id": "P-205",
                        "name": "USB-C Cable",
                        "quantity": 2,
                        "specs": { "length": "2m", "braided": True }
                    }
                ]
            }
        ]
    }
}

def flatten_json(y):
    """Recursively flattens a nested dictionary."""
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            # For lists, we convert them to strings to keep them in one cell
            out[name[:-1]] = str(x)
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

# 1. Flatten the dictionary
flattened_data = flatten_json(data)

# 2. Extract keys for header and values for the row
headers = flattened_data.keys()
row_values = flattened_data.values()

# 3. Write to CSV
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)    # Write Header
    writer.writerow(row_values) # Write Data Row

print("CSV file 'output.csv' has been created successfully.")