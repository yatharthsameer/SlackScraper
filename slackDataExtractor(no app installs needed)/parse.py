import json
import csv

# Load JSON data from the file
with open('users.json', 'r') as json_file:
    data = json.load(json_file)

# Extract desired fields and create a list of dictionaries
output_data = []
for user in data:
    profile = user.get('profile', {})
    real_name = profile.get('real_name', '')
    phone = profile.get('phone', '')
    email = profile.get('email', '')
    title = profile.get('title', '')

    output_data.append({
        'real_name': real_name,
        'phone': phone,
        'email': email,
        'title': title
    })

# Write the extracted data into a CSV file
csv_fields = ['real_name', 'phone', 'email', 'title']
csv_filename = 'output.csv'

with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_fields)
    writer.writeheader()
    for row in output_data:
        writer.writerow(row)

print(f'CSV file "{csv_filename}" created.')
