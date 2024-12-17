import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError
from Transactional_client import mailchimp_transactional_client

def run():
  try:
    # Get the Mailchimp transactional client
    mailchimp_transactional = mailchimp_transactional_client()  
    response = mailchimp_transactional.users.ping()
    print('API called successfully: {}'.format(response))
  except ApiClientError as error:
    print('An exception occurred: {}'.format(error.text))

run()