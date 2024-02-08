from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from jzbot.shell import Shell
from os.path import dirname

sysinfo_router = Router()

sysInfoString = '===[ System Information ]==='

sysInfoAllButtons = InlineKeyboardMarkup(
    inline_keyboard = [[
        InlineKeyboardButton(text='Arch', callback_data='arch'),
        InlineKeyboardButton(text='OS', callback_data='os')
    ],
    [
        InlineKeyboardButton(text='Ip', callback_data='ip'),
        InlineKeyboardButton(text='Uptime', callback_data='uptime')
    ],
    [
        InlineKeyboardButton(text='CPU', callback_data='cpu'),
        InlineKeyboardButton(text='GPU', callback_data='gpu')
    ],
    [
        InlineKeyboardButton(text='Neofetch', callback_data='neofetch')
    ]]
)

sysInfoBackButton = InlineKeyboardMarkup(
    inline_keyboard = [[
        InlineKeyboardButton(text='Back', callback_data='back')
    ]]
)

@sysinfo_router.message(Command('sysinfo'))
async def command_sysinfo(message: Message) -> None:
    await message.reply(text=sysInfoString, reply_markup=sysInfoAllButtons)

@sysinfo_router.callback_query(lambda c: c.data in ['arch', 'os', 'ip', 'uptime', 'cpu', 'gpu', 'neofetch', 'back'])
async def sysinfo_callback_query(cq: CallbackQuery):
    if cq.data == 'back':
        reply_markup = sysInfoAllButtons
        text = sysInfoString
    else:
        reply_markup = sysInfoBackButton
        text = await Shell(f'{dirname(__file__)}/sysinfo.sh {cq.data}').stdout
    try:
        await cq.message.edit_text(reply_markup=reply_markup, text=text)
    except:
        pass
