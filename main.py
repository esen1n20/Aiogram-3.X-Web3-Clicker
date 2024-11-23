import asyncio
from aiogram import Bot, Dispatcher, F
from nastroyka import config
from handlers import user_commands



async def main():
    
    bot = Bot(config.bot_token.get_secret_value())
    
    dp = Dispatcher()

    
    dp.include_routers(
       user_commands.router
    )
    
    
    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)



if __name__ == "__main__":
    asyncio.run(main())