import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from . import config 


def authenticate_create_token():
   # If modifying these scopes, delete the file token.json.
  SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly", 
            "https://www.googleapis.com/auth/presentations.readonly", 
            "https://www.googleapis.com/auth/documents"]
  config.creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    config.creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not config.creds or not config.creds.valid:
    if config.creds and config.creds.expired and config.creds.refresh_token:
      config.creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      config.creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(config.creds.to_json())

  

def main():
  authenticate_create_token()
  



if __name__ == '__main__':
    main()
    