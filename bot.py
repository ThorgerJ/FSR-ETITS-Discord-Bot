import discord

token = "ODE0MjM3NzI4ODM2MTU3NTMx.YDa7-g.bJBVl_0c1k72Y6DSY85uP5kP2ws"
channel_id = 814239399205929065
role_id = 814985448526446642

class MyClient(discord.Client):

	async def on_ready(self):
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Christof Paar"))
		print('Bot logged in as {0}'.format(self.user))

	async def on_message(self, message):
		if message.content.startswith('$server'):
			await message.channel.send('{0.guild.name} {0.guild.id}'.format(message))

		if message.content.startswith('$roles'):
			for r in message.guild.roles:
				await message.channel.send('{0.name} {0.id}'.format(r).replace('@', ''))

		if message.content.startswith('$vchannels'):
			for v in message.guild.voice_channels:
				await message.channel.send('{0.name} {0.id}'.format(v))

		if message.content.startswith('$about'):
			await message.channel.send('FSR-Bot with <3 from ~~TJ~~ FSR ETITS')


	async def on_voice_state_update(self, member, before, after):
		
		if after.channel != None:
			if after.channel.id == channel_id:

				guild = member.guild
				role = guild.get_role(role_id)

				if role is None:
					return

				try:
					await member.add_roles(role)
				except Exception as e:
					print(e)

		if before.channel != None:
			if before.channel.id == channel_id:
				
				guild = member.guild
				role = guild.get_role(role_id)

				if role is None:
					return

				try:
					await member.remove_roles(role)
				except Exception as e:
					print(e)

client = MyClient()
client.run(token)

