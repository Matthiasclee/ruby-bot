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
		command = shlex.split(message.content.replace("!rb ", "", 1).replace("\"", "").replace("'", ""))[0]
		if command == "help":
			embed=discord.Embed(title="RubyBot", description = "A bot that executes ruby code", color=0xffffff)
			embed.add_field(name="help", value="Usage: !rb help\nShows this list", inline=False)
			embed.add_field(name="run", value="Usage: !rb run <code>\nRuns code. If you react with 🔁, the code reruns.", inline=False)
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
			varsdef = "user_name = '" + message.author.name + "'; user_id = '" + str(message.author.id) + "'; user_tag = '" + str(message.author.discriminator) + "';exec_user=user_name;exec_id=user_id;exec_tag=user_tag;"
			toRun = varsdef + toRun
			embed=discord.Embed(title="Running...", description = "```Running...```", color=0xffffff)
			msg = await message.reply(embed=embed, mention_author=False)
			result = subprocess.run(['/usr/local/CLIrb/rb', toRun], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			stdout = result.stdout.decode('utf-8')
			stderr = result.stderr.decode('utf-8')
			out = stdout + "\n\n" + stderr
			embed=discord.Embed(title="Output", description = "```\n" + out + "\n```", color=0xffffff)
			await msg.edit(embed=embed)
			await msg.add_reaction("🔁")


@client.event
async def on_guild_join(guild):
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="ruby on " + str(len(client.guilds)) + " servers"))

@client.event
async def on_guild_remove(guild):
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="ruby on " + str(len(client.guilds)) + " servers"))

@client.event
async def on_raw_reaction_add(ctx):
	message_id = str(ctx.message_id)
	user = ctx.member
	if user == client.user:
		return;
	else:
		guild = user.guild
		emoji = ctx.emoji.name
		if emoji == "🔁":
			channel = discord.utils.get(guild.channels, id=ctx.channel_id)
			msg = await channel.fetch_message(message_id)
			if msg.author == client.user:
				embed=discord.Embed(title="Rerunning...", description = "```Rerunnning...```", color=0xffffff)
				await msg.edit(embed=embed)
				code_message = await channel.fetch_message(str(msg.reference.message_id))
				toRun = code_message.content.replace("!rb run", "", 1)
				toRunNoSpaces = toRun.replace(" ", "")
				if toRun.startswith("\n"):
					toRun = toRun.replace("\n", "", 1)
				if toRunNoSpaces.startswith("```rb"):
					toRun = toRun.replace("```rb", "", 1)
				elif toRunNoSpaces.startswith("```"):
					toRun = toRun.replace("```", "", 1)
				if toRun.endswith("```"):
					toRun = reverse(reverse(toRun).replace("```", "", 1))
				varsdef = "user_name = '" + code_message.author.name + "'; user_id = '" + str(code_message.author.id) + "'; user_tag = '" + str(code_message.author.discriminator) + "';exec_user='" + user.name + "';exec_id='"+str(user.id)+"';exec_tag='" + str(user.discriminator) + "';"
				toRun = varsdef + toRun
				result = subprocess.run(['/usr/local/CLIrb/rb', toRun], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				stdout = result.stdout.decode('utf-8')
				stderr = result.stderr.decode('utf-8')
				out = stdout + "\n\n" + stderr
				embed=discord.Embed(title="Output", description = "```\n" + out + "\n```", color=0xffffff)
				await msg.edit(embed=embed)
				await msg.remove_reaction(emoji, user)

client.run("OTMxMzYwNTUyMzEwMTczNzU2.YeDTGw.EvQUVBsEO9nykyUIID2xMgS5H_Q")



















