from pyrogram import Client as c

api_id = input('\nEnter your Api ID: ')
api_hash = input('\nEnter your Api Hash: ')
print('\nEnter phone number if asked!!')

u = c(':memory:', api_id=api_id, api_hash=api_hash)

with u:
    string = u.export_session_string()
    print("\nHERE YOUR SESSIONS STRING, COPY AND DON'T SHARE:")
    print(f'\n{string}')
