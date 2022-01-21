import discord
import shlex
from discord.ext.commands import has_permissions
import requests
import json
from os.path import exists
import subprocess

client = discord.Client()

def reverse(string):
    return string[::-1]

@client.event
async def on_ready():
	print("Bot ready!")
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="ruby on " + str(len(client.guilds)) + " servers"))

	for guild in client.guilds:
		print(guild.name + ": " + str(guild.id))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith("!rb "):
		command = shlex.split(message.content.replace("!rb ", "", 1))[0]
		if command == "help":

			# await message.channel.send("")
			embed=discord.Embed(title="RubyBot", description = "A bot that executes ruby code", color=0xffffff)
			embed.add_field(name="help", value="Usage: !rb help\nShows this list", inline=False)
			embed.add_field(name="run", value="Usage: !rb run <code>\nRuns code", inline=False)
			await message.channel.send(embed = embed)
		if command == "run":
			toRun = message.content.replace("!rb run", "", 1)
			toRunNoSpaces = toRun.replace(" ", "")
			if toRun.startswith("\n"):
				toRun = toRun.replace("\n", "", 1)
			if toRunNoSpaces.startswith("```rb"):
				toRun = toRun.replace("```rb", "", 1)
			elif toRunNoSpaces.startswith("```"):
				toRun = toRun.replace("```", "", 1)
			if toRun.endswith("```"):
				toRun = reverse(reverse(toRun).replace("```", "", 1))
			result = subprocess.run(['/usr/local/CLIrb/rb', toRun], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			stdout = result.stdout.decode('utf-8')
			stderr = result.stderr.decode('utf-8')
			out = stdout.replace('`', '\\`').replace('>', '\\>') + "\n\n" + stderr.replace('`', '\\`').replace('>', '\\>')
			embed=discord.Embed(title="RubyBot", description = "```" + out + "```", color=0xffffff)
			await message.reply(embed=embed, mention_author=False)


@client.event
async def on_guild_join(guild):
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="ruby on " + str(len(client.guilds)) + " servers"))

@client.event
async def on_guild_remove(guild):
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="ruby on " + str(len(client.guilds)) + " servers"))


client.run("OTMxMzYwNTUyMzEwMTczNzU2.YeDTGw.EvQUVBsEO9nykyUIID2xMgS5H_Q")



















