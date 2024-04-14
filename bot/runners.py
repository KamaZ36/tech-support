from aiogram import Bot, Dispatcher

from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from settings import settings


async def polling_startup(bot: Bot) -> None:
    await bot.delete_webhook(drop_pending_updates=settings.skip_updating)


async def webhook_startup(bot: Bot):
    await bot.set_webhook(
        f"{settings.webhook_url}",
        drop_pending_updates=settings.skip_updating,
        secret_token=settings.webhook_secret
    )
    print("Webhook successfully")


async def webhook_shutdown(bot: Bot):
    if not settings.use_webhook:
        return
    if await bot.delete_webhook():
        print("Dropped main bot webhook.")
    else:
        print("Failed to drop main bot webhook.")
    await bot.session.close()


def run_webhook(dp: Dispatcher, bot: Bot):
    app: web.Application = web.Application()
    dp.startup.register(webhook_startup)
    dp.shutdown.register(webhook_shutdown)

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=settings.webhook_secret
    )
    webhook_requests_handler.register(app, path=settings.webhook_path)
    setup_application(app, dp, bot=bot)

    return web.run_app(app, host=settings.webapp_host, port=settings.webapp_port)


def run_polling(dp: Dispatcher, bot: Bot) -> None:
    dp.startup.register(polling_startup)
    return dp.run_polling(bot)
