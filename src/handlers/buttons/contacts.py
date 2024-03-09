from aiogram import Router, F, types
from aiogram.utils.text_decorations import html_decoration
from aiogram.utils.i18n import lazy_gettext as __

router = Router()


@router.message(F.text == __("☎️ Kontaktlar"))
async def on_contact(message: types.Message):
    message_text = (
        html_decoration.bold("Kontaktlar\n")
        + html_decoration.italic("🔍 Savol va takliflar uchun raqamlar:\n\n")
        + html_decoration.italic(
            "☎️ Call markaz: " + html_decoration.bold("+998 (99) 140-09-99\n")
        )
        + html_decoration.italic(
            "☎️ Qo'shimcha raqam: " + html_decoration.bold("+998 (97) 776-17-17")
        )
    )
    await message.answer(text=message_text)
