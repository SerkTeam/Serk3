# -*- coding: utf-8 -*-
#Serk_Bot

import TOBY
import requests
from TOBY.lib.curve.ttypes import *
from datetime import datetime
# https://kaijento.github.io/2017/05/19/web-scraping-youtube.com/
# from imgurpython import ImgurClient
import time,random,sys,json,codecs,threading,glob,re

cl = TOBY.LINE()
print "Serk_Bot"
cl.login(qr=True)
cl.loginResult
print "Serkl-Login Success\n"

ki = TOBY.LINE()
print "Serk_Bot"
ki.login(qr=True)
ki.loginResult
print "Serk2-Login Success\n"

kk = TOBY.LINE()
print "Serk_Bot"
kk.login(qr=True)
kk.loginResult
print "Serk3-Login Success\n\n=====[Serk Sukses All Login]====="

# client_id = ''
# client_secret = ''
# access_token = ''
# refresh_token = ''

# client = ImgurClient(client_id, client_secret, access_token, refresh_token)

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

# album = None
# image_path = 'tmp/tmp.jpg'

helpMessage ="""
||=====> [~S͟͟͟͞͞͞E͟͟͟͞͞͞R͟͟͟͞͞͞K͟͟͟͞͞͞*B͟͟͟͞͞͞O͟͟͟͞͞͞T͟͟͟͞͞͞~] <=====||


┏━━━━ೋ• ❄ •ೋ━━━━━┓
     ❁Command For Member❁
┗━━━━ೋ• ❄ •ೋ━━━━━┛

➣ .Me
➣ Rate
➣ /music
➣ /lirik
➣ Apakah
➣ Dosa @
➣ Up Chat
➣ Creator
➣ Tob say
➣ GCreator
➣ .Youtube
➣ Pahala @
┏━━━━ೋ• ❄ •ೋ━━━━━┓ ​
   ❁Commannd For Creator❁ 
┗━━━━ೋ• ❄ •ೋ━━━━━┛

➣ Admadd @
➣ Admrem @
➣ Adminlist
➣ InviteMeTo:

┏━━━━ೋ• ❄ •ೋ━━━━━┓ ​
   ❁Commannd For Admin❁ 
┗━━━━ೋ• ❄ •ೋ━━━━━┛

******************
|| Me           ||
|| Id           ||
|| Gn           ||
|| Sp           ||
|| Out          ||
|| Mid          ||
|| Test         ||
|| Gift         ||
|| Glist        ||
|| Spam:        ||
|| Mid @        ||
|| Ginfo        ||
|| Ciduk        ||
|| Album        ||
|| Urlon        ||
|| Backup       ||
|| Kernel       ||
|| Cancel       ||
|| Invite       ||
|| Respon       ||
|| Tagall       ||
|| Cname:       ||
|| Urloff       ||
|| Recover      ||
|| Runtime      ||
|| random:      ||
|| Cctv On      ||
|| All mid      ||
|| Cury PP      ||
|| Cstatus:     ||
|| Contact:     ||
|| Serk out     ||
|| List ban     ||
|| Serk join    ||
|| Grouppict    ||
|| Set album    ||
|| Ban group:   ||
|| Set member   ||
|| Leavegroup:  ||
|| Remove chat  ||
|| Hapus album  ||
|| Gcreator:inv ||
|| leaveallgroup||
******************

┏━━━━ೋ• ❄ •ೋ━━━━━┓ ​
      ❁Commannd INFO❁ 
┗━━━━ೋ• ❄ •ೋ━━━━━┛

******************
|| Bc           ||
|| Mid @        ||
|| Check:       ||
|| Copy @       ||
|| Info @       ||
|| Steal dp @   ||
|| Steal home @ ||
******************

┏━━━━ೋ• ❄ •ೋ━━━━━┓ ​
       ❁Commannd Bot❁ 
┗━━━━ೋ• ❄ •ೋ━━━━━┛
☆ Set ☆ 
☆ [Link on/off]
☆ [Contact on/off] 
☆ [Auto join on/off] 
☆ [Auto leave on/off] 
☆ [Auto add on/off] 
☆ [Jam on/off]
☆ [Like on/off]
☆ [Protect on/off]
☆ [qrprotect on/off]
☆ [Inviteprotect on/off]
☆ [Cancelprotect on/off]
☆ [Allprotect on/off]
☆ [Mprotect on/off]

┏━━━━ೋ• ❄ •ೋ━━━━━┓ ​
      ❁Commannd Mimic❁ 
┗━━━━ೋ• ❄ •ೋ━━━━━┛

☬ Mimic:on
☬ ListTarget
☬ Mimic:add: @
☬ Mimic:del: @

┏━━━━ೋ• ❄ •ೋ━━━━━┓ ​
     ❁Commannd Penting❁ 
┗━━━━ೋ• ❄ •ೋ━━━━━┛

􀜁􀇔 Guest On/Off
􀜁􀇔 Mad On/Off
􀜁􀇔 Qr On/Off
􀜁􀇔 Join On/off
􀜁􀇔 Autokick On/Off
􀜁􀇔 Auto cancel:on/off
􀜁􀇔 Ban @ 
􀜁􀇔 Blacklist @
􀜁􀇔 Unban @
􀜁􀇔 Kill Ban
􀜁􀇔 Kill @
􀜁􀇔 Nk
􀜁􀇔 Vk
􀜁􀇔 Mayhem
━━━━━━━━━━━━━━━━━
||||     「Info Bot :」     ||||
━━━━━━━━━━━━━━━━━
|🔰 Creator Bot              |
|   ™RadenRamadhan™         |
|   ™MiLLove™               |
|🔰 Based on   : LIN3-TCR    |
|🔰 Support By : ~S͟͟͟͞͞͞E͟͟͟͞͞͞R͟͟͟͞͞͞K͟͟͟͞͞͞*T͟͟͟͞͞͞E͟͟͟͞͞͞A͟͟͟͞͞͞M͟͟͟͞͞͞*~|
|🔰 Version 2.9.0.7          |
━━━━━━━━━━━━━━━━━
"""
KAC=[cl,ki,kk]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Bots=[mid,Amid,Bmid]
admin=["ucbd1374cb68242824dc21abcd7d6f669","u3fa0c0964985cd663d1fce84507e9b9b"]
creator=["ucbd1374cb68242824dc21abcd7d6f669","u3fa0c0964985cd663d1fce84507e9b9b"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Owner : line://ti/p/~rd.rmdhn",
    "lang":"JP",
    "comment":"Owner : line://ti/p/~rd,rmdhn",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"S͠E͠R͠K͠*B͠O͠T͠*1͠",
    "cName2":"S͠E͠R͠K͠*B͠O͠T͠*2",
    "cName3":"S͠E͠R͠K͠*B͠O͠T͠*3",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectguest":False,
    "Protectcancel":False,
    "ProtectQR":False,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n„1¤79„1¤79" + Name
                wait2['ROM'][op.param1][op.param2] = "„1¤79„1¤79" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if "stealgroupimage" in msg.text:
            group = client.getGroup(msg.to)
            sendMessage(msg.to,"Image Groups :\n=> http://dl.profile.line-cdn.net/" + group.pictureStatus)
        if "setbio:" in msg.text:
          string = msg.text.replace("setbio:","")
          if len(string.decode('utf-8')) <= 100000000000000000:
              profile = client.getProfile()
              profile.statusMessage = string
              client.updateProfile(profile)
              client.sendMessage(msg.to,"Update Bio Done")
          else:
              pass
        #------Open QR Kick start------#
        if op.type == 10:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                   G = cl.getGroup(op.param1)
                   G = ki.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   ki.kickoutFromGroup(op.param1,[op.param2])
                   cl.updateGroup(G)
        #------Open QR Kick finish-----#

        #------Invite User Kick start------#
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots:
                  random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#

        if op.type == 17:
            if op.param2 not in Bots:
                joinblacklist = op.param2.replace("„1¤7„1¤7",',')
                joinblacklistX = joinblacklist.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, joinblacklistX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 17:
           if op.param2 in Bots:
              return
           ginfo = cl.getGroup(op.param1)
           random.choice(KAC).sendText(op.param1, "Hallo " + cl.getContact(op.param2).displayName)
           random.choice(KAC).sendText(op.param1, "Selamat Datang Di Grup  " + str(ginfo.name))
           random.choice(KAC).sendText(op.param1, "Creator Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
           random.choice(KAC).sendText(op.param1, "Budayakan Baca Note yah Ka 😊\nSemoga Betah Kk 😘")
           random.choice(KAC).sendText(op.param1, "Silahkan Patuhi Peraturan & Jangan Nakal Ya!!!")  
           print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
           if op.param2 in Bots:
              return
           random.choice(KAC).sendText(op.param1, "Good Bye" + "Semoga Tenang Disana")
           print "MEMBER HAS LEFT THE GROUP"
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)


        if op.type == 19:
            if op.param3 in admin:
                 random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                 random.choice(KAC).inviteIntoGroup(op.param1,admin)
            else:
                pass

        if op.type == 19:
            if op.param2 not in admin:
                 random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                 wait["blacklist"][op.param2] = True
                 print "kicker kicked"
            else:
                pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group„1¤7„1¤7\n["+op.param1+"]\n„1¤7„1¤7\n["+op.param2+"]\n„1¤7„1¤7„1¤7„1¤7„1¤7„1¤7„1¤7¡è„1¤7„1¤70¡0„1¤7„1¤71ª0„1¤7„1¤7„1¤70¡0„1¤7„1¤7„1¤7„1¤7„1¤7\n„1¤70ô9„1¤70Š2„1¤7„1¤7‚7Ž8„1¤70§3„1¤70ý1„1¤70á6„1¤7„1¤71ª0„1¤7„1¤7„1¤7")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client„1¤7„1¤7„1¤7„1¤7„1¤7„1¤70Ù0„1¤7„1¤7or„1¤7„1¤7„1¤7„1¤7`„1¤70û20»4„1¤7„1¤714„1¤7„1¤70³9„1¤7„1¤7î”\n["+op.param1+"]\n„1¤7„1¤7\n["+op.param2+"]\n„1¤7„1¤7„1¤7„1¤7„1¤7„1¤7„1¤7¡è„1¤7„1¤70¡0„1¤7„1¤71ª0„1¤7„1¤7„1¤70¡0„1¤7„1¤7„1¤7„1¤7„1¤7\n„1¤70ô9„1¤70Š2„1¤7„1¤7‚7Ž8„1¤70§3„1¤70ý1„1¤70á6„1¤7„1¤71ª0„1¤7„1¤7„1¤7")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client„1¤7„1¤7„1¤7„1¤7„1¤7„1¤70Ù0„1¤7„1¤7or„1¤7„1¤7„1¤7„1¤7`„1¤70û20»4„1¤7„1¤714„1¤7„1¤70³9„1¤7„1¤7î”\n["+op.param1+"]\n„1¤7„1¤7\n["+op.param2+"]\n„1¤7„1¤7„1¤7„1¤7„1¤7„1¤7„1¤7¡è„1¤7„1¤70¡0„1¤7„1¤71ª0„1¤7„1¤7„1¤70¡0„1¤7„1¤7„1¤7„1¤7„1¤7\n„1¤70ô9„1¤70Š2„1¤7„1¤7‚7Ž8„1¤70§3„1¤70ý1„1¤70á6„1¤7„1¤71ª0„1¤7„1¤7„1¤7")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client„1¤7„1¤7„1¤7„1¤7„1¤7„1¤70Ù0„1¤7„1¤7or„1¤7„1¤7„1¤7„1¤7`„1¤70û20»4„1¤7„1¤714„1¤7„1¤70³9„1¤7„1¤7î”\n["+op.param1+"]\n„1¤7„1¤7\n["+op.param2+"]\n„1¤7„1¤7„1¤7„1¤7„1¤7„1¤7„1¤7¡è„1¤7„1¤70¡0„1¤7„1¤71ª0„1¤7„1¤7„1¤70¡0„1¤7„1¤7„1¤7„1¤7„1¤7\n„1¤70ô9„1¤70Š2„1¤7„1¤7‚7Ž8„1¤70§3„1¤70ý1„1¤70á6„1¤7„1¤71ª0„1¤7„1¤7„1¤7")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message

        #------Cancel User Kick start------#
        if op.type == 32:
            if op.param2 not in Bots:
               cl.kickoutFromGroup(op.param1,[op.param2])
        #-----Cancel User Kick Finish------#

            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL„1¤70„1¤79„1¤76„1¤79„1¤7„1¤7\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpMessage)
					else:
						cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Gn ","")
						cl.updateGroup(X)
					else:
						cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot1 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Cv1 gn ","")
						ki.updateGroup(X)
					else:
						ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot2 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Cv2 gn ","")
						kk.updateGroup(X)
					else:
						kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot3 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Cv3 gn ","")
						kc.updateGroup(X)
					else:
						kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Kick ","")
					cl.kickoutFromGroup(msg.to,[midd])
            elif "Bot1 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv1 kick ","")
					ki.kickoutFromGroup(msg.to,[midd])
            elif "Bot2 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv2 kick ","")
					kk.kickoutFromGroup(msg.to,[midd])
            elif "Bot3 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv3 kick ","")
					kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Invite ","")
					cl.findAndAddContactsByMid(midd)
					cl.inviteIntoGroup(msg.to,[midd])
            elif "Bot1 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv1 invite ","")
					ki.findAndAddContactsByMid(midd)
					ki.inviteIntoGroup(msg.to,[midd])
            elif "Bot2 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv2 invite ","")
					kk.findAndAddContactsByMid(midd)
					kk.inviteIntoGroup(msg.to,[midd])
            elif "Bot3 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv3 invite ","")
					kc.findAndAddContactsByMid(midd)
					kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': mid}
					cl.sendMessage(msg)
            elif msg.text in ["Bot1"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Amid}
					ki.sendMessage(msg)
            elif msg.text in ["Bot2"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Bmid}
					kk.sendMessage(msg)
            elif msg.text in ["Ã¦â€žâ„1¤7ºÃ£ÂÂ®Ã£Æ’â„1¤7”Ã£Æ’Â¬Ã£â„1¤7šÂ¼Ã£Æ’Â³Ã£Æ’Ë„1¤7","Gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '5'}
					msg.text = None
					cl.sendMessage(msg)
            elif msg.text in ["Ã¦â€žâ„1¤7ºÃ£ÂÂ®Ã£Æ’â„1¤7”Ã£Æ’Â¬Ã£â„1¤7šÂ¼Ã£Æ’Â³Ã£Æ’Ë„1¤7","Bot1 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '6'}
					msg.text = None
					ki.sendMessage(msg)
            elif msg.text in ["Ã¦â€žâ„1¤7ºÃ£ÂÂ®Ã£Æ’â„1¤7”Ã£Æ’Â¬Ã£â„1¤7šÂ¼Ã£Æ’Â³Ã£Æ’Ë„1¤7","Bot2 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '8'}
					msg.text = None
					kk.sendMessage(msg)
            elif msg.text in ["Ã¦â€žâ„1¤7ºÃ£ÂÂ®Ã£Æ’â„1¤7”Ã£Æ’Â¬Ã£â„1¤7šÂ¼Ã£Æ’Â³Ã£Æ’Ë„1¤7","Bot3 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '10'}
					msg.text = None
					kc.sendMessage(msg)
            elif msg.text in ["Ã¦â€žâ„1¤7ºÃ£ÂÂ®Ã£Æ’â„1¤7”Ã£Æ’Â¬Ã£â„1¤7šÂ¼Ã£Æ’Â³Ã£Æ’Ë„1¤7","All gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '12'}
					msg.text = None
					ki.sendMessage(msg)
					kk.sendMessage(msg)
					kc.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						if X.invitee is not None:
							gInviMids = [contact.mid for contact in X.invitee]
							cl.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"No one is inviting")
							else:
								cl.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						G = k3.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							k3.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								k3.sendText(msg.to,"No one is inviting")
							else:
								k3.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							k3.sendText(msg.to,"Can not be used outside the group")
						else:
							k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on","Urlon"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 ourl","Cv1 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Done Chivas")
						else:
							ki.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 ourl","Cv2 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = False
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Done Chivas")
						else:
							kk.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 ourl","Cv3 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = False
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done Chivas")
						else:
							kc.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off","Urloff"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = True
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot1 curl","Bot1 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = ki.getGroup(msg.to)
						X.preventJoinByTicket = True
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Done Chivas")
						else:
							ki.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Can not be used outside the group")
						else:
							ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot2 curl","Bot2 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = True
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Done Chivas")
						else:
							kk.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot3 curl","Bot3 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = True
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done Chivas")
						else:
							kc.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
					ki.sendText(msg.to,Amid)
					kk.sendText(msg.to,Bmid)
					kc.sendText(msg.to,Cmid)
            elif "Mid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
            elif "Bot1 mid" == msg.text:
				if msg.from_ in admin:
					ki.sendText(msg.to,Amid)
            elif "Bot2 mid" == msg.text:
				if msg.from_ in admin:
					kk.sendText(msg.to,Bmid)
            elif "Bot3 mid" == msg.text:
				if msg.from_ in admin:
					kc.sendText(msg.to,Cmid)
            elif msg.text in ["Wkwk"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "100",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "10",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "9",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["You"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "7",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "6",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Please"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "4",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "3",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "110",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "101",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
            elif msg.text in ["Wc"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "247",
										"STKPKGID": "3",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Cury PP"]:
				if msg.from_ in admin:
					tl_text = msg.text.replace("TL","")
					cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cn ","")
					if len(string.decode('utf-8')) <= 20:
						profile = cl.getProfile()
						profile.displayName = string
						cl.updateProfile(profile)
						cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv1 rename "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cv1 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = ki.getProfile()
						profile_B.displayName = string
						ki.updateProfile(profile_B)
						ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv2 rename "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cv2 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = kk.getProfile()
						profile_B.displayName = string
						kk.updateProfile(profile_B)
						kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
				if msg.from_ in admin:
					mmid = msg.text.replace("Mc ","")
					msg.contentType = 13
					msg.contentMetadata = {"mid":mmid}
					cl.sendMessage(msg)
            elif msg.text in ["Guest On","guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Guest Off","guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Ã©â‚¬Â£Ã§ÂµÂ¡Ã¥â„1¤7¦Ë„1¤7:Ã£â€šÂªÃ£Æ’Â„1¤7","K on","Contact on","Ã©Â¡Â¯Ã§Â¤ÂºÃ¯Â¼Å¡Ã©â€“â„1¤7„1¤7"]:
				if msg.from_ in admin:
					if wait["contact"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["contact"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Ã©â‚¬Â£Ã§ÂµÂ¡Ã¥â„1¤7¦Ë„1¤7:Ã£â€šÂªÃ£Æ’â„1¤7„1¤7","K off","Contact off","Ã©Â¡Â¯Ã§Â¤ÂºÃ¯Â¼Å¡Ã©â€”Å„1¤7"]:
				if msg.from_ in admin:
					if wait["contact"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done ")
					else:
						wait["contact"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã¥Ââ„1¤7šÃ¥Å„1¤7 :Ã£â€šÂªÃ£Æ’Â„1¤7","Join on","Auto join:on","Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã¥ÂÆ’Ã¥Å„1¤7 Ã¯Â¼Å¡Ã©â€“â„1¤7„1¤7"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã¥Ââ„1¤7šÃ¥Å„1¤7 :Ã£â€šÂªÃ£Æ’â„1¤7„1¤7","Join off","Auto join:off","Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã¥ÂÆ’Ã¥Å„1¤7 Ã¯Â¼Å¡Ã©â€”Å„1¤7"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
				if msg.from_ in admin:
					try:
						strnum = msg.text.replace("Gcancel:","")
						if strnum == "off":
							wait["autoCancel"]["on"] = False
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
							else:
								cl.sendText(msg.to,"Ã¥â€¦Â³Ã¤Âºâ„1¤7 Ã©â„1¤7šâ‚¬Ã¨Â¯Â·Ã¦â€¹â„1¤7™Ã§Â»ÂÃ£â‚¬â€šÃ¨Â¦ÂÃ¦â„1¤7”Â¶Ã¥Â¼â‚¬Ã¨Â¯Â·Ã¦Å’â€¡Ã¥Â®Å¡Ã¤ÂºÂºÃ¦â„1¤7¢Â°Ã¥Ââ„1¤7˜Ã©â‚¬Â")
						else:
							num =  int(strnum)
							wait["autoCancel"]["on"] = True
							if wait["lang"] == "JP":
								cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
							else:
								cl.sendText(msg.to,strnum + "Ã¤Â½Â¿Ã¤ÂºÂºÃ¤Â»Â¥Ã¤Â¸â€¹Ã§Å¡â„1¤7žÃ¥Â°ÂÃ§Â»â„1¤7žÃ§â„1¤7Â¨Ã¨â„1¤7¡ÂªÃ¥Å Â¨Ã©â„1¤7šâ‚¬Ã¨Â¯Â·Ã¦â€¹â„1¤7™Ã§Â»Â„1¤7")
					except:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Value is wrong")
						else:
							cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã©â‚¬â‚¬Ã¥â„1¤7¡Â„1¤7:Ã£â€šÂªÃ£Æ’Â„1¤7","Leave on","Auto leave:on","Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã©â‚¬â‚¬Ã¥â„1¤7¡ÂºÃ¯Â¼Å¡Ã©â„1¤7“â„1¤7„1¤7"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â‚¬Ã£â‚¬â„1¤7„1¤7")
            elif msg.text in ["Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã©â‚¬â‚¬Ã¥â„1¤7¡Â„1¤7:Ã£â€šÂªÃ£Æ’â„1¤7„1¤7","Leave off","Auto leave:off","Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â„1¤7¹â„1¤7¢Ã©â‚¬â‚¬Ã¥â„1¤7¡ÂºÃ¯Â¼Å¡Ã©â„1¤7”Å„1¤7"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already")
            elif msg.text in ["Ã¥â€¦Â±Ã¦Å“â„1¤7„1¤7:Ã£â€šÂªÃ£Æ’Â„1¤7","Share on","Share on"]:
				if msg.from_ in admin:
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â‚¬Ã£â‚¬â„1¤7„1¤7")
            elif msg.text in ["Ã¥â€¦Â±Ã¦Å“â„1¤7„1¤7:Ã£â€šÂªÃ£Æ’â„1¤7„1¤7","Share off","Share off"]:
				if msg.from_ in admin:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â„1¤7¦Â³Ã¦â„1¤7“Â­Ã£â‚¬â€„1¤7")
            elif msg.text in ["Key","help","Help"]:
                cl.sendText(msg.to,helpMessage)
#--------------------------------------------------------
            elif "Leaveallgroup" == msg.text:
                gid = cl.getGroupIdsJoined()
                if msg.from_ in Creator:
                            for i in gid:
                             cl.sendText(i,"Bot di paksa keluar oleh owner!")
                             cl.leaveGroup(i)
                             ki.leaveGroup(i)
                             kk.leaveGroup(i)
                             kc.leaveGroup(i)
                             cl.sendText(msg.to,"Success leave all group")
#--------------------------------------------------------
            elif "Recover" in msg.text:
                if msg.from_ in admin:
                        thisgroup = cl.getGroups([msg.to])
                        Mids = [contact.mid for contact in thisgroup[0].members]
                        mi_d = Mids[:33]
                        cl.createGroup("Recover", mi_d)
                        cl.sendText(msg.to,"Success recover")
#--------------------------------------------------------
            elif msg.text in ["Remove chat"]:
                if msg.from_ in admin:
                        cl.removeAllMessages(op.param2)
                        ki.removeAllMessages(op.param2)
                        kk.removeAllMessages(op.param2)
                        cl.sendText(msg.to,"Removed all chat succes")
#--------------------------------------------------------
            elif "Set member: " in msg.text:
                if msg.from_ in admin:
                    jml = msg.text.replace("Set member: ","")
                    wait["Members"] = int(jml)
                    cl.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)
                else:
                    cl.sendText(msg.to, "Khusus Admin")
#--------------------------------------------------------
            elif msg.text.lower() == 'Set':
                md = "✃┈┈☫ รεƭƭเɳɠร ☫┈┈✍ \n\n"
                if wait["contact"] == True: md+=" ❂͜͡☆➣ Contact:on \n"
                else: md+=" ❂͜͡☆➣Contact:off􀜁􀄰 \n"
                if wait["autoJoin"] == True: md+=" ❂͜͡☆➣ Auto Join:on \n"
                else: md +=" ❂͜͡☆➣ Auto Join:off \n"
                if wait["autoCancel"]["on"] == True:md+=" ❂͜͡☆➣ Auto cancel:" + str(wait["autoCancel"]["members"]) + " \n"
                else: md+=" ❂͜͡☆➣ Group cancel:off \n"
                if wait["likeOn"] == True: md+=" ❂͜͡☆➣ Auto Like:on \n"
                else: md+=" ❂͜͡☆➣ Auto Like:off \n"
                if wait["leaveRoom"] == True: md+=" ❂͜͡☆➣ Auto leave:on \n"
                else: md+=" ❂͜͡☆➣ Auto leave:off \n"
                if wait["timeline"] == True: md+=" ❂͜͡☆➣ Share:on \n"
                else:md+=" ❂͜͡☆➣ Share:off \n"
                if wait["autoAdd"] == True: md+=" ❂͜͡☆➣ Auto add:on \n"
                else:md+=" ❂͜͡☆➣ Auto add:off \n"
                if wait["Backup"] == True: md+=" ❂͜͡☆➣ Backup:on \n"
                else:md+=" ❂͜͡☆➣ Backup:off \n"
                if wait["commentOn"] == True: md+=" ❂͜͡☆➣ Auto Coment:on \n"
                else:md+=" ❂͜͡☆➣ Auto Coment:off \n"
                if wait["protect"] == True: md+=" ❂͜͡☆➣ Protect:on \n"
                else:md+=" ❂͜͡☆➣Protect:off \n"
                if wait["linkprotect"] == True: md+=" ❂͜͡☆➣ ProtectQr:on \n"
                else:md+=" ❂͜͡☆➣ PotectQr:off \n"
                if wait["inviteprotect"] == True: md+=" ❂͜͡☆➣ Invite Protect:on \n"
                else:md+=" ❂͜͡☆➣ Invite Protect:off \n"
                if wait["MProtection"] == True: md+=" ❂͜͡☆➣ MProtection:on \n"
                else: md+=" ❂͜͡☆➣ MProtection:off \n"
                if wait["cancelprotect"] == True: md+=" ❂͜͡☆➣ Cancel Protect:on \n"
                else:md+=" ❂͜͡☆➣ Cancel Protect:off \n"
                if wait["atjointicket"] == True: md+=" ❂͜͡☆➣ AtJoin Group Ticket:on \n"
                else:md+=" ❂͜͡☆➣ Atjoin Group Ticket:off \n\n ☬⟿ℛℹℴ⟿Ȿ⟿ℬᝪᝨ⟿☬"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'Me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif cms(msg.text,["Creator","Mee"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendText(msg.to,"down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊upupupup")            
            elif "Set album:" in msg.text:
                gid = msg.text.replace("Set album:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album👈")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak👈")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "æžš\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    cl.sendText(msg.to,mg)
            elif "Album " in msg.text:
                gid = msg.text.replace("Album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 pieces\n"
            elif "Hapus album " in msg.text:
                gid = msg.text.replace("Hapus album ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["gid"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
            elif msg.text.lower() == 'Group id':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Group cancelall","Rejectall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif msg.text in ["MProtection:on"]:
                if wait["MProtection"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Member Protection On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                   wait["MProtection"] = True
                   if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Member Protection On")
                   else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["MProtection:off"]:
                if wait["MProtection"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Member Protection Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                   wait["MProtection"] = False
                   if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Member Protection Off")
                   else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Backup:on","Backup on"]:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
                    else:
                        cl.sendText(msg.to,"Backup On")
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup On")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Backup:off","Backup off"]:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Backup Off")
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup Off")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Auto add on","Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On👈")
                    else:
                        cl.sendText(msg.to,"Already On👈")
            elif msg.text in ["Auto add off","Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off👈")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add:" in msg.text:
                wait["message"] = msg.text.replace("Pesan add:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Commment Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Comment:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ👈")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Comment:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Comen","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif "gurl+" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl+","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"ã‚°ãƒ«ãƒ¼ãƒ—ä»¥å¤–ã§ã¯ä½¿ç”¨ã§ãã¾ã›ã‚“??")
            
            elif "gurl" in msg.text:
                if msg.toType == 1:
                    tid = msg.text.replace("gurl","")
                    turl = ki.getUserTicket(tid)
                    ki.sendText(msg.to,"line://ti/p" + turl)
                else:
                    ki.sendText(msg.to,"error")

            elif "gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Bladd"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Bldel"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")

            elif msg.text in ["Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    kontak = cl.getContacts(commentBlack)
                num=1
                msgs="User Blacklist List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blacklist user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)

            elif msg.text.lower() == 'Jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'Jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) < 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'Up':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")
#-----------------------------------------------
            elif msg.text in ["Tagall"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    ki.sendMessage(msg)
                except Exception as error:
                    print error
#-----------------------------------------------

            elif msg.text in ["Serk Masuk","Serk join","Beb masuk"]:
				if msg.from_ in admin:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							ki.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							kk.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							G = cl.getGroup(msg.to)
							G.preventJoinByTicket = True
							ki.updateGroup(G)
							kk.updateGroup(G)
							print "kicker ok" 
							G.preventJoinByTicket(G)
							ki.updateGroup(G)
							kk.updateGroup(G)
							cl.sendText(msg.to,"Bot Semua Join!!")
							cl.sendText(msg.to,"Respon!!")
							cl.sendText(msg.to,"S͠E͠R͠K͠*B͠O͠T͠*1͠ Respon")
							ki.sendText(msg.to,"S͠E͠R͠K͠*B͠O͠T͠*2 Respon")
							kk.sendText(msg.to,"S͠E͠R͠K͠*B͠O͠T͠*3 Respon")
							cl.sendText(msg.to,"Semua Respon Boss")
#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Cv3 join"]:
				if msg.from_ in admin:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							kc.acceptGroupInvitationByTicket(msg.to,Ticket)
							print "kicker ok"
							G.preventJoinByTicket = True
							kc.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Serk out","Serk pulang","Beb pulang"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							cl.leaveGroup(msg.to)
							ki.leaveGroup(msg.to)
							kk.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye 1"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye 2"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
							kk.leaveGroup(msg.to)
						except:
							pass
			elif msg.text in ["Cv1 @bye"]:
                if msg.from_ in admin:
				    if msg.toType == 2:
					    ginfo = cl.getGroup(msg.to)
					    try:
					     	ki.leaveGroup(msg.to)
					    except:
					     	pass
            elif msg.text in ["Cv2 @bye"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kk.leaveGroup(msg.to)
						except:
							pass
			elif msg.text in ["Cv3 @bye"]:
				if msg.toType == 2:
					ginfo = cl.getGroup(msg.to)
					try:
						kc.leaveGroup(msg.to)
					except:
						pass
#-----------------------------------------------
            elif msg.text in ["Kill"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = ki.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							kk.sendText(msg.to,"Fuck You")
							kc.sendText(msg.to,"Fuck You")
							return
						for jj in matched_list:
							try:
								klist=[ki,kk,kc]
								kicker=random.choice(klist)
								kicker.kickoutFromGroup(msg.to,[jj])
								print (msg.to,[jj])
							except:
								print
            elif "Mayhem" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Mayhem","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    cl.sendText(msg.to,"¡¸ Mayhem\nMayhem is STARTING7¬8\n' abort' to abort7¬8")
                    ki.sendText(msg.to,"¡¸ Mayhem ¡¹\n46 victims shall yell hul¡¤la¡¤ba¡¤loo7¬8\n/0·5h0¬5l0¬5b0¬50·4lo0Æ0o,0·4h0¬5l0¬5b0¬50·5lo0Æ0o/")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Tidak ditemukan")
                    else:
                        for target in targets:
                            if not target in Bots:
                                try:
                                   klist=[cl,ki,kk]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   ki.sendText(msg.to,"Mayhem done")
            elif "Nk " in msg.text:
				if msg.from_ in admin:
					if msg.from_ in admin:
						nk0 = msg.text.replace("Nk ","")
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
							sendMessage(msg.to,"user does not exist")
							pass
						else:
							for target in targets:
									try:
										klist=[cl,ki,kk,kc]
										kicker=random.choice(klist)
										kicker.kickoutFromGroup(msg.to,[target])
										print (msg.to,[g.mid])
									except:
										ki.sendText(msg.to,"Succes Cv")
										kk.sendText(msg.to,"Fuck You"),
            elif "Blacklist @ " in msg.text:
				if msg.from_ in admin:
					_name = msg.text.replace("Blacklist @ ","")
					_kicktarget = _name.rstrip(' ')
					gs = ki2.getGroup(msg.to)
					targets = []
					for g in gs.members:
						if _kicktarget == g.displayName:
							targets.append(g.mid)
							if targets == []:
								cl.sendText(msg.to,"Not found")
							else:
								for target in targets:
									try:
										wait["blacklist"][target] = True
										f=codecs.open('st2__b.json','w','utf-8')
										json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
										k3.sendText(msg.to,"Succes Cv")
									except:
										ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Ban]ok"
						_name = msg.text.replace("Ban @","")
						_nametarget = _name.rstrip('  ')
						gs = cl.getGroup(msg.to)
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Tidak DiTemukan")
						else:
							for target in targets:
								try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									ki.sendText(msg.to,"Berhasil")
								except:
									ki.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Unban]ok"
						_name = msg.text.replace("Unban @","")
						_nametarget = _name.rstrip('  ')
						gs = cl.getGroup(msg.to)
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							cl.sendText(msg.to,"Tidak DiTemukan")
							ki.sendText(msg.to,"Tidak DiTemukan")
						else:
							for target in targets:
								try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									ki.sendText(msg.to,"Berhasil")
								except:
									ki.sendText(msg.to,"Berhasil")
#-----------------------------------------------
            elif "Vk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#-----------------------------------------------
            elif msg.text in ["Test"]:
				if msg.from_ in admin:
                  cl.sendText(msg.to,"Serk1 HADIR")
                  ki.sendText(msg.to,"Serk2 HADIR")
                  kk.sendText(msg.to,"Serk3 HADIR")
#-----------------------------------------------
            elif "Tob say " in msg.text:
					bctxt = msg.text.replace("Tob say ","")
					cl.sendText(msg.to,(bctxt))
					ki.sendText(msg.to,(bctxt))
					kk.sendText(msg.to,(bctxt))
            elif msg.text in ["Creator"]:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ucbd1374cb68242824dc21abcd7d6f669"}
                    ki.sendText(msg.to,"MyCreator")
                    kk.sendText(msg.to,"Jangan Lupa Di Add Ya!!!")
                    ki.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u3fa0c0964985cd663d1fce84507e9b9b"}
                    ki.sendText(msg.to,"MyCreator")
                    kk.sendText(msg.to,"Jangan Lupa Di Add Ya!!!")
                    ki.sendMessage(msg)
#-----------------------------------------------
            elif "Mid @" in msg.text:
                  _name = msg.text.replace("Mid @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  for g in gs.members:
                      if _nametarget == g.displayName:
                          cl.sendText(msg.to, g.mid)
                      else:
                          pass
#--------------------------------------------------------
            elif "Bc " in msg.text:
                bc = msg.text.replace("Bc: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                      cl.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~rd.rmdhn")
                      cl.sendText(msg.to,"Success BC Bos")
#--------------------------------------------------------
            elif "Spam " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam ")+str(txt[1])+" "+str(jmlh + " ","")
                tulisan = jmlh * (teks+"\n")
                 #@reno.a.w
                if txt[1] == "on":
                    if jmlh <= 300:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 300:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
#-----------------------------------------------
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Up Chat","Up chat","up chat","Upchat","upchat"]:
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"􀔃􀆶squared up!􏿿")
        #-------------Fungsi Spam Finish---------------------#
            elif msg.text == "Cctv On":
                    cl.sendText(msg.to, "Siderss")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    print wait2

            elif msg.text == "Ciduk":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "== Bakekok Sider == %s\nthat's it\n\nPeople who have ignored reads\n%skampret lo sider. 7¬8\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n¡¸set¡¹you can send 7¬8 read point will be created 7¬8")
#-----------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       ki.sendText(msg.to,"Grup Creator Telah Diinvite")
                       print "success inv gCreator"
                    except:
                       pass
#-----------------------------------------------
#-----------------------------------------------
            elif "Cstatus:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                else:
                    cl.sendText(msg.to,"Done")
            elif "Cstatus1:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                else:
                    ki.sendText(msg.to,"Done")
#-----------------------------------------------
            elif "Cname:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cname:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
            elif "Cname1:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cname:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.displayName = string
                    Ki.updateProfile(profile)
#-----------------------------------------------
            elif "Group pict" in msg.text.lower():            
                print "[command]steal executing"
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)
                print "[command]steal executed"

#-----------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
            elif "Rate" in msg.text:
                tanya = msg.text.replace("Rate","")
                jawab = ("10%","20%","30%","40%","50%","60%","70%","80%","90%","100%")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
            elif "Dosa @" in msg.text:
                tanya = msg.text.replace("Dosa @","")
                jawab = ("Tidak ada","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Dosanya " + tanya + " adalah " + jawaban + " Tobat dong ")
            elif "Pahala @" in msg.text:
                tanya = msg.text.replace("Pahala @","")
                jawab = ("Tidak ada","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Pahalanya " + tanya + " adalah " + jawaban + "Tingkatkan lagi  ")
#-------------------------------------------------------------
            elif "Stalk " in msg.text:
                print "[Command]Stalk executing"
                stalkID = msg.text.replace("Stalk ","")
                subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])
                files = glob.glob("tmp/*.jpg")
                for file in files:
                    os.rename(file,"tmp/tmp.jpg")
                fileTmp = glob.glob("tmp/tmp.jpg")
                if not fileTmp:
                    cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                    print "[Command]Stalk,executed - no image found"
                else:
                    image = upload_tempimage(client)
                    cl.sendText(msg.to, format(image['link']))
                    subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
                    print "[Command]Stalk executed - succes"
#----------------------------------------------
            elif '/music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('.music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
#-----------------------------------------------
            elif '/lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(param))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
#-------------------------------------------------
            elif msg.text in ["Backup","backup"]:
                if msg.from_ in admin:
                    try:
                       cl.updateDisplayPicture(backup.pictureStatus)
                       cl.updateProfile(backup)
                       cl.sendText(msg.to, "Telah kembali semula")
                    except Exception as e:
                       cl.sendText(msg.to, str(e))
#-----------------------------------------------
            elif "InviteMeTo: " in msg.text:
                if msg.from_ in creator:
                    gid = msg.text.replace("InviteMeTo: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin saya tidak di dalam grup itu")
#------------------------------------------------
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    ginfo = ki.getGroup(msg.to)
                    ginfo = kk.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
                    ki.sendMessage(msg)
                    kk.sendText(msg.to,"Pembuat Grup =>" + gCreator1)
#-----------------------------------------------
            elif "Admadd @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admadd @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan")
                                ki.sendText(msg.to,"Selamat Kamu Admin Baru")
                                kk.sendText(msg.to,"Selamat Ya Selamat")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Lu bukan Creator")
                    cl.sendText(msg.to,"Admin/Member Tidak Bisa Menggunakan Command Add Admin")
                    ki.sendText(msg.to,"Cuma Creator Yang bisa Menggunakan")
            elif "Admrem @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admrem @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus")
                                ki.sendText(msg.to,"Kamu DiPecat Jadi Admin :(")
                                kk.sendText(msg.to,"Yang Sabar Ya Boss..")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    ki.sendText(msg.to,"Command DiTolak")
                    cl.sendText(msg.to,"Admin atau Member Tidak Bisa Menggunakan")
                    ki.sendText(msg.to,"Admin atau Member Tidak Bisa Menggunakan")

            elif msg.text in ["Adminlist","adminlist"]:
              if msg.from_ in creator:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                    ki.sendText(msg.to,"The adminlist is empty")
                    kk.sendText(msg.to,"Tidak Ada Admin")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    ki.sendText(msg.to,"Tunggu...")
                    kk.sendText(msg.to,"Sabar Jink")
                    mc = ""
                    for mi_d in admin:
                        mc += "=>" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------------------------------
            elif msg.text in ["Mad On","mad on"]:
              if msg.from_ in admin:
                 if wait["Protectcancel"] == True:
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Dont cancel anyone ! cause me angry!")
                         ki.sendText(msg.to,"Jgn cancel undangan atau autokick!")
                     else:
                         cl.sendText(msg.to,"done")
                         ki.sendText(msg.to,"sudah")
                 else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                        ki.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"done")
            elif msg.text in ["Mad Off","mad off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                        ki.sendText(msg.to,"Protect Csncel Off")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"sudah")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                        ki.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"sudah")
#-----------------------------------------------
            elif msg.text.lower() == 'Runtime':
                eltime = time.time() - mulai
                van = "Serk_Bot Sudah Berjalan Selama "+waktu(eltime)
                cl.sendText(msg.to,van)
                
            elif msg.text is None:
                return
#--------------------------------------------------------
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass
#-------------------------------------------------------- 
            elif msg.text in ["Kernel","kernel"]:
                 if msg.from_ in admin:
                     botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
                     cl.sendText(msg.to, botKernel)
                     print "[Command]Kernel executed"
                 else:
                     cl.sendText(msg.to,"Command denied.")
                     cl.sendText(msg.to,"Admin permission required.")
                     print "[Error]Command denied - Admin permission required"
#--------------------------------------------------------
            elif "Steal dp @" in msg.text:
                nama = msg.text.replace("Steal dp @","")
                target = nama.rstrip(' ')
                van = cl.getGroup(msg.to)
                for linedev in van.members:
                    if target == linedev.displayName:
                        midddd = cl.getContact(linedev.mid)
                        PATH = "http://dl.profile.line-cdn.net/" + midddd.pictureStatus
                    cl.sendImageWithURL(msg.to,PATH)
#------------------------------------------
            elif "Steal home @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:                                                                   
                            ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#-----------------------------------------------------------
            elif msg.text in ["Protect Off","Mode Off"]:
              if msg.from_ in admin:
                if wait["Protectgroupname"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Gname Off")
                    else:
                        cl.sendText(msg.to,"Gname OFF")
                else:
                    wait["Protectgroupname"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Gname Off")
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")      
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Invite Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Invite Off")
                    else:
                        cl.sendText(msg.to,"done")
#-----------------------------------------------
            elif "Info @" in msg.text:
                nama = msg.text.replace("Info @","")
                target = nama.rstrip(' ')
                tob = cl.getGroup(msg.to)
                for g in tob.members:
                    if target == g.displayName:
                        mid = cl.getContact(g.mid)
                        try:
                            cover = cl.channel.getCover(g.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + mid.displayName + "\n[Mid]:\n" + tob.mid + "\n[BIO]:\n" + mid.statusMessage + "\n[Ava]:\nhttp://dl.profile.line-cdn.net/" + mid.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass
#-----------------------------------------------
            elif "Contact:" in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Contact:","")
                    msg.contentType = 13
                    msg.contentMetadata = {"mid":midd}
                    cl.sendMessage(msg)
                    ki.sendText("Tuh Midnya Boss")
#-----------------------------------------------
            elif msg.text in ["Protect On","Mode On"]:
              if msg.from_ in admin:
                if wait["Protectgroupname"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                        ki.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"Gname ON")
                        ki.sendText(msg.to,"Gname ON")
                else:
                    wait["Protectgroupname"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                        ki.sendText(msg.to,"Protect Group On")
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                        ki.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                        ki.sendText(msg.to,"Protect Cancel On")
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Block On")
                        ki.sendText(msg.to,"Auto Block On")
                    else:
                        cl.sendText(msg.to,"Block On")
                        ki.sendText(msg.to,"Block On")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Block On")
                        ki.sendText(msg.to,"Auto Block On")
                    else:
                        cl.sendText(msg.to,"Block On")
                        ki.sendText(msg.to,"Block On")
#-----------------------------------------------
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
            		cl.sendText(msg.to,text)
            		ki.sendText(msg.to,text)
            		kk.sendText(msg.to,text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            							 	 "STKID": "6",
            							 	 "STKPKGID": "1",
            							 	 "STKVER": "100" }
            			cl.sendMessage(msg)
            			ki.sendMessage(msg)
            			kk.sendMessage(msg)
            		elif msg.contentType == 13:
            			msg.contentType = 13
            			msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			cl.sendMessage(msg)
            			ki.sendMessage(msg)
            			kk.sendMessage(msg)
            elif "Mimic:" in msg.text:
            	if msg.from_ in admin:
            		cmd = msg.text.replace("Mimic:","")
            		if cmd == "on":
            			if mimic["status"] == False:
            				mimic["status"] = True
            				cl.sendText(msg.to,"Mimic on")
            				ki.sendText(msg.to,"Mimic on")
            				kk.sendText(msg.to,"Mimic Aktif")
            			else:
            				cl.sendText(msg.to,"Mimic already on")
            				ki.sendText(msg.to,"Mimic already on")
            				kk.sendText(msg.to,"Mimic Sudah On")
            		elif cmd == "off":
            			if mimic["status"] == True:
            				mimic["status"] = False
            				cl.sendText(msg.to,"Mimic off")
            				ki.sendText(msg.to,"Mimic off")
            				kk.sendText(msg.to,"Mimic Mati")
            			else:
            				cl.sendText(msg.to,"Mimic already off")
            				ki.sendText(msg.to,"Mimic already off")
            				kk.sendText(msg.to,"Mimic Telah Mati")
            		elif "add:" in cmd:
            			target0 = msg.text.replace("Mimic:add:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			gInfo = ki.getGroup(msg.to)
            			gInfo = kk.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            				ki.sendText(msg.to,"No targets")
            				kk.sendText(msg.to,"Tidak Ada Target")
            			else:
            				for target in targets:
            					try:
            						mimic["target"][target] = True
            						cl.sendText(msg.to,"Success added target")
            						ki.sendText(msg.to,"Success added target")
            						kk.sendText(msg.to,"Berhasil Menambahkan Target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed")
            						ki.sendText(msg.to,"Failed")
            						kk.sendText(msg.to,"Gagal")
            						break
            		elif "del:" in cmd:
            			target0 = msg.text.replace("Mimic:del:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			gInfo = ki.getGroup(msg.to)
            			gInfo = kk.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            				ki.sendText(msg.to,"No targets")
            				kk.sendText(msg.to,"Tidak Ada Target")
            			else:
            				for target in targets:
            					try:
            						del mimic["target"][target]
            						cl.sendText(msg.to,"Success deleted target")
            						ki.sendText(msg.to,"Success deleted target")
            						kk.sendText(msg.to,"Berhasil Menambahkan Target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed!")
            						ki.sendText(msg.to,"Failed!")
            						kk.sendText(msg.to,"Gagal")
            						break
            		elif cmd == "ListTarget":
            			if mimic["target"] == {}:
            				cl.sendText(msg.to,"No target")
            				ki.sendText(msg.to,"No target")
            				kk.sendText(msg.to,"Tidak Ada Target")
                    	else:
                    		lst = "<<Lit Target>>"
                    		total = len(mimic["target"])
                    		for a in mimic["target"]:
                				if mimic["target"][a] == True:
                					stat = "On"
                				else:
                					stat = "Off"
                				lst += "\n->" + cl.getContact(mi_d).displayName + ki.getContact(mi_d).displayName +" | " + stat
                                cl.sendText(msg.to,lst + "\nTotal:" + total)
                                ki.sendText(msg.to,lst + "\nTotal:" + total)
#-----------------------------------------------
            elif ".Youtube " in msg.text:
                 query = msg.text.replace(".Youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
#--------------------------------------------------------
            elif msg.text in ["Join on","Autojoin:on"]:
                wait["AutoJoin"] = True
                cl.sendText(msg.to,"AutoJoin Active")

            elif msg.text in ["Join off","Autojoin:off"]:
                wait["AutoJoin"] = False
                cl.sendText(msg.to,"AutoJoin inActive")

#--------------------------------------------------------
            elif msg.text in ["Autocancel:on"]:
                wait["AutoCancel"] = True
                cl.sendText(msg.to,"The group of people and below decided to automatically refuse invitation")
                print wait["AutoCancel"][msg.to]

            elif msg.text in ["Autocancel:off"]:
                wait["AutoCancel"] = False
                cl.sendText(msg.to,"Invitation refused turned off")
                print wait["AutoCancel"][msg.to]
#--------------------------------------------------------
            elif "Qr:on" in msg.text:
                wait["Qr"] = True
                cl.sendText(msg.to,"QR Protect Active")

            elif "Qr:off" in msg.text:
                wait["Qr"] = False
                cl.sendText(msg.to,"Qr Protect inActive")
#--------------------------------------------------------
            elif "Autokick:on" in msg.text:
                wait["AutoKick"] = True
                cl.sendText(msg.to,"AutoKick Active")

            elif "Autokick:off" in msg.text:
                wait["AutoKick"] = False
                cl.sendText(msg.to,"AutoKick inActive")
#--------------------------------------------------------
            elif msg.text in ["K on","Contact:on"]:
                wait["Contact"] = True
                cl.sendText(msg.to,"Contact Active")

            elif msg.text in ["K off","Contact:off"]:
                wait["Contact"] = False
                cl.sendText(msg.to,"Contact inActive")
#--------------------------------------------------------
            elif msg.text in ["hmm"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Batuk Kong??")
            elif msg.text in ["wkwkwk"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"malik mana ya , gw jadi kangen naena sama dia")
            elif msg.text in ["Cv say chomel pekok"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Chomel pekok ô€œô€…”Har Harô¿¿")
					kk.sendText(msg.to,"Chomel pekok ô€œô€…”Har Harô¿¿")
					kc.sendText(msg.to,"Chomel pekok ô€œô€…”Har Harô¿¿")
            elif msg.text in ["#welcome"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Selamat datang di Grup")
					kk.sendText(msg.to,"Jangan nakal ok!")
#-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Respon","respon","Respon Dong","respon dong"]:
              if msg.from_ in admin:
                #cl.sendText(msg.to,"Luffy On")
                ki.sendText(msg.to,"•••")
                kk.sendText(msg.to,"••••")
                ki.sendText(msg.to,"•••••")
                kk.sendText(msg.to,"••••••")
                ki.sendText(msg.to,"•••••••")
                kk.sendText(msg.to,"••••••••")
                ki.sendText(msg.to,"•••••••••")
                kk.sendText(msg.to,"••••••••••")
                ki.sendText(msg.to,"•••••••••••")
                cl.sendText(msg.to,"Respon Complete")
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
				if msg.from_ in admin:
					start = time.time()
					cl.sendText(msg.to, "Please Wait..")
					elapsed_time = time.time() - start
					cl.sendText(msg.to, "%sseconds" % (elapsed_time))
					ki.sendText(msg.to, "%sseconds" % (elapsed_time))
					kk.sendText(msg.to, "%sseconss" % (elapsed_time))

#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
				if msg.from_ in admin:
					wait["wblacklist"] = True
					cl.sendText(msg.to,"send contact")                  
            elif msg.text in ["Unban"]:
				if msg.from_ in admin:
					wait["dblacklist"] = True
					cl.sendText(msg.to,"send contact")					
            elif msg.text in ["Banlist"]:
				if msg.from_ in admin:
					if wait["blacklist"] == {}:
						cl.sendText(msg.to,"nothing")
					else:
						cl.sendText(msg.to,"Blacklist user")
						mc = ""
						for mi_d in wait["blacklist"]:
							mc += "„1¤7" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						cocoa = ""
						for mm in matched_list:
							cocoa += mm + "\n"
						cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							cl.sendText(msg.to,"There was no blacklist user")
							return
						for jj in matched_list:
							cl.kickoutFromGroup(msg.to,[jj])
						cl.sendText(msg.to,"Bye...")
            elif msg.text in ["Clear"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						group = ki.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.invitee]
						for _mid in gMembMids:
							cl.cancelGroupInvitation(msg.to,[_mid])
						cl.sendText(msg.to,"Cancel Success!")
						ki.sendText(msg.to,"Cancel Success!")
            elif "random:" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						strnum = msg.text.replace("random:","")
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						try:
							num = int(strnum)
							group = cl.getGroup(msg.to)
							for var in range(0,num):
								name = "".join([random.choice(source_str) for x in xrange(10)])
								time.sleep(0.01)
								group.name = name
								cl.updateGroup(group)
						except:
							cl.sendText(msg.to,"Error")
            elif "album" in msg.text:
				if msg.from_ in admin:
					try:
						albumtags = msg.text.replace("album","")
						gid = albumtags[:6]
						name = albumtags.replace(albumtags[:34],"")
						cl.createAlbum(gid,name)
						cl.sendText(msg.to,name + "created an album")
					except:
						cl.sendText(msg.to,"Error")
            elif "fakecÃ¢â€ â„1¤7„1¤7" in msg.text:
				if msg.from_ in admin:
					try:
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						name = "".join([random.choice(source_str) for x in xrange(10)])
						anu = msg.text.replace("fakecÃ¢â€ â„1¤7„1¤7","")
						cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
					except Exception as e:
						try:
							cl.sendText(msg.to,str(e))
						except:
							pass
#--------------------------------------------------------
            elif "Cleanse" in msg.text:
                if msg.toType == 2:
                    print "Kick all member"
                    _name = msg.text.replace("Cleanse","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"Dadaaah~")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                 if target not in admin:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except Exception as e:
                                    cl.sendText(msg.to,str(e))
                                    cl.inviteIntoGroup(msg.to, targets)
#--------------------------------------------------------
#Restart_Program
            elif msg.text in ["Bot:restart"]:
                if msg.from_ in Creator:
                    cl.sendText(msg.to, "Bot has been restarted")
                    restart_program()
                    print "@Restart"
                else:
                    cl.sendText(msg.to, "No Access")
#--------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
			for zx in range(0,20):
				hasil = cl.activity(limit=20)
				if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
					try:    
						cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By ™RadenRamadhan™ \n\nLike Like LIke\nId: line://ti/p/~rd.rmdhn")
						kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By ™RadenRamadhan™ \n\nLike Like LIke\nId: line://line.me/R/ti/p/%40dlh6592k")
                        ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By ™RadenRamadhan™ \n\nLike Like LIke\nId: line://line.me/R/ti/p/%40dlh6592k")
                        cl.sendText(msg.to, "Success~")
                        print "Lagi Otw Nge-Like"
					except:
							pass
				else:
						print "Sudah DiLike Semua Kok"
			time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
