import os
import asyncio
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

# Вставте свої токени
BOT_TOKEN = os.getenv("BOT_TOKEN") or "7558726763:AAHjgT38QegjAcMup2xsrclm2AfZ46hQLxI"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or "AIzaSyAcFq5gJ5B4qZaRM7aK96-4-sNUMxQ-N0M"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()  # Dispatcher створюється без аргументів у aiogram 3.x

# Налаштування Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

@dp.message()
async def handle_message(message: Message):
    response = model.generate_content(message.text)
    await message.answer(response.text)

async def main():
    # Підключаємо бота до диспетчера
    dp.include_router(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())