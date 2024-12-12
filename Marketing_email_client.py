from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file (usually in the root directory)


def mailchimp_marketing_client():
    """Retrieves API credentials from environment variables and creates a Mailchimp Marketing client.

    Returns:
        Client: A Mailchimp Marketing client object.

    Raises:
        ValueError: If either MC_MARKETING_API_KEY or MC_SERVER_PREFIX environment variable is not set.
    """

    api_key = os.environ.get('MC_MARKETING_API_KEY')
    server_prefix = os.environ.get('MC_SERVER_PREFIX')

    if not api_key:
        raise ValueError("MC_MARKETING_API_KEY environment variable not set.")

    if not server_prefix:
        raise ValueError("MC_SERVER_PREFIX environment variable not set.")

    try:
        mailchimp_marketing = Client()
        mailchimp_marketing.set_config({
            "api_key": api_key,
            "server": server_prefix
        })
        return mailchimp_marketing
    
    except ApiClientError as error:        
        return ("An exception occurred: {}".format(error.text))

