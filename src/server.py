import discord
import os
from dotenv import load_dotenv
import time

load_dotenv()
bot = discord.Bot()

@bot.slash_command(name="ping")
async def global_command(ctx):
    await ctx.respond(f"Pong in {round(bot.latency*1000, 1)}ms!")

@bot.event
async def on_ready():
    print("Started successfully")

print("Starting...")
bot.run(os.environ.get('TOKEN'))