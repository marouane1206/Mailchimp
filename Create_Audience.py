from Marketing_email_client import mailchimp_marketing_client
from mailchimp_marketing.api_client import ApiClientError


# Get the Mailchimp Marketing client
mailchimp_marketing = mailchimp_marketing_client()

# Create a message body
body = {
"permission_reminder": "You are receiving this email because you opted in via Lintermediaire.ma.",
"email_type_option": False,
"campaign_defaults": {
    "from_name": "L'intermediaire",
    "from_email": "admin@lintermediaire.ma",
    "subject": "Marketing Email List",
    "language": "EN_US"
},
"name": "Lintermediaire",
"contact": {
    "company": "Lintermediaire",
    "address1": "Villa 336 , Rue des Lucioles",
    "address2": "Riviera, oasis",
    "city": "Casablanca",
    "country": "Morocco"
}
}
try:
    response = mailchimp_marketing.lists.create_list(body)
    print('API called successfully: {}'.format(response))
except ApiClientError as error:
    print("An exception occurred: {}".format(error.text))