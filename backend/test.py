# this will be a file to test several things
# 1. pulling presentation information from slides - COMPLETE
# 2. summarizing that information based on our topic key words - COMPLETE
# 3. writing the summaries to a google doc - COMPLETE

from api import auth, docs, drive, slides, config
from llm import keys, summarize



def main(): 
    auth.authenticate_create_token()
    presentations = drive.get_presentations()
    chosen_pres = []
    chosen_pres.append(presentations[0]['id'])
    chosen_pres.append(presentations[1]['id'])
    presentation_text = slides.get_mult_pres_text(chosen_pres)
     
    summary = summarize.create_summary(presentation_text, "Vertex Cover")

    docs.create_document("cheat-sheet-generator", summary.content)
    
    return

if __name__ == '__main__':
    main()

