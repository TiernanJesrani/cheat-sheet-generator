import config
import auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# get a list of presentations the user has access to
def get_presentations():
    try:

        drive_service = build('drive', 'v3', credentials=config.creds)

        response = drive_service.files().list(q="mimeType='application/vnd.google-apps.presentation'",
                                      fields='files(id, name, webViewLink)').execute()
        files = response.get('files', [])

        return files

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")

def main():
    auth.authenticate_create_token()
    print(get_presentations())

if __name__ == '__main__':
    main()
