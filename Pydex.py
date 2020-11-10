import wolframalpha

user_input = input("Ask a question: ")
app_id = "E7H2EU-267UWJ7XRP"

client = wolframalpha.Client(app_id)

result = client.query(user_input)
answer = next(result.results).text

print(answer)

