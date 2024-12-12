import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file (usually in the root directory)


def mailchimp_transactional_client():
  """Retrieves API credentials from environment variables and creates a Mailchimp Transactional client.

  Returns:
    Client: A Mailchimp Transactional client object.

  Raises:
    ValueError: If MC_TRANSACTIONAL_API_KEY environment variable is not set.
  """
  try:
    # Retrieve the API key from the environment variable
    api_key = os.environ.get('MC_TRANSACTIONAL_API_KEY')

    # Check if the environment variable is set
    if not api_key:
      raise ValueError("MC_TRANSACTIONAL_API_KEY environment variable not set.")

    # Create the MailchimpTransactional client using the API key
    mailchimp_transactional = MailchimpTransactional.Client(api_key)
    return mailchimp_transactional

  except ApiClientError as error:        
        return ("An exception occurred: {}".format(error.text))