import os
import time
import json

# 3rd party libraries
import requests
import jwt

# Scope must be at least one of:
# https://www.googleapis.com/auth/compute.readonly  
# https://www.googleapis.com/auth/cloud-platform  
# https://www.googleapis.com/auth/monitoring.read 
# Request multiple scopes with a space-delimited string

SCOPE = "https://www.googleapis.com/auth/monitoring.read"


def getCredentials():
    # Get credentials from env variables
    # Or file
    # Or user input if no vars
    email = ''
    secret = ''
    credential_file = ''
    if os.environ.get("GOOGLE_SERVICE_CREDENTIALS", None):
        credential_file = os.environ["GOOGLE_SERVICE_CREDENTIALS"]
    else:
        if os.environ.get("SERVICE_ACCOUNT_EMAIL", None):
            email = os.environ["SERVICE_ACCOUNT_EMAIL"]
        else:
            email = raw_input("Enter service account email address: ")
        if os.environ.get("SERVICE_ACCOUNT_SECRET", None):
            secret = os.environ["SERVICE_ACCOUNT_SECRET"]
        else:
            secret = raw_input("Enter service account key: ")

    if credential_file:
        creds = json.load(open(credential_file, 'r'))
        email = creds['client_email']
        secret = creds['private_key']

    return (email, secret)


def requestToken():
    header = {"alg": "RS256", "typ": "JWT"}  # Google uses SHA256withRSA
    # See https://developers.google.com/identity/protocols/OAuth2ServiceAccount#authorizingrequests
    email, secret = getCredentials()

    issued = int(time.time())
    expires = issued + 3600  # Expires in 1 hour

    authorization_url = "https://www.googleapis.com/oauth2/v4/token"
    payload = {"iss": email,  # Issuer Claim
               "scope": SCOPE,
               "aud": authorization_url,  # Audience Claim
               "exp": expires,
               "iat": issued  # Issued At Claim
               }

    sig = jwt.encode(payload, secret, algorithm="RS256", headers=header)
    params = {"grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
              "assertion": sig}

    r = requests.post(authorization_url, data=params)

    if r.ok:
        print r.json()['access_token']
    else:
        print r.text

if __name__ == "__main__":
    requestToken()