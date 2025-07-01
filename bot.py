import logging
import asyncio
import aiohttp
from aiogram import Bot, Dispatcher

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

async def check_upbit_listings():
    url = "https://api.upbit.com/v1/market/all?isDetails=false"
    known_markets = set()
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    data = await resp.json()
                    new_markets = {item["market"] for item in data if item["market"].startswith("KRW-")}
                    added = new_markets - known_markets
                    if added:
                        msg = f"🆕 Найдены новые листинги на Upbit:\n" + "\n".join(added)
                        await bot.send_message(chat_id=CHAT_ID, text=msg)
                        known_markets.update(added)
        except Exception as e:
            logging.error(f"Ошибка: {e}")
        await asyncio.sleep(300)

async def notify_alive():
    while True:
        try:
            await bot.send_message(chat_id=CHAT_ID, text="🤖 Бот работает. Мониторим листинги Upbit...")
        except Exception as e:
            logging.error(f"Ошибка при отправке уведомления: {e}")
        await asyncio.sleep(18000)

async def main():
    await asyncio.gather(check_upbit_listings(), notify_alive())

if __name__ == "__main__":
    asyncio.run(main())
