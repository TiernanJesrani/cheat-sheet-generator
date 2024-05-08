# start the llm summarize from scratch
from openai import OpenAI
from . import keys


client = OpenAI (
    api_key = keys.api_key
)

def message(text, topic):
    return [
        {"role": "system", "content": "You will be given a list of topics, the list may contain several or only one topic. For each topic in the list, pull relevant information from the text section that would be helpful on a cheat sheet for an exam; for example put actual formulas, or practice problems and solutions from the text section pertaining to the specific topic. Separate topics with a label as a header for each topic, followed by the relevant information, and then a new line separation. Each topic should have 200 words or less of information."},
        {"role": "user", "content": "Text: %s, Topic: %s" % (text, topic)}
    ]


def create_summary(text, topic):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=message(text, topic)
    )

    return completion.choices[0].message

def create_multiple_summaries(text, topics):
    message = ""
    for topic in topics:
        message += (create_summary(text, topic)).content
        message += '\n'
    
    return message



# if __name__ == '__main__':
#     create_summary(text, topic)
