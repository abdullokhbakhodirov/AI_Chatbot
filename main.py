from chat_gpt import gpt_turbo
from unique_code import get_unique_code_from_file, write_unique_code_to_file, checking
from pgadmin import add_user, add_data2


def gpt(id):
    count = checking(id)
    while True:
        question = input("You>>> ")
        if question == 'exit':
            break
        answer = gpt_turbo(question, id=id)
        print(f"Daemon>>> {answer}")
        count += 1
        add_data2(str(count), id)



if get_unique_code_from_file() or len(str(get_unique_code_from_file())) == 36 or get_unique_code_from_file() == 'creator':
    try: 
        gpt(get_unique_code_from_file())
    except:
        gpt(get_unique_code_from_file())
else:
    print("You are using our program for the first time so our command from NeuralSage Industry wants to ask you several question fro registration")
    username = input("Your name>>> ")
    password = input("Password>>> ")
    email = input("Email>>> ")
    id = write_unique_code_to_file()
    add_user(id, username, password, '{}', email)
    print("Now you can use our DAEMON chatbot")
    try: 
        gpt(id)
    except:
        gpt(id)
