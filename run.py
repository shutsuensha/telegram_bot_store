import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers import router as user_router
from app.admin import admin as admin_router
from app.database.models import async_main

from aiogram.client.session.aiohttp import AiohttpSession



async def main():
    load_dotenv()
    
    await async_main()
    
    session = AiohttpSession(proxy='http://proxy.server:3128')
    bot = Bot(token=os.getenv('TOKEN'), session=session)
    dp = Dispatcher()
    
    dp.include_routers(user_router, admin_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
