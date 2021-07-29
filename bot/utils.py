from pyrogram.errors import UserNotParticipant

AUTH_CHANNEL = None

async def is_subscribed(_, client, message):
    user_id = message.from_user.id
    if not AUTH_CHANNEL:
        return True
    try:
        chat_member = await client.get_chat_member(chat_id=int(AUTH_CHANNEL), user_id=user_id)
    except UserNotParticipant:
        return False
    if chat_member.status in ["creator", "administrator", "member", "restricted"]:
        return True
    else:
        return False
