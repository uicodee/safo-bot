from aiogram import Dispatcher

from src.handlers import commands, buttons, contents, callbacks


def setup(dp: Dispatcher):
    commands.setup(dp)
    buttons.setup(dp)
    callbacks.setup(dp)
    contents.setup(dp)
