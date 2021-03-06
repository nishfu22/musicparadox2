# (C) supun-maduraga my best friend for his project on call-music-plus

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from config import BOT_NAME, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>โจ **Welcome {query.message.from_user.mention}** \n
๐ญ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ๐ฎ๐น๐น๐ผ๐ ๐๐ผ๐ ๐๐ผ ๐ฝ๐น๐ฎ๐ ๐บ๐๐๐ถ๐ฐ ๐ผ๐ป ๐ด๐ฟ๐ผ๐๐ฝ๐ ๐๐ต๐ฟ๐ผ๐๐ด๐ต ๐๐ต๐ฒ ๐ป๐ฒ๐ ๐ง๐ฒ๐น๐ฒ๐ด๐ฟ๐ฎ๐บ'๐ ๐๐ผ๐ถ๐ฐ๐ฒ ๐ฐ๐ต๐ฎ๐๐ !**

๐ก **๐๐ถ๐ป๐ฑ ๐ผ๐๐ ๐ฎ๐น๐น ๐๐ต๐ฒ ๐๐ผ๐'๐ ๐ฐ๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฎ๐ป๐ฑ ๐ต๐ผ๐ ๐๐ต๐ฒ๐ ๐๐ผ๐ฟ๐ธ ๐ฏ๐ ๐ฐ๐น๐ถ๐ฐ๐ธ๐ถ๐ป๐ด ๐ผ๐ป ๐๐ต๐ฒ ยป ๐ ๐๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฏ๐๐๐๐ผ๐ป !**

โ **๐๐ผ๐ฟ ๐ถ๐ป๐ณ๐ผ๐ฟ๐บ๐ฎ๐๐ถ๐ผ๐ป ๐ฎ๐ฏ๐ผ๐๐ ๐ฎ๐น๐น ๐ณ๐ฒ๐ฎ๐๐๐ฟ๐ฒ ๐ผ๐ณ ๐๐ต๐ถ๐ ๐ฏ๐ผ๐, ๐ท๐๐๐ ๐๐๐ฝ๐ฒ /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "โ Add me to your Group โ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "โ How to use Me", callback_data="cbguides")
                ],[
                    InlineKeyboardButton(
                         "๐ Commands", callback_data="cbhelp"
                    ),
                    InlineKeyboardButton(
                        "๐ Donate", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "๐ฅ Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "๐ Wiki's Page", url="https://github.com/levina-lab/veezmusic/wiki/Veez-Music-Wiki's")
                ],[
                    InlineKeyboardButton(
                        "๐งช Source Code ๐งช", url="https://github.com/levina-lab/VeezMusic"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ก Hello {query.message.from_user.mention} welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Basic Commands", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "๐ Advanced Commands", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Admin Commands", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๐ Sudo Commands", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Bot Owner Commands", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Fun Commands", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ here is the basic commands</b>

๐ง [ GROUP VC CMD ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name)ย?- search video from youtube detailed
/vsong (video name)ย?- download video from youtube detailed
/lyric - (song name) lyrics scrapper
/vk (song name) - download song from inline mode

๐ง [ CHANNEL VC CMD ]

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/admincache - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ here is the advanced commands</b>

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/cache - refresh the admin cache
/ping - check the bot ping status
/uptime - check the bot uptime status

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ here is the admin commands</b>

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite assistant join to your group
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/silent - mute the music player on voice chat
/unsilent - unmute the music player on voice chat
/musicplayer (on / off) - disable / enable music player in your group

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ here is the sudo commands</b>

/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/stats - show the bot statistic

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ here is the owner commands</b>

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

๐ note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ here is the fun commands</b>

/chika - check it by yourself
/wibu - check it by yourself
/asupan - check it by yourself
/truth - check it by yourself
/dare - check it by yourself

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Command List", callback_data="cbhelps"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**๐ก here is the control menu of bot:**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โธ pause music", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "โถ๏ธ resume music", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โฉ skip music", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "โน end music", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ mute player", callback_data="cbmute"
                    ),
                    InlineKeyboardButton(
                        "๐ unmute player", callback_data="cbunmute"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ del cmd", callback_data="cbdelcmds"
                    )
                ]
            ]
        )
    )



@Client.on_callback_query(filters.regex("cbdelcmds"))
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information:</b>
        
**๐ก Feature:** delete every commands sent by users to avoid spam in groups !

**โ usage:**

 1๏ธโฃ to turn on feature:
     ยป type `/delcmd on`
    
 2๏ธโฃ to turn off feature:
     ยป type `/delcmd off`
      
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhelps"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ก Hello {query.message.from_user.mention} welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Basic Commands", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "๐ Advanced Commands", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Admin Commands", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๐ Sudo Commands", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Bot Owner Commands", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Fun Commands", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguides"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก BACK", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
