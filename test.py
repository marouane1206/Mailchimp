import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file (usually in the root directory)


def run():
  """Sends a ping request to the Mailchimp API and handles potential errors.

  This function retrieves the API key from the environment variable named
  'MAILCHIMP_API_KEY' and uses it to create a MailchimpTransactional client.
  It then sends a ping request to the API and prints the response or any errors
  that occur.
  """

  try:
    # Retrieve the API key from the environment variable
    api_key = os.environ.get('MAILCHIMP_API_KEY')

    # Check if the environment variable is set
    if not api_key:
      raise ValueError("MAILCHIMP_API_KEY environment variable not set.")

    # Create the MailchimpTransactional client using the API key
    mailchimp = MailchimpTransactional.Client(api_key)

    # Send a ping request to the API
    response = mailchimp.users.ping()

    # Print the response on success
    print('API called successfully: {}'.format(response))

  except ApiClientError as error:
    # Print the error message if an API error occurs
    print('An exception occurred: {}'.format(error.text))

if __name__ == '__main__':
  run()