from pyrogram import Client as c

id = input('\nEnter your Api ID: ')
hash = input('\nEnter your Api Hash: ')
print('\nEnter phone number if asked!!')

u = c(':memory:', api_id=id, api_hash=hash)

with u:
    string = u.export_session_string()
    print("\n HERE YOUR SESSIONS STRING, COPY AND DON'T SHARE:")
    print(f'\n{string}')