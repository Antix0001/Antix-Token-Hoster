from keep_alive import keep_alive
import os
os.system("pip install yaml")
import discord, json, requests, yaml
from discord.ext import commands
from colored import fg, attr

class colors:
  pink = fg('#FF4DE1')
  gray = fg('#E6F0F5')
  redd = fg('#FF0051')
  blue = fg('#6CFE00')
######################################
config = yaml.safe_load(open("config.yml"))["settings"]
tkn = os.environ['tkn'] #keep's your token safe
r = config['status']
i = config['emoji']
######################################
client = commands.Bot(command_prefix="Antix", self_bot=True)
payload = {"text": r,"emoji_name": i}
headers = {"Authorization":tkn,"content-type":"application/json"}

@client.event
async def on_ready():
   print(f'''
{colors.redd}  █████╗  ███╗  ██╗ ████████╗ ██╗  ██╗  ██╗
{colors.gray} ██╔══██╗ ████╗ ██║ ╚══██╔══╝ ██║  ╚██╗██╔╝
{colors.redd} ███████║ ██╔██╗██║    ██║    ██║   ╚███╔╝
{colors.gray} ██╔══██║ ██║╚████║    ██║    ██║   ██╔██╗
{colors.redd} ██║  ██║ ██║ ╚███║    ██║    ██║  ██╔╝╚██╗
{colors.gray} ╚═╝  ╚═╝ ╚═╝  ╚══╝    ╚═╝    ╚═╝  ╚═╝  ╚═╝ 
{colors.pink}[>] WELCOME TO ANTIX HOSTER
{colors.pink}[>] Connected as : {client.user}"
{colors.pink}[>] Made by Antix#0013{colors.gray}
''')
   requests.patch("https://discord.com/api/v9/users/@me/settings",headers=headers,json={"status": "idle","custom_status": payload})
  
keep_alive()  
client.run(tkn)
