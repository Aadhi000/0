class script(object):
    START_TXT = """<b>ʜᴇʟʟᴏ {},
ᴍʏ ɴᴀᴍᴇ ɪs <a href=https://t.me/{}><b>{}</b></a>. ɪ ᴀᴍ ᴀɴ ᴇxᴛʀᴀ ᴏʀᴅɪɴᴀʀʏ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴘᴏᴡᴇʀs.ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴀᴅᴍɪɴ ɪ ᴡɪʟʟ sʜᴏᴡ ᴍʏ ᴘᴏᴡᴇʀs ᴛʜᴇɪʀ</b>"""   
    
    STATUS_TXT = """<b>╭━━━╮╭━━━━╮╭━━━╮╭━━━━╮╭━━━╮
┃╭━╮┃┃╭╮╭╮┃┃╭━╮┃┃╭╮╭╮┃┃╭━╮┃
┃╰━━╮╰╯┃┃╰╯┃┃╱┃┃╰╯┃┃╰╯┃╰━━╮
╰━━╮┃╱╱┃┃╱╱┃╰━╯┃╱╱┃┃╱╱╰━━╮┃
┃╰━╯┃╱╱┃┃╱╱┃╭━╮┃╱╱┃┃╱╱┃╰━╯┃
╰━━━╯╱╱╰╯╱╱╰╯╱╰╯╱╱╰╯╱╱╰━━━╯
📑 ғɪʟᴇs sᴀᴠᴇᴅ: {}
👩🏻‍💻 ᴜsᴇʀs: {}
👥 ɢʀᴏᴜᴘs: {}
🗂️ ᴏᴄᴄᴜᴘɪᴇᴅ: {}</b>"""
 
    HELP_TXT = """𝙷𝙴𝚈 {}
ʜᴇʀᴇ ɪs ᴀʟʟ ᴍʏ ʜᴇʟᴘ ᴛᴏᴏʟ's 😇"""
    ABOUT_TXT = """<b>❖ ᴍʏ ɴᴀᴍᴇ : ᴀᴊᴀx ᴘʀᴏ ᴍᴀx</b>
<b>❖ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/AboutAadhi>ᴀᴀᴅʜɪ</a></b>
<b>❖ ʟɪʙʀᴀʀʏ : ᴘʀᴏɢʀᴀᴍ</b>
<b>❖ ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ </b>
<b>❖ ᴅᴀᴛᴀʙᴀsᴇ : ᴍᴏɴɢᴏᴅʙ</b>
<b>❖ sᴇʀᴠᴇʀ : ʜᴇʀᴜᴋᴏ</b>
<b>❖ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ3.1.37 </b>
<b>❖ ᴜᴘᴅᴀᴛᴇᴢ : <a href=https://t.me/MWUpdatez>ᴍᴡ ᴜᴘᴅᴀᴛᴇᴢ</a></b>
<b>❖ ʏᴛ ᴄʜᴀɴɴᴇʟ : <a href=https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA>ᴏᴘᴜs ᴛᴇᴄʜᴢ</a></b>"""

    DONATION_TXT = """<b>𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧 & 𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧</b> 

›› <b>𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧</b>

⪼ <b>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 💳. 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/AboutAadhi><b>ꪖꪖᦔꫝỉ</b></a> ᚛━━━━━━━━━━━━

›› <b>𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧</b>

⪼ <b>𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 . 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐀𝐧𝐝 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/AboutAadhi><b>ꪖꪖᦔꫝỉ</b></a> ᚛━━━━━━━━━━━━"""
    PROMOTION_TXT = """<b>〄 𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 〄</b>

⪼ <b>𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 . 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐀𝐧𝐝 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/AboutAadhi><b>ꪖꪖᦔꫝỉ</b></a> ᚛━━━━━━━━━━━━""" 
    FILE_TXT = """<b>๏ <u>ғɪʟᴇ sᴛᴏʀᴇ ᴍᴏᴅᴜʟᴇ</u></b>

<b>ʙʏ ᴜsɪɴɢ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ʏᴏᴜ ᴄᴀɴ sᴛᴏʀᴇ ғɪʟᴇs ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ᴀɴᴅ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ sᴀᴠᴇᴅ ғɪʟᴇs.ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ғɪʟᴇs ғʀᴏᴍ ᴀ ᴘᴜʙʟɪᴄ ᴄʜᴀɴɴᴇʟ sᴇɴᴅ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ʟɪɴᴋ ᴏʀ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ғɪʟᴇs ғʀᴏᴍ ᴀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ʏᴏᴜ ᴍᴜsᴛ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ғɪʟᴇs...//</b>

⪼ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ  ›

➪ /plink ›› <b>ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇᴅɪᴀ ᴛᴏ ɢᴇᴛ ʟɪɴᴋ</b>
➪ /pbatch ›› <b>ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ғɪʟᴇ ʟɪɴᴋs ғᴏʀ ᴍᴀᴋɪɴɢ ʟɪɴᴋ ᴏғ ᴍᴏʀᴇ ᴛʜᴀɴ ᴏɴᴇ ғɪʟᴇ</b>
➪ /batch ›› <b>ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ғɪʟᴇ ʟɪɴᴋs ғᴏʀ ᴍᴀᴋɪɴɢ ʟɪɴᴋ ᴏғ ᴍᴏʀᴇ ᴛʜᴀɴ ᴏɴᴇ ғɪʟᴇ</b>

⪼ ᴇxᴀᴍᴘʟᴇ ›

<code>/batch https://t.me/MWUpdatez/3 https://t.me/MWUpdatez/8</code>

ᴄʀᴇᴅɪᴛs ›› <a href=https://t.me/MWUpdatez><b>ᴍᴡ ᴜᴘᴅᴀᴛᴇᴢ</b></a>"""   
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
•/whois :-give a user full details"""
    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b>⚡ ᴊᴜsᴛ sᴏᴍᴇ ᴋɪɴᴅ ᴏғ ғᴜɴ ᴛʜɪɴɢs ⚡</b>
 
𝟣. /dice - ʀᴏʟᴇ ᴛʜᴇ ᴅɪᴄᴇ 
𝟤. /Throw 𝗈𝗋 /Dart - ᴛᴏ ᴍᴀᴋᴇ ᴅᴀʀᴛ 
3. /Runs - sᴏᴍᴇ ʀᴀɴᴅᴏᴍ ᴅɪᴀʟᴏɢᴜᴇs 
4. /Goal or /Shoot - ᴛᴏ ᴍᴀᴋᴇ ᴀ ɢᴏᴀʟ ᴏʀ sʜᴏᴏᴛ
5. /luck or /cownd - sᴘɪɴ ᴀɴᴅ ᴛʀʏ ʏᴏᴜʀ ʟᴜᴄᴋ"""
    DEPLOY_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴅᴇᴘʟᴏʏ..?</b> 
  
<b>ᴅᴇᴘʟᴏʏ ᴛᴜᴛᴏʀɪᴀʟ ››</b> <i><b>https://youtu.be/kB9TkCs8cX0</b></i>

<b>ᴡɪʟʟ ᴀᴅᴅ ʜᴇʀᴇ sᴏᴏɴ •_•</b>

<b>sʜᴀʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ</b>
ᴄʀᴇᴅɪᴛs ›› <a href=https://t.me/MWUpdatez><b>ᴍᴡ ᴜᴘᴅᴀᴛᴇᴢ</b></a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and ᗩᒍᗩ᙭  will respond whenever a keyword is found the message

<b>NOTE:</b>
1. ᗩᒍᗩ᙭ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ</b>

<b>sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ ғᴏʀ ᴡʜᴏ ʟᴏᴠᴇs ᴛᴏ ʜᴇᴀʀ sᴏɴɢs. ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ sᴏɴɢ ᴡɪᴛʜ sᴜᴘᴇᴛ ғᴀsᴛ sᴘᴇᴇᴅ.</b>

<b>ᴄᴏᴍᴍᴀɴᴅ</b>

››  /song sᴏɴɢ ɴᴀᴍᴇ

ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ

ᴄʀᴇᴅɪᴛs :- <a href=https://t.me/OpusTechz>ᴏᴘᴜs ᴛᴇᴄʜᴢ</a>"""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>ᴍᴇssᴀɢᴇ ᴘɪɴɴᴇʀ../</b>

<b>ᴀʟʟ ᴛʜᴇ ᴘɪɴ ʀᴇʟᴀᴛᴇᴅ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ғɪɴᴅ ʜᴇʀᴇ:</b>

<b>📌ᴄᴏᴍᴍᴀɴᴅs📌</b>

◉ /pin :- ᴛᴏ ᴘɪɴ ᴀ ᴍᴇssᴀɢᴇ 
◉ /unpin :- ᴛᴏ ᴜɴᴘɪɴ ᴀ ᴍᴇssᴀɢᴇ"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

• /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

• These commands works on both pm and group.
• These commands can be used by any group member."""
    TTS_TXT = """Help: <b> TTS 🎤 module:</b>

Translate text to speech

<b>Commands and Usage:</b>

• /tts <text> : convert text to speech

<b>NOTE:</b>

• IMDb should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>🌟 Ping:</b>

Helps you to know your ping 🚶🏼‍♂️

<b>Commands:</b>

• /alive - To check you are alive.
• /help - To get help.
• /ping - To get your ping.
• /repo - Source Code.
• /channel - Channel Details.
• /ajax - Bot Link.
<b>🏹Usage🏹 :</b>

• This commands can be used in pms and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""
    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

🤧 /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    PRIVATEBOT_TXT = """<b>ᴀᴊᴀx ᴘʀᴏ ᴍᴀx</b>
<b>›› ᴡᴏʀᴋɪɴɢ ᴘᴇʀғᴇᴄᴛʟʏ</b>
<b>›› ʀᴇᴘʟʏ ᴡɪᴛʜɪɴ ᴛᴇɴ sᴇᴄᴏɴᴅs</b>
<b>›› ᴡɪᴛʜ ᴇxᴛʀᴀ ғᴇᴀᴛᴜʀᴇs</b>
<b>›› ᴏᴡɴᴇʀ <a href=https://t.me/AboutAadhi>ᴀᴀᴅʜɪ</a></b>"""

    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

◉ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-ᗩᒍᗩ᙭  Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ᗩᒍᗩ᙭ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MWUpdatez)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴏɴ - ᴏғғ ᴍᴏᴅᴜʟᴇ</b>

<b>ᴜsᴇ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴛᴜʀɴ ᴏɴ ᴀɴᴅ ᴏғғ ᴛʜᴇ ғɪʟᴛᴇʀ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴀɴᴅ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜᴇ ᴏᴛʜᴇʀ ғᴇᴀᴛᴜʀᴇs</b>

<b>ᴄᴏᴍᴍᴀɴᴅs :-
<b>›› /autofilter on - ᴛᴏ ᴇɴᴀʙʟᴇ ᴛʜᴇ ᴀᴜᴛᴏғɪʟᴛᴇʀ</b>
<b>›› /autofilter off - ᴛᴏ ᴅɪsᴀʙʟᴇᴅ ᴛʜᴇ ᴀᴜᴛᴏғɪʟᴛᴇʀ</b>

<b>ᴄʀᴇᴅɪᴛs :- <a href=https://t.me/OpusTechz>ᴏᴘᴜs ᴛᴇᴄʜᴢ</a></b>"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of ᗩᒍᗩ᙭ 

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban_user  - <code>to ban a user.</code>
• /unban_user  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
   
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
    REPORT_TXT = """➤ 𝐇𝐞𝐥𝐩: Rᴇᴘᴏʀᴛ ⚠️

ᴄᴀɴ ʀᴇᴘᴏʀᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀᴅᴋɪɴs ʙʏ ᴛʜɪs ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ᴅᴏɴ'ᴛ ᴍɪsᴜsᴇ.

➤ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ

➪/report 𝗈𝗋 @admins - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾)."""

    CORONA_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖢𝗈𝗏𝗂𝖽

𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚍𝚊𝚒𝚕𝚢 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚌𝚘𝚟𝚒𝚍 

➤ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ

➪ /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/covid 𝖨𝗇𝖽𝗂𝖺</code>"""

    URLSHORT_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋

ᴜʀʟ sʜᴏʀᴛᴇʀ  

➤ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ

➪ /short: 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/kB9TkCs8cX0</code>"""

    VIDEO_TXT ="""ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ᴍᴏᴅᴜʟᴇ.

• 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦

𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/kB9TkCs8cX0)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
<code>/mp4 https://youtu.be/kB9TkCs8cX0</code>
<code>/video https://youtu.be/kB9TkCs8cX0</code>"""

    ZOMBIES_TXT = """ʜᴇʟᴘs ᴛᴏ ᴋɪᴄᴋ ᴜsᴇʀᴀ

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    IMAGE_TXT = """➤ 𝐇𝐞𝐥𝐩: Iᴍᴀɢᴇ

ʜᴇʟᴘs ᴛᴏ ᴇᴅɪᴛ ᴀɴʏ ɪᴍᴀɢᴇ 

➤ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ

➪ 𝖩𝗎𝗌𝗍 𝗌𝖾𝗇𝖽 𝗆𝖾 𝖺 𝗂𝗆𝖺𝗀𝖾 𝗍𝗈 𝖾𝖽𝗂𝗍 ✨

𝖬𝖺𝖽𝖾 𝖻𝗒 <a href=https://t.me/MWUpdatez>ᴍᴡ ᴜᴘᴅᴀᴛᴇᴢ</a>"""

    STICKER_TXT = """sᴛɪᴄᴋᴇʀ ɪ'ᴅ ɢᴇɴᴇʀᴀᴛᴏʀ ᴏғ ғɪɴᴅᴇʀ.
• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
  ⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 
◉ Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """ʜᴇʟᴘs ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴛʜᴜᴍʙɴᴀɪʟ
    
⭕𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
𝘛𝘺𝘱𝘦 /ytthumb 𝘈𝘯𝘥 𝘝𝘪𝘥𝘦𝘰 𝘓𝘪𝘯𝘬

• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦
<code>/ytthumb https://youtu.be/UyzJ9KEoU0w</code>"""

    ABOOK_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄

ᴘᴅғ ғɪʟᴇ ᴛᴏ ᴀᴜᴛᴏ ғɪʟᴇ ᴄᴏɴᴠᴇʀᴛᴇʀ ✯

➤ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ

➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    GTRANS_TXT = """𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋

ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘs ʏᴏᴜ ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ ᴛᴇxᴛ ᴛᴏ ᴀɴʏ ʟᴀɴɢᴜᴀɢᴇ.ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
➤ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ
➪/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    RESTRIC_TXT = """➤ 𝐇𝐞𝐥𝐩: Mᴜᴛᴇ 🚫

ᴛʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴀ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴛʜᴀᴛ ᴄᴀɴ ᴜsᴇ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴛʜᴇɪʀ ɢʀᴏᴜᴘ ᴍᴏʀᴇ ᴇғғᴇᴄᴛɪᴠᴇʟʏ.

➪/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌"""
    CREATOR_REQUIRED = """❗<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """❗<b>എന്നെ Admin ആക്കത്ത സ്ഥലത്ത് ഞാൻ നിക്കില്ല പോകുവാ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ഇപ്പൊ എല്ലാം അടിച്ചുമാറ്റി തരാം...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""

    ENGLISH_TXT = """Look in Google or any internet browser's and find the right movie name and send it here for the movie / series ....\n\nIf you still do not get it. Send a message to group in this way Movie Name & year after @admin. Example: @admin Kurup.\n\nWe will try to upload if requested one is theatre print. Ott and Dvd released movies, will upload within 24 hours."""

    MALAYALAM_TXT = """Google അല്ലെങ്കിൽ ഏതേലും internet browser's ഇൽ നോക്കി ശരിയായ സിനിമയുടെ പേര് കണ്ടെത്തി ഇവിടെ നൽകുക എന്നാലേ സിനിമ / സീരിയസ് കിട്ടുകയുള്ളു....\n\nഎന്നിട്ടും കിട്ടുന്നില്ല എങ്കിൽ. @admin ശേഷം മൂവി Name & year. Example : @admin Kurup 2021 ഈ രീതിയിൽ  ഗ്രൂപ്പിൽ സെന്റ് ചെയുക. 24 മണിക്കൂറിനുള്ളിൽ അഡ്മിൻ കിട്ടിയാൽ upload ചെയ്യാം..\n\nതിയേറ്ററിൽ റിലീസ് ആയ മൂവിയാണ് ചോദിച്ചതെങ്കിൽ upload ചെയ്യാൻ ശ്രമിക്കാം. ott Dvd റിലീസ് ആയത് ആണെങ്കിൽ തന്നിരിക്കും."""
