import tkinter.messagebox as mb
import sys
from loguru import logger

logger.remove()
logger.add(sys.stderr, format="<level>{message}</level>")


def field_error():
    mb.showerror("Ошбика", "Заполните все поля.")


def degree_error():
    mb.showerror("Ошбика", "Размер вектора должен быть степенью двойки! Используйте Дискретное преобразование Фурье.")
    return
