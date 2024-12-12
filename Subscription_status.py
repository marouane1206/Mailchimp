import hashlib
from mailchimp_marketing.api_client import ApiClientError
from Marketing_email_client import mailchimp_marketing_client
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file (usually in the root directory)

# Get the Mailchimp Marketing client
mailchimp_marketing = mailchimp_marketing_client()

list_id = os.environ.get('MC_AUDIENCE_ID')

member_email = "admin@lintermediaire.ma"
member_email_hash = hashlib.md5(member_email.encode('utf-8').lower()).hexdigest()

try:
  response = mailchimp_marketing.lists.get_list_member(list_id, member_email_hash)
  print("Response: {}".format(response['status']))
except ApiClientError as error:
  print("An exception occurred: {}".format(error.text))