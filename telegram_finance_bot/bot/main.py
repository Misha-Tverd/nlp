import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import env
import os
from dotenv import load_dotenv


load_dotenv("../.env")



TOKEN = os.getenv("")