from tg_bot import tg_bot_start
from vk_bot import vk_bot_start

import threading


if __name__ == '__main__':
    tg_thread = threading.Thread(target=tg_bot_start)
    vk_thread = threading.Thread(target=vk_bot_start)

    tg_thread.start()
    vk_thread.start()
