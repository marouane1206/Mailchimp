from Marketing_email_client import mailchimp_marketing_client
from mailchimp_marketing.api_client import ApiClientError
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file (usually in the root directory)

# Get the Mailchimp Marketing client
mailchimp_marketing = mailchimp_marketing_client()

# Get the Audience ID
list_id = os.environ.get('MC_AUDIENCE_ID')

# Set the contact details
first_name = "Marouane"
Last_name = "Sanhaji"
email = "marouane.sanhaji@gmail.com"
status = "subscribed"

member_info = {
    "email_address": email,
    "status": status,
    "merge_fields": {
      "FNAME": first_name,
      "LNAME": Last_name
    }
  }

try:
  response = mailchimp_marketing.lists.add_list_member(list_id, member_info)
  print("response: {}".format(response))
except ApiClientError as error:
  print("An exception occurred: {}".format(error.text))