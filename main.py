from tg_bot import launch_tg_bot
from vk_bot import launch_vk_bot
from dotenv import load_dotenv

import threading


if __name__ == '__main__':
    load_dotenv()

    tg_thread = threading.Thread(target=launch_tg_bot)
    vk_thread = threading.Thread(target=launch_vk_bot)

    tg_thread.start()
    vk_thread.start()
