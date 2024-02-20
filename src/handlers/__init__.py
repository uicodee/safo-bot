from aiogram import Dispatcher

from src.handlers import commands, buttons, contents


def setup(dp: Dispatcher):
    commands.setup(dp)
    buttons.setup(dp)
    contents.setup(dp)
