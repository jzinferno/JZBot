from aiogram import Dispatcher

from .SysInfo import sysinfo_router

dp = Dispatcher()

dp.include_routers(
    sysinfo_router
)
