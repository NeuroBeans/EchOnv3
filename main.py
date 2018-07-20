
import numpy as np
import collect_data
import neuroweb as nw
import os
from pywinauto.application import Application
import time
from pywinauto import keyboard

app = Application(backend="uia").start("OscGraph.exe")
#time.sleep(5)

path = "C:/Users/Public/Documents/ZETLab/trifo/result/oscgrph_1.dtu"  # ПУТЬ К ДАННЫМ
data, classes = collect_data.collect_data(path,app)
nw.neuroweb(data,classes)
app.kill()

