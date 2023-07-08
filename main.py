import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot olarak giriş yapıldı: {bot.user.name}')

@bot.command()
async def cekilis(ctx, *isimler):
    isimler = list(isimler)  # Tuple'ı liste olarak dönüştürme

    if len(isimler) < 10:
        await ctx.send("Lütfen en az 10 isim girin.")
        return

    random.shuffle(isimler)

    takim1 = isimler[:5]
    takim2 = isimler[5:]

    embed = discord.Embed(title="Çekiliş Sonuçları", color=discord.Color.green())

    takim1_text = "\n".join([f"{i+1}. {takim1[i]}" for i in range(5)])
    takim2_text = "\n".join([f"{i+1}. {takim2[i]}" for i in range(5)])

    embed.add_field(name="Takım 1:", value=takim1_text, inline=False)
    embed.add_field(name="Takım 2:", value=takim2_text, inline=False)

    await ctx.send(embed=embed)

# Discord bot tokeni
bot.run('you will enter your discord bot token here')
