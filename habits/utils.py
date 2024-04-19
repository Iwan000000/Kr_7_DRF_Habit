from Kr_7_DRF_Habit.settings import TELEGRAM_BOT_API_KEY
import requests


telegram_token = TELEGRAM_BOT_API_KEY
send_message_url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'


def send_telegram_message(habit):
    """Функция отправки сообщения в Telegram"""
    user = habit.user
    message = create_message(habit, user)
    requests.post(
        url=send_message_url,
        data={
            'chat_id': user.telegram,
            'text': message
        })


def create_message(habit, user):
    """Функция создания сообщения"""
    if habit.reward:
        reward_text = f"После этого вы сможете получить {habit.reward}!"
    else:
        reward_text = f"После этого вы можете {habit.associated_nice_habit.action}!"
    result = f"Привет, {user.name}! Сегодня в {habit.time} в {habit.place} вам следует {habit.action} " \
             f"в течение {habit.duration_time}! {reward_text} Удачи!!!"
    return result
