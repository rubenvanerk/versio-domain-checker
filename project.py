#!/usr/bin/env python
import yaml
import os
from os.path import join, dirname
from dotenv import load_dotenv
import json
import requests

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# open config.yaml
with open("config.yaml", 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# set endpoint
VERSIO_API_ENDPOINT = 'https://www.versio.nl/testapi/v1/' if config['test_mode'] else 'https://www.versio.nl/api/v1/'

# create auth
versio_email_address = os.getenv('VERSIO_EMAIL_ADDRESS')
versio_password = os.getenv('VERSIO_PASSWORD')
auth = (versio_email_address, versio_password)

# get list of already registered domains on current account
response = requests.get(VERSIO_API_ENDPOINT + 'domains', auth=auth)
json_response = json.loads(response.text)
registered_domains_details = json_response['DomainsList']
registered_domains = [d['domain'] for d in registered_domains_details]

# remove registered domains from wanted domains
wanted_domains = config['domains']
domains_to_check = [i for i in wanted_domains if i not in registered_domains]

# remove all domains that aren't available
available_domains = []
for domain in domains_to_check:
    response = requests.get(VERSIO_API_ENDPOINT + 'domains/' + domain + '/availability', auth=auth)
    json_response = json.loads(response.text)
    if json_response['available']:
        available_domains.append(domain)

# register all remaining domains
contact_id = config['contact_id']
for domain in available_domains:
    print('registering ' + domain)
    registration_request = {'contact_id': contact_id, 'years': '1', 'auto_renew': 'false'}
    response = requests.post(VERSIO_API_ENDPOINT + 'domains/' + domain, auth=auth, data=registration_request)
    json_response = json.loads(response.text)
    print(json_response)

# send notification with registered domains
