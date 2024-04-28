import config
import auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_presentation_text(pres_id):
    try:
        service = build("slides", "v1", credentials=config.creds)

        # Call the Slides API
        presentation = (
            service.presentations().get(presentationId=pres_id).execute()
        )
        
        # need to make something which groups all of the text from a presentation into relevant order
        # so we pass potentially concatendated information to the llm that we took from a presentation


        
    
    except HttpError as err:
        print(err)

    slides = presentation.get("slides", [])

    slides_text = {}

    for slide in slides:
        slide_id = slide['objectId']
        slide_elements = slide.get('pageElements', [])
        slide_content = ""
        for element in slide_elements:
            if 'shape' in element and 'text' in element['shape']:
               text_elements = element['shape']['text'].get('textElements', [])
               for text_element in text_elements:
                    if 'textRun' in text_element:
                        text = text_element['textRun']['content']
                        slide_content += text + "\n"
        slides_text[slide_id] = slide_content

    print(slides_text)

def main():
    auth.authenticate_create_token()
    get_presentation_text('12bJXqLGbmSexRn_debWLlhbR2rD3sS0-OFlhPXoCn3A')

if __name__ == '__main__':
    main()