# When deploy on your local machine, please use ‘pip install openai‘ to install OpenAI library
import openai
import getpass

# Insert your OPENAI API Key here
# Do not publish or reveal Your API KEY
# Find your API Key at: https://platform.openai.com/account/api-keys
openai.api_key = "PUT KEY HERE"

chat_messages_old = [{
  "role": "system",
  "content": "You are a mathematics calculator."
}, {
  "role": "system",
  "content": "You must strictly format your answer in JSON."
}, {
  "role": "system",
  "content": "When you don't have an answer output N/A"
}, {
  "role":
  "system",
  "content":
  "When you answer, try NOT give any textual explanation and reasoning."
}, {
  "role":
  "system",
  "content":
  "You should output your result in this format: {\"result\": \"YOUR ANSER\", \"reasoning\": \"YOUR REASONING (when needed)\"}"
}, {
  "role":
  "system",
  "content":
  "When user is asking to exit/quit the chat, let them know they may enter 'exit' to exit the program"
}]

chat_messages = []

current_model = "gpt-3.5-turbo"


def get_msg_from_input():
  user_input = input("user: ")

  if user_input == "exit":
    print("\n*** Program Exited ***\n")
    exit()
  message = {"role": "system", "content": user_input.__str__()}
  chat_messages.append(message)
  #possibly add some functionality to save here
  create_chat()
  chat_messages.clear()


def get_new_apikey():
  if input("system: Enter a new API key? Y/N: ") == "Y":
    openai.api_key = getpass.getpass("Your API Key (Your input is hidden): ")
    print(
      "system: Key entered. Your updated Key will only be apply to current session. Please update your key in source code."
    )
  else:
    print("Enter \'exit\' to exit program.\n")


def create_chat():
  try:
    response = openai.ChatCompletion.create(model=current_model,
                                            messages=chat_messages)

    response_msg = response['choices'][0]['message']
    chat_messages.append(response_msg)
    print(response_msg['role'] + ": " + response_msg['content'])
  except openai.error.AuthenticationError:
    print(
      "system: Something went wrong when authenticating with server (AuthenticationError)"
    )
    print(
      "system: Your API key or token might be invalid, expired, or revoked")
    print(
      "system: Check or find your OpenAI API key at: https://platform.openai.com/account/api-keys"
    )
    get_new_apikey()
  except openai.error.RateLimitError:
    print("system: You have hit your assigned rate limit. (RateLimitError)")
    print(
      "system: If your are not a pay as you go user, add your payment mehtods at: https://platform.openai.com/account/billing/overview"
    )
    print(
      "system: Or manage your usage rate at: https://platform.openai.com/account/billing/limits"
    )
    get_new_apikey()
  except openai.error.Timeout:
    print("system: Your Request timed out. (Timeout)")
    print(
      "system: Please retry after a brief wait. Check OpenAI system status at: https://status.openai.com/?slack_message_token=default_success"
    )
    print("Enter \'exit\' to exit program.\n")
  except openai.error.ServiceUnavailableError:
    print(
      "system: OpenAI service is currently unavaliable (ServiceUnavailableError)"
    )
    print(
      "system: Please retry after a brief wait. Check OpenAI system status at: https://status.openai.com/?slack_message_token=default_success"
    )
    print("Enter \'exit\' to exit program.\n")
  except openai.error.InvalidRequestError:
    print(
      "system: Your request was malformed or missing some required parameters, such as a token or an input. (InvalidRequestError)"
    )
    print(
      "system: Chect OpenAi documentation at: https://platform.openai.com/docs/api-reference/"
    )
    print("Enter \'exit\' to exit program.\n")
  except openai.error.APIConnectionError:
    print(
      "system: Something went wrong while connecting to OpenAI's API. (APIConnectionError)"
    )
    print(
      "system: If you are running on replit. Check replit's system status at: https://status.replit.com"
    )
    print(
      "system: On your own deployment, check your network settings, proxy configuration, SSL certificates, or firewall rules."
    )
    print("Enter \'exit\' to exit program.\n")
  except Exception as e:
    print(
      "system: Something went wrong when parsing your message or communicating to server"
    )
    print("error_message: \n" + e.__str__())
    print("Enter \'exit\' to exit program.\n")


print("\n******* Welcome to 118GPT *******")
print("Current Model: " + current_model)
print("Enter \'exit\' to exit program.\n")

while True:
  print(chat_messages)  
  get_msg_from_input()
