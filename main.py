from email import header
from urllib import response
import discord
import challonge
import requests
import random
import json
from discord.ext import commands

config = {
    'token': 'MTAyNzIyOTcxMDQ4MjE2NTgyMQ.GVsR4l.Hgb36Cj3yH1Yx7xMnWonIxU4iF6-wAjEynJ3U4',
    'prefix': '$',
}
intents = discord.Intents.all()
challonge.set_credentials("Murder12891", "nWMHWJKNYbUqF7OHlwuKmLS4CttstyBFSgSQfGyL")
turik = challonge.tournaments.show("2re7hxcp")
bot = commands.Bot(command_prefix=config['prefix'], intents = intents)
@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент

@bot.command(pass_context = True)
async def agents(ctx):
    response = requests.get('https://valorant-api.com/v1/agents', params={'language':'ru-RU'})
    res = json.loads(response.text)
    data = res.get('data')
    answer = ' Существующие на данный момент Агенты: '
    for i in data:
        print(i.get('displayName'))
        answer += ' '
        answer += i.get('displayName')
        answer +=';'
    await ctx.send(answer)

@bot.command(pass_context = True)
async def randomMap(ctx):
    response = requests.get('https://valorant-api.com/v1/maps', params={'language':'ru-RU'})
    res = json.loads(response.text)
    data = res.get('data')
    answer = random.choice(data).get('displayName')
    await ctx.send(answer)   

@bot.command(pass_context = True)
async def randomAgent(ctx):
    response = requests.get('https://valorant-api.com/v1/agents', params={'language':'ru-RU'})
    res = json.loads(response.text)
    data = res.get('data')
    answer = random.choice(data).get('displayName')
    await ctx.send(answer)

@bot.command(pass_context = True)
async def Reg(ctx, name):
    try:
        parts = challonge.participants.create(turik["id"], name)
        print("Зарегистрирована команда " + name)
        await ctx.send("Команда "+name+" Успешно зарегестрирована") 
    except:
        await ctx.send("Возникла ошибка при регистрации, возможно название команды уже занято") 





bot.run(config['token'])