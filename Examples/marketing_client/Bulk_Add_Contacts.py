import json
from marketing_client import mailchimp_marketing_client
from mailchimp_marketing.api_client import ApiClientError
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file (usually in the root directory)

# Get the Mailchimp Marketing client
mailchimp_marketing = mailchimp_marketing_client()

# Get the Audience ID
list_id = os.environ.get('MC_AUDIENCE_ID')

# Read the JSON file
try:
  with open("Data/Contacts.json", "r") as file:
    member_data = json.load(file)  # Clearer variable name

  # Use enumerate to iterate with member ID (string)
  member_info_list = []  # Create an empty list for member dictionaries
  for member_id, member_details in member_data.items():
    # Check if member_details is a dictionary (handle potential nested structures)
    if isinstance(member_details, dict):
      # Extract member information and create a dictionary for each member
      member_info_list.append({
        "email_address": member_details.get("email_address"),
        "status": member_details.get("status"),
        "merge_fields": member_details.get("merge_fields"),
        # Optional fields (assuming they are not always present)
        "phone_number": member_details.get("Phone Number", None),
        "tags": member_details.get("Tags", None),
      })
    else:
      print(f"Error: Unexpected data format for member with ID {member_id}. Skipping.")

except FileNotFoundError:
  print("Error: Contacts.json file not found.")
  exit(1)

try:
  # Call the API function with member information as a list of dictionaries
  response = mailchimp_marketing.lists.batch_list_members(list_id, {"members": member_info_list})
  print("Batch update successful.")
  print(response)
except ApiClientError as error:
  print("An exception occurred: {}".format(error.text))