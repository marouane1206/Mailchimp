import hashlib
import logging
from mailchimp_marketing.api_client import ApiClientError
from marketing_client import mailchimp_marketing_client
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file (usually in the root directory)

# Set up logging
logging.basicConfig(filename='unsubscribe_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def unsubscribe(email):
    """Unsubscribes a user from a Mailchimp audience.

    Args:
        email (str): The email address of the user to unsubscribe.

    Returns:
        dict: The API response on successful unsubscription, or an error message.
    """

    try:
        # Get the Mailchimp Marketing client
        mailchimp_marketing = mailchimp_marketing_client()

        # Get the Audience ID
        list_id = os.environ.get('MC_AUDIENCE_ID')
        member_email = email
        member_email_hash = hashlib.md5(member_email.encode('utf-8').lower()).hexdigest()
        member_update = {"status": "unsubscribed"}

        # Update the list member
        response = mailchimp_marketing.lists.update_list_member(list_id, member_email_hash, member_update)
        logging.info(f"Unsubscribed user: {email}")
        return response

    except ApiClientError as error:
        logging.error(f"Error unsubscribing user: {email} - {error}")
        return {"error": f"An exception occurred: {error.text}"}