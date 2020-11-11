import wolframalpha
import wikipedia

while True:
    user_input = input("Ask a question: ")
    try:
        # Based on Wolfram Alpha
        app_id = "E7H2EU-267UWJ7XRP"
        client = wolframalpha.Client(app_id)
        result = client.query(user_input)
        answer = next(result.results).text
        print(answer)
    except:
        # Based on Wikipedia
        # wikipedia.set_lang("") - If you want to change language
        print(wikipedia.summary(user_input, sentences=2))



