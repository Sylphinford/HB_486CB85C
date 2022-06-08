import os
import random
from nonebot.exceptions import CQHttpError
from nonebot import MessageSegment
from hoshino import R, Service, priv


sv_help = '''
?
'''.strip()

sv = Service(
    name = 'nya',  
    use_priv = priv.NORMAL, 
    manage_priv = priv.ADMIN, 
    visible = False, 
    enable_on_default = True, 
    bundle = '通用', 
    help_ = sv_help 
    )

@sv.on_fullmatch(["帮助nya"])
async def bangzhu(bot, ev):
    await bot.send(ev, sv_help, at_sender=True)
    
###################################################

folder_rec_onitan = R.get('gurunya/onitan/').path
folder_gif_miao = R.get('gurunya/miao/').path
folder_gif_wang= R.get('gurunya/wang/').path
folder_rec_nya= R.get('gurunya/nya_rec/').path

######################################################

def get_rec_onitan():
    files = os.listdir(folder_rec_onitan)
    filename = random.choice(files)
    rec = R.get('gurunya/onitan/', filename)
    return rec

def get_gif_miao():
    files = os.listdir(folder_gif_miao)
    filename = random.choice(files)
    rec = R.get('gurunya/miao/', filename)
    return rec

def get_gif_wang():
    files = os.listdir(folder_gif_wang)
    filename = random.choice(files)
    rec = R.get('gurunya/wang/', filename)
    return rec

def get_rec_nya():
    files = os.listdir(folder_rec_nya)
    filename = random.choice(files)
    rec = R.get('gurunya/nya_rec/', filename)
    return rec

###################################################


@sv.on_keyword(('摸头','摸摸头','么么哒'), only_to_me=True)
async def rec_onitan(bot, ev) -> MessageSegment:
    file = get_rec_onitan()
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("Failed to send")



#@sv.on_prefix("喵",only_to_me=False)
@sv.on_keyword('喵', only_to_me=False)
async def miao(bot, ev) -> MessageSegment:
    if random.random() < 0.35: #gurunya
        file = get_rec_nya()
        try:
                rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
                await bot.send(ev, rec)
        except CQHttpError:
                sv.logger.error("Failed to send")  
    else:
        file = get_gif_miao()
        try:
                rec = MessageSegment.image(f'file:///{os.path.abspath(file.path)}')
                await bot.send(ev, rec)
        except CQHttpError:
                sv.logger.error("Failed to send")
        
        


@sv.on_fullmatch(('喵帕斯','喵帕斯~'), only_to_me=False)
async def nyanpass(bot, ev) -> MessageSegment:
        filename = 'nyanpass.mp3'
        file = R.get('gurunya/nyanpass', filename)
        try:
            rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
            await bot.send(ev, rec)
        except CQHttpError:
            sv.logger.error("Failed to send")

            
@sv.on_keyword('汪', only_to_me=False)
async def wang(bot, ev) -> MessageSegment:
    file = get_gif_wang()
    try:
        rec = MessageSegment.image(f'file:///{os.path.abspath(file.path)}')
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("Failed to send")
  
