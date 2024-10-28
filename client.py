# to ingreate ai in jarvis we need to pay for api key
import openai

openai.api_key = "sk-2zHHhCYQLt2g-FYJt3lvGkT46htfyYZa1w4mtsM9WRT3BlbkFJd9l_uKxVR6JgIgPmVKFm30xse8DsV1c2WRZWtReGgA"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the weather like today?"}
    ]
)

print(response.choices[0].message['content'])

