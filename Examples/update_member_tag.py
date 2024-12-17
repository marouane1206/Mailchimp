import hashlib
from mailchimp_marketing.api_client import ApiClientError
from Marketing_email_client import mailchimp_marketing_client
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file (usually in the root directory)

def update_member_tags(email, tag_name):
  """
  Updates a Mailchimp list member's tags.

  Args:
      email (str): The email address of the member.
      tag_name (str, optional): The name of the tag to add or update.

  Returns:
      dict: The API response on success, or an error message.
  """

  subscriber_hash = hashlib.md5(email.encode('utf-8')).hexdigest()
  # Get the Mailchimp Marketing client
  mailchimp_marketing = mailchimp_marketing_client()
  # Get the Audience ID
  list_id = os.environ.get('MC_AUDIENCE_ID')

  try:
      response = mailchimp_marketing.lists.update_list_member_tags(list_id, subscriber_hash, {
          "tags": [{
              "name": tag_name,
              "status": "active"
          }]
      })
      return response
  except ApiClientError as error:
      return {"error": f"An exception occurred: {error.text}"}

