import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import config 
import auth

def main():
    auth.authenticate_create_token()

if __name__ == '__main__':
    main()