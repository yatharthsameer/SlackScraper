#!/usr/bin/env python
import os
import argparse
from json_utils import load_json, dump_json
from slack import WebClient
import json
import csv

# Function to ensure directory existence
def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

# Load Slack API token from env.json
config = load_json('./env.json')

# Specify the directory where your JSON files will be located
json_directory = "./output/users/members/"

# Create a new CSV file to write the extracted data
csv_file_path = "extracted_data_with_channels.csv"

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-u', '--update', help='update channels', action="store_true")
    args = vars(ap.parse_args())

    # Initialize Slack WebClient with your token
    sc = WebClient(
        token="xoxb-ADD-YOUR-SLACK-BOT-API-TOKEN-HERE")

    # Retrieve user list
    response_users = sc.users_list()
    users = response_users['members']

    # Retrieve list of channels
    response_channels = sc.conversations_list(types="public_channel,private_channel")
    channels = response_channels['channels']

    # Create a dictionary to store users and their channels
    users_and_channels = {}

    # Iterate through channels to retrieve members
    for channel in channels:
        response_members = sc.conversations_members(channel=channel['id'])
        members = response_members['members']

        # Store members' details for each channel
        for member_id in members:
            user = next((user for user in users if user['id'] == member_id), None)
            if user:
                user_details = {
                    'real_name': user['real_name'],
                    'email': user['profile'].get('email', ''),  # Handle missing 'email' field
                    # Add other user details you need
                }
                if member_id not in users_and_channels:
                    users_and_channels[member_id] = {'user_details': user_details, 'channels': []}
                users_and_channels[member_id]['channels'].append(channel['name'])

    # Loop through retrieved users and their channels
    for user in users:
        user_name = user['name']
        memb_path = ensure_dir('./output/users/members')
        user_path = '{}/{}.json'.format(memb_path, user_name)

        try:
            old_json = load_json(user_path)
            if not args['update']:
                print('Already have user {}, skipping...'.format(user_name))
                continue
        except Exception as e:
            old_json = {}
            print('No existing messages, starting from scratch...')

        # Get user's channels from the dictionary
        user_channels = users_and_channels.get(user['id'], {}).get('channels', [])

        # Combine user data and channel data
        user_data = {
            'user': user,
            'channels': user_channels
        }

        print('ADDING ', user_name)

        # Dump combined data to JSON
        dump_json(user_path, user_data)

    # Create a new CSV file to write the extracted data
    with open(csv_file_path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
    
        # Write the header row to the CSV file
        csv_writer.writerow(["Real Name", "Email", "Phone", "Channels"])
    
        # Loop through each JSON file in the directory
        for filename in os.listdir(json_directory):
            if filename.endswith(".json"):
                with open(os.path.join(json_directory, filename), "r") as json_file:
                    data = json.load(json_file)
                
                    user_info = data.get("user", {})
                
                    # Extract the desired fields from the JSON data
                    real_name = user_info.get("real_name", "")
                    email = user_info["profile"].get("email", "")
                    phone = user_info["profile"].get("phone", "")
                    channels = data.get("channels", [])
                
                    # Write the extracted data to the CSV file
                    csv_writer.writerow([real_name, email, phone, ",".join(channels)])

    print("Data extracted and saved to", csv_file_path)

    # Delete JSON files
    for filename in os.listdir(json_directory):
        if filename.endswith(".json"):
            json_file_path = os.path.join(json_directory, filename)
            os.remove(json_file_path)
            print("Deleted JSON file:", json_file_path)
