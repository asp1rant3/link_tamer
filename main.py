import hashlib
import pyshorteners
from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle

API_TOKEN = 'TOKEN'  # API

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def shortener(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)


@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    url = shortener(inline_query.query)
    input_content = InputTextMessageContent(url, parse_mode='HTML')
    result_id: str = hashlib.md5(url.encode()).hexdigest()
    item = InlineQueryResultArticle(
        id=result_id,
        title=inline_query.query or "URL Shortener",
        description='Shortened link',
        input_message_content=input_content
    )
    await inline_query.answer([item], is_personal=True)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)