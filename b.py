from linepy3 import *
from justgood import imjustgood
from BEAPI import BEAPI
from Liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import timedelta, date
from datetime import datetime
from thrift.protocol import TCompactProtocol
from thrift.transport import THttpClient
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
import calculators
from calculators.apself import ApCalculator
from humanfriendly import format_timespan, format_size, format_number, format_length
from Naked.toolshed.shell import execute_js
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from wikiapi import WikiApi
from random import randint
from shutil import copyfile
import youtube_dl
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#=========================================================
#f = open('token1.txt','r')
#token = f.read()

#cl = LINE("{}".format(str(token)))
#f.close()
cl = LINE("brontakmail2@gmail.com","cinta123")
cl.log("Auth Token : " + str(cl.authToken))
cl.log("Timeline Token : " + str(cl.tl.channelAccessToken))
#=========================================================
oepoll = OEPoll(cl)
#=========================================================
#=========================================================
clProfile = cl.getProfile()
clSettings = cl.getSettings()
#=========================================================
clMID = cl.profile.mid
mid = cl.profile.mid
creator = ["uc019c475bb64a081ae7c151d4af82e3b"]
owner = [clMID]
admin = [clMID]
staff = [clMID]
KAC = [cl]
ABC = [cl]
Bots = [mid]
Tuyul = creator + owner+ admin + staff
#=========================================================
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []
leave = []
msg_dict = {}
msg_dict1 = {}
#=========================================================
settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeCover":{},
    "autoJoinTicket":False,
    "readerPesan": "Gw @!, Kang Sider",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

tailah = {
    "siderTemp": {},
    "siderPesan": "You can join chat?",
}

read = { 
    "readMember": {},
    "readPoint": {}
}

tes = {
    "Message": {},
    "msg": {},
}

tes2 = {
    "Message2": {},
    "msg2": {},
}

peler = { 
    "receivercount": 0,
    "sendcount": 0
}

wait = {
    "Limit": 50,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "tiktok":True,
    "contact":False,
    'autoBlock':False,
    'autoJoin':True,
    'autoAdd':True,
    'autotext':True,
    'autoLeave':False,
    'Timeline':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "stickerOn":False,
    "sticker":False,
    "smule": True,
    "changevp": False,
    "changeFoto": {},
    "likeOn": False,
    "stickers": {},
    "salam" : "وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ",
    "apikey" : "dedeuned",
    "call" : False,
    "callText": "Maaf kak belum bisa naik",
    "apkTikel": True,
    "AddstickerSider": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "AddstickerPesan": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "AddstickerWelcome": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "AddstickerLeave": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "stk":{},
    "selfbot":True,
    "token":True,
    "yt":True,
    "responGc":False,
    "Images":{},
    "Img":{},
    "Addimage":{},
    "Videos":{},
    "Video":{},
    "Addvideo":{},
    "laranganOn":True,
    "chat":False,
    "link":"https://i.gifer.com/7CJk.gif",
    "link":"https://www.smule.com",
    "mention":"Halo Sider, Ketahuan Ngintip",
    "Respontag":"Jangan Suka Tag Teg Tog Kaka, Jewer Nih Kapok!!",
    "leave":"Terimakasih Kak Sudah Pernah Ada Di Room ini, Sampai Jumpa Lagi",
    "welcome":"Selemat Datang, Salam Kenal Ya Kak, Semoga Betah Kak",
    "comment":"""
╭─「 BRK TEAMBOTS」─
│• 
│• Done Like & Comment
│• Add Owner kami""",
    "message":"""
Hai @!
Thanks for add me
OPENT RENTAL BOT
• Selfbot only
1. helper + Sb + js
2. full template
3. none template
• Bot Protect
1. owner bot
2. protect room
3. protect event room
• Bot Golang
1. war cl go
2. protect go
• Token primery
1. token fresh
2. 1 token 1 no
2. sudah add
Tap link for order
line.me/ti/p/~tuyulaza
""",
    "unsend":False,
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

comd = {
    "help": "help",
    "speed": "speed",
    "kick": "kick",
    "tagall": "hay",
    "cban": "cban",
    "siderOn": "sider on",
    "siderOff": "sider off",
    "bye": "@bye",
    "unsend": "unsend"
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

temptag = {
    "stealtag":False,
    "respontag":False,
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('sticker.json', 'r') as fp:
    stickers = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

stickersOpen = codecs.open("sticker.json","r","utf-8")
stickers = json.load(stickersOpen)

mulai = time.time()

def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def runtime2(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Menit %02d Detik' % (mins, secs)
   
def pretyPrintJson(djson):
        print(json.dumps(djson, indent=4, sort_keys=True))   

def allowLiff():
    url = 'https://access.line.me/dialog/api/permissions'
    data = {'on': ['P','CM'],'off': []}
    headers = {'X-Line-Access': cl.authToken,'X-Line-Application': cl.server.APP_NAME,'X-Line-ChannelId': '1602687308','Content-Type': 'application/json'}
    requests.post(url, json=data, headers=headers)

def flex3(to, text):
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    data = { "type": "flex", "altText": "FLEX 2021", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": text, "size": "10px", "color": "#ffffff", "wrap": True } ], "backgroundColor": "#000000" }, "footer": { "type": "box", "layout": "vertical", "contents": [ { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/YD34zFx/ezgif-com-gif-maker-35.png", "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True, "offsetBottom": "1px" } ], "position": "absolute", "width": "17px", "height": "17px", "borderWidth": "0.5px", "borderColor": "#00ff00", "cornerRadius": "50px", "offsetTop": "2px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "βŘҜ-Ŧ€ΔΜ-βØŦŞ", "size": "10px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "115px", "height": "15px", "borderWidth": "0.5px", "borderColor": "#00ff00", "cornerRadius": "2px", "offsetTop": "2.5px", "offsetStart": "33px" } ], "backgroundColor": "#000000" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=uc019c475bb64a081ae7c151d4af82e3b" }, "styles": { "footer": { "separator": True, "separatorColor": "#00ff00" } } } }
    sendTemplate(to, data)

def flexbrk(to, text):
    contact = cl.getProfile()
    mids = [contact.mid]
    status = cl.getContact(mid)
    scover = cl.getProfileCoverURL(mid)
    data = {"type": "flex","altText": "FLEX 2021","contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": text, "size": "10px", "color": "#00ffff", "align": "center", "offsetBottom": "7px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/wMYd317/ezgif-com-gif-maker-11.png", "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "17px", "height": "17px", "borderWidth": "1px", "cornerRadius": "2px", "borderColor": "#00ffff", "offsetBottom": "5px", "offsetStart": "7px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "βŘҜ-Ŧ€ΔΜ-βØŦŞ", "size": "10px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "120px", "height": "17px", "borderWidth": "1px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetBottom": "5px", "offsetStart": "30px" }, { "type": "box", "layout": "vertical", "contents": [], "position": "absolute", "width": "160px", "height": "2px", "backgroundColor": "#00ffff", "offsetTop": "20px", "offsetStart": "0.5px" } ], "backgroundColor": "#000000", "width": "160px", "height": "50px", "borderWidth": "1px", "borderColor": "#00ffff", "cornerRadius": "10px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=uc019c475bb64a081ae7c151d4af82e3b" } } }
    sendTemplate(to, data)

def flex2(to, text):
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    data = { "type": "flex", "altText": "FLEX 2021", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": text, "size": "10px", "color": "#ffffff", "wrap": True } ], "backgroundColor": "#000000" }, "footer": { "type": "box", "layout": "vertical", "contents": [ { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/YD34zFx/ezgif-com-gif-maker-35.png", "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True, "offsetBottom": "1px" } ], "position": "absolute", "width": "17px", "height": "17px", "borderWidth": "0.5px", "borderColor": "#00ff00", "cornerRadius": "50px", "offsetTop": "2px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "βŘҜ-Ŧ€ΔΜ-βØŦŞ", "size": "10px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "115px", "height": "15px", "borderWidth": "0.5px", "borderColor": "#00ff00", "cornerRadius": "2px", "offsetTop": "2.5px", "offsetStart": "33px" } ], "backgroundColor": "#000000" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=uc019c475bb64a081ae7c151d4af82e3b" }, "styles": { "footer": { "separator": True, "separatorColor": "#00ff00" } } } }
    sendTemplate(to, data)

def flexhelp(to, text):
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    contact = cl.getContact(mid)
    data = {"type": "flex","altText": "FLEX 2021","contents": { "type": "carousel", "contents": [ { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/h8bC8T2/1639913956273.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:3", "backgroundColor": "#000000" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "VERSION V17", "size": "5px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "46.5px", "height": "8px", "backgroundColor": "#000000", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetEnd": "10px", "offsetBottom": "1.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "BRK TEAM BOTS", "size": "5px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "46.5px", "height": "8px", "backgroundColor": "#000000", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetBottom": "1.5px", "offsetStart": "12px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "MAIN MENU", "size": "10px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "77px", "height": "15px", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "backgroundColor": "#000000", "offsetTop": "16.5px", "offsetEnd": "14px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/VMbJz0P/ezgif-com-gif-maker-27.png", "animated": True } ], "position": "absolute", "width": "32px", "height": "32px", "backgroundColor": "#000000", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "50px", "offsetTop": "2.5px", "offsetStart": "7px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/VMbJz0P/ezgif-com-gif-maker-27.png", "size": "full", "aspectRatio": "2:3", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "130px", "height": "170px", "offsetTop": "50px", "offsetStart": "15px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "ADMIN", "size": "10px", "color": "#00ffff", "align": "center", "offsetTop": "2px" } ], "position": "absolute", "width": "100px", "height": "20px", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetTop": "60px", "offsetStart": "30px", "action": { "type": "uri", "label": "action", "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Admin" }, "backgroundColor": "#00000080" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "GROUP", "size": "10px", "color": "#00ffff", "align": "center", "offsetTop": "2px" } ], "position": "absolute", "width": "100px", "height": "20px", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetTop": "90px", "offsetStart": "30px", "action": { "type": "uri", "label": "action", "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Group" }, "backgroundColor": "#00000080" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "BANNED", "size": "10px", "color": "#00ffff", "align": "center", "offsetTop": "2px" } ], "position": "absolute", "width": "100px", "height": "20px", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetTop": "120px", "offsetStart": "30px", "action": { "type": "uri", "label": "action", "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Banned" }, "backgroundColor": "#00000080" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "STATUS", "size": "10px", "color": "#00ffff", "align": "center", "offsetTop": "2px" } ], "position": "absolute", "width": "100px", "height": "20px", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetTop": "150px", "offsetStart": "30px", "action": { "type": "uri", "label": "action", "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Status" }, "backgroundColor": "#00000080" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "SETTING", "size": "10px", "color": "#00ffff", "align": "center", "offsetTop": "2px" } ], "position": "absolute", "width": "100px", "height": "20px", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetTop": "180px", "offsetStart": "30px", "action": { "type": "uri", "label": "action", "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Setting" }, "backgroundColor": "#00000080" } ], "paddingAll": "0px", "cornerRadius": "10px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=uc019c475bb64a081ae7c151d4af82e3b" } }, { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/h8bC8T2/1639913956273.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:3", "backgroundColor": "#000000" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "VERSION V17", "size": "5px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "46.5px", "height": "8px", "backgroundColor": "#000000", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetEnd": "10px", "offsetBottom": "1.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "BRK TEAM BOTS", "size": "5px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "46.5px", "height": "8px", "backgroundColor": "#000000", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetBottom": "1.5px", "offsetStart": "12px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "MAIN MENU", "size": "10px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "77px", "height": "15px", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "backgroundColor": "#000000", "offsetTop": "16.5px", "offsetEnd": "14px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/VMbJz0P/ezgif-com-gif-maker-27.png", "animated": True } ], "position": "absolute", "width": "32px", "height": "32px", "backgroundColor": "#000000", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "50px", "offsetTop": "2.5px", "offsetStart": "7px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/VMbJz0P/ezgif-com-gif-maker-27.png", "size": "full", "aspectRatio": "2:3", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "130px", "height": "170px", "offsetTop": "50px", "offsetStart": "15px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "PROTECT", "size": "10px", "color": "#00ffff", "align": "center", "offsetTop": "2px" } ], "position": "absolute", "width": "100px", "height": "20px", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetTop": "60px", "offsetStart": "30px", "action": { "type": "uri", "label": "action", "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Protect" }, "backgroundColor": "#00000080" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "HELP JS", "size": "10px", "color": "#00ffff", "align": "center", "offsetTop": "2px" } ], "position": "absolute", "width": "100px", "height": "20px", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetTop": "90px", "offsetStart": "30px", "action": { "type": "uri", "label": "action", "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Help%20js" }, "backgroundColor": "#00000080" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "TRANSLATE", "size": "10px", "color": "#00ffff", "align": "center", "offsetTop": "2px" } ], "position": "absolute", "width": "100px", "height": "20px", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetTop": "120px", "offsetStart": "30px", "action": { "type": "uri", "label": "action", "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Translate" }, "backgroundColor": "#00000080" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "REMOTE", "size": "10px", "color": "#00ffff", "align": "center", "offsetTop": "2px" } ], "position": "absolute", "width": "100px", "height": "20px", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetTop": "150px", "offsetStart": "30px", "action": { "type": "uri", "label": "action", "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Remote" }, "backgroundColor": "#00000080" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "PROFILE", "size": "10px", "color": "#00ffff", "align": "center", "offsetTop": "2px" } ], "position": "absolute", "width": "100px", "height": "20px", "borderWidth": "0.5px", "borderColor": "#00ffff", "cornerRadius": "2px", "offsetTop": "180px", "offsetStart": "30px", "action": { "type": "uri", "label": "action", "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Profile" }, "backgroundColor": "#00000080" } ], "paddingAll": "0px", "cornerRadius": "10px" } } ] } }
    sendTemplate(to, data)

def sendFlexVideo(to, videoUrl, thumbnail='dark'):
    main = ["dark","red","cyan","yellow","green","white"]
    if thumbnail in main:
       thumbnail = f"https://i.ibb.co/njrRhyv/1643889938543.jpg"
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer %s' % token.accessToken}
    data = {'messages': [{'type': 'video','originalContentUrl': videoUrl,'previewImageUrl': thumbnail,}]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendFlexAudio(to, link):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer %s' % token.accessToken}
    data = {'messages': [{'type': 'audio','originalContentUrl': link,'duration': 250000}]}
    requests.post(url, headers=headers, data=json.dumps(data))


def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendCarousel(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendCarousel(to,col):
    col = json.dumps(col)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=col, headers=headers)

def sendFoter(to, text):
    data = {"type": "text","text": text,"sentBy": {"label": "❑ ᴀᴘᴋ-ʙᴏᴛꜱ ❑","iconUrl": "https://i.ibb.co/TrcSqCX/ezgif-com-gif-maker-8.png","linkUrl": "line://nv/profilePopup/mid=u35aa06efe8cfc198633554199261cc60"}}
    sendTemplate(to, data)

def failOverAPI():
    try:
        result = requests.get("https://api.boteater.xyz",timeout=0.5)
        if result.status_code == 200:
            return "https://api.boteater.xyz"
        else:
            return "https://api.boteater.us"
    except:
        return "https://api.boteater.us"

def cytmp4(to,url):
    import pafy
    vid = pafy.new(url,basic=False)
    result = vid.streams[-1]
    return result.url
    links = cytmp4(anunya);links = 'https://'+cl.google_url_shorten(links)
    
def pendekin(to,url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    return resp['id']

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "update profile failed"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("vp.mp4")

def changeProfileVideo(to):
    if settings['changevp']['picture'] == None:
        return cl.sendReplyMessage(msg_id, to, "Foto tidak ditemukan")
    elif settings['changevp']['video'] == None:
        return cl.sendReplyMessage(msg_id, to, "Video tidak ditemukan")
    else:
        path = settings['changevp']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendReplyMessage(msg_id, to, "Gagal update profile")
        path_p = settings['changevp']['picture']
        settings['changevp']['status'] = False
        cl.updateProfilePicture(path_p, 'vp')

def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "╭─「 Daftar anggota 」\n├↘\n├↘1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n├↘\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "├↘ {}. ".format(str(no))
            else:
                textx += "╰─「 Mentions {} Member 」".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendTextMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@KhieGans  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(cl.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + cl.getContact(clMID).picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def apkMention(to, text="", mids=[]):
        arrData = ""
        arr = []
        mention = "@Mmk "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 5
                else:slen = len(textx);elen = len(textx) + 5
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"5","M":'+json.dumps(mid)+'}'
        text_ = '@Khiez'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers2(to, mids=[]):
    if clMID in mids: mids.remove(clMID)
    parsed_len = len(mids)//20+1
    result = '╭─── • MENTIONS •\n'
    mention = '@zeroxyuuki\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '│ %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╰─── • βŘҜ-Ŧ€ΔΜ-βØŦŞ •\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            cl.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def removeCmd(cmd, text):
	key = Setmain["keyCommand"]
	#if Setmain["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            print ("[25,26] SEND MESSAGE")
            return
        
        if op.type == 11 or op.type == 122:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                except:
                    pass
                    
        if op.type == 13 or op.type == 124:
            if clMID in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                       cl.acceptGroupInvitation(op.param1)
                    else:
                       cl.acceptGroupInvitation(op.param1)                      

            if clMID in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)                      

        if op.type == 13 or op.type == 124:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    babi = op.param3.replace("",',')
                    memek = babi.split(",")
                    for sodok in memek:
                       cl.cancelGroupInvitation(op.param1,[sodok])
                       cl.kickoutFromGroup(op.param1,[op.param2])
                       wait["blacklist"] == True

        if op.type == 17 or op.type == 130:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                cover = cl.getProfileCoverURL(op.param2)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                gname = cl.getGroup(op.param1)
                BRKBOTS = "WELCOME MEMBERS\n"
                BRKBOTS += "• Name : @!\n"
                BRKBOTS += "• Time : "+datetime.strftime(timeNow,'%H:%M:%S')
                BRKBOTS += "\n• Date : "+datetime.strftime(timeNow,'%d-%m-%Y')
                BRKBOTS += "\n• Room : {}".format(gname.name)
                BRKBOTS += "\n{}".format(wait["welcome"])
                cl.sendMention(op.param1, str(BRKBOTS),' ', [op.param2])                                                
                sid = str(wait["AddstickerWelcome"]["sid"])
                spkg = str(wait["AddstickerWelcome"]["spkg"])
                cl.sendSticker(op.param1, spkg, sid)

        if op.type == 15 or op.type == 128:
            if op.param1 in leave:
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                cover = cl.getProfileCoverURL(op.param2)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                gname = cl.getGroup(op.param1)
                BRKBOTS = "WELCOME MEMBERS\n"
                BRKBOTS += "• Name : @!\n"
                BRKBOTS += "• Time : "+datetime.strftime(timeNow,'%H:%M:%S')
                BRKBOTS += "\n• Date : "+datetime.strftime(timeNow,'%d-%m-%Y')
                BRKBOTS += "\n• Room : {}".format(gname.name)
                BRKBOTS += "\n{}".format(wait["leave"])
                cl.sendMention(op.param1, str(BRKBOTS),' ', [op.param2])                                                    
                sid = str(wait["AddstickerLeave"]["sid"])
                spkg = str(wait["AddstickerLeave"]["spkg"])
                cl.sendSticker(op.param1, spkg, sid)

        if op.type == 17 or op.type == 130:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    cl.kickoutFromGroup(op.param1,[op.param2])            
                        
                return

        if op.type == 0:
            return
        if op.type == 5:
              if wait["autoAdd"] == True:
                  cl.sendMention(op.param1, str(wait["message"]), '',[op.param1])                                                                                     
                  sid = str(wait["AddstickerPesan"]["sid"])
                  spkg = str(wait["AddstickerPesan"]["spkg"])
                  cl.sendSticker(msg.to, spkg, sid)

        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)
                cl.sendMention(op.param1, "@!\nSorry Auto Block Is Active, Please Comment In Time Line For Unblock Contact tq..",'',[op.param1])                

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭─「 Gambar Dihapus 」\n│ Pengirim : "
                                ret_ = "│ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n│ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "╭─「 Pesan Dihapus 」\n"
                                ret_ += "│ Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n│ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n│ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n│ Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n╰───────────"
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "╭─「 Sticker Dihapus 」\n"
                                ret_ += "│ Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n│ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n│ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                ret_ += "\n╰───────────"
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 19 or op.type == 133:     
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 32 or op.type == 126:                 
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                        
                return

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                cl.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if op.param1 in Setmain["RAreadPoint"]:
                if op.param2 in Setmain["RAreadMember"][op.param1]:
                    pass
                else:
                    Setmain["RAreadMember"][op.param1][op.param2] = True
            else:
                pass

        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        contact = cl.getContact(op.param2)
                        tz = pytz.timezone("Asia/Jakarta")
                        cover = cl.getProfileCoverURL(op.param2)
                        TUYUL = ["ngopi kak","apa kabar kak","naik yuk","diem diem bae","Makan om","Hai kak","Nikung on","Pm gosong"]                                
                        timeNow = datetime.now(tz=tz)
                        BRKBOTS = "@! "
                        BRKBOTS += random.choice(TUYUL)
                        cl.sendMention(op.param1, str(BRKBOTS),' ',[op.param2])
                        sid = str(wait["AddstickerSider"]["sid"])
                        spkg = str(wait["AddstickerSider"]["spkg"])
                        cl.sendSticker(op.param1, spkg, sid)                           
			
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              cl.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              cl.kickoutFromGroup(msg.to, [msg._from])
   
        if op.type == 25 or op.type == 26:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                to = msg.to
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != cl.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return

            except:
                pass

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            stickername = str(text)
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver         
               if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention["M"] in clMID:
                           contact = cl.getContact(msg._from)
                           anu = contact.displayName
                           cl.sendReplyMessage(msg.to,id, anu)
                           sid = str(wait["AddstickerTag"]["sid"])
                           spkg = str(wait["AddstickerTag"]["spkg"])
                           cl.sendSticker(msg.to, spkg, sid)
                           break
                                                                                                    
               if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in clMID:
                           cl.sendMention(msg.to, 'Sorry @!\n• Mention Kick Aktif!',' ', [msg._from])
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break

               if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                 if temptag["respontag"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   GANTENG = ["Tag mele","Sorry sibuk","Opo Cok","Kick nih tag mele"]                                
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   BRKBOTS = "@! "
                   BRKBOTS += random.choice(GANTENG)
                   sid = str(wait["AddstickerTag"]["sid"])
                   spkg = str(wait["AddstickerTag"]["spkg"])
                   for mention in mentionees:
                        if mention["M"] in clMID:
                            try:
                                cl.sendMention(msg.to, "{}".format(BRKBOTS),'', [sender])
                                cl.sendSticker(msg.to, spkg, sid)
                            except:
                                pass
                                                       
               if msg.contentType == 6:
                  if wait["responGc"] == True:
                      tz = pytz.timezone("Asia/Jakarta")
                      timeNow = datetime.now(tz=tz)
                      ginfo = cl.getGroup(to)
                      xyz = cl.getContact(sender)
                      b = msg.contentMetadata['GC_EVT_TYPE']
                      c = msg.contentMetadata["GC_MEDIA_TYPE"]
                      if c == 'AUDIO' and b == "S":
                          arg = "START CALL GROUP"
                          arg += "\n• Initiator: {}".format(xyz.displayName)
                          arg += "\n• Time : "+datetime.strftime(timeNow,'%H:%M:%S')
                          arg += "\n• Date : "+datetime.strftime(timeNow,'%d-%m-%Y')
                          arg += "\n• Types of: Voice"
                          arg += "\n• Room: {}".format(ginfo.name)
                          cl.sendReplyMessage(msg.id,to, str(arg))
                      if c == 'VIDEO' and b == "S":
                          arg = "START CALL GROUP"
                          arg += "\n• Initiator: {}".format(xyz.displayName)
                          arg += "\n• Time : "+datetime.strftime(timeNow,'%H:%M:%S')
                          arg += "\n• Date : "+datetime.strftime(timeNow,'%d-%m-%Y')
                          arg += "\n• Types of: Video"
                          arg += "\n• Room: {}".format(ginfo.name)
                          cl.sendReplyMessage(msg.id,to, str(arg))
                      if c == 'LIVE' and b == "S":
                          arg = "START LIVE GROUP"
                          arg += "\n• Initiator: {}".format(xyz.displayName)
                          arg += "\n• Time : "+datetime.strftime(timeNow,'%H:%M:%S')
                          arg += "\n• Date : "+datetime.strftime(timeNow,'%d-%m-%Y')
                          arg += "\n• Types of: Live"
                          arg += "\n• Room: {}".format(ginfo.name)
                          cl.sendReplyMessage(msg.id,to, str(arg))
                      else:
                          mills = int(msg.contentMetadata["DURATION"])
                          seconds = (mills / 1000) % 60
                          if c == "AUDIO" and b == "E":
                              arg = "END CALL GROUP"
                              arg += "\n• Initiator: {}".format(xyz.displayName)
                              arg += "\n• Time : "+datetime.strftime(timeNow,'%H:%M:%S')
                              arg += "\n• Date : "+datetime.strftime(timeNow,'%d-%m-%Y')
                              arg += "\n• Types of: Voice"
                              arg += "\n• Room: {}".format(ginfo.name)
                              cl.sendReplyMessage(msg.id,to, str(arg))
                          if c == "VIDEO" and b == "E":
                              arg = "END CALL GROUP"
                              arg += "\n• Initiator: {}".format(xyz.displayName)
                              arg += "\n• Time : "+datetime.strftime(timeNow,'%H:%M:%S')
                              arg += "\n• Date : "+datetime.strftime(timeNow,'%d-%m-%Y')
                              arg += "\n• Types of: Video"
                              arg += "\n• Room: {}".format(ginfo.name)
                              cl.sendReplyMessage(msg.id,to, str(arg))
                          if c == "LIVE" and b == "E":
                              arg = "END CALL GROUP"
                              arg += "\n• Initiator: {}".format(xyz.displayName)
                              arg += "\n• Time : "+datetime.strftime(timeNow,'%H:%M:%S')
                              arg += "\n• Date : "+datetime.strftime(timeNow,'%d-%m-%Y')
                              arg += "\n• Types of: Live"
                              arg += "\n• Room: {}".format(ginfo.name)
                              cl.sendReplyMessage(msg.id,to, str(arg))

               if msg.contentType == 7:
                 if wait["stickerOn"] == True:
                    msg.contentType = 0
                    cl.sendReplyMessage(msg.id,to,"╭─「 Cek ID Sticker 」\n├↘ STKID : " + msg.contentMetadata["STKID"] + "\n├↘ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n├↘ STKVER : " + msg.contentMetadata["STKVER"]+ "\n├↘\n╰─「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"╭─「 Contact Info 」\n├↘ Nama : " + msg.contentMetadata["displayName"] + "\n├↘ MID : " + msg.contentMetadata["mid"] + "\n├↘ Status Msg : " + contact.statusMessage + "\n├↘ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            stickername = str(text)
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = "「 Detail Postingan 」"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(sender)
                                auth = "\n• Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\n• Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n• Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\n• Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n• Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                            cl.sendReplyMessage(msg.id,to, str(ret_))

               if msg.contentType == 16:
                    if wait["likeOn"] == True:
                        url = msg.contentMetadata["postEndUrl"]
                        cl.likePost(url[25:58], url[66:], likeType = 1001)
                        cl.createComment(url[25:58], url[66:], wait["comment"])
                        cl.sendMention(msg.to, "@!\nSudah Di Like Kak"," ",[msg._from])
                        
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["AddstickerTag"]["status"] == True:
                        wait["AddstickerTag"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerTag"]["spkg"] = msg.contentMetadata['STKPKGID']
                        cl.sendReplyMessage(msg.id,to, "Add Stickers Tag Succes ♪")
                        wait["AddstickerTag"]["status"] = False     
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["AddstickerSider"]["status"] == True:
                        wait["AddstickerSider"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerSider"]["spkg"] = msg.contentMetadata['STKPKGID']
                        cl.sendReplyMessage(msg.id,to,"Add stickers sider ♪")
                        wait["AddstickerSider"]["status"] = False                   
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["AddstickerPesan"]["status"] == True:
                        wait["AddstickerPesan"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerPesan"]["spkg"] = msg.contentMetadata['STKPKGID']
                        cl.sendReplyMessage(msg.id,to,"Succes add Stickers ♪")
                        wait["AddstickerPesan"]["status"] = False                   
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["AddstickerWelcome"]["status"] == True:
                        wait["AddstickerWelcome"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerWelcome"]["spkg"] = msg.contentMetadata['STKPKGID']
                        cl.sendReplyMessage(msg.id,to,"Succes add Stickers ♪")
                        wait["AddstickerWelcome"]["status"] = False                   
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["AddstickerLeave"]["status"] == True:
                        wait["AddstickerLeave"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerLeave"]["spkg"] = msg.contentMetadata['STKPKGID']
                        cl.sendReplyMessage(msg.id,to,"Succes add Stickers Leave ♪")
                        wait["AddstickerLeave"]["status"] = False                   
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                            
               if msg.contentType == 7:
                   if msg._from in admin:
                       try:
                           if wait["sticker"] == True:
                               wait["stickers"][wait["stk"]] = msg.contentMetadata
                               wait["stk"] = {}
                               wait["sticker"] = False
                               f=codecs.open("wait.json","w","utf-8")
                               json.dump(wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                               cl.sendReplyMessage(msg.id,to,"Stickers saved")
                       except Exception as e:
                           sendFoter(msg.to,"{}".format(str(e)))
                       
               if msg.contentType == 7:
                 if wait["stickerOn"] == True:
                    msg.contentType = 0
                    cl.sendReplyMessage(msg.id,to,"╭─「 Cek ID Sticker 」\n├↘ STKID : " + msg.contentMetadata["STKID"] + "\n├↘ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n├↘ STKVER : " + msg.contentMetadata["STKVER"]+ "\n├↘\n╰─「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendReplyMessage(msg.id,to," ╭─「 Contact Info 」\n├↘ Nama : " + msg.contentMetadata["displayName"] + "\n├↘ MID : " + msg.contentMetadata["mid"] + "\n├↘ Status Msg : " + contact.statusMessage + "\n╰─ 「Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMention(msg.to, '@!\n• Sudah Dalam List\n• Ketik Abort For Stop Contact',' ', [msg._from])
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMention(msg.to, '@!\n• Add to botlist\n• Ketik abort for stop contact',' ', [msg._from])
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMention(msg.to, '@!\n• Botlist has been deleted\n• Ketik abort for stop contact',' ', [msg._from])
                    else:
                        wait["dellbots"] = True
                        cl.sendMention(msg.to, '@!\n• Contact not in botlist\n• Ketik abort for stop contact',' ', [msg._from])
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMention(msg.to, '@!\n• Allready in stafflist\n• Ketik abort for stop contact',' ', [msg._from])
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMention(msg.to, '@!\n• Add to stafflist\n• Ketik abort for stop contact',' ', [msg._from])
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMention(msg.to, '@!\n• Stafflist has been deleted\n• Ketik abort for stop contact',' ', [msg._from])
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMention(msg.to, '@!\n• Contact non in stafflist\n• Ketik abort for stop contact',' ', [msg._from])
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMention(msg.to, '@!\n• Allready in adminlist\n• Ketik abort for stop contact',' ', [msg._from])
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMention(msg.to, '@!\n• Add to adminlist\n• Ketik abort for stop contact',' ', [msg._from])
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMention(msg.to, '@!\n• Adminlist has been deleted\n• Ketik abort for stop contact',' ', [msg._from])
                    else:
                        wait["delladmin"] = True
                        cl.sendMention(msg.to, '@!\n• Contact non adminlist\n• Ketik abort for stop contact',' ', [msg._from])
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMention(msg.to, '@!\n• Allready in blacklist\n• Ketik abort for stop contact',' ', [msg._from])
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMention(msg.to, '@!\n• Add to blacklist\n• Ketik abort for stop contact',' ', [msg._from])
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMention(msg.to, '@!\n• Blacklist has been deleted\n• Ketik abort for stop contact',' ', [msg._from])
                    else:
                        wait["dblacklist"] = True
                        cl.sendMention(msg.to, '@!\n• Contact not in blacklist\n• Ketik abort for stop contact',' ', [msg._from])
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMention(msg.to, '@!\n• Allready in talkbanlist\n• Ketik abort for stop contact',' ', [msg._from])
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMention(msg.to, '@!\n• Add to talkbanlist\n• Ketik abort for stop contact',' ', [msg._from])
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMention(msg.to, '@!\n• Talkbanlist has been deleted\n• Ketik abort for stop contact',' ', [msg._from])
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMention(msg.to, '@!\n• Contact not in talkbanlist\n• Ketik abort for stop contact',' ', [msg._from])
#UPDATE FOTO
               if msg.contentType == 1:
                if msg._from in admin:
                  if wait["Addimage"] == True:
                    try:
                        cl.downloadObjectMsg(msg.id,'path','dataFoto/'+wait["Img"]+'.jpg')
                        cl.sendReplyMessage(msg.id,to, "Berhasil menambahkan gambar")
                        wait["Img"] = {}                
                        wait["Addimage"] = False
                    except Exception as e:
                        cl.downloadObjectMsg(msg.id,'path','dataFoto/'+wait["Img"]+'.jpg')
                        cl.sendReplyMessage(msg.id,to, "Berhasil menambahkan gambar")
                        wait["Img"] = {}
                        wait["Addimage"] = False
               if msg.contentType == 2:
                if msg._from in admin:
                  if wait["Addvideo"] == True:
                    try:
                        cl.downloadObjectMsg(msg.id,'path','dataVideo/'+wait["Video"]+'.mp4')
                        cl.sendReplyMessage(msg.id,to, "Berhasil menambahkan video")
                        wait["Video"] = {}                
                        wait["Addvideo"] = False
                    except Exception as e:
                        cl.downloadObjectMsg(msg.id,'path','dataVideo/'+wait["Video"]+'.mp4')
                        cl.sendReplyMessage(msg.id,to, "Berhasil menambahkan video")
                        wait["Video"] = {}
                        wait["Addvideo"] = False
               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendReplyMessage(msg.id,to, "Group picture has been updated")
               if msg.contentType == 1:
                   if msg._from in admin:
                       if clMID in wait["changeFoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del wait["changeFoto"][clMID]
                            cl.updateProfilePicture(path)
                            cl.sendReplyMessage(msg.id,to, "Picture profile has been update")
                   if msg._from in admin:
                       if clMID in settings["changeCover"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del settings["changeCover"][clMID]
                            cl.updateProfileCover(path)
                            cl.sendReplyMessage(msg.id,to, "Picture profile has been update")                                              

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                    for cmd in cmd.split(","):
                        if cmd == "chatbot on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                ret = "Chatbot Enabled."
                                cl.sendReplyMessage(msg.id,to, str(ret))
                        elif cmd == "chatbot off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                ret = "Chatbot Disabled."
                                cl.sendReplyMessage(msg.id,to, str(ret))

                        elif cmd == comd["help"]:
                            if wait["selfbot"] == True:
                                if msg._from in admin:
                                    BRKBOTS = "╭── • SELFBOT MENU •\n"
                                    BRKBOTS += "├ • Admin\n"
                                    BRKBOTS += "├ • Banned\n"
                                    BRKBOTS += "├ • Group\n"
                                    BRKBOTS += "├ • Setting\n"
                                    BRKBOTS += "├ • Protect\n"
                                    BRKBOTS += "├ • Nodejs\n"
                                    BRKBOTS += "├ • List\n"
                                    BRKBOTS += "├ • Media\n"
                                    BRKBOTS += "├ • Translate\n"
                                    BRKBOTS += "├ • Profile\n"
                                    BRKBOTS += "├ • Status\n"
                                    BRKBOTS += "├ • Chatbot on/off\n"
                                    BRKBOTS += "╰── • βŘҜ-Ŧ€ΔΜ-βØŦŞ •"
                                    cl.sendReplyMessage(msg.id,to, str(BRKBOTS))
                              
                        elif cmd == "clear":
                            if wait["selfbot"] == True:
                                if msg._from in admin:
                                    #process = os.popen('cd /tmp/ && rm -r *')
                                    process = os.popen('sync; echo 1 > /proc/sys/vm/drop_caches')
                                    a = process.read()
                                    ret = "Cleared a chace server"
                                    cl.sendReplyMessage(msg.id,to, str(ret))
    
                        elif cmd == "remote":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                brk = "╭────────────────\n"
                                brk += "├─≽ HELP REMOTE \n"
                                brk += "├ • Tag: (number)\n"
                                brk += "├ • Grupinfo (number)\n"
                                brk += "├ • Grupmem (number)\n"
                                brk += "├ • Gurl (number)\n"
                                brk += "├ • Closeqr (number)\n"
                                brk += "├ • Openqr (number)\n"
                                brk += "├ • Bye: (number)\n"
                                brk += "├ • Bantai: (number)\n"
                                brk += "├ • Invite: (number)\n"
                                brk += "╰────────────────"
                                cl.sendReplyMessage(msg.id,to, str(brk))
    
                        elif cmd == "group":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                brk = "╭────────────────\n"
                                brk += "├─≽ HELP GROUP \n"
                                brk += "├ • Url\n"
                                brk += "├ • Me\n"
                                brk += "├ • Tag\n"
                                brk += "├ • Hay\n"
                                brk += "├ • Stag\n"
                                brk += "├ • Clear\n"
                                brk += "├ • {}\n".format(comd["speed"])
                                brk += "├ • Ginfo\n"
                                brk += "├ • Reboot\n"
                                brk += "├ • About\n"
                                brk += "├ • Runtime\n"
                                brk += "├ • Respontime\n"
                                brk += "├ • Gruplist\n"
                                brk += "├ • Clearchat\n"
                                brk += "├ • Clearallfriend\n"
                                brk += "├ • Cek @\n"
                                brk += "├ • Mid @\n"
                                brk += "├ • Find @\n"
                                brk += "├ • Block @\n"
                                brk += "├ • Call @\n"
                                brk += "├ • Addfriend @\n"
                                brk += "├ • Delfriend @\n"
                                brk += "├ • Idline (id)\n"
                                brk += "├ • Refresh/Abort\n"
                                brk += "├ • Buka qr\n"
                                brk += "├ • Tutup qr\n"
                                brk += "├ • Gnamegrup (text)\n"
                                brk += "├ • Uns (jumlah)\n"
                                brk += "├ • Jumlah: (jumlah)\n"
                                brk += "├ • Spamcall\n"
                                brk += "├ • Spamcall: (jumlah)\n"
                                brk += "├ • Spamcall (jumlah)\n"
                                brk += "├ • Scall (jumlah) @\n"
                                brk += "├ • Spamtag (jumlah) @\n"
                                brk += "├ • Spam on jumlah|text\n"
                                brk += "├ • Tag (jumlah di pm)\n"
                                brk += "├ • Gift: mid jumlah\n"
                                brk += "╰────────────────"
                                cl.sendReplyMessage(msg.id,to, str(brk))

                        elif cmd == "profile":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                brk = "╭────────────────\n"
                                brk += "├─≽ HELP PROFILE \n"
                                brk += "├ • Myname\n"
                                brk += "├ • Mypict\n"
                                brk += "├ • Mybio\n"
                                brk += "├ • Pict @\n"
                                brk += "├ • Bio @\n"
                                brk += "├ • Name @\n"
                                brk += "├ • Cover @\n"
                                brk += "├ • Steal @\n"
                                brk += "├ • Updatefoto\n"
                                brk += "├ • Myname: (name)\n"
                                brk += "├ • Mybio: (text)\n"
                                brk += "├ • Cvp: (link yt)n"
                                brk += "╰────────────────"
                                cl.sendReplyMessage(msg.id,to, str(brk))

                        elif cmd == "admin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                brk = "╭────────────────\n"
                                brk += "├─≽ HELP ADMIN \n"
                                brk += "├ • Blc\n"
                                brk += "├ • Adminlist\n"
                                brk += "├ • Botlist\n"
                                brk += "├ • Bot:on\n"
                                brk += "├ • Staff:on\n"
                                brk += "├ • Admin:on\n"
                                brk += "├ • Bot:repeat\n"
                                brk += "├ • Staff:repeat\n"
                                brk += "├ • Admin:repeat\n"
                                brk += "├ • {} @\n".format(comd["kick"])
                                brk += "├ • Ulti @\n"
                                brk += "├ • Invite @\n"
                                brk += "├ • Botadd/dell @\n"
                                brk += "├ • Staffadd/dell @\n"
                                brk += "├ • AdminAdd/dell @\n"
                                brk += "├ • Contact bot\n"
                                brk += "├ • Contact admin\n"
                                brk += "╰────────────────"
                                cl.sendReplyMessage(msg.id,to, str(brk))

                        elif cmd == "banned":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                brk = "╭────────────────\n"
                                brk += "├─≽ HELP BANNED \n"
                                brk += "├ • Blc\n"
                                brk += "├ • Banlist\n"
                                brk += "├ • {}\n".format(comd["cban"])
                                brk += "├ • Ban:on\n"
                                brk += "├ • Unban:on\n"
                                brk += "├ • Ban @\n"
                                brk += "├ • Unban @\n"
                                brk += "├ • Talkban @\n"
                                brk += "├ • Untalkban @\n"
                                brk += "├ • Talkbanlist @\n"
                                brk += "╰────────────────"
                                cl.sendReplyMessage(msg.id,to, str(brk))

                        elif cmd == "nodejs":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                brk = "╭────────────────\n"
                                brk += "├─≽ HELP NODEJS \n"
                                brk += "├ • {} @\n".format(comd["kick"])
                                brk += "├ • /kick @\n"
                                brk += "├ • /kill (name)\n"
                                brk += "├ • Nukeall\n"
                                brk += "├ • Bypass\n"
                                brk += "├ • Bantai: (number)\n"
                                brk += "╰────────────────"
                                cl.sendReplyMessage(msg.id,to, str(brk))

                        elif cmd == "setting":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                brk = "╭────────────────\n"
                                brk += "├─≽ HELP SETTING \n"
                                brk += "├ • Cekpesan\n"
                                brk += "├ • Cekwelcome\n"
                                brk += "├ • Cekleave\n"
                                brk += "├ • Cekrespon\n"
                                brk += "├ • Ceksider\n"
                                brk += "├ • Cekcomment\n"
                                brk += "├ • Sticker tag\n"
                                brk += "├ • Sticker welcome\n"
                                brk += "├ • Stickef leave\n"
                                brk += "├ • Sticker sider\n"
                                brk += "├ • Sticker pesan\n"
                                brk += "├ • Cmdkick: (cmd)\n"
                                brk += "├ • Cmdhelp: (cmd)\n"
                                brk += "├ • Cmdspeed: (cmd)\n"
                                brk += "├ • Cmdtagall: (cmd)\n"
                                brk += "├ • Cmdunsend: (cmd)\n"
                                brk += "├ • Cmdbye: (cmd)\n"
                                brk += "├ • Cmdcban: (cmd)\n"
                                brk += "├ • Cmdsider on: (cmd)\n"
                                brk += "├ • Cmdsider off: (cmd)\n"
                                brk += "├ • Autojoin on/off\n"
                                brk += "├ • Autoleave on/off\n"
                                brk += "├ • Autoadd on/off\n"
                                brk += "├ • Autoblock on/off\n"
                                brk += "├ • Autoread on/off\n"
                                brk += "├ • Autolike on/off\n"
                                brk += "├ • Autotext on/off\n"
                                brk += "├ • Autochat on/off\n"
                                brk += "├ • Respon on/off\n"
                                brk += "├ • Responcall on/off\n"
                                brk += "├ • Callpm on/off\n"
                                brk += "├ • Unsend on/off\n"
                                brk += "├ • Smule on/off\n"
                                brk += "├ • Yturl on/off\n"
                                brk += "├ • Tiktokurl on/off\n"
                                brk += "├ • Jointicket on/off\n"
                                brk += "├ • Sticker on/off\n"
                                brk += "├ • Contact on/off\n"
                                brk += "├ • Timeline on/off\n"
                                brk += "╰────────────────"
                                cl.sendReplyMessage(msg.id,to, str(brk))

                        elif cmd == "media":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                brk = "╭────────────────\n"
                                brk += "├─≽ HELP MEDIA \n"
                                brk += "├ • Corona\n"
                                brk += "├ • Info bmkg\n"
                                brk += "├ • Porn (query)\n"
                                brk += "├ • Image (query)\n"
                                brk += "├ • Google (query)\n"
                                brk += "├ • Cctv code\n"
                                brk += "├ • Cctv (number)\n"
                                brk += "├ • Musik: (title)\n"
                                brk += "├ • Smule (idamule)\n"
                                brk += "├ • Smuleprofile (id)\n"
                                brk += "├ • Ytmp3 (query)\n"
                                brk += "├ • Ytmp4 (query)\n"
                                brk += "├ • Lowongan kerja\n"
                                brk += "├ • Acara tv\n"
                                brk += "├ • Acaratv (chanel)\n"
                                brk += "├ • Surahlist\n"
                                brk += "├ • Surah: (ayat)\n"
                                brk += "├ • Joox: (query)\n"
                                brk += "├ • Tiktok: (username)\n"
                                brk += "├ • Instagram: (username)\n"
                                brk += "├ • Text 1 s/d 5 (text)\n"
                                brk += "├ • Resi-jnt: (resi)\n"
                                brk += "├ • Resi-rex: (resi)\n"
                                brk += "├ • Resi-sicepat: (resi)\n"
                                brk += "├ • Resi-ninja: (resi)\n"
                                brk += "├ • Resi-pos: (resi)\n"
                                brk += "├ • Cuaca (kota)\n"
                                brk += "├ • Sholat (kota)\n"
                                brk += "├ • Fancytext (text)\n"
                                brk += "├ • Zodiak (query)\n"
                                brk += "├ • Instagram (username) \n"
                                brk += "├ • Ponsel (merek)\n"
                                brk += "├ • Imagetext (query)\n"
                                brk += "├ • Nama (name)\n"
                                brk += "├ • Lahir (ttl)\n"
                                brk += "├ • Mimpi (query) \n"
                                brk += "├ • Lyrik (title)\n"
                                brk += "├ • Calkulator (bilangan)\n"
                                brk += "╰────────────────"
                                cl.sendReplyMessage(msg.id,to, str(brk))

                        elif cmd == "protect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                brk = "╭────────────────\n"
                                brk += "├─≽ HELP PROTECT \n"
                                brk += "├ • Pqr on/off\n"
                                brk += "├ • Pkick on/off\n"
                                brk += "├ • Pjoin on/off\n"
                                brk += "├ • Pinvite on/off\n"
                                brk += "├ • Pcancel on/off\n"
                                brk += "├ • Notag on/off\n"
                                brk += "├ • Listprotect\n"
                                brk += "├ • Promax on/off\n"
                                brk += "╰────────────────"
                                cl.sendReplyMessage(msg.id,to, str(brk))
                        elif cmd == "list":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                brk = "╭──────────────────\n"
                                brk += "├≽ 🧑‍💻OPEN ORDER🧑‍💻 \n"
                                brk += "├ • SelfBot templet onli 50k\n"
                                brk += "├ • Selfbot temp+Ajs 75k\n"
                                brk += "├ • Protect 12bot AllRoom 200k\n"
                                brk += "├ • Protect Room event a/s 200k\n"
                                brk += "├ • Pcancel on/off\n"
                                brk += "├ • SEWA HELPER SB ONLI+JS 200K\n"
                                brk += "├ • 🤖GOLANG WAR🤖\n"
                                brk += "├ • Bot war sb multi Go =35k/bots\n"
                                brk += "├ • Jumlah Bots bisa riquest\n"
                                brk += "├ • 🧑‍💻VPS+TOKEN🧑‍💻\n"
                                brk += "├ • Token Primary 5k 1token 1no\n"
                                brk += "├ • 🧑‍💻LINODE🧑‍💻\n"
                                brk += "├ • 1CORE 2GB 60k via atm\n"
                                brk += "├ • 2CORE 4GB 100k via atm\n"
                                brk += "├ • 4CORE 8GB 180k via atm\n"
                                brk += "├ • 6CORE 16GB 280k via atm\n"
                                brk += "├ • RENTAL VPS MASA GARANSI\n"
                                brk += "├ • AKUN LINODE SALDO $100 260K\n"
                                brk += "├ • 👇KEPOIN AJA👇\n"
                                brk += "├ • ID LINE: botbrk\n"
                                brk += "├ • WA: 085882415817\n"
                                brk += "├ • 🏧PAYMEN🏧\n"
                                brk += "├ • BCA: 7295319283\n"
                                brk += "├ • NAMA: NURSIN\n"
                                brk += "├ • DANA: 085882415817\n"
                                brk += "╰───────────────────"
                                cl.sendReplyMessage(msg.id,to, str(brk))

                        elif cmd == "translate":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                brk = "╭────────────────\n"
                                brk += "├─≽ HELP TRANSLATE \n"
                                brk += "├ • Indo (text)\n"
                                brk += "├ • Eng (text)\n"
                                brk += "├ • Jawa (text)\n"
                                brk += "├ • Sunda (text)\n"
                                brk += "├ • Arab (text)\n"
                                brk += "├ • Thai (text)\n"
                                brk += "├ • Rusia (text)\n"
                                brk += "├ • Spanyol (text)\n"
                                brk += "├ • Itali (text)\n"
                                brk += "├ • Francis (text)\n"
                                brk += "├ • Japan (text)\n"
                                brk += "├ • Korea (text)\n"
                                brk += "├ • Vietnam (text)\n"
                                brk += "├ • Turki (text)\n"
                                brk += "├ • Malay (text)\n"
                                brk += "├ • German (text)\n"
                                brk += "├ • Filipin (text)\n"
                                brk += "├ • China (text)\n"
                                brk += "╰────────────────"
                                cl.sendReplyMessage(msg.id,to, str(brk))

                        elif cmd == "cmd list":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                brk = "╭─「👥 Cmd List ??」\n"
                                for u in comd:
                                    brk += "├❑ {} : {}\n".format(u,comd[u])
                                brk += '╰────────'
                                cl.sendReplyMessage(msg.id,to, str(brk))
                                                         
                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                G = cl.getContact(sender)
                                albrk = "╭── • SELF STATUS •\n"
                                albrk += "├ • User : {}\n".format(G.displayName)
                                albrk += "├ • Time : "+datetime.strftime(timeNow,'%H:%M:%S')+"\n"
                                albrk += "├ • Date : "+datetime.strftime(timeNow,'%d-%m-%Y')+"\n"
                                if wait["smule"] == True: albrk +="├ • Smule ⊷ ✓\n"
                                else: albrk +="├ • Smule ⊷ ✗\n"
                                if wait["yt"] == True: albrk +="├ • Youtube ⊷ ✓\n"
                                else: albrk +="├ • Youtube ⊷ ✗\n"
                                if wait["tiktok"] == True: albrk +="├ • Tiktok ⊷ ✓\n"
                                else: albrk +="├ • Tiktok ⊷ ✗\n"
                                if wait["contact"] == True: albrk +="├ • Contact ⊷ ✓\n"
                                else: albrk +="├ • Contact ⊷ ✗\n"
                                if wait["unsend"] == True: albrk +="├ • Unsend ⊷ ✓\n"
                                else: albrk +="├ • Unsend ⊷ ✗\n"
                                if wait["Timeline"] == True: albrk +="├ • Timeline ⊷ ✓\n"
                                else: albrk +="├ • Timeline ⊷ ✗\n"
                                if temptag["stealtag"] == True: md7="├ • Respon ⊷ ✓\n"
                                else: albrk +="├ • Respon ⊷ ✗\n"
                                if wait["autoBlock"] == True: albrk +="├ • Auto Block ⊷ ✓\n"
                                else: albrk +="├ • Auto Block ⊷ ✗\n"
                                if wait["talkban"] == True: albrk +="├ • Talkban ⊷ ✓\n"
                                else: albrk +="├ • Talkban ⊷ ✗\n"
                                if wait["Mentionkick"] == True: albrk +="├ • Notag ⊷ ✓\n"
                                else: albrk +="├ • Notag ⊷ ✗\n"
                                if wait["autoJoin"] == True: albrk +="├ • Auto Join ⊷ ✓\n"
                                else: albrk +="├ • Auto Join ⊷ ✗\n"
                                if wait["autoAdd"] == True: albrk +="├ • Auto Add ⊷ ✓\n"
                                else: albrk +="├ • Auto Add ⊷ ✗\n"
                                if wait["likeOn"] == True: albrk +="├ • Auto Like ⊷ ✓\n"
                                else: albrk +="├ • Auto Like ⊷ ✗\n"
                                if wait["responGc"] == True: albrk +="├ • Respon Call ⊷ ✓\n"
                                else: albrk +="├ • Respon Call ⊷ ✗\n"
                                if msg.to in welcome: albrk +="├ • Welcome Msg ⊷ ✓\n"
                                else: albrk +="├ • Welcome Msg ⊷ ✗\n"
                                if wait["autoLeave"] == True: albrk +="├ • Auto Leave ⊷ ✓\n"
                                else: albrk +="├ • Auto Leave ⊷ ✗\n"
                                if msg.to in leave: md18="├ • Leave Msg ⊷ ✓\n"
                                else: albrk +="├ • Leave Msg ⊷ ✗\n"
                                if msg.to in protectqr: albrk +="├ • Pro Qr ⊷ ✓\n"
                                else: albrk +="├ • Pro Qr ⊷ ✗\n"
                                if msg.to in protectjoin: albrk +="├ • Pro Join ⊷ ✓\n"
                                else: albrk +="├ • Pro Join ⊷ ✗\n"
                                if msg.to in protectkick: albrk +="├ • Pro Kick ⊷ ✓\n"
                                else: albrk +="├ • Pro Kick ⊷ ✗\n"
                                if msg.to in protectcancel: albrk +="├ • Pro Cancel ⊷ ✓\n"
                                else: albrk +="├ • Pro Cancel ⊷ ✗\n"
                                if msg.to in protectinvite: albrk +="├ • Pro Invite ⊷ ✓\n╰── • βŘҜ-Ŧ€ΔΜ-βØŦŞ • ──"
                                else: albrk +="├ • Pro Invite ⊷ ✗\n╰── • βŘҜ-Ŧ€ΔΜ-βØŦŞ • ──"
                                cl.sendReplyMessage(msg.id,to, str(albrk))
                                                                
                        elif cmd == "rejectall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ginvited = cl.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                    cl.sendReplyMessage(msg.id,to, "Rejected {} Group Invite".format(str(len(ginvited))))
                                else:
                                    cl.sendReplyMessage(msg.id,to,"Nothing Invite Group")
                                
                        elif cmd == "cancelall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                    group = cl.getGroup(to)
                                    if group.invitee is None or group.invitee == []:
                                        cl.sendReplyMessage(msg.id,to,"Nothing Pending Member")
                                    else:
                                        invitee = [contact.mid for contact in group.invitee]
                                        for inv in invitee:
                                            cl.cancelGroupInvitation(to, [inv])
                                        cl.sendReplyMessage(msg.id,to,"Cancelled {} Group Pending".format(str(len(invitee))))
                                
                        elif cmd == "accept:all":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                    group = cl.getGroup(to)
                                    if group.invitee is None or group.invitee == []:
                                        cl.sendReplyMessage(msg.id,to,"No Have Groups Invitation.")
                                    else:
                                        invitee = [contact.mid for contact in group.invitee]
                                        for acc in invitee:
                                            cl.acceptGroupInvitation(to, [acc])
                                        cl.sendReplyMessage(msg.id,to,"Join {} Groups".format(str(len(invitee))))
                              
                        elif cmd == "logout":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                cl.sendMention(msg.to, 'LOGOUT SELFBOT\n• User : @!\m• LogOut From Selfbot\n• Selfbot Sudah Tidak Aktif',' ', [msg._from])
                                sys.exit("Logout")
                              
                        elif cmd.startswith('about'):
                            if wait["selfbot"] == True:
                                if msg._from in admin:
                                    try:
                                        arr = []
                                        today = datetime.today()
                                        thn = 2018 
                                        bln = 8    #isi bulannya yg sewa
                                        hr = 9   #isi tanggalnya yg sewa
                                        future = datetime(thn, bln, hr)
                                        days = (str(future - today))
                                        comma = days.find(",")
                                        days = days[:comma]
                                        h = cl.getContact(clMID)
                                        groups = cl.getGroupIdsJoined()
                                        contactlist = cl.getAllContactIds()
                                        kontak = cl.getContacts(contactlist)
                                        favorite = cl.getFavoriteMids()
                                        fil = cl.getSettings().privacyReceiveMessagesFromNotFriend
                                        seal = cl.getSettings().e2eeEnable
                                        blockedlist = cl.getBlockedContactIds()
                                        src = cl.getSettings().privacySearchByUserid
                                        kontak2 = cl.getContacts(blockedlist)
                                        status = {"kick": "", "invite": ""}
                                        try:cl.kickoutFromGroup(to, [clMID]);status["kick"] = "Normal"
                                        except:status["kick"] = "Limit"
                                        try:cl.inviteIntoGroup(to, [clMID]);status["invite"] = "Normal"
                                        except:status["invite"] = "Limit"
                                        if src == True:alid = "Add From LineID : True"
                                        else:alid = "Add From LineID : False"                            
                                        if seal == True:letsel = "Letter Sealing : True"
                                        if seal == False:letsel = "Letter Sealing : False"
                                        if fil == True:fpes = "Filter Message : False"
                                        if fil == False:fpes = "Filter Message : True"
                                        APK = "╭─── • ABOUT • ───"
                                        APK += "\n├ • Name : {}".format(h.displayName)
                                        APK += "\n├ • Group : {}".format(str(len(groups)))
                                        APK += "\n├ • Friend : {}".format(str(len(kontak)))
                                        APK += "\n├ • Favorite: {}".format(str(len(favorite)))
                                        APK += "\n├ • Blocked : {}".format(str(len(kontak2)))
                                        APK += "\n├ • Chat send : {}".format(str(peler["sendcount"]))
                                        APK += "\n├ • Chat received : {}".format(str(peler["receivercount"]))
                                        APK += "\n├ • {}".format(alid)
                                        APK += "\n├ • {}".format(letsel)
                                        APK += "\n├ • {}".format(fpes)
                                        APK += "\n├ • Kick : %s" % status["kick"]
                                        APK += "\n├ • Invite : %s" % status["invite"]
                                        APK += "\n├ • Type : Selfbot"
                                        APK += "\n├ • Version : V 17"
                                        APK += "\n╰── • βŘҜ-Ŧ€ΔΜ-βØŦŞ • ──"
                                        cl.sendReplyMessage(msg.id,to, str(APK))
                                    except Exception as e:
                                        cl.sendReplyMessage(msg.id,to, str(e))
                               
                        elif cmd.startswith("mid "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendReplyMessage(msg.id,to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Steal " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendReplyMessage(msg.id,to, "╭─「 Contact Info 」\n│ Nama : "+str(mi.displayName)+"\n│ Mid : " +key1+"\n│ Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif ("/ti/g/" in msg.text):
                           if msg._from in admin or msg._from in staff:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                    if l not in n_links:
                                       n_links.append(l)
                                 for ticket_id in n_links:
                                    group = cl.findGroupByTicket(ticket_id)
                                    cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    cl.sendReplyMessage(msg.id,to, "Masuk : %s" % str(group.name))

                        elif text.lower() == "clearchat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   cl.sendReplyMessage(msg.id,to, "Cleared messages ♪")
                               except:
                                   pass
                                
                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:  
                                sep = text.split(" ")
                                txt = text.replace(sep [0] + " ","")
                                groups = cl.getGroupIdsJoined()
                                for group in groups:
                                    cl.sendMessage(group, "{}".format(str(txt)))
                                cl.sendReplyMessage(msg.id,to, "Broadcast {} Group".format(str(len(groups))))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendReplyMessage(msg.id,to, "Setkey Anda: " + str(Setmain["keyCommand"]))
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed...")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "Update to {}".format(str(key).lower()))

                        elif cmd.startswith("setsider: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Gagal mengganti key")
                               else:
                                   wait["mention"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "Update to {}".format(str(key).lower()))

                        elif cmd.startswith("setapikey: "):
                          if wait["selfbot"] == True:
                            if msg._from in "uccd11f359de903676aa3021f8095bd0f":
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Gagal mengganti key")
                               else:
                                   wait["apikey"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "Success update apikey")

                        elif cmd.startswith("setwelcome: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   wait["welcome"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to,"{}".format(str(key).lower()))

                        elif cmd.startswith("setleave: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to,"Failed..!!")
                               else:
                                   wait["leave"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to,"{}".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendReplyMessage(msg.id,to,"Succes")

                        elif cmd == "reboot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendReplyMessage(msg.id,to,"Waitting 1 second")
                               time.sleep(5)
                               Setmain["restartPoint"] = msg.to
                               cl.sendReplyMessage(msg.id,to,"Be reboot to pee.")
                               restartBot()
                                                          
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                cl.sendReplyMessage(msg.id,to, bot)
                               
                        elif cmd == "blocklist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                blockedlist = cl.getBlockedContactIds()
                                kontak = cl.getContacts(blockedlist)
                                num=1
                                msgs="「 Blocked List 」\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTotal Blocked : %i" % len(kontak)
                                cl.sendReplyMessage(msg.id,to, msgs)
                                
                        elif cmd.startswith("delfriend "):
                            if wait["selfbot"] == True:
                                if msg._from in admin:
                                    if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                            for ls in lists:
                                                contact = cl.getContact(ls)
                                                cl.deleteContact(ls)
                                            cl.sendMention(msg.to, 'Delete Friend\n@!\n• Delete for lis friend',' ', [ls])
                                
                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendReplyMessage(msg.id,to,"┏━━[ FRIEND LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Friends ]")
                               
                        elif cmd.startswith("bye:"):
                            if wait["selfbot"] == True:
                              if msg._from in admin:
                                  separate = cmd.split(":")
                                  number = cmd.replace(separate[0] + ":","")
                                  groups = cl.getGroupIdsJoined()
                                  try:
                                      group = groups[int(number)-1]
                                      G = cl.getGroup(group)
                                      try:
                                          cl.leaveGroup(G.id)
                                      except:
                                          cl.leaveGroup(G.id)
                                      cl.sendReplyMessage(msg.id,to,"Leave Group : " + G.name)
                                  except Exception as error:
                                      cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd == "ginfo":
                            if wait["selfbot"] == True:
                                if msg._from in admin:
                                    try:
                                        G = cl.getGroup(msg.to)
                                        if G.invitee is None:
                                            gPending = "0"
                                        else:
                                            gPending = str(len(G.invitee))
                                            if G.preventedJoinByTicket == True:
                                                gQr = "Tertutup"
                                                gTicket = "Tidak ada"
                                            else:
                                                gQr = "Terbuka"
                                                gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                            timeCreated = []
                                            timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                            cl.sendReplyMessage(msg.id,to,"╭─「 Group Info 」\n├↘ Nama Group : {}".format(G.name)+ "\n├↘ ID Group : {}".format(G.id)+ "\n├↘ Pembuat : {}".format(G.creator.displayName)+ "\n├↘ Waktu Dibuat : {}".format(str(timeCreated))+ "\n├↘ Jumlah Member : {}".format(str(len(G.members)))+ "\n├↘ Jumlah Pending : {}".format(gPending)+ "\n├↘ Group Qr : {}".format(gQr)+ "\n├↘ Group Ticket : {}".format(gTicket))
                                            cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                            cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                                    except Exception as e:
                                        cl.sendReplyMessage(msg.id,to,str(e))

                        elif cmd.startswith("infogrup "):
                            if wait["selfbot"] == True:
                                if msg._from in admin:
                                    separate = text.split(" ")
                                    number = text.replace(separate[0] + " ","")
                                    groups = cl.getGroupIdsJoined()
                                    ret_ = ""
                                    try:
                                        group = groups[int(number)-1]
                                        G = cl.getGroup(group)
                                        try:
                                            gCreator = G.creator.displayName
                                        except:
                                            gCreator = "Tidak ditemukan"
                                            if G.invitee is None:
                                                gPending = "0"
                                            else:
                                                gPending = str(len(G.invitee))
                                                if G.preventedJoinByTicket == True:
                                                    gQr = "Tertutup"
                                                    gTicket = "Tidak ada"
                                                else:
                                                    gQr = "Terbuka"
                                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                                timeCreated = []
                                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                                ret_ += "DETAILE GROUPS"
                                                ret_ += "\n• Nama Group : {}".format(G.name)
                                                ret_ += "\n• ID Group : {}".format(G.id)
                                                ret_ += "\n• Pembuat : {}".format(gCreator)
                                                ret_ += "\n• Waktu Dibuat : {}".format(str(timeCreated))
                                                ret_ += "\n• Jumlah Member : {}".format(str(len(G.members)))
                                                ret_ += "\n• Jumlah Pending : {}".format(gPending)
                                                ret_ += "\n• Group Qr : {}".format(gQr)
                                                ret_ += "\n• Group Ticket : {}".format(gTicket)
                                                cl.sendReplyMessage(msg.id,to, str(ret_))
                                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                                    except Exception as e:
                                        cl.sendReplyMessage(msg.id,to,str(e))

                        elif cmd.startswith("gurl "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              separate = text.split(" ")
                              number = text.replace(separate[0] + " ","")
                              groups = cl.getGroupIdsJoined()
                              ret_ = ""
                              try:
                                  group = groups[int(number)-1]
                                  G = cl.getGroup(group)
                                  G.preventedJoinByTicket = False
                                  cl.updateGroup(G)
                                  try:
                                      gCreator = G.creator.mid
                                      dia = cl.getContact(gCreator)
                                      zx = ""
                                      zxc = ""
                                      zx2 = []
                                      xpesan = '「 Sukses Open Qr 」\n• Creator :  '
                                      diaa = str(dia.displayName)
                                      pesan = ''
                                      pesan2 = pesan+"@a\n"
                                      xlen = str(len(zxc)+len(xpesan))
                                      xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                      zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                      zx2.append(zx)
                                      zxc += pesan2
                                  except:
                                      gCreator = "Tidak ditemukan"
                                  if G.invitee is None:
                                      gPending = "0"
                                  else:
                                      gPending = str(len(G.invitee))
                                  if G.preventedJoinByTicket == True:
                                      gQr = "Tertutup"
                                      gTicket = "Tidak ada"
                                  else:
                                      gQr = "Terbuka"
                                      gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                  timeCreated = []
                                  timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                  ret_ += xpesan+zxc
                                  ret_ += "• Nama : {}".format(G.name)
                                  ret_ += "\n• Group Qr : {}".format(gQr)
                                  ret_ += "\n• Pendingan : {}".format(gPending)
                                  ret_ += "\n• Group Ticket : {}".format(gTicket)
                                  ret_ += ""
                                  cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                              except:
                                  pass

                        elif cmd.startswith("close "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              separate = text.split(" ")
                              number = text.replace(separate[0] + " ","")
                              groups = cl.getGroupIdsJoined()
                              ret_ = ""
                              try:
                                  group = groups[int(number)-1]
                                  G = cl.getGroup(group)
                                  G.preventedJoinByTicket = True
                                  cl.updateGroup(G)
                                  try:
                                      gCreator = G.creator.mid
                                      dia = cl.getContact(gCreator)
                                      zx = ""
                                      zxc = ""
                                      zx2 = []
                                      xpesan = '「 Sukses Close Qr 」\n• Creator :  '
                                      diaa = str(dia.displayName)
                                      pesan = ''
                                      pesan2 = pesan+"@a\n"
                                      xlen = str(len(zxc)+len(xpesan))
                                      xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                      zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                      zx2.append(zx)
                                      zxc += pesan2
                                  except:
                                      gCreator = "Tidak ditemukan"
                                  if G.invitee is None:
                                      gPending = "0"
                                  else:
                                      gPending = str(len(G.invitee))
                                  if G.preventedJoinByTicket == True:
                                      gQr = "Tertutup"
                                      gTicket = "Tidak ada"
                                  else:
                                      gQr = "Terbuka"
                                      gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                  timeCreated = []
                                  timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                  ret_ += xpesan+zxc
                                  ret_ += "• Nama : {}".format(G.name)
                                  ret_ += "\n• Group Qr : {}".format(gQr)
                                  ret_ += "\n• Pendingan : {}".format(gPending)
                                  ret_ += "\n• Group Ticket : {}".format(gTicket)
                                  ret_ += ""
                                  cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                              except:
                                  pass

                        elif cmd.startswith("infomem "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              separate = msg.text.split(" ")
                              number = msg.text.replace(separate[0] + " ","")
                              groups = cl.getGroupIdsJoined()
                              ret_ = ""
                              try:
                                  group = groups[int(number)-1]
                                  G = cl.getGroup(group)
                                  no = 0
                                  ret_ = ""
                                  for mem in G.members:
                                      no += 1
                                      ret_ += "\n " "├• "+ str(no) + ". " + mem.displayName
                                  cl.sendReplyMessage(msg.id,to, "├↘ Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                              except: 
                                  pass

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                groups = cl.getGroupIdsJoined()
                                ret_ = "╭───────────────\n├─≽ ᴅᴀꜰᴛᴀʀ ɢʀᴏᴜᴘ ️"
                                no = 1
                                for gid in groups:
                                    group = cl.getGroup(gid)
                                    ret_ += "\n├≽• {}. {}  {}".format(str(no), str(group.name), str(len(group.members)))
                                    no = (no+1)
                                ret_ += "\n╰───────────────"
                                cl.sendReplyMessage(msg.id,to, str(ret_))

                        elif cmd == "buka qr":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendReplyMessage(msg.id,to,"Open Link Groups")

                        elif cmd == "tutup qr":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendReplyMessage(msg.id,to,"Blocked Url Groups")

                        elif cmd == "url":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendReplyMessage(msg.id,to, "Nama : "+str(x.name)+ "\nUrl : http://line.me/R/ti/g/"+gurl)
                                                                                     
                                                        
                        elif cmd == "me":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                cl.sendMessageMusic(msg.to, sender)

                        elif cmd.startswith("musik:"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                set = text.split(" ")
                                mod = text.replace(set[0] + " ","")
                                mode = mod.split("|")
                                search = str(mode[0])
                                api = BEAPI()
                                main = api.jooxSearch(search)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if len(mode) == 1:
                                    num = 0
                                    ret_ = "MUSIK RESULT\n"
                                    for youtube in main["result"]:
                                        num += 1
                                        ret_ += "• {}. {}\n".format(str(num), str(youtube["msong"]))
                                    ret_ += "EXAMPLE FOR PLAY\n"
                                    ret_ += "Ketik {} | No urutuan di atas".format(str(text))
                                    cl.sendReplyMessage(msg.id,to, str(ret_))
                                elif len(mode) == 2:
                                    num = int(mode[1])
                                    if num <= len(main["result"]):
                                        pixel = main["result"] [num - 1]
                                        kontol = "MUSIK DETAILE"
                                        kontol += "\n• Artis : {}".format(pixel["artist"])
                                        kontol += "\n• Album : {}".format(pixel["malbum"])
                                        kontol += "\n• Title : {}".format(pixel["title"])
                                        kontol += "\n• Rilis : {}".format(pixel["public_time"])
                                        cl.sendReplyMessage(msg.id,to, str(kontol))
                                        sendFlexAudio(to, "{}".format(pixel["mp3Url"]))                                         

                        elif cmd.startswith("joox:"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                set = text.split(" ")
                                search = text.replace(set[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                data = api.joox(search)
                                sendFlexAudio(to, "{}".format(data["result"]["mp3Url"]))

                        elif cmd.startswith("imagetext:"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                set = text.split(" ")
                                search = text.replace(set[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                data = api.imagetext(search)
                                img = data["result"]
                                cl.sendImageWithURL(to, str(img))                        

                        elif cmd.startswith("uns "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                sep = text.split(" ")
                                args = text.replace(sep[0] + " ", "")
                                mes = 0
                                try:
                                    mes = int(args[1])
                                except:
                                    mes = 1
                                M = cl.getRecentMessagesV2(to, 101)
                                MId = []
                                for ind, i in enumerate(M):
                                    if ind == 0:
                                        pass
                                    else:
                                        if i._from == cl.profile.mid:
                                            MId.append(i.id)
                                            if len(MId) == mes:
                                                break
                                def unsMes(id):
                                    cl.unsendMessage(id)
                                for i in MId:
                                    thread1 = threading.Thread(target=unsMes, args=(i,))
                                    thread1.start()
                                    thread1.join()
                                cl.unsendMessage(msg.id)
                                                                                                                                    
                        elif cmd == "tag":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              cl.unsendMessage(msg.id)
                              group = cl.getGroup(to)
                              midMembers = [contact.mid for contact in group.members]
                              midSelect = len(midMembers)//20
                              for mentionMembers in range(midSelect+1):
                                  no = 0
                                  ret_ = "「 Mention member 」\n"
                                  dataMid = []
                                  for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n{}. @!".format(str(no))
                                  ret_ += "\n\n「 Jumlah {} member 」".format(str(len(dataMid)))
                                  apkMention(to, ret_, dataMid)    
   
                        elif cmd == comd["tagall"]:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              cl.unsendMessage(msg.id)
                              members = []
                              if msg.toType == 1:
                                  room = cl.getCompactRoom(to)
                                  members = [mem.mid for mem in room.contacts]
                              elif msg.toType == 2:
                                  group = cl.getCompactGroup(to)
                                  members = [mem.mid for mem in group.members]
                              else:
                                  return cl.sendMessage(to, 'Failed mentionall members, use this command only on room or group chat')
                              if members:
                                  mentionMembers2(to, members)
        
                        elif cmd.startswith("tag: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              separate = msg.text.split(":")
                              number = msg.text.replace(separate[0] + ":"," ")
                              groups = cl.getGroupIdsJoined()
                              gid = groups[int(number)-1]                                                                                                      
                              members = []
                              if msg.toType == 1:
                                  room = cl.getCompactRoom(gid)
                                  members = [mem.mid for mem in room.contacts]
                              elif msg.toType == 2:
                                  group = cl.getCompactGroup(gid)
                                  members = [mem.mid for mem in group.members]
                              else:
                                  return cl.sendMessage(to, 'Failed mentionall members, use this command only on room or group chat')
                              if members:
                                  mentionMembers2(gid, members)
                                  cl.sendReplyMessage(msg.id,to, "Remote Mentions Group: " + str(group.name))                                                  

                        elif 'https://www.smule.com/' in msg.text or  'https://link.smule.com/' in msg.text or  'https://www.smule.com/sing' in msg.text:
                          if wait["smule"] == True:
                            try:
                                spilt = msg.text.split(" ")
                                txt = spilt
                                no = 0 + 1
                                no += 1
                                data = "{}".format(str(len(txt)))
                                c=ApCalculator()
                                c.run('{} - 1'.format(data))
                                kala = {"write":""}
                                date = kala["write"] = c.lcd
                                ang = kala["write"]
                                hasil = int(ang)
                                aturan = txt[hasil]
                                api = BEAPI()
                                res = api.smulePost(aturan)
                                kontol = "╭── • SMULE URL • ──"
                                kontol += "\n├ • Id : {}".format(res["result"]["owner"]["handle"])
                                kontol += "\n├ • Type : {}".format(res["result"]["ensemble_type"])
                                kontol += "\n├ • Format : {}".format(res["result"]["type"])
                                kontol += "\n├ • Like : {}".format(res["result"]["stats"]["total_loves"])
                                kontol += "\n├ • Gift : {}".format(res["result"]["stats"]["total_gifts"])
                                kontol += "\n├ • Listens : {}".format(res["result"]["stats"]["total_listens"])
                                kontol += "\n├ • Comment : {}".format(res["result"]["stats"]["total_comments"])
                                kontol += "\n╰── • βŘҜ-Ŧ€ΔΜ-βØŦŞ ──"
                                cl.sendReplyMessage(msg.id,to, str(kontol))
                                if res["result"]["type"] == "audio":
                                    sendFlexAudio(to, "{}".format(res["result"]["media_url"]))
                                else:
                                    sendFlexVideo(to, "{}".format(res["result"]["video_media_url"]))
                            except Exception as error:
                                print(error)                                                   
#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendReplyMessage(msg.id,to,"Send a Picture ♪")
                                
                        elif cmd == "updatecover":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changeCover"][clMID] = True
                                cl.sendReplyMessage(msg.id,to,"Send a Picture ♪")

                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["changeFoto"][clMID] = True
                                cl.sendReplyMessage(msg.id,to,"Send a Picture ♪")
                               
                                
                        elif cmd.startswith("myname: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              separate = msg.text.split(" ")
                              string = msg.text.replace(separate[0] + " ","")
                              if len(string) <= 10000000000:
                                  profile = cl.getProfile()
                                  profile.displayName = string
                                  cl.updateProfile(profile)
                                  cl.sendReplyMessage(msg.id,to,"Update to " + string + "")

                        elif cmd.startswith("cek "):
                           if wait["selfbot"] == True:
                             if msg._from in admin:
                               separate = msg.text.split(" ")
                               mid = msg.text.replace(separate[0] + " ","")
                               if mid is not None:
                                   listMid = mid.split("*")
                                   if len(listMid) > 1:
                                       for a in listMid:
                                           cl.sendContact(to,a)
                                   else:
                                       cl.sendContact(to,mid)

                        elif cmd.startswith("stag"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                gname = cl.getGroup(msg.to)
                                local = [contact.mid for contact in gname.members]
                                try:
                                    lur = len(local)//20
                                    for fu in range(lur+1):
                                        hdc = u''
                                        sell=0
                                        com=[]
                                        for rid in gname.members[fu*20 : (fu+1)*20]:
                                            com.append({"S":str(sell), "E" :str(sell+6), "M":rid.mid})
                                            sell += 7
                                            hdc += u'@A_RFU\n'
                                            atas = '\n╭───────────────\n│Mention {} '.format(str(gname.name))
                                            atas += '\n│Total {} Members\n╰───────────────'.format(str(len(local)))
                                        cl.sendMessage(to, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                                except Exception as error:
                                    cl.sendMessage(to, str(error)) 

                        elif cmd.startswith("addtext "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                sep = text.split(" ")
                                apl = text.replace(sep[0] + " ","")
                                sam = apl.split("/")
                                chat1 = sam[0]
                                chat2 = sam[1]
                                apk = ""+chat1
                                tes["Message"][apk] = chat2
                                tes["msg"] = chat1
                                anu = tes["msg"]+'.'
                                cl.sendReplyMessage(msg.id,to,"Command %s created."%chat1)
                                tes["msg"] = {}

                        elif cmd == "list text":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if tes["Message"] == {}:
                                    cl.sendReplyMessage(msg.id,to,"empty text")
                                else:
                                    mc = ""
                                    jml = 1
                                    for listword in tes["Message"]:
                                        mc += "\n"+str(jml)+". "+listword+""
                                        jml += 1
                                    cl.sendReplyMessage(msg.id,to, "List text :\n"+str(mc))

                        elif cmd.startswith("deltext "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                sep = text.split(" ")
                                xres = text.replace(sep[0] + " ","")
                                tetx = text.replace(sep[0] + " ","")
                                if xres in tes["Message"]:
                                    del tes["Message"][xres]                                        
                                    cl.sendReplyMessage(msg.id,to,"Command %s has been removed."%tetx)
                                else:
                                    cl.sendReplyMessage(msg.id,to,"Command %s does not exist."%tetx)

                        elif msg.text.lower() in tes["Message"]:
                            if wait["autotext"] == True:
                                sid = tes["Message"][msg.text.lower()]
                                cl.sendReplyMessage(msg.id, to, sid)     
                            
                        elif cmd == "screen -ls":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              process = os.popen('screen -list')
                              a = process.read()
                              cl.sendReplyMessage(msg.id,to, "{}".format(a))
                              process.close()

                        elif cmd == "myname":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              h = cl.getContact(sender)
                              cl.sendReplyMessage(msg.id,to, "「 Name 」\n"+str(h.displayName))
                            
                        elif cmd == "mybio":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              h = cl.getContact(sender)
                              cl.sendReplyMessage(msg.id,to, "「 Status 」\n"+str(h.statusMessage))
                            
                        elif cmd == "mypict":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              h = cl.getContact(sender)
                              image = "http://dl.profile.line-cdn.net/" + h.pictureStatus
                              cl.sendImageWithURL(msg.to, image)     

                        elif cmd == "myvideo":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              h = cl.getContact(sender)
                              if h.videoProfile == None:
                              	return cl.sendMessage(to, "「 Video 」\nNone")
                              cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")       
#===========BOT UPDATE============#                                                     
                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n│'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n│"
                                cl.sendReplyMessage(msg.id,to, "╭─「 User botlist」\n│\n│"+ma+"\n╰──「 Total「%s」User Botlist 」" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n│'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n│"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n│'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n│"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n│'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n│"
                                cl.sendReplyMessage(msg.id,to, "╭─「 List Admin Selfbot 」\n│\n│Owner:\n│"+ma+"\n│Admin:\n│"+mb+"\n│Staff:\n│"+mc+"\n╰──「Total「%s」Team 」" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n│'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n│"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n│'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n│"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n│'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n│"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n│'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n│"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n│'
                                    me += str(e) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendReplyMessage(msg.id,to, "╭─「 Setting Protection List 」\n│\n│ PROTECT URL :\n│"+ma+"\n│ PROTECT KICK :\n│"+mb+"\n│ PROTECT JOIN :\n│"+md+"\n│ PROTECT CANCEL:\n│"+mc+"\n│ PROTECT INVITE:\n│"+me+"\n╰──「 Total「%s」Protect 」" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))


                        elif cmd == comd["bye"]:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendReplyMessage(msg.id,to,"Sayonara......")
                                cl.leaveGroup(msg.to)

                        elif cmd == "respontime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendReplyMessage(msg.id,to,"「 Respontime 」\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == comd["speed"]:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                start = time.time()
                                cl.sendMessage("u0a94a68c058d99a72f95b420a0b7a493", "test speed")
                                speed = time.time() - start
                                ping = speed * 1000
                                cl.sendReplyMessage(msg.id,to, "{} ms".format(str(speedtest(ping))))
                             
                        elif cmd == comd["siderOn"]:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendReplyMessage(msg.id,to,"Sider Enable ♪") #\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  cl.unsendMessage(msg.id)
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == comd["siderOff"]:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendReplyMessage(msg.id,to,"Sider Disable ♪") #\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  cl.unsendMessage(msg.id)
                              else:
                                  cl.sendReplyMessage(msg.id,to,"None Active..!!")
                             
                        elif cmd.startswith("find "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  key1 = key["MENTIONEES"][0]["M"]
                                  a = cl.getGroupIdsJoined();i = cl.getGroups(a)
                                  c = []
                                  for h in i:
                                      g = [c.append(h.name[0:20]+',.s/'+str(len(h.members))) for d in h.members if key1 in d.mid]
                                  h = "╭「 Find Contact 」─"
                                  no = 0
                                  for group in c:
                                      no += 1
                                      h+= "\n│{}. {} | {}".format(no, group.split(',.s/')[0], group.split(',.s/')[1])
                                  cl.sendReplyMessage(msg.id,to, h+"\n╰─「 {} Groups I Found it 」".format(len(c)))                                
                                
                        elif cmd.startswith("tag "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              text = removeCmd("tag", text)
                              sep = text.split(" ")
                              text = text.replace(sep[0] + " ", text)
                              cond = text.split(" ")
                              jml = int(cond[0])
                              for x in range(jml):
                                  name = cl.getContact(to)
                                  RhyN_(to, name.mid)
                                
                        elif cmd.startswith("spam "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              dzin = removeCmd("spam", text)
                              line = dzin.split("|")
                              count = int(line[1])
                              text1 = removeCmd("spam"+str(line[0])+"|"+str(count)+"|", text)
                              text2 = count * (text1+"\n")
                              if line[0] == "on":
                                  if count <= 1000:
                                      for a in range(count):
                                          cl.sendMessage(msg.to, str(text1))
                                  else:
                                      cl.sendMessage(msg.to, "Max 1000.")
                              if line[0] == "off":
                                  if count <= 1000:
                                      cl.sendMessage(msg.to, str(text2))
                                  else:
                                      cl.sendMessage(msg.to, "Max 1000.")
                            
                        elif cmd == "clearallfriend":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              n = len(cl.getAllContactIds())
                              try:
                                  cl.clearContacts()
                              except: 
                                  pass
                              t = len(cl.getAllContactIds())
                              cl.sendReplyMessage(msg.id,to,"Type: Friendlist\n • Detail: Clear Contact\n • Before: %s Friendlist\n • After: %s Friendlist\n • Total removed: %s Friendlist\n • Status: Succes.."%(n,t,(n-t)))
#===========Hiburan============#
                        elif cmd == "cctv code":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                             api = imjustgood(wait["apikey"])
                             data = api.cctv_code()
                             brk = "RESULT CCTV"
                             for b in data["result"]["active"]:
                                 brk += "\n• {} {}".format(b,data["result"]["active"][b])
                             cl.sendReplyMessage(msg.id,to, "{}\nExample : Cctv (number)".format(brk))
                        elif cmd.startswith('cctv '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    args = text.split(" ")
                                    userId = text.replace(args[0] + " ","")
                                    api = imjustgood(wait["apikey"])
                                    data = api.cctvSearch(userId)
                                    brk = "DETAIL CCTV INFO"
                                    brk += "\nArea : {}".format(data["result"]["area"])
                                    brk += "\nWilayah : {}".format(data["result"]["wilayah"])
                                    cl.sendReplyMessage(msg.id,to, str(brk))
                                    cl.sendVideoWithUrl(to, "{}".format(data["result"]["video"]))
                                except Exception as error:
                                    cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith('lyrik '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                             args = text.split(" ")
                             userId = text.replace(args[0] + " ","")
                             api = imjustgood(wait["apikey"])
                             data = api.lyric(userId)
                             brk = "• Title : {}".format(data["result"]["title"])
                             brk += "\n• Artist : {}".format(data["result"]["artist"])
                             brk += "\n{}".format(data["result"]["lyric"])
                             cl.sendReplyMessage(msg.id,to, str(brk))

                        elif cmd.startswith('exc'):
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                              try:
                                 sep = text.split('\n')
                                 kontol = text.replace(sep[0] + '\n','')
                                 exec()
                              except Exception as e:
                                 cl.sendReplyMessage(msg.id,to, "[ INFO ] Error :\n " + str(e))       

                        elif cmd.startswith('nama '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = imjustgood(wait["apikey"])
                               data = api.nama(userId)
                               result  = "• Name : {}".format(data["result"]["name"])
                               result += "\n• Karakter : {}".format(data["result"]["definition"])
                               result += "\n• Description : {}".format(data["result"]["description"])
                               cl.sendReplyMessage(msg.id,to, str(result))

                        elif cmd.startswith('tiktok '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = imjustgood(wait["apikey"])
                               data = api.tiktok(userId)
                               result  = "Username : {}".format(data["result"]["username"])
                               result += "\nFullname : {}".format(data["result"]["fullname"])
                               result += "\nPrivate : {}".format(data["result"]["private"])
                               result += "\nVerified : {}".format(data["result"]["private"])
                               result += "\nBiography : {}".format(data["result"]["biography"])
                               result += "\nFollowers : {}".format(data["result"]["followers"])
                               result += "\nFollowing : {}".format(data["result"]["following"])
                               result += "\nLikes : {}".format(data["result"]["likes"])
                               if data["result"]["lastpost"] != []:
                                   for a in data["result"]["lastpost"]:
                                       result  = "\Lastpost"
                                       result += "\n- Caption : {}".format(a["desc"])
                                       result += "\n- Created : {}".format(a["created"])
                                       result += "\n- Comments : {}".format(a["comment"])
                                       result += "\n- Playing : {}".format(a["playing"])
                                       result += "\n- Share : {}".format(a["share"])
                                   cl.sendReplyMessage(msg.id,to, str(result))
                                   sendFlexVideo(to, "{}".format(a["videoUrl"]))

                        elif cmd.startswith('lahir '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = imjustgood(wait["apikey"])
                               data = api.lahir(userId)
                               brk = "Lahir : {}".format(data["result"]["lahir"])
                               brk += "\nHari : {}".format(data["result"]["hari"])
                               brk += "\nZodiac : {}".format(data["result"]["zodiak"])
                               brk += "\nUltah : {}".format(data["result"]["ultah"])
                               brk += "\nUsia : {}".format(data["result"]["usia"])
                               cl.sendReplyMessage(msg.id,to, str(brk))

                        elif cmd.startswith('calculator '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = imjustgood(wait["apikey"])
                               data = api.calc(userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]))
                           
                        elif cmd.startswith('mimpi '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              try:
                                  args = text.split(" ")
                                  userId = text.replace(args[0] + " ","")
                                  api = imjustgood(wait["apikey"])
                                  data = api.mimpi(userId)
                                  brk = "ARTI DARI MIMPI"
                                  for vi in data["result"]:
                                      brk += "\nMimpi : {}".format(vi["dream"])
                                      brk += "\n{}".format(vi["meaning"])
                                  cl.sendReplyMessage(msg.id,to, str(brk))
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith('image '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = imjustgood(wait["apikey"])
                               data = api.wallpaper(userId)
                               for bot in data["result"]:
                                   cl.sendImageWithURL(to, str(bot))

                        elif cmd.startswith('text '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               vi = text.split(" ")
                               vi1 = text.replace(vi[0] + " ","")
                               mode = vi1.split(" ")
                               search = str(mode[0])
                               kontol = {"id": "1","text": "{}".format(vi1),"text2": "{}".format(search)}
                               api = BEAPI()
                               res = api.textPro(kontol) 
                               cl.sendImageWithURL(to, "{}".format(res["result"]))
                        elif cmd.startswith('text1 '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               vi = text.split(" ")
                               vi1 = text.replace(vi[0] + " ","")
                               api = BEAPI()
                               kontol = {"id": "2","text": "{}".format(vi1)}
                               res = api.textPro(kontol)
                               cl.sendImageWithURL(to, "{}".format(res["result"]))
                        elif cmd.startswith('text2 '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               vi = text.split(" ")
                               vi1 = text.replace(vi[0] + " ","")
                               kontol = {"id": "9","text": "{}".format(vi1),"text2": "{}".format(vi1)}
                               api = BEAPI()  
                               res = api.textPro(kontol)
                               cl.sendImageWithURL(to, "{}".format(res["result"]))
                        elif cmd.startswith('text3 '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               vi = text.split(" ")
                               vi1 = text.replace(vi[0] + " ","")
                               api = BEAPI()
                               kontol = {"id": "4","text": "{}".format(vi1)}
                               res = api.textPro(kontol)
                               cl.sendImageWithURL(to, "{}".format(res["result"]))
                        elif cmd.startswith('text4 '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               vi = text.split(" ")
                               vi1 = text.replace(vi[0] + " ","")
                               api = BEAPI()
                               kontol = {"id": "5","text": "{}".format(vi1)}
                               res = api.textPro(kontol)
                               cl.sendImageWithURL(to, "{}".format(res["result"]))
                        elif cmd.startswith('text5 '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               vi = text.split(" ")
                               vi1 = text.replace(vi[0] + " ","")
                               api = BEAPI()
                               kontol = {"id": "6","text": "{}".format(vi1)}
                               res = api.textPro(kontol)
                               cl.sendImageWithURL(to, "{}".format(res["result"]))

                        elif cmd.startswith('eng '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("en", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('japan '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("ja", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('korea '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("ko", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('india '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("hi", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('francis '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("fr", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('arab '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("ar", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('china '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("zh-CN", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('itali '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("it", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('malay '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("ms", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('turki '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("tr", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('rusia '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("ru", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('spanyol '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("es", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('sunda '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("su", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('indo '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("id", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('thai '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("th", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('vietnam '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("vi", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('jawa '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("jw", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('filipin '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("tl", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                        elif cmd.startswith('german '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = BEAPI()
                               data = api.googleTranslate("de", userId)
                               cl.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                           
                        elif cmd.startswith('ytmp3 '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api  = imjustgood(wait["apikey"])
                               data = api.youtube(userId)
                               xyz = "\n• author : {}".format(data["result"]["author"])
                               xyz += "\n• Duration : {}".format(data["result"]["duration"])
                               xyz += "\n• Watched : {}".format(data["result"]["watched"])
                               xyz += "\n• Title : {}".format(data["result"]["title"])
                               cl.sendReplyMessage(msg.id,to, str(xyz))
                               sendFlexAudio(to, "{}".format(data["result"]["audioUrl"]))

                        elif cmd.startswith('porn '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api  = imjustgood(wait["apikey"])
                               data = api.porn(userId)
                               xyz = "RESULT PORN VIDEOS"
                               xyz += "\n• Quality : {}".format(data["result"]["quality"])
                               xyz += "\n• Duration : {}".format(data["result"]["duration"])
                               xyz += "\n• Title : {}".format(data["result"]["title"])
                               cl.sendReplyMessage(msg.id,to, str(xyz))
                               sendFlexVideo(to, "{}".format(data["result"]["videoUrl"]))

                        elif cmd.startswith('ytmp4 '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api  = imjustgood(wait["apikey"])
                               data = api.youtube(userId)
                               xyz = "• author : {}".format(data["result"]["author"])
                               xyz += "\n• Duration : {}".format(data["result"]["duration"])
                               xyz += "\n• Watched : {}".format(data["result"]["watched"])
                               xyz += "\n• Title : {}".format(data["result"]["title"])
                               cl.sendReplyMessage(msg.id,to, str(xyz))
                               sendFlexVideo(to, "{}".format(data["result"]["videoUrl"]))

                        elif cmd.startswith('cuaca '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = imjustgood(wait["apikey"])
                               data = api.cuaca(userId)
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               xyz = "CUACA INFO"
                               xyz += "\n• Time : "+datetime.strftime(timeNow,'%H:%M:%S')
                               xyz += "\n• Date : "+datetime.strftime(timeNow,'%d-%m-%Y')
                               xyz += "\n• Wilayah : {}".format(data["result"]["location"])
                               xyz += "\n• Cuaca : {}".format(data["result"]["description"])
                               xyz += "\n• Persentase : {}".format(data["result"]["humidity"])
                               xyz += "\n• Temperatur : {}".format(data["result"]["temperatur"])
                               xyz += "\n• Kecepatan angin : {}".format(data["result"]["wind"])
                               cl.sendReplyMessage(msg.id,to, str(xyz))

                        elif cmd.startswith('sholat '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = imjustgood(wait["apikey"])
                               data = api.adzan(userId)
                               xyz = "JADWAL SHALLAT"
                               xyz += "\n• Date : {}".format(data["result"]["tanggal"])
                               xyz += "\n• Wilayah : {}".format(data["result"]["wilayah"])
                               xyz += "\n• Ashar : {}".format(data["result"]["adzan"]["ashar"])
                               xyz += "\n• Dhuha : {}".format(data["result"]["adzan"]["dhuha"])
                               xyz += "\n• Dzuhur : {}".format(data["result"]["adzan"]["dzuhur"])
                               xyz += "\n• Imsyak : {}".format(data["result"]["adzan"]["imsyak"])
                               xyz += "\n• Isya : {}".format(data["result"]["adzan"]["isya"])
                               xyz += "\n• Maghrib : {}".format(data["result"]["adzan"]["maghrib"])
                               xyz += "\n• Subuh : {}".format(data["result"]["adzan"]["subuh"])
                               xyz += "\n• Fajar : {}".format(data["result"]["adzan"]["terbit"])
                               cl.sendReplyMessage(msg.id,to, str(xyz))

                        elif cmd == "corona":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               api = imjustgood(wait["apikey"])
                               data = api.corona()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               xyz = "COUNT COVID 19"
                               xyz += "\n• Time : "+datetime.strftime(timeNow,'%H:%M:%S')
                               xyz += "\n• Date : {}".format(data["result"]["date"])
                               xyz += "\nINDONESIA"
                               xyz += "\n• Terjangkit : {}".format(data["result"]["indonesia"]["case"])
                               xyz += "\n• Sembuh : {}".format(data["result"]["indonesia"]["fit"])
                               xyz += "\n• Meninggal : {}".format(data["result"]["indonesia"]["rip"])
                               xyz += "\nSELURUH DUNIA"
                               xyz += "\n• Terjangkit : {}".format(data["result"]["world"]["case"])
                               xyz += "\n• Sembuh : {}".format(data["result"]["world"]["fit"])
                               xyz += "\n• Meninggal : {}".format(data["result"]["world"]["rip"])
                               cl.sendReplyMessage(msg.id,to, str(xyz))

                        elif cmd == "surahlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               api = imjustgood(wait["apikey"])
                               data = api.alquran()
                               brk  = "LIST SURAH AL-QUR'AN"
                               for qs in data:
                                   brk += "\n{}".format(qs)
                               cl.sendReplyMessage(msg.id,to, str(brk)) 

                        elif cmd.startswith('surah '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              try:
                                  args = text.split(" ")
                                  userId = text.replace(args[0] + " ","")
                                  api = imjustgood(wait["apikey"])
                                  data = api.alquranQS(userId) 
                                  audioUrl = data["result"]["audio"]
                                  brk = "Di Turunkan Di :{}\n".format(data["result"]["place"])
                                  brk += "{}".format(data["result"]["desc"])
                                  cl.sendReplyMessage(msg.id,to, (brk))
                                  sendFlexAudio(to, str(audioUrl))
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to, "ERROR!\nText Terlalu Panjang!!")         

                        elif cmd == "info bmkg":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               api = imjustgood(wait["apikey"])
                               data = api.bmkg()
                               xyz = "INFO BMKG"
                               xyz += "\n• Time : {}".format(data["result"]["pukul"])
                               xyz += "\n• Date : {}".format(data["result"]["tanggal"])
                               xyz += "\n• Wilayah : {}".format(data["result"]["wilayah"])
                               xyz += "\n• Kukuatan : {}".format(data["result"]["kekuatan"])
                               xyz += "\n• Kedalaman : {}".format(data["result"]["kedalaman"])
                               xyz += "\n• Kordinat : {}".format(data["result"]["kordinat"])
                               xyz += "\n• Lokasi : {}".format(data["result"]["lokasi"])
                               xyz += "\n• Arahan : {}".format(data["result"]["arahan"])
                               xyz += "\n• Saran : {}".format(data["result"]["saran"])
                               cl.sendReplyMessage(msg.id,to, str(xyz))

                        elif cmd.startswith('fancytext '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = imjustgood(wait["apikey"])
                               data = api.fancy(userId) 
                               brk = "FANCY RESULT :\n"
                               for s in data["result"]:
                                   brk += "\n{}\n".format(s)
                               cl.sendReplyMessage(msg.id,to, str(brk))         

                        elif cmd.startswith('acaratv '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = imjustgood(wait["apikey"])
                               data = api.acaratv_channel(userId) 
                               brk = "Jadwal Acara TV"
                               for a in data["result"]:
                                   brk += "\n{}".format(a)
                               cl.sendReplyMessage(msg.id,to, str(brk))    

                        elif cmd == "acara tv":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               api = imjustgood(wait["apikey"])
                               data   = api.acaratv()
                               result = "ACARA TV"
                               for a in data["result"]:
                                   for b in a:
                                       result += "\n\nChannel : {}".format(b)
                                       for c in a[b]:
                                           result += "\n{}".format(c)
                               cl.sendReplyMessage(msg.id,to, str(result))      

                        elif cmd == "lowongan kerja":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               api = imjustgood(wait["apikey"])
                               data   = api.karir()
                               number = 0
                               apkbot = "INFO LOWONGAN KERJA"
                               for a in data["result"]:
                                   number += 1
                                   apkbot += "\n\n{}. {}".format(number,a["perusahaan"])
                                   apkbot += "\nLokasi : {}".format(a["lokasi"])
                                   apkbot += "\nProfesi : {}".format(a["profesi"])
                                   apkbot += "\nBagian : {}".format(a["bagian"])
                                   apkbot += "\nJabatan : {}".format(a["jabatan"])
                                   apkbot += "\nGaji : {}".format(a["gaji"])
                                   apkbot += "\nPendidikan : {}".format(a["pendidikan"])
                                   apkbot += "\nPengalaman : {}".format(a["pengalaman"])
                                   apkbot += "\nSyarat : {}".format(a["syarat"])
                                   apkbot += "\nDeskirpsi : {}".format(a["deskripsi"])
                                   apkbot += "\nSumber : {}".format(a["sumber"])
                               cl.sendReplyMessage(msg.id,to, str(apkbot))     

                        elif cmd.startswith("zodiak"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                set = text.split(" ")
                                search = text.replace(set[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                data = api.zodiac(search)
                                brk = "ZODIAK INFO"
                                brk += "\n• Sign : {}".format(data["result"]["zodiac"])
                                brk += "\n• Couple : {}".format(data["result"]["couple"])
                                brk += "\n• Date Range : {}".format(data["result"]["date"])
                                brk += "\n• Lucky Color : {}".format(data["result"]["color"])
                                brk += "\n• Lucky Time : {}".format(data["result"]["time"])
                                brk += "\n• Lucky Number : {}".format(data["result"]["number"])
                                brk += "\n• Public : {}".format(data["result"]["public"])
                                brk += "\n• Money : {}".format(data["result"]["money"])
                                brk += "\n• Love Couple : {}".format(data["result"]["love"]["couple"])
                                brk += "\n• Love Single : {}".format(data["result"]["love"]["single"])
                                cl.sendReplyMessage(msg.id,to, str(brk)) 

                        elif cmd.startswith('instagram '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              try:
                                  args = text.split(" ")
                                  userId = text.replace(args[0] + " ","")
                                  api = imjustgood(wait["apikey"])
                                  data = api.instagram(userId) 
                                  brk = "INSTAGRAM PROFILE"
                                  brk += "\n• Name : {}".format(data["result"]["fullname"])
                                  brk += "\n• User Name : {}".format(data["result"]["username"])
                                  brk += "\n• Follower : {}".format(data["result"]["follower"])
                                  brk += "\n• Following : {}".format(data["result"]["following"])
                                  brk += "\n• Insta Post : {}".format(data["result"]["post"])
                                  brk += "\n• Catagory : {}".format(data["result"]["business"]["category"])
                                  brk += "\n• Biography : {}".format(data["result"]["biography"])
                                  if data["result"]["lastpost"] != []:
                                      number  = 0
                                      brk += "\nLASTPOST"
                                      for a in data["result"]["lastpost"]:
                                          brk += "\n{}. {}".format(number, a["caption"])
                                          brk += "\n• Like : {}".format(a["like"])
                                          brk += "\n• Comment : {}".format(a["comment"])
                                          brk += "\n• Created : {}".format(a["created"])
                                  cl.sendReplyMessage(msg.id,to, str(brk))
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to,str(error))

                        elif cmd.startswith('google '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               args = text.split(" ")
                               userId = text.replace(args[0] + " ","")
                               api = imjustgood(wait["apikey"])
                               data = api.search(userId) 
                               number = 0
                               result = "GOOGLE SEARCH RESULT :"
                               for s in data["result"]:
                                   number += 1
                                   result += "\n{}. {}".format(number,s["title"])
                                   result += "\n{}".format(s["snippet"])
                                   result += "\n{}".format(s["url"])
                               cl.sendReplyMessage(msg.id,to, str(result))                  

                        elif cmd.startswith("ponsel"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                set = text.split(" ")
                                search = text.replace(set[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                data = api.cellular(search)
                                number = 0
                                brk = "SPESIFIKASI PONSEL\n"
                                for a in data["result"]:
                                    number += 1
                                    brk += "\n• {}. {}\n".format(number,a["brands"])
                                    brk += "\n• Release : {}".format(a["release"])
                                    brk += "\n• Chipset : {}".format(a["chipset"])
                                    brk += "\n• Screen : {}".format(a["screen"])
                                    brk += "\n• Battery : {}".format(a["battery"])
                                    brk += "\n• Display : {}".format(a["display"])
                                    brk += "\n• Ram : {}".format(a["ram"])
                                    brk += "\n• Storage : {}\n".format(a["storage"])
                                cl.sendReplyMessage(msg.id,to, str(brk)) 

                        elif cmd.startswith("cvp: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                sep = text.split(" ")
                                FckVeza = text.replace(sep[0] + " ","")
                                FckVezaGans = cl.getContact(sender)
                                cl.sendReplyMessage(msg.id,to, "Loading 3-5 mins")
                                pic = "http://dl.profile.line-cdn.net/{}".format(FckVezaGans.pictureStatus)
                                subprocess.getoutput('youtube-dl --format mp4 --output vp.mp4 {}'.format(FckVeza))
                                pict = cl.downloadFileURL(pic)
                                vids = "vp.mp4"
                                changeVideoAndPictureProfile(pict, vids)
                                cl.sendReplyMessage(msg.id,to, "Update Dual Profile Video ♪")
                                os.remove("vp.mp4")

                        elif 'https://vt.tiktok.com/' in msg.text:
                          if wait["selfbot"] == True:
                            if wait["tiktok"] == True:
                              try:
                                  spilt = msg.text.split(" ")
                                  txt = spilt
                                  no = 0 + 1
                                  no += 1
                                  data = "{}".format(str(len(txt)))
                                  c=ApCalculator()
                                  c.run('{} - 1'.format(data))
                                  kala = {"write":""}
                                  date = kala["write"] = c.lcd
                                  ang = kala["write"]
                                  hasil = int(ang)
                                  aturan = txt[hasil]
                                  api = BEAPI()
                                  res = api.tiktokPostV2(aturan)
                                  sendFlexVideo(to, res["result"]["download"])
                              except Exception as error:
                                  print(error)

                        elif 'https://youtu.be/' in msg.text:
                          if wait["selfbot"] == True:
                            if wait["yt"] == True:
                              try:
                                  spilt = msg.text.split(" ")
                                  txt = spilt
                                  no = 0 + 1
                                  no += 1
                                  data = "{}".format(str(len(txt)))
                                  c=ApCalculator()
                                  c.run('{} - 1'.format(data))
                                  kala = {"write":""}
                                  date = kala["write"] = c.lcd
                                  ang = kala["write"]
                                  hasil = int(ang)
                                  aturan = txt[hasil]
                                  api = BEAPI()
                                  res = api.youtubeDownloadUrl(aturan)
                                  cl.sendReplyMessage(msg.id,to, "{}".format(res["result"]["title"])) 
                                  sendFlexVideo(to, res["result"]["mp4"])
                              except Exception as error:
                                  print(error)

                        elif cmd.startswith("resi-sicepat:"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              try:
                                  memek = text.split(" ")
                                  ngewe = text.replace(memek[0] + " ","")
                                  api = BEAPI()
                                  kontol = api.trackingResi(ngewe,"sicepat")
                                  brk  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                  brk += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                  brk += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                  brk += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                  brk += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                  brk += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                  for a in kontol["result"]["manifest"]:
                                      brk += "\n\n{}".format(a["manifest_description"])
                                      brk += "\nJam : {}".format(a["manifest_time"])
                                      brk += "\nTanggal :{}".format(a["manifest_date"])
                                      brk += "\nTanggal :{}".format(a["city_name"])
                                  cl.sendReplyMessage(msg.id,to, str(brk)) 
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith("resi-pos:"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              try:
                                  memek = text.split(" ")
                                  ngewe = text.replace(memek[0] + " ","")
                                  api = BEAPI()
                                  kontol = api.trackingResi(ngewe,"pos")
                                  brk  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                  brk += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                  brk += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                  brk += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                  brk += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                  brk += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                  for a in kontol["result"]["manifest"]:
                                      brk += "\n\n{}".format(a["manifest_description"])
                                      brk += "\nJam : {}".format(a["manifest_time"])
                                      brk += "\nTanggal :{}".format(a["manifest_date"])
                                      brk += "\nTanggal :{}".format(a["city_name"])
                                  cl.sendReplyMessage(msg.id,to, str(brk)) 
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith("resi-rex:"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              try:
                                  memek = text.split(" ")
                                  ngewe = text.replace(memek[0] + " ","")
                                  api = BEAPI()
                                  kontol = api.trackingResi(ngewe,"rex")
                                  brk  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                  brk += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                  brk += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                  brk += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                  brk += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                  brk += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                  for a in kontol["result"]["manifest"]:
                                      brk += "\n\n{}".format(a["manifest_description"])
                                      brk += "\nJam : {}".format(a["manifest_time"])
                                      brk += "\nTanggal :{}".format(a["manifest_date"])
                                      brk += "\nTanggal :{}".format(a["city_name"])
                                  cl.sendReplyMessage(msg.id,to, str(brk)) 
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith("resi-jnt:"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              try:
                                  memek = text.split(" ")
                                  ngewe = text.replace(memek[0] + " ","")
                                  api = BEAPI()
                                  kontol = api.trackingResi(ngewe,"jnt")
                                  brk  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                  brk += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                  brk += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                  brk += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                  brk += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                  brk += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                  for a in kontol["result"]["manifest"]:
                                      brk += "\n\n{}".format(a["manifest_description"])
                                      brk += "\nJam : {}".format(a["manifest_time"])
                                      brk += "\nTanggal :{}".format(a["manifest_date"])
                                      brk += "\nTanggal :{}".format(a["city_name"])
                                  cl.sendReplyMessage(msg.id,to, str(brk)) 
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith("resi-ninja:"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              try:
                                  memek = text.split(" ")
                                  ngewe = text.replace(memek[0] + " ","")
                                  api = BEAPI()
                                  kontol = api.trackingResi(ngewe,"ninja")
                                  brk  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                  brk += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                  brk += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                  brk += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                  brk += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                  brk += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                  for a in kontol["result"]["manifest"]:
                                      brk += "\n\n{}".format(a["manifest_description"])
                                      brk += "\nJam : {}".format(a["manifest_time"])
                                      brk += "\nTanggal :{}".format(a["manifest_date"])
                                      brk += "\nTanggal :{}".format(a["city_name"])
                                  cl.sendReplyMessage(msg.id,to, str(brk)) 
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith("smuleprofile:"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                set = text.split(" ")
                                mod = text.replace(set[0] + " ","")
                                api = BEAPI()
                                kontol = api.smuleUser(mod)
                                pretyPrintJson(kontol)        

                        elif cmd.startswith("smule:"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                set = text.split(" ")
                                mod = text.replace(set[0] + " ","")
                                mode = mod.split("|")
                                search = str(mode[0])
                                api = BEAPI()
                                res = api.smulePerformance(search)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if len(mode) == 1:
                                    num = 0
                                    ret_ = "SMULE SONG LIST\n"
                                    for youtube in res["result"]:
                                        num += 1
                                        ret_ += "\n•{}. {}".format(str(num), str(youtube["title"]))
                                    ret_ += "\nEXAMPLE PLAY"
                                    ret_ += "\n{} | No urutuan di atas ".format(str(text))
                                    cl.sendReplyMessage(msg.id,to, str(ret_))
                                elif len(mode) == 2:
                                    num = int(mode[1])
                                    if num <= len(res["result"]):
                                        pixel = res["result"][num - 1]
                                        kontol = "DETAIL SMULE"
                                        kontol += "\n• Like : {}".format(pixel["stats"]["total_loves"])
                                        kontol += "\n• Gift : {}".format(pixel["stats"]["total_gifts"])
                                        kontol += "\n• Listens : {}".format(pixel["stats"]["total_listens"])
                                        kontol += "\n• Comment : {}".format(pixel["stats"]["total_comments"])
                                        kontol += "\n• Title : {}".format(pixel["title"])
                                        cl.sendReplyMessage(msg.id,to, str(kontol))
                                        if pixel['type'] == "audio":
                                            sendFlexAudio(to, "{}".format(pixel["media_url"]))
                                        else:
                                            sendFlexVideo(to, "{}".format(pixel["video_media_url"]))
                                                                                    
                        elif cmd.startswith("gnamegrup"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                  X = cl.getGroup(to)
                                  X.name = text.split(" ")
                                  cl.updateGroup(X)
                                  cl.sendReplyMessage(msg.id,to, str(X.name))
                                                               
                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              text_ = cmd.replace("spamtag ", "")
                              cond = text_.split(" ")
                              text = text_.replace(cond[0] + " ", "")
                              jml = int(cond[0])
                              if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                      if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                  for ls in lists:
                                      contact = cl.getContact(ls)
                                      text = text.replace("@{}".format(str(contact.displayName)),"")
                                  if "|" in text:
                                      cond = text.split("|")
                                      fm = cond[0]
                                      lm = cond[1]
                                  else:
                                      fm = ""
                                      lm = text
                                  for ls in lists:
                                      for x in range(jml):
                                          sendMention(to, ls, str(fm), str(lm))
                                  cl.sendReplyMessage(msg.id,to, "Mention {}\nWith amount {} tags ".format(str(len(lists)), str(jml)))
                                  return
                              else:
                                  cl.sendReplyMessage(msg.id,to, "Nothing user :v")
                                  return
                                    
                        elif cmd.startswith("call "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                group = cl.getGroup(to)
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    for var in range(0,500):                                        	
                                        cl.acquireGroupCallRoute(to)                                            
                                        members = [ls for ls in lists]
                                        cl.inviteIntoGroupCall(to, contactIds=members)
                                    try:
                                        cl.sendReplyMessage(msg.id,to, "Success 500 invite call group")
                                        break
                                    except Exception as error:
                                        cl.sendReplyMessage(msg.id,to, str(error))                     
                             
                        elif cmd.startswith("block "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.blockContact(ls)
                                cl.sendMention(msg.to, 'Block Contact By Mention\n• User : @!\n• Add to blocklist user',' ', [ls])
                                
                        elif cmd.startswith("scall "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              sep = text.split(" ")
                              num = int(sep[1])
                              try:                           
                                  if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                                      names = re.findall(r'@(\w+)', text)
                                      mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                      mentionees = mention['MENTIONEES']
                                      lists = []
                                      for mention in mentionees:
                                          if mention["M"] not in lists:
                                              lists.append(mention["M"])
                                      for ls in lists:
                                          for var in range(0,num):
                                              group = cl.getGroup(to)
                                              members = [ls]
                                              kunkun = cl.getContact("uccd11f359de903676aa3021f8095bd0f").displayName
                                              cl.acquireGroupCallRoute(to)
                                              cl.inviteIntoGroupCall(to, contactIds=members)
                                          cl.sendReplyMessage(msg.id,to, "Success Invite Groups Call")
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to, str(error))
                                                                                                             
                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                cl.sendReplyMessage(msg.id,to, "Changed to " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendReplyMessage(msg.id,to, "Changed to " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendReplyMessage(msg.id,to, str(e))
                                    else:
                                        cl.sendReplyMessage(msg.id,to, "Jumlah melebihi 1000")
        
                        elif cmd.startswith('pict '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               res = '╭───「 Picture Status 」'
                               no = 0
                               if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                                   mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                                   if len(mentions['MENTIONEES']) == 1:
                                       profile = cl.getContact(mentions['MENTIONEES'][0]['M'])
                                       if profile.pictureStatus:
                                           path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                                           cl.sendImageWithURL(to, path)
                                       else:
                                           cl.sendReplyMessage(msg.id,to, 'Failed steal picture status, user `%s` doesn\'t have a picture status' % profile.displayName)
                                
                        elif cmd.startswith('cover '):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               res = '╭───「 Picture Cover 」'
                               no = 0
                               if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                                   mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                                   if len(mentions['MENTIONEES']) == 1:
                                       mid = mentions['MENTIONEES'][0]['M']
                                       cover = cl.getProfileCoverURL(mid)
                                       cl.sendImageWithURL(to, cover)
                                   else:
                                       cl.sendReplyMessage(msg.id,to, 'Failed steal picture status, user `%s` doesn\'t have a picture status' % profile.displayName)
                                    
                        elif cmd.startswith("video "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:  
                              if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    if contact.videoProfile == None:
                                    	continue
                                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus + "/vp"
                                    cl.sendVideoWithURL(to, str(path))
                                                                            
                        elif cmd.startswith("name "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:  
                              if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.sendReplyMessage(msg.id,to, "{}".format(str(contact.displayName)))
                                    
                        elif cmd.startswith("bio "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:  
                              if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.sendReplyMessage(msg.id,to,"{}".format(str(contact.statusMessage)))
                                
                        elif cmd.startswith("addfriend "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:  
                              if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.findAndAddContactsByMid(ls)
                                cl.sendMention(msg.to, 'AddFriend By Mention\n• User : @!\n• Add to friendlist',' ', [ls])
                                
                        elif cmd.startswith("ulti "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:  
                              if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        cl.sendMention(msg.to, 'Sorry @!\n• I Kick Invite & Cancell',' ', [ls])
                                        cl.kickoutFromGroup(to, [ls])
                                        cl.inviteIntoGroup(to, [ls])
                                        cl.cancelGroupInvitation(to, [ls])
                                    except:
                                       cl.sendReplyMessage(msg.id,to,"Limited !")
      
                        elif cmd.startswith("invite "):
                            if wait["selfbot"] == True:
                                if msg._from in creator or msg._from in owner or msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:                                                                            
                                        try:      
                                            cl.findAndAddContactsByMid(target)
                                            cl.inviteIntoGroup(to,[target])                                             
                                            cl.sendMention(msg.to, 'Invite By Mention\n• User : @!\n• Succes Invite Target',' ', [target])
                                        except:
                                            cl.sendMention(msg.to, 'Status : Failed\n• User : @!\n• Sudah berada di room\nAtau pendingan room',' ', [target])

                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendReplyMessage(msg.id,to, "Invite {} Call Groups".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        cl.acquireGroupCallRoute(to)
                                        cl.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendReplyMessage(msg.id,to, str(e))
                                else:
                                    cl.sendReplyMessage(msg.id,to, "Jumlah melebihi batas")

                        elif cmd.startswith("spamcall "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                proses = text.split(" ")
                                strnum = text.replace(proses[0] + " ","")
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                cl.sendReplyMessage(msg.id,to, "Invite {} Call Groups".format(str(strnum)))
                                jumlah = int(strnum)
                                if jumlah <= 1000:
                                   for x in range(jumlah):
                                   	try:
                                           cl.acquireGroupCallRoute(to)
                                           cl.inviteIntoGroupCall(to, contactIds=members)
                                   	except Exception as e:
                                          cl.sendText(msg.to,str(e))

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif cmd.startswith("idline: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   sep = text.split(" ")
                                   kontoll = text.replace(sep[0] + " ","")
                                   memek = cl.findContactsByUserid(kontoll)
                                   if True:
                                       cl.sendReplyMessage(msg.id,to, "http://line.me/ti/p/~" + kontoll)
                                       cl.sendMessage(msg.to, None, contentMetadata={'mid': memek.mid}, contentType=13)
                               except:
                                   cl.sendReplyMessage(msg.id,to, "Invalid Line Id !")                                                       
#===========Protection============#
                        elif cmd.startswith("welcomemsg "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              brk = text.split(" ")
                              spl = text.replace(brk[0] + " ","")
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Sudah Aktif ♪"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Leave Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendReplyMessage(msg.id,to,"Welcome Enable ✓")
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Leave Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Leave Msg sudah tidak aktif"
                                    cl.sendReplyMessage(msg.id,to,"Welcome Disable ✓")

                                
                        elif cmd.startswith("leavemsg "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              brk = text.split(" ")
                              spl = text.replace(brk[0] + " ","")
                              if spl == 'on':
                                  if msg.to in leave:
                                       msgs = "Leave Msg sudah aktif"
                                  else:
                                       leave.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Leave Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendReplyMessage(msg.id,to, "Leave Msg Enable ✓")
                              elif spl == 'off':
                                    if msg.to in leave:
                                         leave.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Leave Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Leave Msg sudah tidak aktif"
                                    cl.sendReplyMessage(msg.id,to,"Leave Msg Disable ✓")

                        elif cmd.startswith("pro:"):
                            if wait["selfbot"] == True:
                              if msg._from in admin:
                                  separate = cmd.split(":")
                                  number = cmd.replace(separate[0] + ":","")
                                  groups = cl.getGroupIdsJoined()
                                  try:
                                      group = groups[int(number)-1]
                                      G = cl.getGroup(group)
                                      try:
                                          protectqr.append(G.id)
                                      except:
                                          protectqr.append(G.id)
                                      cl.sendReplyMessage(msg.id,to,"Success Protect : " + G.name)
                                  except Exception as error:
                                      cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith("pqr "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              brk = text.split(" ")
                              spl = text.replace(brk[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendReplyMessage(msg.id,to, "「Enable」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendReplyMessage(msg.id,to, "「Disable」\n" + msgs)

                        elif cmd.startswith("pkick "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              brk = text.split(" ")
                              spl = text.replace(brk[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendReplyMessage(msg.id,to, "「Enable」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendReplyMessage(msg.id,to,"「Disable」\n" + msgs)

                        elif cmd.startswith("pjoin "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              brk = text.split(" ")
                              spl = text.replace(brk[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendReplyMessage(msg.id,to,"「Enable」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendReplyMessage(msg.id,to,"「Disable」\n" + msgs)

                        elif cmd.startswith("pcancell "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              brk = text.split(" ")
                              spl = text.replace(brk[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendReplyMessage(msg.id,to,"「Enable」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendReplyMessage(msg.id,to,"「Disable」\n" + msgs)

                        elif cmd.startswith("pinvite "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              brk = text.split(" ")
                              spl = text.replace(brk[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect in : " +str(ginfo.name)
                                  cl.sendReplyMessage(msg.id,to,"Activated\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    cl.sendReplyMessage(msg.id,to,"「Disable」\n" + msgs)

                        elif cmd.startswith("maxpro "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              brk = text.split(" ")
                              spl = text.replace(brk[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Max protection enable "
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Max protection allready On"
                                  cl.sendReplyMessage(msg.id,to,"Type Protection\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Max protection Disable"
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Max protection allready disble"
                                    cl.sendReplyMessage(msg.id,to,"Type Protection\n" + msgs)

#===========KICKOUT============#

                        elif cmd.startswith(comd["kick"]):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           cl.sendMention(msg.to, 'Sorry @! i fuck your ass',' ', [target])
                                           cl.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif cmd.startswith("adminadd "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMention(msg.to, '@!\nAdd to user adminlist',' ', [target])
                                       except:
                                           pass

                        elif cmd.startswith("staffadd "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMention(msg.to, '@!\nAdd to user stafflist',' ', [target])
                                       except:
                                           pass

                        elif cmd.startswith("botadd "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           cl.sendMention(msg.to, '@!\nAdd to user botlist',' ', [target])
                                       except:
                                           pass

                        elif cmd.startswith("admindell "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Tuyul:
                                       try:
                                           admin.remove(target)
                                           cl.sendMention(msg.to, '@!\nAdmin has been deleted',' ', [target])
                                       except:
                                           pass

                        elif cmd.startswith("staffdell "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Tuyul:
                                       try:
                                           staff.remove(target)
                                           cl.sendMention(msg.to, '@!\nStaff has been deleted',' ', [target])
                                       except:
                                           pass

                        elif cmd.startswith("botdell "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Tuyul:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMention(msg.to, '@!\nBot has been deleted',' ', [target])
                                       except:
                                           pass
                                           
                        elif cmd == "admin:on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendReplyMessage(msg.id,to, "Send a Contact")

                        elif cmd == "admin:repeat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendReplyMessage(msg.id,to, "Send a Contact")

                        elif cmd == "staff:on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendReplyMessage(msg.id,to, "Send a Contact")

                        elif cmd == "staff:repeat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendReplyMessage(msg.id,to, "Send a Contact")

                        elif cmd == "bot:on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendReplyMessage(msg.id,to, "Send a Contact")

                        elif cmd == "bot:repeat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendReplyMessage(msg.id,to, "Send a Contact")

                        elif cmd == "refresh" or cmd == 'abort':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendReplyMessage(msg.id,to, "All command abort")

                        elif cmd == "contact admin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendReplyMessage(msg.id,to, "Notag Enable ✓")                          
                        elif cmd == "notag off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                cl.sendReplyMessage(msg.id,to, "Notag Disable ✓")
          
                        elif cmd == "callpm on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["call"] = True
                                cl.sendReplyMessage(msg.id,to, "Notife call pm enable")                          
                        elif cmd == "callpm off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["call"] = False
                                cl.sendReplyMessage(msg.id,to, "Notif call pm disable")
                  
                        elif cmd == "respon on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                temptag["respontag"] = True
                                cl.sendReplyMessage(msg.id,to, "Auto Respon Enable ✓")                          
                        elif cmd == "respon off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                temptag["respontag"] = False
                                cl.sendReplyMessage(msg.id,to, "Auto Respon Disable ✓")
                           
                        elif cmd == "autoread on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["autoRead"] = True
                                cl.sendReplyMessage(msg.id,to, "Auto Read Enable ✓")                            
                        elif cmd == "autoread off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["autoRead"] = False
                                cl.sendReplyMessage(msg.id,to, "Auto Read Disable ✓")

                        elif cmd == "contact on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendReplyMessage(msg.id,to, "Detail contact Enable ✓")                            
                        elif cmd == "contact off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendReplyMessage(msg.id,to, "Detail Contact Disable ✓")

                        elif cmd == "autotext on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autotext"] = True
                                cl.sendReplyMessage(msg.id,to, "Autotext Enable ✓")                           
                        elif cmd == "autotext off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autotext"] = False
                                cl.sendReplyMessage(msg.id,to, "Autotext Disable")

                        elif cmd == "autoblock on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                cl.sendReplyMessage(msg.id,to, "Auto Block Enable")
                            
                        elif cmd == "autoblock off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                cl.sendReplyMessage(msg.id,to, "Auto Block Disable")

                        elif cmd == "unsend on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = True
                                cl.sendReplyMessage(msg.id,to, "Unsend Chat Enable")                           
                        elif cmd == "unsend off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = False
                                cl.sendReplyMessage(msg.id,to, "Unsend Chat Disable")

                        elif cmd == "timeline on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = True
                                cl.sendReplyMessage(msg.id,to, "Detail Post Enable")                            
                        elif cmd == "timeline off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = False
                                cl.sendReplyMessage(msg.id,to, "Detail Post Disable")

                        elif cmd == "autojoin on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendReplyMessage(msg.id,to, "Auto Join Enable.")                          
                        elif cmd == "autojoin off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendReplyMessage(msg.id,to, "Auto Join Disable")

                        elif cmd == "autoleave on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendReplyMessage(msg.id,to, "Auto Leave Enable")                            
                        elif cmd == "autoleave off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendReplyMessage(msg.id,to, "Auto Leave Disable")

                        elif cmd == "autoadd on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendReplyMessage(msg.id,to, "Auto Add Enable")                          
                        elif cmd == "autoadd off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendReplyMessage(msg.id,to, "Auto Add Disable")

                        elif cmd == "sticker on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendReplyMessage(msg.id,to, "Detail Sticker On")                      
                        elif cmd == "sticker off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendReplyMessage(msg.id,to, "Detail sticker Off")
                                
                        elif cmd == "smule on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["smule"] = True
                                cl.sendReplyMessage(msg.id,to, "Smule url enable")                            
                        elif cmd == "smule off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["smule"] = False
                                cl.sendReplyMessage(msg.id,to, "Smule url disable")

                        elif cmd == "jointicket on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                cl.sendReplyMessage(msg.id,to, "Join Ticket On.")                            
                        elif cmd == "jointicket off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                cl.sendReplyMessage(msg.id,to, "Join Ticket Off.")
                                
                        elif cmd == "autolike on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["likeOn"] = True
                                cl.sendReplyMessage(msg.id,to, "Auto Like Enable.")                            
                        elif cmd == "autolike off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["likeOn"] = False
                                cl.sendReplyMessage(msg.id,to, "Auto like Disable.")                                
        
                        elif cmd == "salam on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["chat"] = True
                                cl.sendReplyMessage(msg.id,to, "Salam mgs text enable.")                                
                        elif cmd == "salam off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["chat"] = False
                                cl.sendReplyMessage(msg.id,to, "Salam mgs text disable.")                   
       
                        elif cmd == "yturl off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["yt"] = False
                                cl.sendReplyMessage(msg.id,to, "Youtube url disable.")
                        elif cmd == "yturl on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["yt"] = True
                                cl.sendReplyMessage(msg.id,to, "Youtube url enable.")       
      
                        elif cmd == "tiktokurl off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["tiktok"] = False
                                cl.sendReplyMessage(msg.id,to, "Tiktok url disable.")   
                        elif cmd == "tiktokurl on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["tiktok"] = True
                                cl.sendReplyMessage(msg.id,to, "Tiktok url enable.")       
                                          
                        elif cmd == "responcall on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["responGc"] = True
                                cl.sendReplyMessage(msg.id,to, "Notifed call enable")                                                     
                        elif cmd == "responcall off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["responGc"] = False
                                cl.sendReplyMessage(msg.id,to, "Notifed call disable")
                                                                                      
                        elif cmd == "sticker sider":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["AddstickerSider"]["status"] = True
                                cl.sendReplyMessage(msg.id,to, "Send a stickers ♪")
                            
                        elif cmd == "sticker tag":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["AddstickerTag"]["status"] = True
                                cl.sendReplyMessage(msg.id,to, "Send a stickers ♪")

                        elif cmd == "sticker pesan":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["AddstickerPesan"]["status"] = True
                                cl.sendReplyMessage(msg.id,to, "Send a stickers ♪")

                        elif cmd == "sticker welcome":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["AddstickerWelcome"]["status"] = True
                                cl.sendReplyMessage(msg.id,to, "Send a stickers ♪")

                        elif cmd == "sticker leave":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["AddstickerLeave"]["status"] = True
                                cl.sendReplyMessage(msg.id,to, "Send a stickers ♪")
       
                        elif cmd == comd["cban"]:
                          if wait["selfbot"] == True:  
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                   ret = "Blacklist Empty"
                                   cl.sendReplyMessage(msg.id,to, str(ret))
                              else:
                                   ret = "Cleared {} Blacklist".format(str(len(wait["blacklist"])))
                                   cl.sendReplyMessage(msg.id,to, str(ret))
                                   wait["blacklist"] = {}
                                   
                        elif "ass" in msg.text.lower():
                          if wait["selfbot"] == True:
                             if wait["chat"] == True:  
                                 cl.sendReplyMessage(msg.id,to, wait["salam"])
                    
#===========COMMAND BLACKLIST============#
                        elif cmd.startswith("talkban "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMention(msg.to, '@!\nAdd To Blacklist User',' ', [target])
                                       except:
                                           pass

                        elif cmd.startswith("untalkban "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMention(msg.to, '@!\nUnban Talklban User',' ', [target])
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendReplyMessage(msg.id,to, "Send a contact")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendReplyMessage(msg.id,to,"Send Contact")

                        elif cmd.startswith("ban "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMention(msg.to, '@!\nAdd To Blacklist User',' ', [target])
                                       except:
                                           pass

                        elif cmd.startswith("unban "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMention(msg.to, '@!\nUnban Blacklist User',' ', [target])
                                       except:
                                           pass

                        elif cmd == "ban:on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendReplyMessage(msg.id,to, "Send a contact")

                        elif cmd == "unban:on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendReplyMessage(msg.id,to, "Send a contact")

                        elif cmd == "banlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendReplyMessage(msg.id,to, "No Body Is Banned")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + "• " +cl.getContact(m_id).displayName + "\n"
                                cl.sendReplyMessage(msg.id,to, "BLACKLIST USER\n"+ma+"\n• %s Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendReplyMessage(msg.id,to, "No Body Is Banned")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + "• . " +cl.getContact(m_id).displayName + "\n"
                                cl.sendReplyMessage(msg.id,to, "TALKBAN LIST\n"+ma+"\n• %s Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendReplyMessage(msg.id,to, "No body is baned")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
#===========COMMAND SET============#
                        elif cmd.startswith("setpesan: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   wait["pesan"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setcomment: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   wait["comment"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "{}".format(str(key).lower()))

                                  
                        elif cmd.startswith("cmdspeed: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   comd["speed"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "{}".format(str(key).lower()))
                                  
                        elif cmd.startswith("cmdbye: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   comd["bye"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "{}".format(str(key).lower()))

                        elif cmd.startswith("cmdkick: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   comd["kick"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "{}".format(str(key).lower()))

                        elif cmd.startswith("cmdsider on: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   comd["siderOn"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "{}".format(str(key).lower()))

                        elif cmd.startswith("cmdsider off: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   comd["siderOff"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "{}".format(str(key).lower()))

                        elif cmd.startswith("cmdtagall: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   comd["tagall"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "{}".format(str(key).lower()))

                        elif cmd.startswith("cmdhelp: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   comd["help"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "{}".format(str(key).lower()))

                        elif cmd.startswith("cmdcban: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   comd["cban"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setrespon: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   wait["Respontag"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setcallpm: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   wait["callText"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setspam: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   Setmain["RAmessage1"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setunsend: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMessage(msg.id,to, "Failed..!!")
                               else:
                                   comd["unsend"] = str(key).lower()
                                   cl.sendReplyMessage(msg.id,to, "{}".format(str(key).lower()))

                        elif cmd == "cekpesan":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendReplyMessage(msg.id,to, "Pesan anda\n"+ str(wait["message"]))
                               
                        elif cmd == "cekwelcome":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendReplyMessage(msg.id,to, "Msg Welcome\n" + str(wait["welcome"]))
                               
                        elif cmd == "cekcomment":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendReplyMessage(msg.id,to, "Msg Comment\n" + str(wait["comment"]))                               

                        elif cmd == "cekrespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendReplyMessage(msg.id,to, "Msg Respon\n" + str(wait["Respontag"]))

                        elif cmd == "cekspam":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendReplyMessage(msg.id,to, "Msg Spam\n" + str(Setmain["RAmessage1"]))

                        elif cmd == "ceksider":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendReplyMessage(msg.id,to, "Msg Sider\n" + str(wait["mention"]))
                               
                        elif cmd == "cekcomment":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendReplyMessage(msg.id,to, "Msg Comment\n" + str(wait["comment"]))

                        elif cmd == "cekleave":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendReplyMessage(msg.id,to, "Msg Leave\n" + str(wait["leave"]))

                        elif cmd.startswith("lefft: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        cl.sendMessage(i, "Waitting for notifed success")
                                        cl.leaveGroup(i)
                                        cl.sendReplyMessage(msg.id,to, "Leave all group " +h)

                        elif msg.text.startswith("/kick "):
                          if wait["selfbot"] == True:
                          	if msg._from in owner or msg._from in admin:
                                  nk0 = msg.text.replace("/kick ","")
                                  nk1 = nk0.lstrip()
                                  nk2 = nk1.replace("@","")
                                  nk3 = nk2.rstrip()
                                  _name = nk3
                                  gs = cl.getGroup(msg.to)
                                  targets = []
                                  for s in gs.members:
                                      if _name in s.displayName:
                                          targets.append(s.mid)
                                  if targets == []:
                                    cl.sendMessage(msg.to,"target not found")
                                  lolz = 'simple.js gid={} token={} app={}'.format(to, cl.authToken, "DESKTOPMAC\t11.2.5\tMac_Os\t11.2.5")
                                  for target in targets:
                                      lolz += ' uid={}'.format(target)
                                  execute_js(lolz)

                        elif "/kill " in msg.text:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                pisah = text.split("/kill ")
                                nk0 = text.replace(pisah[0]+"/kill ","")
                                nk1 = nk0.lstrip()
                                _name = nk1
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for i in gs.members:
                                    if _name in i.displayName:
                                        targets.append(i.mid)
                                if targets == []:
                                  cl.sendMessage(msg.to,"target not found")
                                lolz = 'simple.js gid={} token={} app={}'.format(to, cl.authToken, "DESKTOPMAC\t11.2.5\tMac_Os\t11.2.5")
                                for target in targets:
                                    lolz += ' uid={}'.format(target)
                                execute_js(lolz)

                        elif cmd == "@cban":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
	                            xyz = cl.getGroup(to)
	                            mem = [c.mid for c in xyz.members]
	                            targets = []
	                            for x in mem:
	                              if x not in admin:targets.append(x)
	                            if targets:
	                              imnoob = 'simple.js gid={} token={} app={}'.format(to, cl.authToken, "CHROMEOS\t2.1.5\tDefrizal_OS\t1")
	                              for target in targets:
	                                imnoob += ' uid={}'.format(target)
	                              success = execute_js(imnoob)
	                              if success:cl.sendMessage(to, "Success kick %i members." % len(targets))
	                              else:cl.sendMessage(to, "Failed kick %i members." % len(targets))
	                            else:cl.sendMessage(to, "Target not found.")

                        elif cmd.startswith("bantai: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                separate = msg.text.split(":")
                                number = msg.text.replace(separate[0] + ":"," ")
                                groups = cl.getGroupIdsJoined()
                                gid = groups[int(number)-1]                             
                                xyz = cl.getGroup(gid)
                                if xyz.invitee == None:pends = []
                                else:pends = [c.mid for c in xyz.invitee]
                                targp = []
                                for x in pends:
                                  if x not in admin:targp.append(x)
                                mems = [c.mid for c in xyz.members]
                                targk = []
                                for x in mems:
                                  if x not in admin:targk.append(x)
                                lolz = 'dual.js gid={} token={}'.format(gid, cl.authToken)
                                for x in targp:lolz += ' uid={}'.format(x)
                                for x in targk:lolz += ' uik={}'.format(x)
                                execute_js(lolz)

                        elif cmd == "bypass":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                xyz = cl.getGroup(to)
                                if xyz.invitee == None:pends = []
                                else:pends = [c.mid for c in xyz.invitee]
                                targp = []
                                for x in pends:
                                  if x not in owner:targp.append(x)
                                mems = [c.mid for c in xyz.members]
                                targk = []
                                for x in mems:
                                  if x not in owner:targk.append(x)
                                lolz = 'dual.js gid={} token={}'.format(to, cl.authToken)
                                for x in targp:lolz += ' uid={}'.format(x)
                                for x in targk:lolz += ' uik={}'.format(x)
                                execute_js(lolz)

    except Exception as error:
        print (error)

for publicKey in cl.talk.getE2EEPublicKeys():
    cl.talk.removeE2EEPublicKey(publicKey)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                avs = threading.Thread(target=bot(op))
                avs.start()
                avs.join()
                oepoll.setRevision(op.revision)
    except Exception as e:
        pass
