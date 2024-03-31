import discord
import random
from discord.ext import commands
import os
from flask import ctx
import requests
intents = discord.Intents.default()
intents.message_content = True
from random import choice 
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен!')



@bot.command()
async def GP(ctx): 
     '''Сайт о глобальном потеплении'''
     eco = "https://www.un.org/ru/un75/climate-crisis-race-we-can-win" 
     ego = ("Этот сайт поможет нам узнать как бороться с глобальным потеплением!")
     await ctx.send(eco)   
     await ctx.send(ego)

@bot.command()
async def Causes_GP(ctx): 
     '''Причины глобального потепления'''
     Save = "https://www.un.org/ru/climatechange/science/causes-effects-climate-change"
     Answer = ("Давайте узнаем причины глобального потепления!")
     await ctx.send(Save)
     await ctx.send(Answer)

@bot.command()
async def egology(ctx):
    '''Показывает график температуры'''
    Grafik_name = random.choice(os.listdir("Kartinochki"))
    with open(f'Kartinochki/{Grafik_name}', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)    
          

@bot.command()
async def Meme(ctx):
    '''Показывает Мем с решением глобального потепления'''
    Memes_name = random.choice(os.listdir("Memes"))
    with open(f'Memes/{Memes_name}', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)

    First_step = "Первый способ как бороться с ГП - Посадка деревьев,Второй способ - переработка углекислого газа, третий способ - переход на электрические автомобили"
    await ctx.send(First_step)

@bot.command()
async def Met(ctx):
    '''Показывает мем с причинами глобального потепления(Для тех кто не хочет искать на сайте причины ГП)'''
    Ultra_name = random.choice(os.listdir("Memes_2"))
    with open(f'Memes_2/{Ultra_name}', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)

    Second_step = "Причины глобального потепления: Производство электроэнергии, Изготовление товаров, Вырубка лесов, Использование транспорта, Производство продуктов питания, Энергоснабжение зданий, Энергоснабжение зданий "
    await ctx.send(Second_step)

@bot.command()
async def Facts(ctx):
    '''Рандомный факт о глобальном потеплении'''    
    Facts_name = random.choice(os.listdir("Facts"))
    with open(f'Facts/{Facts_name}', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def Rur(ctx):
    '''Советы против глобального потепления'''    
    Sigma_name = random.choice(os.listdir("Sovets"))
    with open(f'Sovets/{Sigma_name}', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command()
async def Cok(ctx):
    '''экологический словарь'''    
    slovar = ["АБИОТИЧЕСКИЕ ФАКТОРЫ СРЕДЫ — совокупность условий неорганической среды, влияющих на организмы."
              "АБРАЗИЯ — разрушение берегов крупных водоемов волнами и прибоем"
               "АБСОРБЦИЯ — поглощение вещества или энергии всей массой (объемом) поглощающего тела"
               "АВТОТРОФИЗМ (trophe — питание) — питание организмов (авто-трофов) неорганическими веществами посредством фотосинтеза или хемосинтеза. Благодаря автотрофии создается первичная продукция"
               "АВТОТРОФНЫЙ — питающийся неорганическими веществами"
               "КОНСЕНСУС — наличие между двумя или более индивидами единства взглядов, исходных ориентаций в каком-либо отношении."
                "КОНТИНУУМ (лат. континуум — непрерывное, сплошное) — представление о пленке жизни Земли как непрерывном целом без разделения на отдельности — экосистемы."
                "КОМБИНИРОВАНИЕ (КООПЕРИРОВАНИЕ) ПРОМЫШЛЕННОГО ПРОИЗВОДСТВА — объединение на одном предприятии нескольких связанных между собой производств с целью создания малоотходных технологий."]
    
    
    
     
    await ctx.send(slovar)

bot.run("MTE0NzgyOTQzNTE5MDQ5NzI4MA.GzFAt1.vhMxBmmlqki6g0x3ivT8nkth4q17bz5ajNPDU8")