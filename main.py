import requests

print('''
      ---------------------
      ABH'S DISCORD SPAMMER
      ---------------------
          @abudgethuman
      ''')

try:
    file = open("token.txt").read()
except:
    open("token.txt", "x")
    file = open("token.txt").read()
    
if file != "":
    token = file
    saved = True
else:
    token = input("Token: ")
    saved = False

headers = {'authorization':token}

user = requests.get("https://discord.com/api/v9/users/@me", headers=headers).json()
if not user["username"]:
    print("Invalid token.")
    exit()

if saved == False:
    save = input(f'Logged in as: {user["username"]}[{user["id"]}]\n\nSave token? y/n: ')
    if save.lower() == 'y':
        file = open("token.txt", "w")
        file.write(token)
        file.close()
        print("Saved.")
        saved = True
else:
    print(f'Logged in as: {user["username"]}[{user["id"]}]')

chId = input("Channel Id: ")
msg = input("Message: ")
amt = int(input("Amount: "))

while amt > 0:
    requests.post(f"https://discord.com/api/v9/channels/{chId}/messages", {"content":msg}, headers=headers)
    print("Sent ", amt)
    amt -= 1
