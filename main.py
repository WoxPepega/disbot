import discord, time, datetime
from discord.ext import commands
from config import settings
client = discord.Client()
keywords = ["Тут","тут","На месте","на месте","Здесь","здесь","+"]
test_key = "####Боты####"
time_of_studie = [datetime.time(9,0,0),datetime.time(14,0,0)]
student_list = [
	276792669380001782, #Пользователь 1
	312693000966893569, #Пользователь 2
	690529575679000016, #Пользователь 3
	403525534000744450, #Пользователь 4
	274560520002892544, #Пользователь 5
	769955349000050566	#Ваш аккаунт
]
current_time = datetime.datetime.now()
stud_num = 0
rdy = True
ppl = 0

bot = commands.Bot(command_prefix = settings['prefix'], self_bot=True)

@bot.event
async def on_ready():
    print("Bot turned on :)")
    print(current_time)
    print(time_of_studie[0]," - ",time_of_studie[1])

@bot.event
async def on_message(message):
	global rdy,ppl
	msg_owner = message.author
	if (test_key in message.content):
		await message.channel.send("(~'_'~)")
	for i in range(len(keywords)):
		if (keywords[i] in message.content):
			checkPereklik()
			print(msg_owner.name,":",datetime.datetime.now().time(),":",rdy,":",ppl)
			if ((msg_owner.id == student_list[5] or msg_owner.id == student_list[1]) and rdy == False):
				time.sleep(1)
				current_time = datetime.datetime.now()
				current_time = current_time.time()
				if (current_time > time_of_studie[0]) and (current_time < time_of_studie[1]):
					time.sleep(8)
					await message.channel.send("+")
					print("Отметился")
					rdy = True
					ppl = 0
					print(rdy)
					#time.sleep(get_lost_time(current_time)+600)

def checkPereklik():
	global ppl,rdy
	if (rdy == True): ppl+=1
	if (ppl >= 4): 
		rdy = False
		print("Перекличка!")

def get_lost_time(cur_time):
	ttime = (time_of_studie[1].hour*60+time_of_studie[1].minute)-(cur_time.hour*60+cur_time.minute)
	print(ttime," and ",ttime*60)
	return (ttime*60)

bot.run(settings['token'], bot=False)
