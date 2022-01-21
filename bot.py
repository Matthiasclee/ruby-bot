import discord
import shlex
from discord.ext.commands import has_permissions
import requests
import json
from os.path import exists
import subprocess

client = discord.Client()


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
			embed=discord.Embed(title="ML Bot", description = "Invite: https://dsc.gg/mlbot", color=0xffffff)
			embed.add_field(name="help", value="Usage: -help\nShows this list", inline=False)
			embed.add_field(name="mute", value="Usage: -mute <user>\nMutes a user (Requires there to be a role named \"Muted\")", inline=False)
			embed.add_field(name="unmute", value="Usage: -unmute <user>\nUnmutes a user", inline=False)
			embed.add_field(name="jail", value="Usage: -jail <user>\nPuts a user in jail (Requires there to be a role named \"Jail\")", inline=False)
			embed.add_field(name="unjail", value="Usage: -unjail <user>\nTakes a user out of jail", inline=False)
			embed.add_field(name="delete", value="Usage: -delete <message id>\nDeletes a message", inline=False)
			embed.add_field(name="nick", value="Usage: -nick <user> <nickname>\nChanges the nickname of a user", inline=False)
			embed.add_field(name="kick", value="Usage: -kick <user>\nKicks a user", inline=False)
			embed.add_field(name="ban", value="Usage: -ban <user> <reason>\nBans a user", inline=False)
			embed.add_field(name="unban", value="Usage: -unban <user id>\nUnbans a user", inline=False)
			embed.add_field(name="addrole", value="Usage: -addrole <user> <role>\nGives a user a role", inline=False)
			embed.add_field(name="removerole", value="Usage: -removerole <user> <role>\nRemoves a role from a user", inline=False)
			embed.add_field(name="rr", value="Usage: -rr <description> <emoji> <role>\nMakes a reacction roles message", inline=False)
			embed.add_field(name="poll", value="Usage: -poll <question> <emoji> <description>\nPosts a poll for users to vote", inline=False)
			embed.add_field(name="results", value="Usage: -results <message id>\nShows the results of a poll", inline=False)
			embed.add_field(name="livepoll", value="Usage: -livepoll <question> <emoji> <description>\nPosts a responsive poll for users to vote", inline=False)
			embed.add_field(name="say", value="Usage: -say <message>\nSays something", inline=False)
			embed.add_field(name="bwl", value="Usage: -bwl <add | remove> <word>\nManages the bad words list", inline=False)
			embed.add_field(name="purge", value="Usage: -purge <messages>\nBulk deletes messages", inline=False)
			await message.channel.send(embed = embed)

		if command == "run":
			toRun = message.content.replace("!rb run", "", 1)
			result = subprocess.run(['/usr/local/CLIrb/rb', toRun], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			stdout = result.stdout.decode('utf-8')
			stderr = result.stderr.decode('utf-8')

			await message.channel.send(stdout.replace('`', '\\`') + "\n\n" + stderr.replace('`', '\\`'))


@client.event
async def on_guild_join(guild):
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="ruby on " + str(len(client.guilds)) + " servers"))

@client.event
async def on_guild_remove(guild):
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="ruby on " + str(len(client.guilds)) + " servers"))


client.run("OTMxMzYwNTUyMzEwMTczNzU2.YeDTGw.EvQUVBsEO9nykyUIID2xMgS5H_Q")



















