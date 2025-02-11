# Repthon - @Repthon
# Copyright (C) 2022 Repthon . All Rights Reserved
#< https://t.me/ZedThon >
# This file is a part of < https://github.com/RepthonArabic/RepthonAr/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/RepthonArabic/RepthonAr/blob/master/LICENSE/>.

import os
import aiohttp
import requests
import re
import time
import sys
import asyncio
from validators.url import url
from subprocess import run as runapp
from datetime import datetime
from pySmartDL import SmartDL
from pathlib import Path
from platform import python_version
from telethon import Button, events ,types, version
from telethon.events import CallbackQuery, InlineQuery
from telethon.utils import get_display_name
from telethon.errors import QueryIdInvalidError
from telethon.tl.types import InputMessagesFilterDocument
from zthon import StartTime, zedub, zedversion
from ..Config import Config
from ..core import check_owner, pool
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..helpers.utils import reply_id, get_user_from_event, _format
from ..helpers.tools import media_type
from . import media_type, progress
from ..utils import load_module, remove_plugin
from ..sql_helper.global_collection import add_to_collectionlist, del_keyword_collectionlist, get_collectionlist_items
from . import SUDO_LIST, edit_delete, edit_or_reply, reply_id, BOTLOG, BOTLOG_CHATID, HEROKU_APP, mention


LOGS = logging.getLogger(os.path.basename(__name__))
LOGS1 = logging.getLogger(__name__)
ZORDR = gvarstatus("Z_ORDR") or "الاوامر"
ZLORDR = gvarstatus("Z_LORDR") or "الاوامر"
ppath = os.path.join(os.getcwd(), "temp", "githubuser.jpg")
GIT_TEMP_DIR = "./temp/"
cmdhd = Config.COMMAND_HAND_LER
DELETE_TIMEOUT = 1
USERID = bot.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
ZEDPIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/e45d01cc4a8b66cba94ee.jpg"
ZPIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/e45d01cc4a8b66cba94ee.jpg"
Malath = f"**🖥┊لـوحـة اوامـر 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 الشفـافـه **\n**🧑🏻‍💻┊المستخـدم ↶** {mention} \n\n**•❐• قـائمـه الاوامـر الـعـامـه :**\n**•❶• اوامــر الـبحـث والـتحميـل **\n**•❷• اوامــر الـبـوت **\n**•❸• اوامــر الـوقـتـي **\n**•❹• اوامــر الـكــروب¹ **\n**•❺• اوامــر الـكــروب² **\n**•❻• اوامــر الـحسـاب **\n**•❼• اوامــر الميـديـا والـصيــغ **\n**•❽• اوامــر الـفــارات **\n**•❾• اوامــر الخـدمــات **\n**•❿• اوامــر الـتســليــه والالـعـاب **\n\n**•❐• او استخـدم الامـر** `.الأوامر` **لعـرض الاوامـر مع الوصـف**"
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")


#لـوحــة الاوامــر - حقــوق ريبـــثون
@zedub.tgbot.on(events.InlineQuery)
@check_owner
async def zed_handler(event):
    builder = event.builder
    result = None
    query = event.text
    await zedub.get_me()
    if query.startswith("الاوامر") and event.query.user_id == zedub.uid:
        buttons = [[Button.inline("•❶•", data="ahmed1"), Button.inline("•❷•", data="ahmed2"), Button.inline("•❸•", data="ahmed3"), Button.inline("•❹•", data="ahmed4"), Button.inline("•❺•", data="ahmed5"),],[Button.inline("•❻•", data="ahmed6"), Button.inline("•❼•", data="ahmed7"), Button.inline("•❽•", data="ahmed8"), Button.inline("•❾•", data="ahmed9"), Button.inline("•❿•", data="ahmad10"),]]
        if ZEDPIC and ZEDPIC.endswith((".jpg", ".png")):
            result = builder.photo(ZEDPIC,text=Malath, buttons=buttons, link_preview=True)
        elif ZEDPIC:
            result = builder.document(ZEDPIC,title="zedub", text=Malath ,buttons=buttons, link_preview=True)
        else:
            result = builder.article(title="zedub",text=Malath,buttons=buttons,link_preview=True)
        await event.answer([result] if result else None)
@zedub.zed_cmd(pattern="الاوامر(?: |$)(.*)")
async def repozedub(event):
    if event.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await event.client.inline_query(TG_BOT, "الاوامر")
    await response[0].click(event.chat_id)
    await event.delete()


@zedub.zed_cmd(pattern=f"الأوامر(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, f"𓆰 [𝗦𝗢𝗨𝗥𝗖𝗘 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 - قائمــة الاوامــر العــامــه](t.me/Repthon) 𓆪\n◐━─━─━─━─**R𝙀𝙋𝙏𝙃𝙊𝙉𖠏**─━─━─━─━◐\n**⌔╎مـرحبـاً عـزيـزي {mention} اضغـط ع الامـر لـ النسـخ - ملاحظـه : ضـع نقطه (.) بداية كل امـر :**\n\n `.م1`**   ➪ اوامـر البحـث والتحميــل** \n\n `.م2`**   ➪ اوامـر البــوت**\n\n `.م3`**   ➪ اوامـر الـوقتــي**\n\n `.م4`**   ➪ اوامـر المجمــوعــه¹**\n\n `.م5`**   ➪ اوامـر المجمــوعــه²**\n\n `.م6`**   ➪ اوامـر الحســاب**\n\n `.م7`**   ➪ اوامـر الميـديـا والصيــغ**\n\n `.م8`**   ➪ اوامـر الفــارات**\n\n `.م9`**   ➪ اوامـر الـخدمــات**\n\n `.م10`** ➪ اوامـر التســليـه والالـعــاب**\n\n ◐━─━─━─━─**𓆩𝐑𝐞𝐩𝐭𝐡𝐨𝐧𓆪**─━─━─━─━◐\n 𓆩 [𝗦𝗢𝗨𝗥𝗖𝗘 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 - قنـاة السـورس](t.me/Repthon) 𓆪")

@zedub.zed_cmd(pattern="م1(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 - اوامــر البحـث والتحميــل](t.me/Repthon) 𓆪\n\n**⎞𝟏⎝** `.بحث`\n**•• ⦇.بحث + اسـم الاغنيـه⦈ لـ تحميـل الاغـاني مـن اليـوتيـوب**\n\n**⎞𝟐⎝** `.اغنيه`\n**•• ⦇.اغنيه + اسـم الاغنيـه⦈ امـر آخـر لـ تحميـل الاغـاني مـن اليـوتيـوب**\n\n**⎞𝟑⎝** `.فيديو`\n**•• ⦇.فيديو + اسـم المقطـع⦈ لـ تحميـل مقـاطع الفيـديـو مـن اليـوتيـوب**\n\n**⎞𝟒⎝** `.تحميل صوت`\n**•• ⦇.تحميل صوت + رابـط⦈ تحميـل المقـاطع الصـوتيه مـن اليـوتيـوب عبـر الرابـط**\n\n**⎞𝟓⎝** `.تحميل فيديو`\n**•• ⦇.تحميل فيديو + رابـط⦈ لـ تحميـل مقـاطع الفيـديـو مـن اليـوتيـوب عبـر الرابـط**\n\n**⎞𝟔⎝** `.يوتيوب`\n**•• ⦇.يوتيوب + كلمـه⦈ البحـث عـن روابـط علـى يوتيـوب **\n\n**⎞𝟕⎝** `.انستا`\n**•• ⦇.انستا + رابـط⦈ لـ تحميـل الصـور ومقـاطع الفيـديـو مـن الانستجــرام**\n\n**⎞𝟖⎝** `.صور`\n**•• ⦇. صور + كلمه⦈ او ⦇.صور + عدد + كلمه⦈ لـ تحميـل الصـور مـن جـوجـل**\n\n**⎞𝟗⎝** `.متحركه`\n**•• ⦇.متحركه + كلمه⦈ او ⦇.متحركه + كلمه + / + عـدد⦈ لـ تحميـل صـور متحـركـه مـن جـوجـل..**\n\n**⎞𝟏𝟎⎝** `.تيك`\n**•• ⦇.تيك + رابـط⦈ او ⦇.توك بالـرد ع رابـط⦈ لـ تحميـل الفيـديـو مـن تيـك تـوك**\n\n**⎞𝟏𝟏⎝** `.لايكي`\n**•• ⦇.لايكي + رابـط⦈ لـ تحميـل الفيـديـو مـن لايكـي**\n\n**⎞𝟏𝟐⎝** `.فيسبوك`\n**•• ⦇.فيسبوك + رابـط⦈ او ⦇.فيس بالـرد ع رابـط⦈ لـ تحميـل الفيـديـو مـن فيـس بـوك**\n\n**⎞𝟏𝟑⎝** `.تويتر`\n**•• ⦇.تويتر + رابـط⦈ لـ تحميـل الفيـديـو مـن تـويتـر**\n\n**⎞𝟏𝟒⎝** `.بن`\n**•• ⦇.بن + رابـط⦈ لـ تحميـل الفيـديـو مـن بنتـرسـت**\n\n**⎞𝟏𝟓⎝** `.سناب`\n**•• ⦇.سناب + رابـط⦈ لـ تحميـل الفيـديـو مـن سنـاب شـات**\n\n**⎞𝟏𝟔⎝** `.كتاب`\n**•• ⦇.كتاب + اسم كتـاب او روايـه⦈ لـ تحميـل الكـتب والروايـات**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉](t.me/Repthon) 𓆪")    
@zedub.zed_cmd(pattern="م2(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 - اوامــر البــوت](t.me/Repthon) 𓆪\n\n**⎞𝟏⎝** `.اعاده تشغيل`\n**•• لـ لتـرسيت واعـادة تشغيـل البـوت**\n\n**⎞𝟐⎝** `.ايقاف البوت`\n**•• لـ ايقـاف البـوت عـن العمـل والغـاء التنصـيب**\n\n**⎞𝟑⎝** `.تحديث`\n**•• لـ البحـث عـن تحديثـات وتحديث البـوت**\n\n**⎞𝟒⎝** `.تحديث الان`\n**•• لـ التحـديث الاولـي لـ البـوت لـ التنصيـب الثـانوي**\n\n**⎞𝟓⎝** `.تحديث البوت`\n**•• لـ التحـديث الثـانوي لـ البـوت لـ التنصيـب الاولـي والثـانوي**\n\n\n**⎞𝟔⎝** `.تعيين اسم البوت`\n**•• لـ تغييـر اسـم البـوت المسـاعد من بـوت فـاذر**\n\n**⎞𝟕⎝** `.تعيين صورة البوت`\n**•• لـ تغييـر صـورة البـوت المسـاعد من بـوت فـاذر**\n\n**⎞𝟖⎝** `.تعيين نبذة البوت`\n**•• لـ تغييـر نبـذة البـوت المسـاعد من بـوت فـاذر**\n\n**⎞𝟗⎝** `.تعيين وصف البوت`\n**•• لـ تغييـر وصـف البـوت المسـاعد من بـوت فـاذر**\n\n\n**⎞𝟏𝟎⎝** `.انلاين تفعيل`\n**•• لـ تفعيـل وضـع انـلاين البـوت المسـاعد من بـوت فـاذر**\n\n**⎞𝟏𝟏⎝** `.انلاين تعطيل`\n**•• لـ تعطيـل وضـع انـلاين البـوت المسـاعد من بـوت فـاذر**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉](t.me/Repthon) 𓆪")
@zedub.zed_cmd(pattern="م3(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 - اوامــر الـوقتــي](t.me/Repthon) 𓆪\n\n**⎞𝟏⎝** `.الاسم تلقائي`\n**•• لوضـع اسـم وقتـي لحسابـك يتغيـر تلقائيـاً كـل دقيقـه مـع الوقـت**\n\n\n**⎞𝟐⎝** `.البايو تلقائي`\n**•• لوضـع بايـو وقتـي يتغيـر تلقائـياً مع الوقـت كـل دقيقـه .. اولاً قـم بالـرد ع نـص البايـو بالامـر (.اضف البايو) **\n\n\n**⎞𝟑⎝** `.البروفايل تلقائي` \n**•• لوضـع بروفايـل وقتـي يتغيـر تلقائيـاً مع حسابـك كل دقيقـه اولاً قـم بالـرد ع الصـوره بالامـر (.اضف صورة الوقتي)**\n\n\n**⎞𝟒⎝** `.انهاء الاسم` / `.انهاء البايو` / `.انهاء البروفايل`\n**•• لـ الغــاء الاوامــر الوقتيــه مـن حســابـك**\n\n\n **𓆩** [𝙎𝙊𝙐𝙍𝘾𝞝 R𝙀𝙋𝙏𝙃𝙊𝙉𖠏](t.me/Repthon) **𓆪**")
@zedub.zed_cmd(pattern="م4(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 - اوامــر المجمــوعــه¹](t.me/Repthon) 𓆪\n\n**⎞𝟏⎝** `.البوتات`\n**•• كشـف وتنظيف مجموعتـك من البوتات .. لمنع التصفير والتفليش والتخريب**\n\n**⎞𝟐⎝** `.قفل البوتات` / `.فتح البوتات`\n**•• قفـل البوتـات بالطـرد التلقائـي .. الامر يمنع حتى المشـرفين من اضافـة البوتات .. في حـال اراد احد المشرفين رفـع بوت وتصفير مجموعتك اثنـاء غيابـك.**\n\n**⎞𝟑⎝** `.قفل الاضافه` / `.فتح الاضافه`  \n**•• قفـل اضافـة الاعضـاء بالطـرد .. مـع تحذيـر صاحـب الاضـافه**\n\n**⎞𝟒⎝** `.قفل الدخول` / `.فتح الدخول `\n**•• قفـل الدخـول بالرابـط بالطـرد التلقائـي .. حيث يقـوم بطـرد المنضم تلقائيـاً .. مـع ارسـال رسـاله تحذيريـه**\n\n**⎞𝟓⎝** `.قفل الميديا` \ `.فتح الميديا `\n**•• قفـل الوسائـط بالمسـح + تقييـد المرسـل من صلاحيـة ارسال الوسائط تلقائيـاً .. مع السمـاح له بارسـال الرسـائل فقـط .. يفيدكـم بـ منـع التفليـش الاباحـي في حال غيابكـم او انشغـالكم .. يسمـح للمشـرفين فقـط بارسـال الوسائـط**\n\n**⎞𝟔⎝** `.قفل الفشار` / `.فتح الفشار`\n**•• لـ مسـح رسـائل الفشار والسب والتكفير تلقائيـاً .. مـع تحذيـر الشخـص المرسـل **\n\n**⎞𝟕⎝** `.قفل الفارسيه` / `.فتح الفارسيه`\n**•• لـ مسـح رسـائل الايرانيين وبوتات الاعلانات الفارسيه تلقائيـاً.. مـع تحذيـر الشخـص المرسـل**\n\n**⎞𝟖⎝** `.قفل الروابط` / `.فتح الروابط`\n**•• قفـل الروابـط بالمسـح التلقائـي .. مع تحذير الشخص المرسل**\n\n**⎞𝟗⎝**`.قفل المعرفات` / `.فتح المعرفات`**•• قفـل المعرفـات بالمسـح التلقائـي .. مع تحذير الشخص المرسل**\n\n**⎞𝟏𝟎⎝** `.قفل الانلاين` / `.فتح الانلاين`\n**•• قفـل رسائل الانلايـن والهمسـات بالمسـح التلقائـي .. مع تحذير الشخص .. يسمـح للمشرفين فقـط بارسال الانلايـن**\n\n**⎞𝟏𝟏⎝** `.قفل الكل` / `.فتح الكل`\n**•• لـ قفـل او فتـح كـل الاوامـر السابقـه**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉](t.me/Repthon) 𓆪")
@zedub.zed_cmd(pattern="م5(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 - اوامــر المجمــوعــه²](t.me/Repthon) 𓆪\n\n**⎞𝟏⎝** `.الرابط`\n**•• لـ جـلب رابـط الكـروب + يجب ان تكون مشرفـاً فيهـا**\n\n**⎞𝟐⎝** `.رسائلي` / `.رسائله`\n**•• لـ عـرض عـدد رسـائلك او رسائل شخـص بالكـروب**\n\n**⎞𝟑⎝** `.حذف رسائلي`\n**•• لـ حـذف جميـع رسـائلك بالكـروب**\n\n**⎞𝟒⎝** `.غادر`\n**•• لـ مغـادرة الكـروب**\n\n**⎞𝟓⎝** `.رفع مشرف`\n**•• لـ رفـع الشخـص مشـرفـاً بالكـروب**\n\n**⎞𝟔⎝** `.تنزيل مشرف`\n**•• لـ تنزيـل الشخـص مـن الاشـراف + يجـب ان تكـون انت من قـام برفعـه مسبقـاً **\n\n**⎞𝟕⎝** `.رفع مالك`\n**•• لـ رفـع الشخـص مشـرفـاً بالكـروب بلقـب مـالك**\n\n**⎞𝟖⎝** `.الاعدادات`\n**•• لـ عـرض اعـدادات الكـروب**\n\n\n**⎞𝟗⎝** `.تاك` / `.all` \n**•• الامـر + كلمـه او بالـرد ع رسـالـه لـ عمـل تـاك بشكـل متقطـع لـ الكـل بالكـروب**\n\n**⎞𝟏𝟎⎝** `.ايقاف التاك`\n**•• لـ إيقـاف التـاك**\n\n\n**⎞𝟏𝟏⎝** `.احصائياتي`\n**•• لـ عـرض قائمـة بـ إحصـائيات دردشـات حسـابك**\n\n**⎞𝟏𝟐⎝** `.كروباتي الكل` / `.كروباتي ادمن` / `.كروباتي مالك` \n**•• لـ عـرض قائمـة بمعلومـات كروباتك**\n\n**⎞𝟏𝟑⎝** `.قنواتي الكل` / `.قنواتي ادمن` / `.قنواتي مالك`\n**•• لـ عـرض قائمـة بمعلومـات قنواتـك**\n\n**⎞𝟏𝟒⎝** `.الاعضاء` / `.المشرفين` \n**•• ⦇.الاعضاء / .المشرفين + معرف او رابـط الكـروب⦈ لـ عـرض قائمـة او ملـف بـ اعضـاء / او مشرفيـن الكـروب**\n\n**⎞𝟏𝟓⎝** `.البوتات`\n**•• ⦇.البوتات + معرف او رابـط الكـروب⦈ لـ عـرض قائمـة بـ بوتـات الكـروب**\n\n**⎞𝟏𝟔⎝** `.الحسابات المحذوفه`\n**•• ⦇.الحسابات المحذوفه او .الحسابات المحذوفه تنظيف⦈ لـ عـرض او تنظيـف الكـروب من الحسـابات المحذوفـه**\n\n**⎞𝟏𝟕⎝** `.مسح المحظورين`\n**•• لـ مسـح محظـورين الكـروب**\n\n\n**⎞𝟏𝟖⎝** `.ضيف`\n**•• ⦇.ضيف + رابط المجموعـه⦈ لـ اضـافة الاعضـاء استخـدم الامـر بالكـروب الهـدف مع اضافه رابط كروبك لـ الامـر**\n\n**⎞𝟏𝟗⎝** `.تفليش`\n**•• لـ تفليـش اعضـاء مجمـوعـه معينـه**\n\n**⎞𝟐𝟎⎝** `.الصورة وضع` / `.الصورة حذف` \n**•• لـ وضـع / حـذف صـورة المجمـوعـة**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉](t.me/Repthon) 𓆪")
@zedub.zed_cmd(pattern="م6(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event,"𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 - اوامــر الحســاب](t.me/Repthon) 𓆪\n\n**⎞𝟏⎝** `.ايدي` او `.ا`\n**•• ⦇.ايدي بالـرد او + معـرف/ايـدي الشخص⦈ لـ عـرض معلومـات الشخـص**\n\n**⎞𝟐⎝** `.الايدي`\n**•• ⦇.الايدي بالـرد⦈ لـ جلـب ايـدي الشخـص والكـروب**\n\n**⎞𝟑⎝** `.صورته`\n**•• ⦇.صورته بالـرد / .صورته الكل بالـرد⦈ لـ جـلب جميـع بروفـايلات الشخـص**\n\n**⎞𝟒⎝** `.اسمه`\n**•• ⦇.اسمه بالـرد⦈ لـ جـلب اسـم الشخـص**\n\n**⎞𝟓⎝** `.الاسماء`\n**•• ⦇.الاسماء بالـرد / .الاسماء + معـرف او ايدي الشخـص⦈ لـ جـلب قائمـة بسجـل اسمـاء حسـاب الشخـص**\n\n**⎞𝟔⎝** `.المعرفات`\n**•• ⦇.المعرفات بالـرد / .المعرفات + معـرف او ايدي الشخـص⦈ لـ جـلب قائمـة بسجـل معـرفـات حسـاب الشخـص**\n\n**⎞𝟕⎝** `.تخزين الخاص تفعيل`\n**•• ⦇الامـر + تفعيل او تعطيل⦈ لـ تخـزين جميـع رسـائل الخـاص بـ كـروب التخـزين**\n\n**⎞𝟖⎝** `.تخزين الكروبات تفعيل`\n**•• ⦇الامـر + تفعيل او تعطيل⦈ لـ تخـزين جميـع تاكـات الكـروبات بـ كـروب التخـزين**\n\n**⎞𝟗⎝** `.الحمايه تفعيل`\n**•• لـ تفعيـل حمايـة الخـاص لـ حسـابك**\n\n**⎞𝟏𝟎⎝** `.الحمايه تعطيل`\n**•• لـ تعطيـل حمايـة الخـاص لـ حسـابك**\n\n**⎞𝟏𝟏⎝** `.قبول`\n**•• لـ السمـاح لـ الشخـص بـ ارسـال رسـائل الخـاص اثنـاء تفعيـل حمـاية الخـاص بحسـابك بـدون تحـذير**\n\n**⎞𝟏𝟐⎝** `.رفض`\n**•• لـ رفـض الشخـص من ارسـال رسـائل الخـاص اثنـاء تفعيـل حمـاية الخـاص بحسـابك**\n\n**⎞𝟏𝟑⎝** `.مرفوض`\n**•• لـ حظـر الشخـص من الخـاص دون تحـذير**\n\n**⎞𝟏𝟒⎝** `.المقبولين`\n**•• لـ عـرض قائمـة بالاشخـاص المقبـولين**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉](t.me/Repthon) 𓆪")
@zedub.zed_cmd(pattern="م7(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 - اوامــر الميــديـا والصيــغ](t.me/Repthon) 𓆪\n\n**⎞𝟏⎝** `.ملصق`\n**•• ⦇.ملصق بالـرد ع صـوره او فيديـو⦈ لـ صنـع ملصـق او ملصـق فيديـو متحـرك**\n\n**⎞𝟐⎝** `.حزمه`\n**•• ⦇.حزمه بالـرد ع ملصـق⦈ لـ تفكيـك حزمـة ملصـق مـا وصنعهـا بحقوقـك**\n\n**⎞𝟑⎝** `.صورته`\n**•• ⦇.حزمة + اسـم بالـرد ع ملصـق⦈ لـ تفكيـك حزمـة ملصـق مـا وصنعهـا بحقـوق الاسـم الـذي ادخلتـه**\n\n**⎞𝟒⎝** `.معلومات الملصق`\n**•• ⦇الامـر بالـرد ع ملصـق⦈ لـ جـلب معلومـات حزمـة الملصـق**\n\n**⎞𝟓⎝** `.ملصقات`\n**•• ⦇الامـر + اسـم⦈ لـ البحـث عن حـزم ملصقـات بـ الاسـم**\n\n\n**⎞𝟔⎝** `.لملصق`\n**•• ⦇الامـر بالـرد ع صـوره⦈ لـ تحويـل الصـوره لـ ملصـق**\n\n**⎞𝟕⎝** `.لصوره`\n**•• ⦇الامـر بالـرد ع ملصـق⦈ لـ تحويـل الملصـق لـ صـوره**\n\n**⎞𝟖⎝** `.لفيد`\n**•• ⦇الامـر بالـرد ع صـوره او ملصـق⦈ لـ تحويـلهـا لـ تصميـم فيديـو **\n\n**⎞𝟗⎝** `.دائري`\n**•• ⦇الامـر بالـرد ع صـوره او ملصـق او فيديـو او متحركـه⦈ لـ تحويـلهـا لـ تصميـم فيديـو دائـري**\n\n**⎞𝟏𝟎⎝** `.لمتحركة`\n**•• ⦇الامـر بالـرد ع ملصـق متحـرك⦈ لـ تحويـله لـ متحـركـه**\n\n**⎞𝟏𝟏⎝** `.حول بصمه`\n**•• ⦇الامـر بالـرد ع فيديـو⦈ لـ استخـراج الصـوت كـ تسجيل صوت بصمه**\n\n**⎞𝟏𝟑⎝** `.حول صوت`\n**••  ⦇الامـر بالـرد ع فيديـو⦈ لـ استخـراج الصـوت كـ ملـف صوت MP3**\n\n**⎞𝟏𝟒⎝** `.لمتحركه`\n**••  ⦇الامـر بالـرد ع صـوره او ملصـق⦈ لـ تحويـلهـا الـى متحـركـه**\n\n**⎞𝟏𝟓⎝** `.لمتحرك`\n**••  ⦇الامـر بالـرد ع فيديـو⦈ لـ تحويـله الـى متحـركـه**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉](t.me/Repthon) 𓆪")
@zedub.zed_cmd(pattern="م8(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 - اوامــر الفــارات](t.me/Repthon) 𓆪\n\n**⎞𝟏⎝** `.ضع فار`\n**•• ⦇الامـر + متغيـر الفـار + القيمـه⦈ لـ اضـافة قيمـة محـدده لـ فـار محـدد**\n**⎞𝟐⎝** `.جلب فار`\n**•• ⦇الامـر + متغيـر الفـار⦈ لـ جـلب قيمـة الفـار المحـدد**\n**⎞𝟑⎝** `.حذف فار`\n**•• ⦇الامـر + متغيـر الفـار⦈ لـ حـذف قيمـة الفـار المحـدد**\n**⎞𝟒⎝** `.استخدامي`\n**•• لـ عـرض ساعـات الاستخـدام والساعـات المتبقيـه لـ بـوتك**\n\n**✾╎قائـمه اوامر تغييـر فـارات الصـور بأمـر واحـد فقـط - لـ اول مـره ع سـورس تليثـون يوزر بـوت 🦾 :**\n**⎞𝟓⎝** `.اضف صورة الفحص`\n**•• ⦇الامـر بالـرد ع صـوره او ميـديـا⦈**\n**⎞𝟔⎝** `.اضف صورة الوقتي`\n**•• ⦇الامـر بالـرد ع صـوره او ميـديـا⦈**\n**⎞𝟕⎝** `.اضف صورة الفحص`\n**•• ⦇الامـر بالـرد ع صـوره او ميـديـا⦈**\n\n**✾╎قائـمه اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط :**\n**⎞𝟖⎝** `.اضف كليشة الحماية`\n**•• ⦇الامـر بالـرد ع نـص الكليشـه⦈**\n**⎞𝟗⎝** `.اضف كليشة الفحص`\n**•• ⦇الامـر بالـرد ع نـص الكليشـه⦈**\n\n**⎞𝟏𝟎⎝** `.اضف رمز الوقتي`\n**•• ⦇الامـر بالـرد ع الـرمـز⦈**\n**⎞𝟏𝟏⎝** `.اضف زخرفة الوقتي`\n**•• ⦇الامـر بالـرد ع ارقـام الزخـرفـه⦈**\n**⎞𝟏𝟑⎝** `.اضف البايو الوقتي`\n**••  ⦇الامـر بالـرد ع البـايـو⦈**\n**⎞𝟏𝟒⎝** `.اضف اسم المستخدم`\n**••  ⦇الامـر بالـرد ع نـص الاسـم⦈**\n**⎞𝟏𝟓⎝** `.اضف كروب الرسائل`\n**••  ⦇الامـر بالـرد ع ايـدي الكـروب⦈**\n**⎞𝟏𝟔⎝** `.اضف كروب السجل`\n**••  ⦇الامـر بالـرد ع ايـدي الكـروب⦈**\n**⎞𝟏𝟕⎝** `.اضف ايديي`\n**••  ⦇الامـر بالـرد ع ايـدي حسـابك⦈**\n**⎞𝟏𝟖⎝** `.اضف نقطة الاوامر`\n**••  ⦇الامـر بالـرد ع الـرمـز الجـديـد⦈**\n**⎞𝟏𝟗⎝** `.اضف رسائل الحماية`\n**••  ⦇الامـر بالـرد ع رقـم عـدد رسـائل تحـذيـر الحمـايـة⦈**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉](t.me/Repthon) 𓆪")
@zedub.zed_cmd(pattern="م9(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 - اوامــر الخـدمـات الاخـرى](t.me/Repthon) 𓆪\n\n**⎞𝟏⎝** `.التخصيص`\n\n**⎞𝟐⎝**`.الترحيب`\n\n**⎞𝟑⎝** `.الردود`\n\n**⎞𝟒⎝** `.الاذاعه`\n\n**⎞𝟓⎝** `.النشر`\n\n**⎞𝟔⎝** `.الكاشف`\n\n**⎞𝟕⎝** `.ستوريات`\n\n**⎞𝟖⎝** `.التحشيش`\n\n**⎞𝟗⎝** `.المساعد`\n\n**⎞𝟏𝟎⎝** `.الطقس`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉](t.me/Repthon) 𓆪")
@zedub.zed_cmd(pattern="م10(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 - اوامــر التســليـه والالعــاب](t.me/Repthon) 𓆪\n\n**✾╎قائـمـه اوامــر التسـليـه :**\n**⎞𝟏⎝** `.تسليه1`\n**⎞𝟐⎝** `.تسليه2`\n**⎞𝟑⎝** `.تسليه3`\n**⎞𝟒⎝** `.تسليه4`\n**⎞𝟓⎝** `.تسليه5`\n**⎞𝟔⎝** `.تسليه6`\n**⎞𝟕⎝** `.تسليه7`\n**⎞𝟖⎝** `.تسليه8`\n**⎞𝟗⎝** `.تسليه9`\n\n**⎞𝟏𝟎⎝** `.تسليه10`\n\n**✾╎قائـمه اوامـر التسـليـه الجـديـده حقـوق سـورس ريبثون :**\n**⎞𝟏𝟏⎝** `.حيوان`\n**•• ⦇الامـر بالـرد / المعـرف / الايدي⦈ امـر تسـليه كشـف حيـوان 😂🐴**\n**⎞𝟏𝟐⎝** `.زاحف`\n**•• بالـرد ع الشخـص**\n**⎞𝟏𝟑⎝** `.مشهور`\n**•• ⦇الامـر بالـرد / المعـرف / الايدي⦈ امـر تسـليه زوجنـي من مشهـور 👨‍⚖💍**\n\n**⎞𝟏𝟒⎝** `.مشهوره`\n**•• ⦇الامـر بالـرد / المعـرف / الايدي⦈ امـر تسـليه زوجنـي من مشهـوره 👰🏻‍♀💍**\n\n**✾╎قائـمه اوامـر التحشيش :**\n**⎞𝟏𝟓⎝** `.التحشيش`\n**•• قـائمـة اوامـر التحشيش والنسـب**\n\n**⎞𝟏𝟔⎝** `.بلاي`\n**•• العــاب الاونــلاين لـ سـورس ريبثون **\n\n**⎞𝟏𝟕⎝** `.معاني` + اسـم\n**•• لـ معـرفـة معـاني الاسمـاء**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 R𝙀𝙋𝙏𝙃𝙊𝙉𖠏](t.me/Repthon) 𓆪")


#الكـالبـاك ابديـت - ريبـــثون
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed")))
@check_owner
async def on_plug_in_callback_query_handler(event):
    buttons = [[Button.inline("•❶•", data="ahmed1"), Button.inline("•❷•", data="ahmed2"), Button.inline("•❸•", data="ahmed3"), Button.inline("•❹•", data="ahmed4"), Button.inline("•❺•", data="ahmed5"),],[Button.inline("•❻•", data="ahmed6"), Button.inline("•❼•", data="ahmed7"), Button.inline("•❽•", data="ahmed8"), Button.inline("•❾•", data="ahmed9"), Button.inline("•❿•", data="ahmad10"),]]
    await event.edit(Malath, buttons=buttons)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed1")))
@check_owner
async def zed_handler(event):
    buttons = [[Button.inline("رجــوع", data="ahmed")]]
    orden1 = "**⎞𝟏⎝** `.بحث`\n\n**⎞𝟐⎝** `.اغنيه`\n\n**⎞𝟑⎝** `.فيديو`\n\n**⎞𝟒⎝** `.تحميل صوت`\n\n**⎞𝟓⎝** `.تحميل فيديو`\n\n**⎞𝟔⎝** `.يوتيوب`\n\n**⎞𝟕⎝** `.انستا`\n\n**⎞𝟖⎝** `.صور`\n\n**⎞𝟗⎝** `.متحركه`\n\n**⎞𝟏𝟎⎝** `.تيك`\n\n**⎞𝟏𝟏⎝** `.لايكي`\n\n**⎞𝟏𝟐⎝** `.فيسبوك`\n\n**⎞𝟏𝟑⎝** `.تويتر`\n\n**⎞𝟏𝟒⎝** `.بن`\n\n**⎞𝟏𝟓⎝** `.سناب`\n\n**⎞𝟏𝟔⎝** `.كتاب`"
    await event.edit(orden1, buttons=buttons)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed2")))
@check_owner
async def zed_handler(zedub):
    text = "**⎞𝟏⎝** `.اعاده تشغيل`\n\n**⎞𝟐⎝** `.ايقاف البوت`\n\n**⎞𝟑⎝** `.تحديث`\n\n**⎞𝟒⎝** `.تحديث الان`\n\n**⎞𝟓⎝** `.تحديث البوت`\n\n\n\n**⎞𝟔⎝** `.تعيين اسم البوت`\n\n**⎞𝟕⎝** `.تعيين صورة البوت`\n\n**⎞𝟖⎝** `.تعيين نبذة البوت`\n\n**⎞𝟗⎝** `.تعيين وصف البوت`\n\n\n\n**⎞𝟏𝟎⎝** `.انلاين تفعيل`\n\n**⎞𝟏𝟏⎝** `.انلاين تعطيل`"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed3")))
@check_owner
async def zed_handler(zedub):
    text = "**⎞𝟏⎝** `.اسم وقتي`\n\n**⎞𝟐⎝** `.بايو وقتي`\n\n**⎞𝟑⎝** `.البروفايل تلقائي` \n\n**⎞𝟒⎝** `.انهاء الاسم` / `.انهاء البايو` / `.انهاء البروفايل`"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed4")))
@check_owner
async def zed_handler(zedub):
    text = "**⎞𝟏⎝** `.البوتات`\n\n**⎞𝟐⎝** `.قفل البوتات` / `.فتح البوتات`\n\n**⎞𝟑⎝** `.قفل الاضافه` / `.فتح الاضافه`  \n\n**⎞𝟒⎝** `.قفل الدخول` / `.فتح الدخول `\n\n**⎞𝟓⎝** `.قفل الميديا` / `.فتح الميديا `\n\n**⎞𝟔⎝** `.قفل الفشار` / `.فتح الفشار`\n\n**⎞𝟕⎝** `.قفل الفارسيه` / `.فتح الفارسيه`\n\n**⎞𝟖⎝** `.قفل الروابط` / `.فتح الروابط`\n\n**⎞𝟗⎝**`.قفل المعرفات` / `.فتح المعرفات`\n\n**⎞𝟏𝟎⎝** `.قفل الانلاين` / `.فتح الانلاين`\n\n**⎞𝟏𝟏⎝** `.قفل الكل` / `.فتح الكل`"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed5")))
@check_owner
async def zed_handler(zedub):
    text = "**⎞𝟏⎝** `.الرابط`\n\n**⎞𝟐⎝**`.رسائلي` / `.رسائله` \n\n**⎞𝟑⎝** `.حذف رسائلي`\n\n**⎞𝟒⎝** `.غادر`\n\n**⎞𝟓⎝** `.رفع مشرف`\n\n**⎞𝟔⎝** `.تنزيل مشرف`\n\n**⎞𝟕⎝** `.رفع مالك`\n\n**⎞𝟖⎝** `.الاعدادات`\n\n**⎞𝟗⎝** `.تاك` / `.all` \n\n**⎞𝟏𝟎⎝** `ايقاف التاك` \n\n\n**⎞𝟏𝟏⎝** `.احصائياتي`\n\n**⎞𝟏𝟐⎝** `.كروباتي الكل` / `.كروباتي ادمن` / `.كروباتي مالك`\n\n**⎞𝟏𝟑⎝** `.قنواتي الكل` / `.قنواتي ادمن` / `.قنواتي مالك`\n\n**⎞𝟏𝟒⎝** `.الاعضاء` / `المشرفين` \n\n**⎞𝟏𝟓⎝** `.البوتات`\n\n**⎞𝟏𝟔⎝** `.الحسابات المحذوفه`\n\n**⎞𝟏𝟕⎝** `.مسح المحظورين`\n\n**⎞𝟏𝟖⎝** `.ضيف`\n\n**⎞𝟏𝟗⎝** `.تفليش`"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed6")))
@check_owner
async def zed_handler(zedub):
    text = "**⎞𝟏⎝** `.ايدي` / `.ا`\n\n**⎞𝟐⎝** `.الايدي`\n\n**⎞𝟑⎝** `.صورته`\n\n**⎞𝟒⎝** `.اسمه`\n\n**⎞𝟓⎝** `.الاسماء`\n\n**⎞𝟔⎝** `.المعرفات`\n\n**⎞𝟕⎝** `.تخزين الخاص تفعيل`\n\n**⎞𝟖⎝** `.تخزين الكروبات تفعيل`\n\n**⎞𝟗⎝** `.الحمايه تفعيل`\n\n**⎞𝟏𝟎⎝** `.الحمايه تعطيل`\n\n**⎞𝟏𝟏⎝** `.قبول`\n\n**⎞𝟏𝟐⎝** `.رفض`\n\n**⎞𝟏𝟑⎝** `.مرفوض`\n\n**⎞𝟏𝟒⎝** `.المقبولين`"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed7")))
@check_owner
async def zed_handler(zedub):
    text = "**⎞𝟏⎝** `.ملصق`\n\n**⎞𝟐⎝** `.حزمه`\n\n**⎞𝟑⎝** `.صورته`\n\n**⎞𝟒⎝** `.معلومات الملصق`\n\n**⎞𝟓⎝** `.ملصقات`\n\n**⎞𝟔⎝** `.لملصق`\n\n**⎞𝟕⎝** `.لصوره`\n\n**⎞𝟖⎝** `.لفيد`\n\n**⎞𝟗⎝** `.دائري`\n\n**⎞𝟏𝟎⎝** `.لمتحركة`\n\n**⎞𝟏𝟏⎝** `.حول بصمه`\n\n**⎞𝟏𝟑⎝** `.حول صوت`\n\n**⎞𝟏𝟒⎝** `.لمتحركه`\n\n**⎞𝟏𝟓⎝** `.لمتحرك`"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed8")))
@check_owner
async def zed_handler(zedub):
    text = "**⎞𝟏⎝** `.ضع فار`\n\n**⎞𝟐⎝** `.جلب فار`\n\n**⎞𝟑⎝** `.حذف فار`\n\n**⎞𝟒⎝** `.استخدامي`\n\n**✾╎قائـمه اوامـر تغييـر فـارات الصـور بأمـر واحـد فقـط بالــرد - لـ اول مـره ع سـورس تليثـون يوزر بـوت :**\n\n**⎞𝟓⎝** `.اضف صورة الحمايه`\n\n**⎞𝟔⎝** `.اضف صورة الوقتي`\n\n**⎞𝟕⎝** `.اضف صورة الفحص`\n\n**✾╎قائـمه اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط بالــرد :**\n\n**⎞𝟖⎝** `.اضف كليشة الحماية`\n\n**⎞𝟗⎝** `.اضف كليشة الفحص`\n\n**⎞𝟏𝟎⎝** `.اضف رمز الوقتي`\n\n**⎞𝟏𝟏⎝** `.اضف زخرفة الوقتي`\n\n**⎞𝟏𝟑⎝** `.اضف البايو الوقتي`\n\n**⎞𝟏𝟒⎝** `.اضف اسم المستخدم`\n\n**⎞𝟏𝟓⎝** `.اضف كروب الرسائل`\n\n**⎞𝟏𝟔⎝** `.اضف كروب السجل`\n\n**⎞𝟏𝟕⎝** `.اضف ايديي`\n\n**⎞𝟏𝟖⎝** `.اضف نقطة الاوامر`\n\n**⎞𝟏𝟗⎝** `.اضف رسائل الحماية`"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed9")))
@check_owner
async def zed_handler(zedub):
    text = "**✾╎قائـمه اوامـر الـخدمـات :**\n\n**⎞𝟏⎝** `.التخصيص`\n\n**⎞𝟐⎝** `.الترحيب`\n\n**⎞𝟑⎝** `.الردود`\n\n**⎞𝟒⎝** `.الاذاعه`\n\n**⎞𝟓⎝** `.النشر`\n\n**⎞𝟔⎝** `.الكاشف`\n\n**⎞𝟕⎝** `.ستوريات`\n\n**⎞𝟖⎝** `.التحشيش`\n\n**⎞𝟗⎝** `.المساعد`\n\n**⎞𝟏𝟎⎝** `.الطقس`"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmad10")))
@check_owner
async def zed_handler(zedub):
    text = "**✾╎قائـمـه اوامــر التسـليـه والالـعــاب :**\n\n**⎞𝟏⎝** `.تسليه` / `.تسليه1`\n**⎞𝟐⎝** `.تسليه2`\n**⎞𝟑⎝** `.تسليه3`\n**⎞𝟒⎝** `.تسليه4`\n**⎞𝟓⎝** `.تسليه5`\n**⎞𝟔⎝** `.تسليه6`\n**⎞𝟕⎝** `.تسليه7`\n**⎞𝟖⎝** `.تسليه8`\n**⎞𝟗⎝** `.تسليه9`\n**⎞𝟏𝟎⎝** `.تسليه10`\n\n**✾╎قائـمه اوامـر التسـليـه الجـديـده حقـوق سـورس ريبثون :**\n\n**⎞𝟏𝟏⎝** `.حيوان` بالـرد\n\n**⎞𝟏𝟐⎝** `.زاحف` بالـرد\n\n**⎞𝟏𝟑⎝** `.مشهور` بالـرد\n\n**⎞𝟏𝟒⎝** `.مشهوره` بالـرد\n\n**⎞𝟏𝟓⎝** `.التحشيش`\n\n**⎞𝟏𝟔⎝** `.معاني` + اسـم\n\n**⎞𝟏𝟕⎝** `.بلاي`"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)


#لوحـة قنــوات الســورس
@zedub.tgbot.on(events.InlineQuery)
@check_owner
async def zed_handler(zedub):
    builder = zedub.builder
    result = None
    query = zedub.text
    await bot.get_me()
    if query.startswith("ريبثون") and zedub.query.user_id == bot.uid:
        channels = f"**•❐• مـرحبــاً عـزيـزي  {mention} **\n**•❐• اليـك مجمـوعــة قنـوات ريبثون ↵ 𝙍𝙀𝙋𝙏𝙃𝙊𝙉 ♥️🦾**\n\n**•❐• استـخـدم الازرار بالاسفــل↓**"
        buttons = [[Button.url("قنـاة السـورس", "https://t.me/Repthon"),],[Button.url("التحـديثـات", "https://t.me/Repthon_up"), Button.url("الفـارات", "https://t.me/Repthon_vars"),],[Button.url("الشـروحـات¹", "https://t.me/Repthonn"),],[Button.url("الشـروحـات²", "https://t.me/Repthonn"),],[Button.url("مطـور السـورس", "https://t.me/E_7_V"),]]
        if ZEDPIC and ZEDPIC.endswith((".jpg", ".png", "gif", "mp4")):
            result = builder.photo(ZEDPIC, text=channels, buttons=buttons, link_preview=False)
        elif ZEDPIC:
            result = builder.document(ZEDPIC,title="zedub",text=channels,buttons=buttons,link_preview=False)
        else:
            result = builder.article(title="zedub",text=channels,buttons=buttons,link_preview=False)
        await zedub.answer([result] if result else None)
@zedub.zed_cmd(pattern="ريبثون")
async def repozedub(zedub):
    if zedub.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if zedub.reply_to_msg_id:
        await zedub.get_reply_message()
    response = await bot.inline_query(TG_BOT, "زدثون")
    await response[0].click(zedub.chat_id)
    await zedub.delete()


@zedub.tgbot.on(InlineQuery)
@check_owner
async def zed_handler(event):
    builder = event.builder
    result = None
    query = event.text
    await zedub.get_me()
    if query.startswith("سورس") and event.query.user_id == zedub.uid:
        Zelzal = f"**•◈• اصــدار الســورس ⤽ 3.1.3**  \n**•◈• المستخــدم ⤽**  {mention}  \n**•◈• وقــت التشغيــل ⤽  {TM}  **\n**•◈• البــوت المســاعـد ⤽  {TG_BOT} **\n**•◈• قنــاة الســورس ⤽  @Repthon **"
        buttons = [[Button.url("قنـاة الســورس", "https://t.me/Repthon"), Button.url("مطـور الســورس", "https://t.me/ZQ_LO")]]
        if ZEDPIC and ZEDPIC.endswith((".jpg", ".png", ".gif", ".mp4")):
            result = builder.photo(ZEDPIC, text=Zelzal, buttons=buttons, link_preview=True)
        elif ZEDPIC:
            result = builder.document(ZEDPIC,title="Repthon",text=Roger,buttons=buttons,link_preview=True)
        else:
            result = builder.article(title="zedub",text=Zelzal,buttons=buttons,link_preview=True)
        await event.answer([result] if result else None)
@zedub.zed_cmd(pattern="سورس")
async def repozedub(event):
    if event.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await zedub.inline_query(TG_BOT, "سورس")
    await response[0].click(event.chat_id)
    await event.delete()
