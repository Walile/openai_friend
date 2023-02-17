import openai
openai.api_key = ''
ask = "\nHuman: 泰國有幾年的歷史?\nAI:"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt= ask,
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)
print(response["choices"][0]["text"])