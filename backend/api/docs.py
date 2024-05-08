from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from . import config 
from . import auth

def create_document(document_title, text):
    try:

        docs_service = build('docs', 'v1', credentials=config.creds)

        created_doc = docs_service.documents().create(body={'title': document_title}).execute()

        requests = [
            {
                'insertText': {
                    'location': {
                        'index': 1,
                    },
                    'text': text,
                }
            }
        ]

        result = docs_service.documents().batchUpdate(
            documentId=created_doc['documentId'],
            body={'requests': requests}
        ).execute()
    
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")



def main():
    auth.authenticate_create_token()
    create_document('Test', 'testing')

if __name__ == '__main__':
    main()