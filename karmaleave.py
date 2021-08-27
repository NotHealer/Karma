import discord
from discord.ext import commands
import colorama
import os
from colorama import Fore
import time
import getpass
import asyncio

client = discord.Client()

whitelist = [
    # discord guild ids you don't want to leave
    123456789012345678,
    876543210987654321
]

print(f'''
{Fore.RED} _                       {Fore.BLUE} __                    
{Fore.RED}| |_ ___ ___ _____ ___ ! {Fore.BLUE}|  |   ___ ___ _ _ ___! 
{Fore.RED}| '_| .'|  _|     | .'|  {Fore.BLUE}|  |__| -_| .'| | | -_| 
{Fore.RED}|_,_|__,|_| |_|_|_|__,|  {Fore.BLUE}|_____|___|__,|\_/|___|
{Fore.WHITE}                          Made by {Fore.YELLOW}NotHealer  
{Fore.WHITE}Check out the github page for updates: {Fore.LIGHTBLUE_EX}https://github.com/NotHealer/KarmaLeave/''')

token = input(f'{Fore.WHITE}Enter SelfUser Token?>> ')


@client.event
async def on_ready():
  print(f'''{Fore.GREEN}Logged in as {Fore.YELLOW}"{client.user}" {Fore.GREEN}(ID:{Fore.YELLOW} {client.user.id}{Fore.GREEN})''')
  time.sleep(10)
  print(f'{Fore.YELLOW}⚡Started Leaving Servers⚡')
  print(f'{Fore.RED}')
  for guild in client.guilds:
        try:
            if guild.id not in whitelist:
                server = client.get_guild(guild.id)
                await server.leave()
        except Exception as e:
            print(e)
  print(f'{Fore.GREEN}⚡All Servers Left⚡')
  print(f'{Fore.YELLOW}⚡Started Unfriending all⚡')
  print(f'{Fore.RED}')
  healer = input(f'{Fore.RED}⚡WANT TO CONTINUE WITH UNFRNDING?(yes or no)>> ')
  if healer == 'yes':
    pass
  else:
    print(f"{Fore.WHITE}Thanks for using {Fore.YELLOW}₭₳Ɽ₥₳\nthe script will automaticly close in 5 seconds")
    time.sleep(5)
    raise SystemExit
  for friends in client.user.friends:
        try:
            await friends.remove_friend()
        except:
            print("Error")
  print(f'{Fore.GREEN}⚡All Unfriended⚡')
  print(f"{Fore.WHITE}Thanks for using {Fore.YELLOW}₭₳Ɽ₥₳\nthe script will automaticly close in 5 seconds")
  time.sleep(5)
  raise SystemExit

client.run(token, bot=False)
