import logging

from .bot import dp
from aiogram import executor

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)


__all__ = ("executor", "dp")