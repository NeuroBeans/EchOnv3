from pywinauto.application import Application
import time
from pywinauto import keyboard
from pywinauto.application import Application
import time
from pywinauto import keyboard


def save_data(app):
    time.sleep(2)
    app.Window_(best_match='Многоканальный осциллограф', top_level_only=True).child_window(title="Запись", auto_id="1016", control_type="Button").click()
    keyboard.SendKeys("{ENTER}")

