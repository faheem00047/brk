# -*- coding: utf-8 -*-
### IMPORT MODUL ###
from BrkBots import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from BEAPI import BEAPI
from Liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from Brk.thrift.protocol import TCompactProtocol
from Brk.thrift.transport import THttpClient
from Brk.ttypes import LoginRequest
from multiprocessing import Pool
from threading import Thread
from time import sleep
from Naked.toolshed.shell import execute_js
from datetime import datetime
from datetime import timedelta, date
import livejson
import os, hashlib, hmac, base64, time,requests
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, pafy, urllib, urllib.parse

#====[ LOGIN DENGAN TOKEN PRIMERY ]==================================================
#vp = LINE("token",appName="ANDROIDLITE\t2.16.0\tAndroid OS\t6.0.1")
#====[ LOGIN DENGAN EMAIL ]==================================================
vp = LINE("brontakquis@gmail.com","cinta1")
vp.log("Mid : " + str(vp.profile.mid))
vp.log("Auth Token : " + str(vp.authToken))
vp.log("Timeline Token : " + str(vp.tl.channelAccessToken))
#======================================================
print("done running helper")
#======================================================
#vp = line
#line = vp
#======================================================
oepoll = OEPoll(vp)
#==================================
ABC = [vp]
Tuyulmid = vp.getProfile().mid
#======================================================
mid = vp.profile.mid
Tuyulmid = vp.profile.mid
#======================================================
vpProfile = vp.getProfile()
#======================================================
Bots = [Tuyulmid]
#======================================================
Creator = ["u88d17513551940a45746fefdba222eb9"]
Owner = ["u88d17513551940a45746fefdba222eb9"]
Admin = ["u88d17513551940a45746fefdba222eb9"]
Staff = ["u40a1e5c5fb3405cd1b2c1ca721af9d3b","uc019c475bb64a081ae7c151d4af82e3b"]
Tuyul = Creator + Owner + Admin + Staff + Bots
#======================================================
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)
premiumOpen = codecs.open("user.json","r","utf-8")
premium = json.load(premiumOpen)
javascriptOpen = codecs.open("userjs.json","r","utf-8")
javascript = json.load(javascriptOpen)
tokenOpen = codecs.open("toket.json","r","utf-8")
token = json.load(tokenOpen)
botStart = time.time()
#======================================================
msg_dict = {}
target = {}
bot1 = []
#======================================================
wait = {
    "protection":True,
    "limitkick":False,
}

db = {
    "rname":"!",
}

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

usr = {
    "caraLogin": """
CARA LOGIN SELFBOT
WAJIB AKTIFKAN NOTIF ROOM INI

1 .UNTUK LINE VERSI TERBARU
KETIK ─≽ Login sb
SIMPAN FOTO BARCODE YANG
KELUAR DARI BOT
LALU KLIK T'ULISAN ─≽ LOGIN HERE
KEMUDIN KLIK PINDAI CODE QR
LALU PILIH FOTO BARCODE
YANG TADI DI SIMPAN
DAN MASUKAN PIN CODE YANG MUNCUL
DI ATAS LAYAR HP KALIAN
DAN LOGIN SUKSES JIKA ADA NOTIF
DARI BOT

2. UNTUK LINE VERSI LAWAS/LAMA
KETIK ─≽ LOGIN SB
KLIK YANG BERTULISKAN ─≽ LOGIN HERE
LALU MASUKAN PIN CODE YANG MUNCUL
DI ATAS LAYAR HP KALIAN
DAN LOGIN SUKSES
JIKA ADA NOTIF DARI BOT

3. UNTUK YANG PERTAMA X BARU LOGIN
SETELAH LOGIN SUKSES 
KETIK ─≽ Allowliff 
UNTUK MENGAKTIFKAN TEMPLATE
""",
}

with open('owner.json', 'r') as fp:
    Owner = json.load(fp)
with open('admin.json', 'r') as fp:
    Admin = json.load(fp)
with open('staff.json', 'r') as fp:
    Staff = json.load(fp)
with open('bots.json', 'r') as fp:
    Bots = json.load(fp)
with open('user.json', 'r') as fp:
    premium = json.load(fp)
with open('userjs.json', 'r') as fp:
    javascript = json.load(fp)

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

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def restartBot():
    print ("Reboot data")
    backupData()
    time.sleep(1)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def getSHA256Sum(*args):
    instance = hashlib.sha256()
    for arg in args:
        if isinstance(arg, str):
            arg = arg.encode()
        instance.update(arg)
    return instance.digest()
def get_issued_at() -> bytes:
    return base64.b64encode(
        f"iat: {int(time.time()) * 60}\n".encode("utf-8")) + b"."
def get_issued_at_lite(mid: str,times) -> bytes:
    return base64.b64encode(
        f"issuedTo: {mid}\niat: {times}\n".encode("utf-8")) + b"." + base64.b64encode("type: YWT\nalg: HMAC_SHA1\n".encode("utf-8"))


def get_digest(key: bytes, iat: bytes) -> bytes:
    return base64.b64encode(hmac.new(key, iat, hashlib.sha1).digest())

def create_token(auth_key: str) -> str:
    mid, key = auth_key.partition(":")[::2]
    key = base64.b64decode(key.encode("utf-8"))
    iat = get_issued_at() #for ios
    #iat = get_issued_at_lite(mid,times) #For lite Token
    digest = get_digest(key, iat).decode("utf-8")
    iat = iat.decode("utf-8")
    return mid + ":" + iat + "." + digest

def logError(text):
    vp.log("ERROR 404 !\n" + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    

def pretyPrintJson(djson):
        print(json.dumps(djson, indent=4, sort_keys=True))

def allowLiff():
    url = 'https://access.line.me/dialog/api/permissions'
    data = {'on': ['P','CM'],'off': []}
    headers = {'X-Line-Access': vp.authToken,'X-Line-Application': vp.server.APP_NAME,'X-Line-ChannelId': '1602687308','Content-Type': 'application/json'}
    requests.post(url, json=data, headers=headers)

def sendFoter(to, text):
    data = {"type": "text","text": text,"sentBy": {"label": "❑ ᴀᴘᴋ-ʙᴏᴛꜱ ❑","iconUrl": "https://i.ibb.co/TrcSqCX/ezgif-com-gif-maker-8.png","linkUrl": "line://nv/profilePopup/mid=u35aa06efe8cfc198633554199261cc60"}}
    sendTemplate(to, data)

def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = vp.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

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

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Hai ".format(str(mid))
        arr = []
        no = 1
        num = 2
        for i in mid:
  #          ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["welcome"]#+"\nDigroup: "+str(ginfo.name)+"\n"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(vp.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        vp.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        vp.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def TagMembers(to, mids=[]):
    if Tuyulmid in mids: mids.remove(Tuyulmid)
    parsed_len = len(mids)//20+1
    result = '╭─── • MENTIONS •\n'
    mention = '@zeroxyuuki\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '├≽ %i• %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╰───⍣ βŘҜ-Ŧ€ΔΜ-βØŦŞ ⍣\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            vp.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
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
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                vp.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def restartBot():
    print ("Reboot data")
    backupData()
    time.sleep(1)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def proqr(grup):
    try:
        kontol = vp.getGroup(grup)
        kontol.preventedJoinByTicket = True
        vp.updateGroup(kontol)
    except:
        pass
    print("Notifed Update Group Qr")
 
def lockmem(grup, target):
    try:
        vp.findAndAddContactsByMid(target)
        vp.inviteIntoGroup(grup, [target])
    except:
        pass
    print("Notifed Protect Members")
 
def kickout(grup, target):
    try:
        vp.kickoutFromGroup(grup, [target])
    except:
        pass
    print("Notifed Kickout From Group")
  
def kickout2(grup, target):
    try:
        vp.kickoutFromGroup(grup, [target])
        vp.inviteIntoGroup(grup, Bots)
    except:
        pass
    print("Notifed Kickout From Group")
  

def invite(grup, target):
    try:
        vp.inviteIntoGroup(grup, Bots)
    except:
        pass
    print("Notifed Invite Group")
 
def antijs(grup, target):
   try:
       vp.inviteIntoGroup(grup, [Zmid])
   except:
       pass
   print("Notifed Invite Group")
 
def cancell(grup, target):
    try:
        vp.cancelGroupInvitation(grup, [target])
    except:
        pass
    print("Notifed Cancell Blacklist")
 
def joined(grup):
    try:
        vp.acceptGroupInvitation(grup)
    except:
        pass
    print("Notifed Join Groups") 
 
def black(target):
    if target not in settings["blacklist"]:
        settings["blacklist"][target] = True
    print("Notifed Blacklist")

def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = premium
        f = codecs.open('user.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = javascript
        f = codecs.open('userjs.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def bot(op):
    try:
        if op.type == 0:
            print ("APK-BOTS")
            return
#=========================================================   
        if op.type == 11 or op.type == 122:
            if op.param3 == '1':
                if op.param1 in settings["pname"]:
                    try:
                        G = vp.getGroup(op.param1)
                    except:
                        pass
                    G.name = settings["pro_name"][op.param1]
                    try:
                        vp.updateGroup(G)
                    except:
                        pass
                    if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in Owner and op.param2 not in Admin and op.param2 not in Staff and op.param2 not in Tuyul:
                        try:
                            h1 = threading.Thread(target=kickout, args=(op.param1, op.param2)).start()
                            h2 = threading.Thread(target=black, args=(op.param2,)).start()
                        except:
                            pass
                    
            if op.param1 in settings["picon"]:
                group = vp.getGroup(op.param1)
                try:
                    G = group.pictureStatus
                except:
                    pass
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in Owner and op.param2 not in Admin and op.param2 not in Staff and op.param2 not in Tuyul:
                    try:
                        h3 = threading.Thread(target=kickout, args=(op.param1, op.param2)).start()
                        h4 = threading.Thread(target=black, args=(op.param2,)).start()
                    except:
                        pass
 
            if op.param1 in settings["protqr"]:
                try:
                    if vp.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in Owner and op.param2 not in Admin and op.param2 not in Staff and op.param2 not in Tuyul:
                            vp.reissueGroupTicket(op.param1)
                            c1 = threading.Thread(target=proqr, args=(op.param1,)).start()
                            c2 = threading.Thread(target=kickout, args=(op.param1, op.param2)).start()
                            c3 = threading.Thread(target=black, args=(op.param2,)).start()
                except:
                    pass
                  
                return                                            
#========================================================= 
        if op.type == 13 or op.type == 124:
            if Tuyulmid in op.param3:
                if settings["autoJoin"] == True:
                    vp.acceptGroupInvitation(op.param1)                  
                    vp.sendMention(op.param1, 'Hallo @!\nThanks For Invite Me',' ', [op.param2])
                              
            if Tuyulmid in op.param3:
            	if settings["autoLeave"] == True:
                	vp.leaveGroup(op.param1)        
#=========================================================
        if op.type == 13 or op.type == 124:
            if op.param1 in settings["protinvite"]:
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in Owner and op.param2 not in Admin and op.param2 not in Staff and op.param2 not in Tuyul:
                    e1 = Thread(target=black, args=(op.param2,))
                    e1.start()
                    e1.join()
                    e2 = Thread(target=kickout, args=(op.param1, op.param2))
                    e2.start()
                    e2.join()
                    Inviter = op.param3.replace("",'\x1e')
                    InviterX = Inviter.split("\x1e")
                    for bantai in InviterX:
                        e3 = Thread(target=cancell, args=(op.param1, bantai))
                        e3.start()
                        e3.join()
#===========================================================                     
        if op.type == 17 or op.type == 130:
            if op.param1 in settings["welcomeMem"]:
                if op.param2 in Bots:
                    return                
                ginfo = vp.getGroup(op.param1)
                contact = vp.getContact(op.param2)
                image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                vp.sendImageWithURL(op.param1, image)                    
#=========================================================== 
        if op.type == 17 or op.type == 130:
            if op.param2 in settings["blacklist"]:
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in Owner and op.param2 not in Admin and op.param2 not in Staff and op.param2 not in Tuyul:
                    z1 = threading.Thread(target=proqr, args=(op.param1,)).start()
                    z2 = threading.Thread(target=kickout, args=(op.param1, op.param2)).start()
#===========================================================  
#===========================================================  
        if op.type == 19 or op.type == 133:     
            if op.param1 in settings["protkick"]:
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in Owner and op.param2 not in Admin and op.param2 not in Staff and op.param2 not in Tuyul:
                    u5 = threading.Thread(target=black, args=(op.param2,)).start()
                    u6 = threading.Thread(target=kickout, args=(op.param1, op.param2)).start()
                    u7 = threading.Thread(target=invite, args=(op.param1, op.param3)).start()
            if op.param3 in Creator:
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in Owner and op.param2 not in Admin and op.param2 not in Staff and op.param2 not in Tuyul:
                    u8 = threading.Thread(target=black, args=(op.param2,)).start()
                    u9 = threading.Thread(target=kickout, args=(op.param1, op.param2)).start()
                    u10 = threading.Thread(target=lockmem, args=(op.param1, op.param3)).start()
            if op.param3 in Owner:
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in Owner and op.param2 not in Admin and op.param2 not in Staff and op.param2 not in Tuyul:
                    d1 = threading.Thread(target=black, args=(op.param2,)).start()
                    d2 = threading.Thread(target=kickout, args=(op.param1, op.param2)).start()
                    d3 = threading.Thread(target=lockmem, args=(op.param1, op.param3)).start()
            if op.param3 in Admin:
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in Owner and op.param2 not in Admin and op.param2 not in Staff and op.param2 not in Tuyul:
                    d4 = threading.Thread(target=black, args=(op.param2,)).start()
                    d5 = threading.Thread(target=kickout, args=(op.param1, op.param2)).start()
                    d6 = threading.Thread(target=lockmem, args=(op.param1, op.param3)).start()
            if op.param3 in Staff:
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in Owner and op.param2 not in Admin and op.param2 not in Staff and op.param2 not in Tuyul:
                    d7 = threading.Thread(target=black, args=(op.param2,)).start()
                    d8 = threading.Thread(target=kickout, args=(op.param1, op.param2)).start()
                    d9 = threading.Thread(target=lockmem, args=(op.param1, op.param3)).start()
#=========================================================
        if op.type == 32 or op.type == 126:                    
            if op.param1 in settings["protcancel"]:
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in Owner and op.param2 not in Admin and op.param2 not in Staff and op.param2 not in Tuyul:
                    c3 = threading.Thread(target=black, args=(op.param2,)).start()
                    c4 = threading.Thread(target=kickout2, args=(op.param1, op.param2)).start()
#========================================================= 
        if op.type == 55:
            if op.param2 in settings["blacklist"]:
                fft = threading.Thread(target=kickout, args=(op.param1, op.param2)).start()   
                        
        if op.type == 26:
            msg = op.message
            if msg._from not in Bots and msg._from not in Creator and msg._from not in Admin and msg._from not in Staff and msg._from not in Owner:
                if msg._from in settings["blacklist"]:  
                    bah = threading.Thread(target=kickout, args=(op.param1, msg._from)).start() 
#=================================================================
        if op.type == 25 or op.type == 26:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
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
            setKey = settings["kunci"].title()
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
              if msg.toType == 0:
                if sender != vp.profile.mid:
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
              if msg.contentType == 13:
                if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                  if settings["addbots"] == True:
                      if msg.contentMetadata["mid"] in Bots:
                          vp.sendMessage(msg.to,"Sudah dalam daftar bots ♪")
                          settings["addbots"] = True
                      else:
                          Bots[msg.contentMetadata["mid"]] = True
                          f=codecs.open('bots.json','w','utf-8')
                          json.dump(Bots, f, sort_keys=True, indent=4,ensure_ascii=False)
                          settings["addbots"] = True
                          vp.sendMessage(msg.to,"daftar bots di tambahkan ♪")
                  if settings["dellbots"] == True:
                      if msg.contentMetadata["mid"] in Bots:
                          del Bots[msg.contentMetadata["mid"]]
                          f=codecs.open('bots.json','w','utf-8')
                          json.dump(Bots, f, sort_keys=True, indent=4,ensure_ascii=False)
                          vp.sendMessage(msg.to,"Bots berhasil di hapus ♪")
                      else:
                          settings["dellbots"] = True
                          vp.sendMessage(msg.to,"Failed ♪")
#ADD STAFF
#ᴏᴡɴᴇʀ
#ᴀᴅᴍɪɴ
#ꜱᴛᴀꜰꜰ
#ʙʟᴀᴄᴋʟɪꜱᴛ
                if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                  if settings["addstaff"] == True:
                      if msg.contentMetadata["mid"] in Staff:
                          vp.sendMessage(msg.to,"Sudah ada dalam daftar staff ♪")
                          settings["addstaff"] = True
                      else:
                          Staff[msg.contentMetadata["mid"]] = True
                          f=codecs.open('staff.json','w','utf-8')
                          json.dump(Staff, f, sort_keys=True, indent=4,ensure_ascii=False)
                          settings["addstaff"] = True
                          vp.sendMessage(msg.to,"Daftar staff di tambahkan ♪")
                  if settings["dellstaff"] == True:
                      if msg.contentMetadata["mid"] in Staff:
                          del Staff[msg.contentMetadata["mid"]]
                          f=codecs.open('staff.json','w','utf-8')
                          json.dump(Staff, f, sort_keys=True, indent=4,ensure_ascii=False)
                          vp.sendMessage(msg.to,"Daftar staff di hapus ♪")
                          settings["dellstaff"] = True
                      else:
                          settings["dellstaff"] = True
                          vp.sendMessage(msg.to,"Failed ♪")
#ADD ADMIN
                if msg._from in Creator or msg._from in Owner:
                  if settings["addadmin"] == True:
                      if msg.contentMetadata["mid"] in Admin:
                          vp.sendMessage(msg.to,"Sudah dalam daftar admin ♪")
                          settings["addadmin"] = True
                      else:
                          Admin[msg.contentMetadata["mid"]] = True
                          f=codecs.open('admin.json','w','utf-8')
                          json.dump(Admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                          settings["addadmin"] = True
                          vp.sendMessage(msg.to,"Daftar staff di tambahkan ♪")
                  if settings["delladmin"] == True:
                      if msg.contentMetadata["mid"] in Admin:
                          del Admin[msg.contentMetadata["mid"]]
                          f=codecs.open('admin.json','w','utf-8')
                          json.dump(Admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                          vp.sendMessage(msg.to,"Daftar admin di hapus ♪")
                      else:
                          settings["delladmin"] = True
                          vp.sendMessage(msg.to,"Failed ♪")
#ADD OWNER
                if msg._from in Creator or msg._from in Owner:
                  if settings["addowner"] == True:
                      if msg.contentMetadata["mid"] in Owner:
                          vp.sendMessage(msg.to,"Sudah dalam daftar owner♪")
                          settings["addowner"] = True
                      else:
                          Owner[msg.contentMetadata["mid"]] = True
                          f=codecs.open('owner.json','w','utf-8')
                          json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                          settings["addowner"] = True
                          vp.sendMessage(msg.to,"Daftar owner di tambahkan ♪")
                  if settings["dellowner"] == True:
                      if msg.contentMetadata["mid"] in Owner:
                          del Owner[msg.contentMetadata["mid"]]
                          f=codecs.open('owner.json','w','utf-8')
                          json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                          vp.sendMessage(msg.to,"Daftar owner di hapus ♪")
                      else:
                          settings["dellowner"] = True
                          vp.sendMessage(msg.to,"Failed ♪")
#ADD BLACKLIST
                if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                  if settings["wblacklist"] == True:
                      if msg.contentMetadata["mid"] in settings["blacklist"]:
                          vp.sendMessage(msg.to,"Sudah dalam daftar blacklist ♪")
                          settings["wblacklist"] = True
                          with open('temp.json', 'w') as fp:
                              json.dump(settings, fp, sort_keys=True, indent=4)
                      else:
                          settings["blacklist"][msg.contentMetadata["mid"]] = True
                          settings["wblacklist"] = True
                          with open('temp.json', 'w') as fp:
                              json.dump(settings, fp, sort_keys=True, indent=4)
                          vp.sendMessage(msg.to,"Blacklist di tambahkan ♪")
                  if settings["dblacklist"] == True:
                      if msg.contentMetadata["mid"] in settings["blacklist"]:
                          del settings["blacklist"][msg.contentMetadata["mid"]]
                          vp.sendMessage(msg.to,"Blacklist di hapus ♪")
                      else:
                          settings["dblacklist"] = True
                          with open('temp.json', 'w') as fp:
                              json.dump(settings, fp, sort_keys=True, indent=4)
                          vp.sendMessage(msg.to,"Failed ♪")
               
        if op.type == 46:
            if op.param2 in Bots:
                vp.removeAllMessages()
                                               
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            setKey = settings["kunci"].title()
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               if msg.toType == 2:
                    to = receiver
            if msg.toType == 2:
              if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                  if settings["groupPicture"] == True:
                      path = vp.downloadObjectMsg(msg_id)
                      settings["groupPicture"] = False
                      vp.updateGroupPicture(msg.to, path)
                      vp.sendMessage(msg.to, "Changed group picture ♪")

            if msg.contentType == 1:
              if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                if settings["Picture"] == True:
                    path = vp.downloadObjectMsg(msg.id)
                    settings["Picture"] = False
                    vp.updateProfilePicture(path)
                    vp.sendMessage(msg.to, "Changed picture profile ♪")
 
            if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                if msg.toType == 0:
                    if settings["autoRead"] == True:
                        vp.sendChatChecked(to, msg_id)
                if msg.toType == 2:
                    if settings["autoRead1"] == True:
                        vp.sendChatChecked(to, msg_id)
              
            if msg.contentType == 0:
                if text is None:
                    return
                        
                if text.lower() == ""+db["rname"]+"help":
                  if settings["selfbot"] == True:
                        ret = "╭─── • USER HELP • ───\n"
                        ret += "├ • Cara login\n"
                        ret += "├ • Login sb\n"
                        ret += "├ • Login js\n"
                        ret += "├ • Logout sb\n"
                        ret += "├ • Logout js\n"
                        ret += "├ • Restart sb\n"
                        ret += "├── • PUBLIK KEY • ──\n"
                        ret += "├ • " +db["rname"]+ "ct:(token)\n"
                        ret += "├ • " +db["rname"]+ "ct2:(token)\n"
                        ret += "├ • " +db["rname"]+ "tag\n"
                        ret += "├ • " +db["rname"]+ "liff\n"
                        ret += "├ • " +db["rname"]+ "mid\n"
                        ret += "├ • " +db["rname"]+ "cek (mid)\n"
                        ret += "├ • " +db["rname"]+ "header\n"
                        ret += "├ • " +db["rname"]+ "simi (quest)\n"
                        ret += "├ • " +db["rname"]+ "smule: (id)\n"
                        ret += "├ • " +db["rname"]+ "musik: (title)\n"
                        ret += "├ • " +db["rname"]+ "tokenlist\n"
                        ret += "├ • " +db["rname"]+ "tr-english (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-indo (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-jawa (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-sunda (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-itali (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-spain (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-francis (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-chinese (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-rusia (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-vietname (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-malay (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-korea (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-japan (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-thai (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-turki (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-filipin (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-arab (txt)\n"
                        ret += "├ • " +db["rname"]+ "tr-indi (txt)\n"
                        ret += "│RNAME : {}\n".format(db["rname"])
                        ret += "├ • " +db["rname"]+ "admin help (admin only)\n"
                        ret += "╰── • βŘҜ-Ŧ€ΔΜ-βØŦŞ • ──"
                        vp.sendReplyMessage(msg.id,to, str(ret))
                        
                elif text.lower() == ""+db["rname"]+"admin help":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        ret = "╭────────────────\n"
                        ret += "├─❑≽ FOR ADMIN HELP •\n"
                        ret += "├≽ " +db["rname"]+ "exec (cmd)\n"
                        ret += "├≽ " +db["rname"]+ "addself (name @)\n"
                        ret += "├≽ " +db["rname"]+ "addjs (name @)\n"
                        ret += "├≽ " +db["rname"]+ "Addme (name)\n"
                        ret += "├≽ " +db["rname"]+ "Addmejs (name)\n"
                        ret += "├≽ " +db["rname"]+ "delusersb (no name)\n"
                        ret += "├≽ " +db["rname"]+ "deluserjs (no name)\n"
                        ret += "├≽ " +db["rname"]+ "delself (@)\n"
                        ret += "├≽ " +db["rname"]+ "deljs: (@)\n"
                        ret += "├≽ " +db["rname"]+ "list user:\n"
                        ret += "├≽ " +db["rname"]+ "list user js\n"
                        ret += "├≽ " +db["rname"]+ "screen -ls\n"
                        ret += "├≽ " +db["rname"]+ "kill (user name)\n"
                        ret += "├≽ " +db["rname"]+ "remove (user name)\n"
                        ret += "├≽ " +db["rname"]+ "killmid (mid)\n"
                        ret += "├≽ " +db["rname"]+ "chatbot on/off\n"
                        ret += "├≽ " +db["rname"]+ "vbye\n"
                        ret += "├≽ " +db["rname"]+ "glist\n"
                        ret += "├≽ " +db["rname"]+ "settings\n"
                        ret += "├≽ " +db["rname"]+ "friendlist\n"
                        ret += "├≽ " +db["rname"]+ "abort\n"
                        ret += "├≽ " +db["rname"]+ "ready\n"
                        ret += "├≽ " +db["rname"]+ "runtime\n"
                        ret += "├≽ " +db["rname"]+ "speed\n"
                        ret += "├≽ " +db["rname"]+ "reboot\n"
                        ret += "├≽ " +db["rname"]+ "rechat\n"
                        ret += "├≽ " +db["rname"]+ "errorlog\n"
                        ret += "├≽ " +db["rname"]+ "allowliff\n"
                        ret += "├≽ " +db["rname"]+ "bye: (numb)\n"
                        ret += "├≽ " +db["rname"]+ "inviteto (numb)\n"
                        ret += "├≽ " +db["rname"]+ "openqr: (numb)\n"
                        ret += "├≽ " +db["rname"]+ "closeqr: (numb)\n"
                        ret += "├≽ " +db["rname"]+ "cname: (name)\n"
                        ret += "├≽ " +db["rname"]+ "cbio: (txt)\n"
                        ret += "├≽ " +db["rname"]+ "uppict on/off\n"
                        ret += "├≽ " +db["rname"]+ "setrname: (txt)\n"
                        ret += "├─❑≽ PROMOTE OR DEMOTE •\n"
                        ret += "├≽ " +db["rname"]+ "ownerlis\n"
                        ret += "├≽ " +db["rname"]+ "adminlist\n"
                        ret += "├≽ " +db["rname"]+ "adminadd (@)\n"
                        ret += "├≽ " +db["rname"]+ "admindell (@)\n"
                        ret += "├≽ " +db["rname"]+ "owneradd (@)\n"
                        ret += "├≽ " +db["rname"]+ "ownerdell (@)\n"
                        ret += "├≽ " +db["rname"]+ "kick (@)\n"
                        ret += "├≽ " +db["rname"]+ "ban (@)\n"
                        ret += "├≽ " +db["rname"]+ "unban (@)\n"
                        ret += "├≽ " +db["rname"]+ "owner:add\n"
                        ret += "├≽ " +db["rname"]+ "owner:dell\n"
                        ret += "├≽ " +db["rname"]+ "admin:add\n"
                        ret += "├≽ " +db["rname"]+ "admin:dell\n"
                        ret += "├─❑≽ PROTECTION ROOM •\n"
                        ret += "├≽ " +db["rname"]+ "pro on/off\n"
                        ret += "├≽ " +db["rname"]+ "proinv on/off\n"
                        ret += "├≽ " +db["rname"]+ "procancel on/off\n"
                        ret += "├≽ " +db["rname"]+ "prokick on/off\n"
                        ret += "├≽ " +db["rname"]+ "iconlock on/off\n"
                        ret += "├≽ " +db["rname"]+ "namelock on/off\n"
                        ret += "├≽ " +db["rname"]+ "protectlist\n"
                        ret += "├≽ " +db["rname"]+ "clearprotect\n"
                        ret += "├≽ " +db["rname"]+ "banlist\n"
                        ret += "├≽ " +db["rname"]+ "cban\n"
                        ret += "├────❑≽ JAVA SCRIPT •\n"
                        ret += "├≽ " +db["rname"]+ "boom\n"
                        ret += "├≽ " +db["rname"]+ "mayhem\n"
                        ret += "├≽ " +db["rname"]+ "bypass: (number)\n"
                        ret += "├≽ !kickname (name)\n"
                        ret += "├≽ !kicklist (@)\n"
                        ret += "├────❑≽ SETTINGS •\n"
                        ret += "├≽ " +db["rname"]+ "autojoin on/off\n"
                        ret += "├≽ " +db["rname"]+ "autoread on/off\n"
                        ret += "├≽ " +db["rname"]+ "autoleave on/off\n"
                        ret += "├≽ " +db["rname"]+ "autojointicket on/off\n"
                        ret += "│RNAME : {}\n".format(db["rname"])
                        ret += "╰────────────────"
                        vp.sendReplyMessage(msg.id,to, str(ret))
                    else:
                        if msg._from not in Creator and msg._from not in Owner and msg._from not in Admin:
                            vp.sendMention(msg.to, 'STATUS : FAILED\n• Sorry : @!\n• Your not in ownerlist',' ', [msg._from])
  
                elif text.lower() == ""+db["rname"]+"tokenlist":
                    brk = "╭─────────────\n"
                    brk += "├─≽ TOKEN LIST\n"
                    brk += "│ 1• Ios-Ipad\n"
                    brk += "│ 2• Chrome\n"
                    brk += "│ 3• Desktopmac\n"
                    brk += "│ 4• Desktopwin\n"
                    brk += "├─≽ Example Get\n"
                    brk += "│ • {}token (number)\n".format(db["rname"])
                    brk += "│ • βŘҜ-Ŧ€ΔΜ-βØŦŞ\n"
                    brk += "╰─────────────\n"
                    vp.sendReplyMessage(msg.id,to, str(brk))  
  
                elif text.lower() == "mid":
                    vp.sendReplyMessage(msg.id,to, msg._from)

                elif text.lower() == ""+db["rname"]+"liff":
                    vp.sendReplyMessage(msg.id,to, "•> Login Liff & Allow <•\n• line://app/1602687308-GXq4Vvk9")

                elif text.startswith(""+db["rname"]+"cek "):
                    separate = msg.text.split(" ")
                    mid = msg.text.replace(separate[0] + " ","")
                    if mid is not None:
                        listMid = mid.split("*")
                        if len(listMid) > 1:
                            for a in listMid:
                                vp.sendContact(to,a)
                        else:
                            vp.sendContact(to,mid)  

                elif text.lower() == ""+db["rname"]+"header":
                    api = BEAPI()
                    data = api.lineAppname()
                    brk = "APPNAME HEADER"
                    brk += "\n   • Android : {}".format(data["result"]["android"])
                    brk += "\n   • Androidlite : {}".format(data["result"]["androidlite"])
                    brk += "\n   • Chromeos : {}".format(data["result"]["chromeos"])
                    brk += "\n   • Desktopmac : {}".format(data["result"]["desktopmac"])
                    brk += "\n   • Desktopwin : {}".format(data["result"]["desktopwin"])
                    brk += "\n   • Ios : {}".format(data["result"]["ios"])
                    brk += "\n   • Iosipad : {}".format(data["result"]["iosipad"])
                    brk += "\nLAST UPDATE : {}".format(data["result"]["lastUpdate"])
                    vp.sendReplyMessage(msg.id,to, str(brk))

                elif text.startswith(""+db["rname"]+"tr-english "):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("en", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-indo "):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("id", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-arab "):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("ar", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-indi "):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("hi", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-chinese "):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("zh-CN", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-vietnam "):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("vi", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-turki "):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("tr", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-thai "):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("th", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-turki "):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("tr", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-filipin"):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("tl", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-sunda"):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("su", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-rusia"):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("ru", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-malay"):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("ms", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-korea"):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("ko", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-jawa"):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("jw", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-japan"):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("ja", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-itali"):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("it", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-spain"):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("es", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-francis"):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("fr", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"tr-german"):
                   args = text.split(" ")
                   userId = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.googleTranslate("gr", userId)
                   vp.sendReplyMessage(msg.id,to, "{}".format(data["result"]["trans"]))
                elif text.startswith(""+db["rname"]+"simi "):
                   args = text.split(" ")
                   search = text.replace(args[0] + " ","")
                   api = BEAPI()
                   data = api.simiSimi("id", search)
                   brk = data["result"]
                   vp.sendReplyMessage(msg.id,to, str(brk))

                elif text.startswith(""+db["rname"]+"musik:"):
                        set = text.split(" ")
                        mod = text.replace(set[0] + " ","")
                        mode = mod.split("|")
                        search = str(mode[0])
                        api = BEAPI()
                        res = api.jooxSearch(search)
                        if len(mode) == 1:
                            num = 0
                            ret_ = "╭─「 🎵 MUSIC 🎵」\n"
                            for youtube in res["result"]:
                                num += 1
                                ret_ += "\n├≽{}. {}".format(str(num), str(youtube["msong"]))
                            ret_ += "\n╰─「βŘҜ-Ŧ€ΔΜ-βØŦŞ」"
                            ret_ += "\nUsage 👇\n Ketik {} | No urutuan di atas ".format(str(text))
                            vp.sendReplyMessage(msg.id,to, str(ret_))
                        elif len(mode) == 2:
                            num = int(mode[1])
                            if num <= len(res["result"]):
                                pixel = res["result"] [num - 1]
                                hasil = "Artist: {}\n".format(pixel["msinger"])
                                hasil += "Judul: {}\n".format(pixel["msong"])
                                hasil += "Album: {}\n".format(pixel["malbum"])
                                hasil += "Created: {}\n".format(pixel["public_time"])
                                brk = "{}".format(pixel["mp3Url"])
                                img = "{}".format(pixel["imgSrc"])
                            vp.sendReplyMessage(msg.id,to, str(hasil))
                            vp.sendImageWithURL(to, str(img))
                            sendFlexAudio(to, str(brk))

                elif text.startswith(""+db["rname"]+"smule:"):
                        set = text.split(" ")
                        mod = text.replace(set[0] + " ","")
                        mode = mod.split("|")
                        search = str(mode[0])
                        api = BEAPI()
                        res = api.smulePerformance(search)
                        if len(mode) == 1:
                            num = 0
                            ret_ = "SEMULE PERFORMANCE\n"
                            for youtube in res["result"]:
                                num += 1
                                ret_ += "\n    •{}. {}".format(str(num), str(youtube["title"]))
                            ret_ += "\nEXAMPLE PLAY👇"
                            ret_ += "\nKetik {} | No urutuan di atas ".format(str(text))
                            vp.sendReplyMessage(msg.id,to, str(ret_))
                        elif len(mode) == 2:
                            num = int(mode[1])
                            if num <= len(res["result"]):
                                pixel = res["result"] [num - 1]
                                hasil = "Id Smule: {}\n".format(pixel["performed_by"])
                                hasil += "Gift: {}\n".format(pixel["stats"]["total_gifts"])
                                hasil += "Diputar: {}\n".format(pixel["stats"]["total_listens"])
                                hasil += "Disukai: {}\n".format(pixel["stats"]["total_loves"])
                                hasil += "Song: {}".format(pixel["title"])
                                songs = "{}\n".format(pixel["media_url"])
                                songvid = "{}\n".format(pixel["video_media_url"])
                            vp.sendReplyMessage(msg.id,to, str(hasil))
                            if pixel['type'] == "audio":
                                sendFlexAudio(to, str(songs))
                            else:
                                sendFlexVideo(to, str(songvid))

                elif text.lower() == ""+db["rname"]+"token 3":
                    try:
                        api = BEAPI()
                        qr = api.lineGetQr("DESKTOPMAC\t7.3.1\tMacOs\t11.6.0")
                        vp.sendReplyMessage(msg.id,to, "Please login 30 secs:\n{}".format(qr["result"]["qrlink"]))
                        vp.sendImageWithURL(to,"{}".format(qr["result"]["qrcode"]))
                        pincode = api.lineGetQrPincode(qr["result"]["session"])
                        vp.sendMessage(msg.to, "Pincode: {}".format(pincode["result"]["pincode"]))
                        auth = api.lineGetQrAuth(qr["result"]["session"])
                        memek = "Your Token:\n{}".format(auth["result"]["accessToken"])
                        memek += "\nYour Cert:\n{}".format(auth["result"]["certificate"])
                        vp.sendReplyMessage(msg.id,to, str(memek))                    
                    except:
                        vp.sendMention(msg.to, 'Connection Timeout\n• Sorry : @!\n• Your code qr expired',' ', [msg._from])
                elif text.lower() == ""+db["rname"]+"token 2":
                    try:
                        api = BEAPI()
                        qr = api.lineGetQr("CHROMEOS\t2.4.7\tChromeOS\t1")
                        vp.sendReplyMessage(msg.id,to, "Please login 30 secs:\n{}".format(qr["result"]["qrlink"]))
                        vp.sendImageWithURL(to,"{}".format(qr["result"]["qrcode"]))
                        pincode = api.lineGetQrPincode(qr["result"]["session"])
                        vp.sendMessage(msg.to, "Pincode: {}".format(pincode["result"]["pincode"]))
                        auth = api.lineGetQrAuth(qr["result"]["session"])
                        memek = "Your Token:\n{}".format(auth["result"]["accessToken"])
                        memek += "\nYour Cert:\n{}".format(auth["result"]["certificate"])
                        vp.sendReplyMessage(msg.id,to, str(memek))
                    except:
                        vp.sendMention(msg.to, 'Connection Timeout\n• Sorry : @!\n• Your code qr expired',' ', [msg._from])
                elif text.lower() == ""+db["rname"]+"token 1":
                    try:
                        api = BEAPI()
                        qr = api.lineGetQr("IOSIPAD\t11.19.0\tIphoneX\t14")
                        vp.sendReplyMessage(msg.id,to, "Please login 30 secs:\n{}".format(qr["result"]["qrlink"]))
                        vp.sendImageWithURL(to,"{}".format(qr["result"]["qrcode"]))
                        pincode = api.lineGetQrPincode(qr["result"]["session"])
                        vp.sendMessage(msg.to, "Pincode: {}".format(pincode["result"]["pincode"]))
                        auth = api.lineGetQrAuth(qr["result"]["session"])
                        memek = "Your Token:\n{}".format(auth["result"]["accessToken"])
                        memek += "\nYour Cert:\n{}".format(auth["result"]["certificate"])
                        vp.sendReplyMessage(msg.id,to, str(memek))
                    except:
                        vp.sendMention(msg.to, 'Connection Timeout\n• Sorry : @!\n• Your code qr expired',' ', [msg._from])
                elif text.lower() == ""+db["rname"]+"token 4":
                    try:
                        api = BEAPI()
                        qr = api.lineGetQr("DESKTOPWIN\t7.3.1\tWindows\t10")
                        vp.sendReplyMessage(msg.id,to, "Please login 30 secs:\n{}".format(qr["result"]["qrlink"]))
                        vp.sendImageWithURL(to,"{}".format(qr["result"]["qrcode"]))
                        pincode = api.lineGetQrPincode(qr["result"]["session"])
                        vp.sendMessage(msg.to, "Pincode: {}".format(pincode["result"]["pincode"]))
                        auth = api.lineGetQrAuth(qr["result"]["session"])
                        memek = "Your Token:\n{}".format(auth["result"]["accessToken"])
                        memek += "\nYour Cert:\n{}".format(auth["result"]["certificate"])
                        vp.sendReplyMessage(msg.id,to, str(memek))
                    except:
                        vp.sendMention(msg.to, 'Connection Timeout\n• Sorry : @!\n• Your code qr expired',' ', [msg._from])
  
                elif text.lower() == ""+db["rname"]+"tag":
                    members = []
                    if msg.toType == 1:
                        room = vp.getCompactRoom(to)
                        members = [mem.mid for mem in room.contacts]
                    elif msg.toType == 2:
                        group = vp.getCompactGroup(to)
                        members = [mem.mid for mem in group.members]
                    else:
                        return vp.sendMessage(to, 'Failed mentionall members, use this command only on room or group chat')
                    if members:
                        TagMembers(to, members)                        
 
                elif text.startswith(""+db["rname"]+"kill"):
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                       args = text.split(" ")
                       brkbots = text.replace(args[0] + " ","")
                       os.system("screen -S {} -X quit".format(str(brkbots)))
                       os.system('rm -rf {}'.format(str(vp)))
                       time.sleep(2)
                       vp.sendReplyMessage(msg.id,to, 'Screen {} has been killed'.format(brkbots))                                     
    
#==================================================================

                elif text.startswith(""+db["rname"]+"killmid"):
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                       sep = text.split(" ")
                       midn = text.replace(sep[0] + " ","")
                       hmm = text.lower()
                       G = vp.getGroup(msg.to)
                       members = [G.mid for G in G.members]
                       targets = []
                       for x in members:
                           contact = cl.getContact(x)
                           msg = op.message
                           testt = contact.displayName.lower()
                           if midn in testt:targets.append(contact.mid)
                       if targets == []:return cl.sendMessage(to,"not found name "+midn)
                       for target in targets:
                           vp.kickoutFromGroup(msg.to,[target])

                elif text.startswith(""+db["rname"]+"exec"):
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        try:
                            anu = msg.text.split("\n")
                            anu2 = msg.text.replace(anu[0] + "\n","")
                            exec(anu2)
                        except Exception as e:
                            vp.sendReplyMessage(msg.id,to, str(e))        

                elif text.startswith("!kicklist "):
                	if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                                nk0 = cmd.replace("!kicklist ","")
                                nk1 = nk0.lstrip()
                                nk2 = nk1.replace("@","")
                                nk3 = nk2.rstrip()
                                _name = nk3
                                gs = vp.getGroup(msg.to)
                                targets = []
                                for s in gs.members:
                                    if _name in s.displayName:
                                        targets.append(s.mid)
                                if targets == []:
                                  cl.sendMessage(msg.to,"target not found")
                                lolz = 'simple.js gid={} token={} app={}'.format(to, vp.authToken, "DESKTOPMAC\t11.2.5\tMac_Os\t11.2.5")
                                for target in targets:
                                    lolz += ' uid={}'.format(target)
                                success = execute_js(lolz)

                elif text.lower() == ""+db["rname"]+"mayhem":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        xyz = vp.getGroup(to)
                        mem = [c.mid for c in xyz.members]
                        targets = []
                        for x in mem:
                          if x not in admin:targets.append(x)
                        if targets:
                          lolz = 'simple.js gid={} token={} app={}'.format(to, vp.authToken)
                          for target in targets:
                            lolz += ' uid={}'.format(target)
                          success = execute_js(lolz)
                          if success:vp.sendMessage(to, "Cleanse %i members." % len(targets))
                          else:vp.sendMessage(to, "Failed kick %i members." % len(targets))
                        else:vp.sendMessage(to, "Target not found.")

                elif text.lower() == ""+db["rname"]+"boom":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        xyz = vp.getGroup(to)
                        if xyz.invitee == None:pends = []
                        else:pends = [c.mid for c in xyz.invitee]
                        targp = []
                        for x in pends:
                          if x not in Owner:targp.append(x)
                        mems = [c.mid for c in xyz.members]
                        targk = []
                        for x in mems:
                          if x not in Owner:targk.append(x)
                        lolz = 'dual.js gid={} token={}'.format(to, vp.authToken)
                        for x in targp:lolz += ' uid={}'.format(x)
                        for x in targk:lolz += ' uik={}'.format(x)
                        execute_js(lolz)

                elif text.startswith(""+db["rname"]+"bypass:"):
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        separate = msg.text.split(":")
                        number = msg.text.replace(separate[0] + ":"," ")
                        groups = vp.getGroupIdsJoined()
                        gid = groups[int(number)-1]                             
                        xyz = vp.getGroup(gid)
                        if xyz.invitee == None:pends = []
                        else:pends = [c.mid for c in xyz.invitee]
                        targp = []
                        for x in pends:
                          if x not in Owner:targp.append(x)
                        mems = [c.mid for c in xyz.members]
                        targk = []
                        for x in mems:
                          if x not in Owner:targk.append(x)
                        lolz = 'dual.js gid={} token={}'.format(gid, vp.authToken)
                        for x in targp:lolz += ' uid={}'.format(x)
                        for x in targk:lolz += ' uik={}'.format(x)
                        succes = execute_js(lolz)
                        if success:
                            vp.sendMessage(to, "succes bypass")
                        else:
                            vp.sendMessage(to, "succes bypass")

                elif text.startswith("!kickname "):
                     if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        pisah = text.split("!kickname ")
                        nk0 = text.replace(pisah[0]+"!kickname ","")
                        nk1 = nk0.lstrip()
                        _name = nk1
                        gs = vp.getGroup(msg.to)
                        targets = []
                        for i in gs.members:
                            if _name in i.displayName:
                                targets.append(i.mid)
                        if targets == []:
                          vp.sendMessage(msg.to,"target not found")
                        lolz = 'simple.js gid={} token={} app={}'.format(to, vp.authToken, "DESKTOPMAC\t11.2.5\tMac_Os\t11.2.5")
                        for target in targets:
                            lolz += ' uid={}'.format(target)
                        success = execute_js(lolz)
#=============================================================================-====                   
#COMMAN USER LOGIN ADMIN OR OWNER OR CREATOR     
                elif text.lower() == "login sb" and msg._from not in premium['listLogin']:
                    if msg._from in premium["myService"]:
                        user = premium["myService"][msg._from]
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        try:
                            kontol = requests.get("https://api.chstore.me/lineqr?appname=DESKTOPMAC\t7.9.1\tXyesiiec-Macbook-Pro\t11")
                            xx = kontol.text
                            data = json.loads(xx)
                            qrlink = data["result"]["qrlink"]
                            qrkode = data["result"]["qrcode"]
                            sesion = data["result"]["session"]
                            vp.sendMention(msg.to, 'Login Request\nUser : @!\n• Login qr 30 detik \n{}'.format(qrlink),' ', [msg._from])
                            vp.sendImageWithURL(msg.to,"{}".format(qrkode))
                            vie = requests.get("https://api.chstore.me/lineqr/pincode?session={}".format(sesion))
                            ko = vie.text
                            data = json.loads(ko)
                            pincode = data["result"]
                            vp.sendReplyMessage(msg.id,to, '{}'.format(pincode))
                            to = requests.get("https://api.chstore.me/lineqr/auth?session={}".format(sesion))
                            aa = to.text
                            auth = json.loads(aa)
                            if msg._from not in premium['listLogin']:
                                premium['listLogin'][msg._from] =  '%s' % user
                                isi = "{}".format(auth["result"]["accessToken"])
                                os.system('cp -r login {}'.format(user))
                                os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                                os.system('screen -dmS {}'.format(user))
                                os.system('screen -r {} -X stuff "cd {} && python3 sb.py \n"'.format(user, user))
                                vp.sendMention(msg.to, 'Request Login\n• User : @!\n• File : {}\n• Login SelfBot Berhasil'.format(user),' ', [msg._from])
                            else:
                                vp.sendMention(msg.to, 'Request Login\n• User : @!\n• FAILED 404!!',' ', [msg._from])
                        except Exception as e:
                            print(e)
                            vp.sendMention(msg.to, 'Connection Timeout\n• User : @!\n• Code qr expired',' ', [msg._from])
                                                   
                elif text.lower() == "login sb" and msg._from in premium['listLogin']:
                    if msg._from in premium["myService"]:
                        vp.sendMention(msg.to, 'STATUS : FAILED\nâ€¢ User : @!\nâ€¢ Please type [ Logout sb ]',' ', [msg._from])
#==================================================================================-====            
                elif text.lower() == "login sb2" and msg._from not in premium['listLogin']:
                    if msg._from in premium["myService"]:
                        user = premium["myService"][msg._from]
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        try:
                            kontol = requests.get("https://api.chstore.me/lineqr?appname=DESKTOPMAC\t7.9.1\tXyesiiec-Macbook-Pro\t11")
                            xx = kontol.text
                            data = json.loads(xx)
                            qrlink = data["result"]["qrlink"]
                            qrkode = data["result"]["qrcode"]
                            sesion = data["result"]["session"]
                            vp.sendMention(msg.to, 'Login Request\nUser : @!\n• Login qr 30 detik \n{}'.format(qrlink),' ', [msg._from])
                            vp.sendImageWithURL(msg.to,"{}".format(qrkode))
                            vie = requests.get("https://api.chstore.me/lineqr/pincode?session={}".format(sesion))
                            ko = vie.text
                            data = json.loads(ko)
                            pincode = data["result"]
                            vp.sendReplyMessage(msg.id,to, '{}'.format(pincode))
                            to = requests.get("https://api.chstore.me/lineqr/auth?session={}".format(sesion))
                            aa = to.text
                            auth = json.loads(aa)
                            if msg._from not in premium['listLogin']:
                                premium['listLogin'][msg._from] =  '%s' % user
                                isi = "{}".format(auth["result"]["accessToken"])
                                os.system('cp -r login {}'.format(user))
                                os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                                os.system('screen -dmS {}'.format(user))
                                os.system('screen -r {} -X stuff "cd {} && python3 brk.py \n"'.format(user, user))
                                vp.sendMention(msg.to, 'Request Login\n• User : @!\n• File : {}\n• Login SelfBot Berhasil'.format(user),' ', [msg._from])
                            else:
                                vp.sendMention(msg.to, 'Request Login\n• User : @!\n• FAILED 404!!',' ', [msg._from])
                        except Exception as e:
                            print(e)
                            vp.sendMention(msg.to, 'Connection Timeout\n• User : @!\n• Code qr expired',' ', [msg._from])

                elif text.lower() == "login sb2" and msg._from in premium['listLogin']:
                    if msg._from in premium["myService"]:
                        vp.sendMention(msg.to, 'STATUS : FAILED\nâ€¢ User : @!\nâ€¢ Please type [ Logout sb ]',' ', [msg._from])
#=========================================================================-====       
                elif text.lower() == "login js" and msg._from not in premium['listLogin']:
                    if msg._from in premium["myService"]:
                        user = premium["myService"][msg._from]
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        try:
                            kontol = requests.get("https://api.chstore.me/lineqr?appname=DESKTOPMAC\t7.9.1\tXyesiiec-Macbook-Pro\t11")
                            xx = kontol.text
                            data = json.loads(xx)
                            qrlink = data["result"]["qrlink"]
                            qrkode = data["result"]["qrcode"]
                            sesion = data["result"]["session"]
                            vp.sendMention(msg.to, 'Login Request\nUser : @!\n• Login qr 30 detik \n{}'.format(qrlink),' ', [msg._from])
                            vp.sendImageWithURL(msg.to,"{}".format(qrkode))
                            vie = requests.get("https://api.chstore.me/lineqr/pincode?session={}".format(sesion))
                            ko = vie.text
                            data = json.loads(ko)
                            pincode = data["result"]
                            vp.sendReplyMessage(msg.id,to, '{}'.format(pincode))
                            to = requests.get("https://api.chstore.me/lineqr/auth?session={}".format(sesion))
                            aa = to.text
                            auth = json.loads(aa)
                            if msg._from not in premium['listLogin']:
                                premium['listLogin'][msg._from] =  '%s' % user
                                isi = "{}".format(auth["result"]["accessToken"])
                                os.system('cp -r login {}'.format(user))
                                os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                                os.system('screen -dmS {}'.format(user))
                                os.system('screen -r {} -X stuff "cd {} && python3 selfbot.py \n"'.format(user, user))
                                vp.sendMention(msg.to, 'Request Login\n• User : @!\n• File : {}\n• Login SelfBot Berhasil'.format(user),' ', [msg._from])
                            else:
                                vp.sendMention(msg.to, 'Request Login\n• User : @!\n• FAILED 404!!',' ', [msg._from])
                        except Exception as e:
                            print(e)
                            vp.sendMention(msg.to, 'Connection Timeout\n• User : @!\n• Code qr expired',' ', [msg._from])
                              
                elif text.lower() == "login js" and msg._from in premium['listLogin']:
                    if msg._from in javascript["myService"]:
                        vp.sendMention(msg.to, 'STATUS : FAILED\nâ€¢ User : @!\nâ€¢ Please type [ Logout sb ]',' ', [msg._from])
#=========================================================================-====                                       
                elif text.startswith(""+db["rname"]+"addself "):
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            if key1 not in premium['myService']:
                                nama = str(text.split(' ')[1])
                                premium['myService'][key1] =  '%s' % nama
                                vp.sendMention(msg.to, 'Add Service Self\n• User : @!\n Add to login service','', [key1])
                            else:
                                vp.sendMention(msg.to, 'Add Service Self\n• User : @!\n• Allready in user service','', [key1])

                elif text.startswith(""+db["rname"]+"addjs "):
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            if key1 not in javascript['myService']:
                                nama = str(text.split(' ')[1])
                                javascript['myService'][key1] =  '%s' % nama
                                vp.sendMention(msg.to, 'Add Service JS\n• User : @!\n• Add to login service','', [key1])
                            else:
                                vp.sendMention(msg.to, 'Add Service JS\n• User @!\n• Allready in user service','', [key1])

                elif text.startswith(""+db["rname"]+"deljs "):
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            if key1 in javascript['myService']:
                                del javascript['myService'][key1]
                                vp.sendMention(msg.to, 'Delete Service Js\n• User : @!\n• Delete service success','', [key1])
                            else:
                                vp.sendMention(msg.to, 'Delet Service Js\n• User : @!\n• Not in service','', [key1])

                elif text.startswith(""+db["rname"]+"delself "):
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        if msg.contentMetadata is not None  and 'MENTION' in msg.contentMetadata:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            if key1 in premium['myService']:
                                del premium['myService'][key1]
                                vp.sendMention(msg.to, 'Delete User Service\n• User : @!\n• Deleted from service','', [key1])
                            else:
                                vp.sendMention(msg.to, 'Delete User Service\n• User : @!\n• Not in service','', [key1])

                elif text.startswith(""+db["rname"]+"delusersb "):
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        h = [a for a in premium['myService']]
                        XYZ = h[int(text.lower().split(' ')[1])-1]
                        user = premium["myService"][XYZ]
                        if XYZ in premium['myService'] and XYZ not in premium['listLogin']:
                            del premium['myService'][XYZ]
                            vp.sendMention(msg.to, 'Delete User Service\n• User : @!\n• Deleted from list login','', [XYZ])
                        if XYZ in premium['listLogin']:
                            del premium['listLogin'][XYZ]
                            del premium['myService'][XYZ]
                            os.system("screen -S {} -X kill".format(user))
                            os.system('rm -r {}'.format(user))
                        vp.sendMention(msg.to, 'Delete User Service\n• User : @!\n• Deleted from list service','', [XYZ])

                elif text.startswith(""+db["rname"]+"deluserjs "):
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        h = [a for a in javascript['myService']]
                        XYZ = h[int(text.lower().split(' ')[1])-1]
                        user = javascript["myService"][XYZ]
                        if XYZ in javascript['myService'] and XYZ not in javascript['listLogin']:
                            del javascript['myService'][XYZ]
                            vp.sendMention(msg.to, 'Delete User Service\n• User : @!\n• Deleted from list login','', [XYZ])
                        if XYZ in javascript['listLogin']:
                            del javascript['listLogin'][XYZ]
                            del javascript['myService'][XYZ]
                            os.system("screen -S {} -X kill".format(user))
                            os.system('rm -r {}'.format(user))
                        vp.sendMention(msg.to, 'Delete User Service\n• User : @!\n• Deleted from list service','', [XYZ])

                elif text.lower() == ""+db["rname"]+"list user js":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        if javascript["myService"] == {}:
                            vp.sendMention(msg.to, "@!\n• List user empty","",[msg._from])
                        else:
                            h = [a for a in javascript['myService']]
                            k = len(h)//20
                            for aa in range(k+1):
                                msgas = '「 List Service 」\n'
                                no=0
                                for a in h:
                                    no+=1
                                    if javascript['myService'][a] == "":cd = "None."
                                    else:cd = javascript['myService'][a]
                                    if no == len(h):msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                                    else:msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                                vp.sendMention(msg.to, msgas,'', h)

                elif text.lower() == ""+db["rname"]+"list user":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        if premium["myService"] == {}:
                            vp.sendMention(msg.to, "@!\n• List user empty","",[msg._from])
                        else:
                            h = [a for a in premium['myService']]
                            k = len(h)//20
                            for aa in range(k+1):
                                msgas = '「 List Service 」\n'
                                no=0
                                for a in h:
                                    no+=1
                                    if premium['myService'][a] == "":cd = "None."
                                    else:cd = premium['myService'][a]
                                    if no == len(h):msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                                    else:msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                                vp.sendMention(msg.to, msgas,'', h)

                elif text.startswith(""+db["rname"]+"addme "):
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        if msg._from not in premium['myService']:
                            nama = str(text.split(' ')[1])
                            premium['myService'][msg._from] =  '%s' % nama
                            vp.sendMention(msg.to, "ADD USER OWNER\n• User : @!\n• Add to login user","",[msg._from])
                        else:
                            vp.sendMention(msg.to, "ADD USER OWNER\n• User : @!\n• Allready in List..","",[msg._from])
                            if msg._from not in Creator or msg._from not in Owner or msg._from not in Admin:
                                vp.sendMention(msg.to, "Sorry @!\n• Your Not Ownerlist","",[msg._from])

                elif text.startswith(""+db["rname"]+"addmejs "):
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        if msg._from not in javascript['myService']:
                            nama = str(text.split(' ')[1])
                            javascript['myService'][msg._from] =  '%s' % nama
                            vp.sendMention(msg.to, "ADD USER OWNER\n• User : @!\n• Add to login user","",[msg._from])
                        else:
                            vp.sendMention(msg.to, "ADD USER OWNER\n• User : @!\n• Allready in List..","",[msg._from])

                elif text.lower() == "logout js" and msg._from in javascript['listLogin']:
                    if msg._from in javascript["myService"]:
                        del javascript['listLogin'][msg._from]
                        user = javascript["myService"][msg._from]
                        os.system("screen -S {} -X quit".format(str(user)))
                        os.system('rm -rf {}'.format(str(user)))
                        time.sleep(2)
                        vp.sendMention(msg.to, 'LOGOUT JS\n• User : @!\n• LogOut From NODEJS',' ', [msg._from])

                elif text.lower() == "logout js" and msg._from not in javascript['listLogin']:
                    if msg._from in javascript["myService"]:
                        vp.sendMention(msg.to, 'STATUS : FAILED\n• User : @!\mPlease first login type [ Login js ]',' ', [msg._from])
#=============================================================================-====                                       
                elif text.lower() == "logout sb" and msg._from in premium['listLogin']:
                    if msg._from in premium["myService"]:
                        del premium['listLogin'][msg._from]
                        user = premium["myService"][msg._from]
                        os.system("screen -S {} -X quit".format(str(user)))
                        os.system('rm -rf {}'.format(str(user)))
                        time.sleep(2)
                        vp.sendMention(msg.to, 'LOGOUT SELFBOT\n• User : @!\nLogOut From Selfbot',' ', [msg._from])

                elif text.lower() == "logout sb" and msg._from not in premium['listLogin']:
                    if msg._from in premium["myService"]:
                        vp.sendMention(msg.to, 'STATUS : FAILED\n• User : @!\nPlease first login type [ Login sb ]',' ', [msg._from])

                elif text.lower() == "cara login":
                    if msg._from in premium["myService"] and msg._from in Owner:
                        vp.sendMention(msg.to, '@!\n{}'.format(db["caraLogin"]),' ', [msg._from])
                    else:
                        vp.sendMention(msg.to, 'Status : Failed\n• @!\n• Your not in list user',' ', [msg._from])
#=============================================================================-====                               
                if text.startswith(""+db["rname"]+"addme ") and msg._from not in Creator and msg._from not in Owner:
                    vp.sendMention(msg.to, 'Status : Failed\n• @!\n• Your not in ownerlist',' ', [msg._from])
                elif text.startswith(""+db["rname"]+"addmejs ") and msg._from not in Creator and msg._from not in Owner:
                    vp.sendMention(msg.to, 'Status : Failed\n• @!\n• Your not in ownerlist',' ', [msg._from])        
                elif text.lower() == ""+db["rname"]+"list user" and msg._from not in Creator and msg._from not in Owner:
                    vp.sendMention(msg.to, 'Status : Failed\n• @!\n• Your not in ownerlist',' ', [msg._from])        
                elif text.lower() == ""+db["rname"]+"list user js" and msg._from not in Creator and msg._from not in Owner:
                    vp.sendMention(msg.to, 'Status : Failed\n• @!\n• Your not in ownerlist',' ', [msg._from])        
                elif text.lower() == "login sb" and msg._from not in premium["myService"]:
                    vp.sendMention(msg.to, 'Status : Failed\n• @!\n• Your not in user lisr',' ', [msg._from])        
                elif text.lower() == "login sb2" and msg._from not in premium["myService"]:
                    vp.sendMention(msg.to, 'Status : Failed\n• @!\n• Your not in user lisr',' ', [msg._from])        
                elif text.lower() == "login js" and msg._from not in javascript["myService"]:
                    vp.sendMention(msg.to, 'Status : Failed\n• @!\n• Your not in user lisr',' ', [msg._from])        
                elif text.lower() == "logout sb" and msg._from not in premium["myService"]:
                    vp.sendMention(msg.to, 'Status : Failed\n• @!\n• Your not in user lisr',' ', [msg._from])        
                elif text.lower() == "login js" and msg._from not in javascript["myService"]:
                    vp.sendMention(msg.to, 'Status : Failed\n• @!\n• Your not in user lisr',' ', [msg._from])        
#=============================================================================-====                                                    
                elif text.lower() == "restart sb":
                    if msg._from in premium["myService"]:
                        user = premium["myService"][msg._from]
                        os.system("screen -S {} -X quit".format(str(user)))
                        os.system('cp -r login {}'.format(user))
                        os.system('screen -dmS {}'.format(user))
                        os.system('screen -r {} -X stuff "cd {} && python3 {}.py \n"'.format(user, user, user))
                        time.sleep(3)
                        vp.sendMention(msg.to, '「  Restart Sb  」\n> @! Succes Restart selfbot',' ', [msg._from])

                elif text.lower().startswith(""+db["rname"]+"remove"):
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        sep = text.split(" ")
                        anu = text.replace(sep[0] + " ","")
                        os.system("screen -S {} -X quit".format(str(anu)))
                        os.system('rm -rf {}'.format(str(anu)))
                        time.sleep(2)
                        vp.sendMention(to, 'Kill User Screen\n• Status : Succes\n • User @!\n• Deleted file : {}'.format(str(anu)),' ', [msg._from])

#=============================================================================
                elif text.lower() == ""+db["rname"]+"screen list":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        proses = os.popen("screen -list")
                        a = proses.read()
                        vp.sendReplyMessage(msg.id,to, "{}".format(str(a)))
                        proses.close()

                elif text.lower() == ""+db["rname"]+"allowliff":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        try:
                            allowLiff()
                            vp.sendReplyMessage(msg.id,to, "Allow Template Succes")
                        except:
                            vp.sendReplyMessage(msg.id,to,"Klick Link and Allow/Izinkan\nline://app/1602687308-GXq4Vvk9")
                            
                elif text.lower() == ""+db["rname"]+"chatbot off":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        settings["selfbot"] = False
                        vp.sendMessage(msg.to, "Chatbot disable ♪")
                        
                elif text.lower() == ""+db["rname"]+"chatbot on":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        settings["selfbot"] = True
                        vp.sendMessage(msg.to, "Chatbot enable ♪")
                           
                elif text.startswith(""+db["rname"]+"kick "):
                    if settings["selfbot"] == True:
                      if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            if target in Bots:
                                pass
                            else:
                                try:
                                    vp.sendMention(msg.to, 'Sorry @! i fuck your ass','', [target])
                                    vp.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
 
                elif text.lower() == ""+db["rname"]+"cban":
                  if settings["selfbot"] == True:  
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      if settings["blacklist"] == {}:
                           vp.sendMention(msg.to, '@!\nNothing Blacklist ♪',' ',[msg._from])
                      else:
                           vp.sendMention(msg.to, '@!\n{} Blacklist cleared ♪'.format(str(len(settings["blacklist"]))),' ',[msg._from])
                           settings["blacklist"] = {}
                           print ("[Command]Blacklist executed")                                                
                        
                elif text.startswith(""+db["rname"]+"setrname:"):
                    if msg._from in Creator or msg._from in Owner:
                        proses = msg.text.split(":")
                        text = msg.text.replace(proses[0] + ":","")
                        try:
                            db["rname"] = text
                            vp.sendMessage(to,"Update rname to : {}".format(text))
                        except:
                            pass
                            
                elif text.startswith(""+db["rname"]+"setwelcome:"):
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        proses = msg.text.split(":")
                        text = msg.text.replace(proses[0] + ":","")
                        try:
                            settings["welcome"] = text
                            vp.sendMessage(to,"Update to :\n" + text + "")
                        except:
                            vp.sendMessage(msg.to,"FAILED 404!!")
                
                elif text.startswith(""+db["rname"]+"ban "):
                    if settings["selfbot"] == True:
                      if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                settings["blacklist"][target] = True
                                vp.sendMessage(to,"Added blacklist ♪")
                            except:
                                pass 
                            
                elif text.startswith(""+db["rname"]+"unban "):
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       targets = []
                       for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                       for target in targets:
                               try:
                                   del settings["blacklist"][target]
                                   vp.sendMessage(to,"Cleared blacklist ♪")
                               except:
                                   pass

                elif text.startswith(""+db["rname"]+"adminadd "):
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       targets = []
                       for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                       for target in targets:
                               try:
                                   Admin[target] = True
                                   f=codecs.open('admin.json','w','utf-8')
                                   json.dump(Admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                   vp.sendMention(msg.to, '@!\nHas been promote to admin ♪','', [target])
                               except:
                                   pass

                elif text.startswith(""+db["rname"]+"admindell "):
                  if settings["selfbot"] == True: 
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       targets = []
                       for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                       for target in targets:
                           #if target not in Admin:
                               try:
                                   del Admin[target]
                                   f=codecs.open('admin.json','w','utf-8')
                                   json.dump(Admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                   vp.sendMention(msg.to, '@!\nHas been delete to admin ♪','', [target])
                               except:
                                   pass

                elif text.startswith(""+db["rname"]+"owneradd "):
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner:
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       targets = []
                       for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                       for target in targets:
                               try:
                                   Owner[target] = True
                                   f=codecs.open('owner.json','w','utf-8')
                                   json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                   vp.sendMention(msg.to, '@!\nHas been promote to owner ♪','', [target])
                               except:
                                   pass

                elif text.startswith(""+db["rname"]+"ownerdell "):
                  if settings["selfbot"] == True: 
                    if msg._from in Creator or msg._from in Owner:
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       targets = []
                       for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                       for target in targets:
                           #if target not in Admin:
                               try:
                                   del Owner[target]
                                   f=codecs.open('owner.json','w','utf-8')
                                   json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                   vp.sendMention(msg.to, '@!\nHas been delete to owner ♪','', [target])
                               except:
                                   pass

                elif text.startswith(""+db["rname"]+"invite "):
                  if settings["selfbot"] == True: 
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:  
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:                                                                            
                            try:      
                                vp.findAndAddContactsByMid(target)
                                vp.inviteIntoGroup(to,[target])                                             
                            except:
                                pass
					
                elif text.lower() == ""+db["rname"]+"cleartemp":
                  if settings["selfbot"] == True: 
                    if msg._from in Creator or msg._from in Owner:
                        process = os.popen('sync; echo 1 > /proc/sys/vm/drop_caches')
                        a = process.read()
                        vp.sendMessage(msg.to, "Cleared tempfile server ♪")
                                             
                elif text.lower() == ""+db["rname"]+"owner:add":
                    if settings["selfbot"] == True:  
                      if msg._from in Creator or msg._from in Owner:  
                        settings["addowner"] = True
                        vp.sendMessage(msg.to,"Send a contact ♪")

                elif text.lower() == ""+db["rname"]+"owner:dell":
                  if settings["selfbot"] == True:  
                    if msg._from in Creator or msg._from in Owner:
                        settings["dellowner"] = True
                        vp.sendMessage(msg.to,"Send a contact ♪")

                elif text.lower() == ""+db["rname"]+"admin:add":
                    if settings["selfbot"] == True:  
                      if msg._from in Creator or msg._from in Owner or msg._from in Admin:  
                        settings["addadmin"] = True
                        vp.sendMessage(msg.to,"Send a contact ♪")

                elif text.lower() == ""+db["rname"]+"admin:dell":
                    if settings["selfbot"] == True:  
                      if msg._from in Creator or msg._from in Owner or msg._from in Admin:  
                        settings["delladmin"] = True
                        vp.sendMessage(msg.to,"Send a contact ♪")
                        
                elif text.lower() == ""+db["rname"]+"friendlist":
                  if settings["selfbot"] == True:  
                    if msg._from in Creator or msg._from in Owner:  
                      contactlist = vp.getAllContactIds()
                      kontak = vp.getContacts(contactlist)
                      num=1
                      msgs="「 FriendList 」\n"
                      for ids in kontak:
                          msgs+="\n%i. %s" % (num, ids.displayName)
                          num=(num+1)
                      msgs+="\n\nTotal Friend : %i" % len(kontak)
                      vp.sendMessage(to, msgs)
  
                elif text.lower() == ""+db["rname"]+"ready":
                  if settings["selfbot"] == True:  
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:  
                      try:vp.kickoutFromGroup(msg.to, ["u5d72909e8c37e0ab805952336f872361"]);wait["limitkick"] = False
                      except:wait["limitkick"] = True
                      md = ""
                      if wait["limitkick"]== True: md+="Status : Limite"
                      else: md+="Status : Normal"
                      vp.sendMessage(msg.to,md)
                                           
                elif text.lower() == "rname":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Staff:  
                        vp.sendMessage(to, db["rname"])
                        
                elif text.lower() == ""+db["rname"]+"abort" or text.lower() == ""+db["rname"]+"refresh":
                    if settings["selfbot"] == True:  
                      if msg._from in Creator or msg._from in Owner or msg._from in Admin:  
                        settings["addowner"] = False
                        settings["dellowner"] = False
                        settings["addadmin"] = False
                        settings["delladmin"] = False
                        vp.sendMessage(to,"「 Save Data 」")
                            
                elif text.lower() == ""+db["rname"]+"ownerlist":
                  if settings["selfbot"] == True:  
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:  
                      if Owner == {}:
                           vp.sendMention2(msg.to, '@! Empty ♪',' ',[msg._from])
                      else:
                           h = [a for a in Owner]
                           k = len(h)//20
                           for aa in range(k+1):
                               msgas = ''
                               no=0
                               for a in h[aa*20 : (aa+1)*20]:
                                   no+=1
                                   if Owner[a] == "":cd = "None."
                                   else:cd = Owner[a]
                                   if no == len(h):msgas+='\n├{}. @!'.format(no,cd)
                                   else:msgas+='\n├{}. @!'.format(no,cd)
                               msgas += "\n╰──────────"
                               vp.sendMention2(msg.to, msgas,'╭「 Owner List 」', h[aa*20 : (aa+1)*20])
                           print ("[Command]Ownerlist executed")
                           
                elif text.lower() == ""+db["rname"]+"adminlist":
                  if settings["selfbot"] == True:  
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:  
                      if Admin == {}:
                           vp.sendMessage(msg.to,"Adminlist empty.")
                      else:
                           h = [a for a in Admin]
                           k = len(h)//20
                           for aa in range(k+1):
                               msgas = ''
                               no=0
                               for a in h[aa*20 : (aa+1)*20]:
                                   no+=1
                                   if Admin[a] == "":cd = "None."
                                   else:cd = Admin[a]
                                   if no == len(h):msgas+='\n├{}. @!'.format(no,cd)
                                   else:msgas+='\n├{}. @!'.format(no,cd)
                               msgas += "\n╰──────────"
                               vp.sendMention2(msg.to, msgas,'╭「 Admin List 」', h[aa*20 : (aa+1)*20])
                           print ("[Command]Adminlist executed")
                           
                elif text.lower() == ""+db["rname"]+"banlist":
                  if settings["selfbot"] == True:  
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      if settings["blacklist"] == {}:
                           vp.sendMessage(msg.to,"No Body Is Banned ♪")
                      else:
                           mc = "│"
                           for mi_d in settings["blacklist"]:
                               mc += "" +vp.getContact(mi_d).displayName + "\n│"
                           vp.sendMessage(msg.to,"╭──────────\n├ Blacklist\n├──────────\n" + mc + "\n├──────────\n├ 「 「%s」 Blacklist 」\n╰──────────"%(str(len(settings["blacklist"]))))
                           print ("[Command]Adminlist executed")
                        
                elif text.lower() == ""+db["rname"]+"protectlist":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:  
                        ma = "│️"
                        mb = "│️"
                        mc = "│️"
                        md = "│️"
                        me = "│️"
                        mf = "│️"
                        mg = "│️"
                        a = 0
                        b = 0
                        c = 0
                        d = 0
                        e = 0
                        f = 0
                        g = 0
                        gid = settings["protinvite"]
                        for group in gid:
                            G = vp.getGroup(group)
                            a = a + 1
                            end = "\n"
                            ma += str(a) + ". " +G.name+ "\n│️"
                        gid = settings["protqr"]
                        for group in gid:
                            G = vp.getGroup(group)
                            b = b + 1
                            end = "\n"
                            mb += str(b) + ". " +G.name+ "\n│️"
                        gid = settings["protcancel"]
                        for group in gid:
                            G = vp.getGroup(group)
                            c = c + 1
                            end = "\n"
                            mc += str(c) + ". " +G.name+ "\n│️"
                        gid = settings["protkick"]
                        for group in gid:
                            G = vp.getGroup(group)
                            d = d + 1
                            end = "\n"
                            md += str(d) + ". " +G.name+ "\n│️"
                        gid = settings["pro_name"]
                        for group in gid:
                            G = vp.getGroup(group)
                            e = e + 1
                            end = "\n"
                            me += str(e) + ". " +G.name+ "\n│️"    
                        gid = settings["picon"]
                        for group in gid:
                            G = vp.getGroup(group)
                            f = f + 1
                            end = "\n"
                            mf += str(f) + ". " +G.name+ "\n│️"       
                        gid = settings["Autopurge"]
                        for group in gid:
                            G = vp.getGroup(group)
                            g = g + 1
                            end = "\n"
                            mg += str(g) + ". " +G.name+ "\n│️"      
                        vp.sendMessage(to,"╭────────────\n│️ᴅᴀꜰᴛᴀʀ ᴘʀᴏᴛᴇᴄᴛ\n╰────────────\n╭────────────\n│️ᴅᴇɴʏ ɪɴᴠɪᴛᴇ:\n"+ma+"\n│️ʟᴏᴄᴋ ᴜʀʟ:\n"+mb+"\n│️ʟᴏᴄᴋ ᴄᴀɴᴄᴇʟʟ:\n"+mc+"\n│️ʟᴏᴄᴋ ᴍᴇᴍʙᴇʀꜱ:\n"+md+"\n│️ɴᴀᴍᴇ ʟᴏᴄᴋ:\n"+me+"\n│️ɪᴄᴏɴ ʟᴏᴄᴋ:\n"+mf+"\n│️ᴀᴜᴛᴏ ᴘᴜʀɢᴇ:\n╰────────────\n╭────────────\n│️βŘҜ-Ŧ€ΔΜ-βØŦŞ\n╰────────────\n"+mg+"╰────────────")
                           
                elif text.lower() == ""+db["rname"]+"glist":
                  if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                    groups = vp.getGroupIdsJoined()
                    ret_ = "╭─「 ᴅᴀꜰᴛᴀʀ ɢʀᴏᴜᴘ 」\n│️"
                    no = 1
                    for gid in groups:
                        group = vp.getGroup(gid)
                        ret_ += "\n├↘{}. {}  {}".format(str(no), str(group.name), str(len(group.members)))
                        no = (no+1)
                    ret_ += "\n╰───────────────"
                    vp.sendMessage(msg.to, str(ret_))
                           
                elif text.startswith(""+db["rname"]+"closeqr:"):
                  if msg._from in Creator or msg._from in Owner:
                    separate = msg.text.split(":")
                    number = msg.text.replace(separate[0] + ":","")
                    groups = vp.getGroupIdsJoined()
                    try:
                        group = groups[int(number)-1]
                        G = vp.getGroup(group)
                        try:
                            G.preventedJoinByTicket = True
                            vp.updateGroup(G)
                        except:
                            G.preventedJoinByTicket = True
                            vp.updateGroup(G)
                        vp.sendMessage(msg.to, "「 Close Qr 」\n\nGroup : " + G.name)
                    except Exception as error:
                        vp.sendMessage(to, str(error))
                        
                elif text.startswith(""+db["rname"]+"openqr:"):
                  if msg._from in Creator or msg._from in Owner:
                    separate = msg.text.split(":")
                    number = msg.text.replace(separate[0] + ":","")
                    groups = vp.getGroupIdsJoined()
                    try:
                        group = groups[int(number)-1]
                        G = vp.getGroup(group)
                        try:
                            G.preventedJoinByTicket = False
                            vp.updateGroup(G)
                            gurl = "https://line.me/R/ti/g/{}".format(str(vp.reissueGroupTicket(G.id)))
                        except:
                            G.preventedJoinByTicket = False
                            vp.updateGroup(G)
                            gurl = "https://line.me/R/ti/g/{}".format(str(vp.reissueGroupTicket(G.id)))
                        vp.sendMessage(msg.to, "「 Open Qr 」\n\nGroup : " + G.name + "\nLink: " + gurl) 
                    except Exception as error:
                        vp.sendMessage(to, str(error))
                        
                elif text.startswith(""+db["rname"]+"bye:"):
                  if msg._from in Creator or msg._from in Owner:
                    separate = msg.text.split(":")
                    number = msg.text.replace(separate[0] + ":","")
                    groups = vp.getGroupIdsJoined()
                    try:
                        group = groups[int(number)-1]
                        G = vp.getGroup(group)
                        try:
                            vp.leaveGroup(G.id)
                        except:
                            vp.leaveGroup(G.id)
                        vp.sendMessage(msg.to, "「Leave 」\n\nGroup : " + G.name)
                    except Exception as error:
                        vp.sendMessage(msg.to, str(error))
                        
                elif text.startswith(""+db["rname"]+"inviteto:"):
                  if msg._from in Creator or msg._from in Owner:
                    separate = msg.text.split(":")
                    number = msg.text.replace(separate[0] + ":","")
                    groups = vp.getGroupIdsJoined()
                    try:
                        group = groups[int(number)-1]
                        G = vp.getGroup(group)
                        try:
                            vp.findAndAddContactsByMid(sender)
                            vp.inviteIntoGroup(G.id,[sender])        
                        except:
                            vp.findAndAddContactsByMid(msg.to)
                            vp.inviteIntoGroup(G.id,[sender])        
                        vp.sendMessage(msg.to, "「 Invite 」\n\nGroup : " + G.name)
                    except Exception as error:
                        vp.sendMessage(msg.to, str(error))
                     
                elif text.lower() == ""+db["rname"]+"welcome on":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        if msg.to in settings["welcomeMem"]:
                            vp.sendMessage(to,"Welcome msg enable ♪")
                        else:
                            settings["welcomeMem"][msg.to] = True
                            vp.sendMessage(to,"Welcome msg disable ♪")
                            
                elif text.lower() == ""+db["rname"]+"welcome off":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        if msg.to not in settings["welcomeMem"]:
                            vp.sendMessage(to,"Welcome msg disable ♪")
                        else:
                            del settings["welcomeMem"][msg.to]
                            vp.sendMessage(to,"Welcome msg enable ♪")                            
  
                elif text.lower() == ""+db["rname"]+"clearprotect":
                    if settings["selfbot"] == True:  
                      if msg._from in Creator or msg._from in Owner or msg._from in Admin:  
                        settings["protinvite"] = {}
                        settings["protqr"] = {}
                        settings["protcancel"] = {}
                        settings["protkick"] = {}
                        settings["war"] = {}
                        settings["projs"] = {}
                        settings["picon"] = {}
                        settings["pname"] = {}
                        settings["pro_name"] = {}
                        vp.sendMessage(to,"Reamoveall protection ♪")  
                        backupData()
                        
                elif text.lower() == ""+db["rname"]+"pro on":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        if msg.to in settings["protinvite"] or msg.to in settings["protqr"] or msg.to in settings["protcancel"] or msg.to in settings["protkick"]:
                            vp.sendMessage(to,"Max protection ♪")
                        else:
                            settings["protinvite"][msg.to] = True
                            settings["protqr"][msg.to] = True
                            settings["protcancel"][msg.to] = True
                            settings["protkick"][msg.to] = True
                            settings["war"][msg.to] = True
                            settings["projs"][msg.to] = True
                            vp.sendMessage(to,"「 All Protection enable 」")
                            
                elif text.lower() == ""+db["rname"]+"pro off":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        if msg.to not in settings["protinvite"] or msg.to not in settings["protqr"] or msg.to not in settings["protcancel"] or msg.to not in settings["protkick"]:
                            vp.sendMessage(to,"Max protection")
                        else:
                            del settings["protinvite"][msg.to]
                            del settings["protqr"][msg.to]
                            del settings["protcancel"][msg.to]
                            del settings["protkick"][msg.to]
                            del settings["war"][msg.to]
                            del settings["projs"][msg.to]
                            vp.sendMessage(to,"「 All protection Disable 」")
                            
                elif text.lower() == ""+db["rname"]+"proinv on":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Staff:
                        if msg.to in settings["protinvite"]:
                            vp.sendMessage(to,"Protect Invite enable")
                        else:
                            settings["protinvite"][msg.to] = True
                            vp.sendMessage(to,"Protect Invite enable")
                            
                elif text.lower() == ""+db["rname"]+"proinv off":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Staff:
                        if msg.to not in settings["protinvite"]:
                            vp.sendMessage(to,"Protect invite disable")
                        else:
                            del settings["protinvite"][msg.to]
                            vp.sendMessage(to,"Protect invite disable")
                            
                elif text.lower() == ""+db["rname"]+"proqr on":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Staff:
                        if msg.to in settings["protqr"]:
                            vp.sendMessage(to,"Protect url enable")
                        else:
                            settings["protqr"][msg.to] = True
                            vp.sendMessage(to,"Protect url enable")
                            
                elif text.lower() == ""+db["rname"]+"proqr off":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Staff:
                        if msg.to not in settings["protqr"]:
                            vp.sendMessage(to,"protect url disable")
                        else:
                            del settings["protqr"][msg.to]
                            vp.sendMessage(to,"protect url disable")

                elif text.lower() == ""+db["rname"]+"prokick on":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Staff:
                        if msg.to in settings["protkick"]:
                            vp.sendMessage(to,"Protect kick enable")
                        else:
                            settings["protkick"][msg.to] = True
                            vp.sendMessage(to,"protect kick enable")
                            
                elif text.lower() == ""+db["rname"]+"prokick off":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Staff:
                        if msg.to not in settings["protkick"]:
                            vp.sendMessage(to,"Protect kick disable")
                        else:
                            del settings["protkick"][msg.to]
                            vp.sendMessage(to,"Protect kick disable")
                            
                elif text.lower() == ""+db["rname"]+"procancel on":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Staff:
                        if msg.to in settings["protcancel"]:
                            vp.sendMessage(to,"Protect cancell enable")
                        else:
                            settings["protcancel"][msg.to] = True
                            vp.sendMessage(to,"Protect cancell enable")
                            
                elif text.lower() == ""+db["rname"]+"procancel off":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Staff:
                        if msg.to not in settings["protcancel"]:
                            vp.sendMessage(to,"Protect cancell disable")
                        else:
                            del settings["protcancel"][msg.to]
                            vp.sendMessage(to,"Protect cancell disable")

                elif text.lower() == ""+db["rname"]+"iconlock on":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Staff:
                        if msg.to in settings["picon"]:
                            vp.sendMessage(to,"Iconlock enable")
                        else:
                            settings["picon"][msg.to] = True
                            vp.sendMessage(to,"Iconlock enable")
                            
                elif text.lower() == ""+db["rname"]+"iconlock off":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Staff:
                        if msg.to not in settings["picon"]:
                            vp.sendMessage(to,"Iconlock disable")
                        else:
                            del settings["picon"][msg.to]
                            vp.sendMessage(to,"Iconlock disable")

                elif text.lower() == ""+db["rname"]+"namelock on":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Staff:
                        if msg.to in settings["pname"] and msg.to in settings["pro_name"]:
                            vp.sendMessage(to, "Namelock enable")
                        else:
                            settings["pname"][msg.to] = True
                            settings["pro_name"][msg.to] = vp.getGroup(msg.to).name
                            vp.sendMessage(to, "Namelock enable")
                            
                elif text.lower() == ""+db["rname"]+"namelock off":
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Staff:
                        if msg.to not in settings["pname"] and msg.to not in settings["pro_name"]:
                            vp.sendMessage(to, "Namelock disable")
                        else:
                            del settings["pname"][msg.to]
                            del settings["pro_name"][msg.to]
                            vp.sendMessage(to, "Namelock disable")
#BATAS SC SELF#
                elif text.lower() == "me":
                    if settings["selfbot"] == True:
                      if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Staff:
                        contact = vp.getContact(sender)
                        vp.sendContact(msg.to, sender)
                  
                elif text.startswith(""+db["rname"]+"cname:"):
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner:
                                sep = text.split(":")
                                string = text.replace(sep[0] + ":","")
                                if len(string) <= 20:
                                    profile = vp.getProfile()
                                    profile.displayName = string
                                    vp.updateProfile(profile)
                                    vp.sendMessage(to,"{}".format(str(string)))
                                                                                                                                
                elif text.startswith(""+db["rname"]+"cbio:"):
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner:
                                sep = text.split(":")
                                string = text.replace(sep[0] + ":","")
                                if len(string) <= 500:
                                    profile = vp.getProfile()
                                    profile.statusMessage = string
                                    vp.updateProfile(profile)
                                    vp.sendMessage(to,"{}".format(str(string)))
                                            
                elif text.lower() == ""+db["rname"]+"reboot":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner:  
                      vp.sendMessage(to, "「 Reboot Data 」")
                      time.sleep(5)
                      vp.sendMessage(to,"Saved Data")
                      restartBot()
                          
                elif text.lower() == ""+db["rname"]+"speed":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      start = time.time()
                      vp.sendReplyMessage(msg.id,to, "Respon Time Speed")
                      speed = time.time() - start
                      ping = speed * 1000
                      vp.sendReplyMessage(msg.id,to, "Speed Time : {} ms !".format(str(speedtest(ping))))
                      
                elif text.lower() == ""+db["rname"]+"errorlog":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner:  
                      with open('error.txt', 'r') as er:
                          error = er.read()
                      vp.sendMessage(to, str(error)) 
                      
                elif text.lower() == ""+db["rname"]+"runtime":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner:  
                        eltime = time.time() - mulai
                        bot = runtime(eltime)
                        vp.sendMessage(msg.to,"RUNNING TIME:\n" + bot)
                                           
                elif text.lower() == ""+db["rname"]+"rechat":
                  if settings["selfbot"] == True:  
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        try:
                            vp.removeAllMessages(op.param2)
                            vp.sendMessage(to,"Cleared chat ♪")                                             
                        except:
                            pass        
 
                elif "/ti/g/" in msg.text.lower():
                   if msg._from in Creator or msg._from in Owner or msg._from in Admin or msg._from in Bots:
                     if settings["autoJoinLink"] == True:
                         link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                         links = link_re.findall(text)
                         n_links = []
                         for l in links:
                            if l not in n_links:
                               n_links.append(l)
                         for ticket_id in n_links:
                            group = vp.findGroupByTicket(ticket_id)
                            vp.acceptGroupInvitationByTicket(group.id,ticket_id)
                            vp.sendMessage(msg.to, "Accpet to : %s" % str(group.name))
                      
#BATAS SC GROUP# 
                elif text.lower() == ""+db["rname"]+"settings":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:  
                        md = "╭────────────────\n"                            
                        md += "├─≽🔹️βŘҜ-Ŧ€ΔΜ-βØŦŞ🔹️\n"
                        md += "├≽🔹️Setkey: " +db["rname"]+ "\n"
                        md += "├≽🔹️🔹️SETTINGS🔹️🔹️\n"                                    
                        if msg.to in settings["picon"]: md+="├≽️✔ ɪᴄᴏɴ ʟᴏᴄᴋ\n"
                        else: md+="├≽️❎ ɪᴄᴏɴ ʟᴏᴄᴋ\n"
                        if msg.to in settings["pro_name"]: md+="├≽️✔ ɴᴀᴍᴇ ʟᴏᴄᴋ\n"
                        else: md+="├≽️❎ ɴᴀᴍᴇ ʟᴏᴄᴋ\n"       
                        if msg.to in settings["war"]: md+="├≽️✔ ᴀᴜᴛᴏ ᴘᴜʀɢᴇ\n"
                        else: md+="├≽️❎ ᴀᴜᴛᴏ ᴘᴜʀɢᴇ\n"
                        if msg.to in settings["protinvite"]: md+="├≽️✔ ᴅᴇɴʏ ɪɴᴠɪᴛᴇ\n"
                        else: md+="├≽️❎ ᴅᴇɴʏ ɪɴᴠɪᴛᴇ\n"
                        if msg.to in settings["protqr"]: md+="├≽️✔ ʟᴏᴄᴋ ᴜʀʟ\n"
                        else: md+="├≽️❎ ʟᴏᴄᴋ ᴜʀʟ\n"
                        if msg.to in settings["protkick"]: md+="├≽️✔ ʟᴏᴄᴋ ᴍᴇᴍʙᴇʀꜱ\n"
                        else: md+="├≽️❎ ʟᴏᴄᴋ ᴍᴇᴍʙᴇʀꜱ\n" 
                        if msg.to in settings["protcancel"]: md+="├≽️✔ ʟᴏᴄᴋ ᴄᴀɴᴄᴇʟʟ\n"
                        else: md+="├≽️❎ ʟᴏᴄᴋ ᴄᴀɴᴄᴇʟʟ\n"
                        if settings["autoJoinLink"]: md+="├≽️✔ ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ\n"
                        else: md+="├≽️❎ ️ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ\n"
                        if settings["autoJoin"]: md+="├≽️✔ ᴀᴜᴛᴏ ᴊᴏɪɴ\n"
                        else: md+="├≽️❎ ᴀᴜᴛᴏ ᴊᴏɪɴ\n"
                        if settings["autoLeave"]: md+="├≽️✔ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ\n╰────────────────"
                        else: md+="├≽️❎ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ\n╰────────────────"
                        vp.sendMessage(msg.to,md)          
                          
                elif text.lower() == ""+db["rname"]+"autojoin on":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      settings["autoJoin"] = True
                      vp.sendMessage(to,"Auto join enable ♪")
                      
                elif text.lower() == ""+db["rname"]+"autojoin off":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      settings["autoJoin"] = False
                      vp.sendMessage(to,"Auto join disable ♪")
                      
                elif text.lower() == ""+db["rname"]+"autojointicket on":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      settings["autoJoinLink"] = True
                      vp.sendMessage(to,"Auto join ticket enable ♪")
                      
                elif text.lower() == ""+db["rname"]+"autojointicket off":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      settings["autoJoinLink"] = False
                      vp.sendMessage(to,"Auto join ticket enable ♪")
                                        
                elif text.lower() == ""+db["rname"]+"autoread on":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      settings["autoRead"] = True
                      vp.sendMessage(to,"Auto read enable ♪")
                      
                elif text.lower() == ""+db["rname"]+"autoread off":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      settings["autoRead"] = False
                      vp.sendMessage(to,"Auto read disable ♪")
                      
                elif text.lower() == ""+db["rname"]+"autoleave on":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      settings["autoLeave"] = True
                      vp.sendMessage(to,"Autoleave enable ♪")
                      
                elif text.lower() == ""+db["rname"]+"autoleave off":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      settings["autoLeave"] = False
                      vp.sendMessage(to,"Autoleave disable ♪")

                elif text.lower() == ""+db["rname"]+"pict off":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      settings["changePicture"] = True
                      vp.sendMessage(to,"Send a picture ♪")
                      
                elif text.lower() == ""+db["rname"]+"pict off":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      settings["changePicture"] = False
                      vp.sendMessage(to,"update picture disable ♪")
                      
                elif text.lower() == ""+db["rname"]+"uppict on":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      settings["Picture"] = True
                      vp.sendMessage(to,"Send a picture ♪")
                      
                elif text.lower() == ""+db["rname"]+"uppict off":
                  if settings["selfbot"] == True:
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                      settings["Picture"] = False
                      vp.sendMessage(to,"update picture disable ♪")
                                              
                elif text.lower() == ""+db["rname"]+"vbye":
                  if settings["selfbot"] == True:  
                    if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                        ginfo = vp.getGroup(msg.to)
                        try:
                            vp.leaveGroup(msg.to)
                        except:  
                            pass
                            
                elif text.startswith(""+db["rname"]+"tk "):
                  if msg._from in Creator or msg._from in Owner or msg._from in Admin:
                     args = text.split(" ")
                     auth = text.replace(args[0] + " ","")
                     for t in auth.split("\n"):
                         if t:
                             vp.sendReplyMessage(msg.id,to, "{}".format(create_token(t)))
                             print(create_token(t))
   
                elif text.startswith(""+db["rname"]+"ct:"):
                  if settings["selfbot"] == True:
                    try:
                        sep = text.split(":")
                        users = text.replace(sep[0] + ":","")
                        gx = LINE("{}".format(users),appName="ANDROIDLITE\t2.17.1\tAndroid OS\t8.1.1")
                        gx.log("Auth Token : " + str(gx.authToken))
                        G = vp.getGroup(msg.to)
                        ginfo = vp.getGroup(msg.to)
                        G.preventedJoinByTicket = False
                        vp.updateGroup(G)
                        invsend = 0
                        Ticket = vp.reissueGroupTicket(msg.to)
                        gx.acceptGroupInvitationByTicket(msg.to, Ticket)
                        gx.sendMessage(msg.to, "Normal")
                        gx.leaveGroup(msg.to)
                    except:
                        vp.sendReplyMessage(msg.id,to,"Token limit atau banchat")
 
                elif text.startswith(""+db["rname"]+"ct2:"):
                  if settings["selfbot"] == True:
                    try:
                        sep = text.split(":")
                        users = text.replace(sep[0] + ":","")
                        gx = LINE("{}".format(users),appName="ANDROIDLITE\t2.17.1\tAndroid OS\t8.1.1")
                        gx.log("Auth Token : " + str(gx.authToken))
                        vp.findAndAddContactsByMid(users)
                        vp.inviteIntoGroup(msg.to, [user])
                        gx.acceptGroupInvitation(msg.to)
                        gx.sendMessage(msg.to, "Normal")
                        gx.leaveGroup(msg.to)
                    except:
                        vp.sendReplyMessage(msg.id,to,"Token limit atau banchat")
                        
                            
        backupData()               
    except Exception as error:
        print (error)
        logError(error)

for publicKey in vp.talk.getE2EEPublicKeys():
    vp.talk.removeE2EEPublicKey(publicKey)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
                    
