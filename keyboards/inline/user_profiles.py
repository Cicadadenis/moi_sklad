# - *- coding: utf- 8 - *-
from utils.db_api.sqlite import get_userx, get_purchasesx


def get_user_profile(user_id):
    get_user = get_userx(user_id=user_id)
    get_purchases = get_purchasesx("*", user_id=user_id)
    count_items = 0
    if len(get_purchases) >= 1:
        for items in get_purchases:
            count_items += int(items[5])
    msg = f"<b>📱 Ваш профиль:</b>\n" \
          f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
          f"🔑 Мой ID: {get_user[1]}\n" \
          f"👤 Логин: <b>@{get_user[2]}</b>\n" \
          f"🕜 Регистрация: {get_user[6]}\n" \
          f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
          f"📊 Тебе Доступно: {get_user[4]} шт\n" \
          f"🔐 Полученно Акаунтов: {count_items} шт"
    return msg


def search_user_profile(user_id):
    get_status_user = get_userx(user_id=user_id)
    get_purchases = get_purchasesx("*", user_id=user_id)
    count_items = 0
    if len(get_purchases) >= 1:
        for items in get_purchases:
            count_items += int(items[5])
    msg = f"<b>📱 Профиль пользователя:</b> <a href='tg://user?id={get_status_user[1]}'>{get_status_user[3]}</a>\n" \
          f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
          f"🔑 ID: {get_status_user[1]}\n" \
          f"👤 Логин: <b>@{get_status_user[2]}</b>\n" \
          f"Ⓜ Имя: <a href='tg://user?id={get_status_user[1]}'>{get_status_user[3]}</a>\n" \
          f"🕜 Регистрация: {get_status_user[6]}\n" \
          f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
          f"📊 Доступно: {get_status_user[4]} шт\n" \
          f"🔐 Выданно Акаунтов: {count_items} шт\n"
    return msg
