import discord as Discord

DISCORD_TOKEN = "MTI3NzQ0NTUyMzgyMDc3NzUxMw.G0nB20.RZ_ORQYTzMx4SGqnyF3grfX4J5wSGJxTeXGJzY"
CHANNEL = 709408355181002847

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = Discord.Client(intents=Discord.Intents.default())

async def send_msg(channel ,message):
    channel = bot.get_channel(channel)
    await channel.send(message)

def run_bot() -> None:
    bot.run(DISCORD_TOKEN)
    