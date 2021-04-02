# KryPtoN Music Bot

[![Actions Badge](https://img.shields.io/github/workflow/status/Kry9toN/KryPtoN-Music-Bot/PyCheck/master?label=Build&style=flat-square&logo=github-actions&logoColor=white&color=98CE00)](https://github.com/Kry9toN/KryPtoN-Music-Bot/actions)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/6275e97d871b45458235492edfa77745)](https://www.codacy.com/gh/Kry9toN/KryPtoN-Music-Bot/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Kry9toN/KryPtoN-Music-Bot&amp;utm_campaign=Badge_Grade)

Music on Voice Calls Telegram

# Support
All distro linux (windows maybe not support)

# Requirements
- Telegram API_ID and API_HASH [Get here](https://my.telegram.org/apps)
- Python 3.7 or higher
- Needs user account not bot from bot father
- Install ffmpeg

# Usage
Install package required
```
$ git clone https://github.com/Kry9toN/KryPtoN-Music-Bot
$ cd KryPtoN-Music-Bot
$ pip install -r requirements.txt
```
Setup config
rename configs_sample.py to configs.py and edit

Execute!
```
$ python3 -m krypton
```

# Heroku 

### Generate String session [IMPORTANT]
Download this file [generate_string_session.py](https://raw.githubusercontent.com/Kry9toN/KryPtoN-Music-Bot/master/generate_string_session.py)

$ pip3 install pyrogram TgCrypto
$ python3 generate_string_session.py
You will get a session string, copy it, Then use heroku commands to push to heroku

## Commands
Command | Description
:--- | :---
/start | To Start The bot.
/help | To Show This Message.
/ping | To Ping All Datacenters Of Telegram.
/skip | To Skip Any Playing Music.
/play youtube/saavn/deezer [song_name] | To Play A Song.
/queue | To Check Queue Status.
/join | To Join Voice Chat.
/leave | To Leave Voice Chat.
/donation | To Display Link Donations

## To-Do
- add moar feature

# Donation
- [Saweria](https://saweria.co/donate/Kry9toN)
- [Paypal](https://www.paypal.me/KomodoOS)

# Credit
[@MarshalX](https://github.com/MarshalX)
[@thehamkercat](https://github.com/thehamkercat)
