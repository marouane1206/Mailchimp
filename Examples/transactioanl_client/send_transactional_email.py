import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError
from Transactional_client import mailchimp_transactional_client

 # Get the Mailchimp transactional client
mailchimp_transactional = mailchimp_transactional_client()  
message = {
    "from_email": "admin@lintermediaire.ma",
    "subject": "Hello world",
    "text": "Welcome to L'intermediaire Transactional!",
    "to": [
      {
        "email": "marouane@lintermediaire.ma",
        "type": "to"
      }
    ]
}

def run():
  try:
    response = mailchimp_transactional.messages.send({"message":message})
    print('API called successfully: {}'.format(response))
  except ApiClientError as error:
    print('An exception occurred: {}'.format(error.text))

run()