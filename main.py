from keep_alive import keep_alive
import requests, sys, time, os, json
from colored import fg, attr
from colorama import Fore, Style

############################################
token = "your-token"
status = "Hey this id is hosted"
emoji = "emoji" 
emoji_id = "<emoji-id>"
############################################

class colors:
  pink = fg('#FF4DE1')
  gray = fg('#E6F0F5')
  redd = fg('#FF0051')
  blue = fg('#6CFE00')
headers = {"Authorization": token, "content-type": "application/json"}

print(f'''
{colors.redd}  █████╗  ███╗  ██╗ ████████╗ ██╗  ██╗  ██╗
{colors.gray} ██╔══██╗ ████╗ ██║ ╚══██╔══╝ ██║  ╚██╗██╔╝
{colors.redd} ███████║ ██╔██╗██║    ██║    ██║   ╚███╔╝
{colors.gray} ██╔══██║ ██║╚████║    ██║    ██║   ██╔██╗
{colors.redd} ██║  ██║ ██║ ╚███║    ██║    ██║  ██╔╝╚██╗
{colors.gray} ╚═╝  ╚═╝ ╚═╝  ╚══╝    ╚═╝    ╚═╝  ╚═╝  ╚═╝ 
{colors.pink}[>] WELCOME TO ANTIX HOSTER
{colors.pink}[>] Your ID is Hosted
{colors.pink}[>] Made by Antix#0013{colors.gray}
''')

class antix:
  def status(self):
    r = requests.patch("https://discord.com/api/v9/users/@me/settings",
                       headers=headers,
                       json={
                         "status": "idle",
                         "custom_status": {
                           "text": status,
                           "emoji_name": emoji,
                           "emoji_id": int(emoji_id)
                         }
                       })
    if r.status_code == 401:
      print("Invalid token")
      sys.exit()
    elif r.status_code == 429:
      print("Too many requests")
      time.sleep(10)
      sys.exit()
    else:
      pass

  def start(self):
    self.status()
    antix().start()
keep_alive()
antix().start()
