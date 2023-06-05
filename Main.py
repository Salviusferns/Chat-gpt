import openai


def chat_with_gpt(message):
  response = openai.Completion.create(engine="text-davinci-003",
                                      prompt=message,
                                      max_tokens=50,
                                      temperature=0.7)
  return response.choices[0].text.strip()


def main():
  api_key = "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"
  openai.api_key = api_key

  user_input = input("User: ")
  while user_input.lower() != "exit":
    response = chat_with_gpt(user_input)
    print("ChatGPT:", response)
    user_input = input("User: ")


if __name__ == "__main__":
  main()
