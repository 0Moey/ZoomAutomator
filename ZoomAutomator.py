import keyboard, time, subprocess
import pandas as pd
from datetime import datetime, date
import os
import subprocess
import platform


while True:
  cached_day = date.today().weekday()
  target_csv = pd.read_csv('map.csv').Type.values[cached_day]
  current_csv = pd.read_csv(target_csv)
  while date.today().weekday() == cached_day:
    timestr = datetime.now().strftime("%H:%M")
    if timestr in current_csv.Time.values:
      index = current_csv.Time.values.tolist().index(timestr)
      ID = current_csv.ID.values[index]
      PASS = current_csv.Pass.values[index]
      if "Win" in platform.system():
        os.startfile(f'zoommtg://zoom.us/join?confno={ID}&pwd={PASS}&zc=0&browser=chrome')
        time.sleep(60)
      elif "Linux" in platform.system():
        os.startfile(f'zoommtg://zoom.us/join?confno={ID}&pwd={PASS}&zc=0&browser=chrome')
        time.sleep(60)
      elif "Darwin" in platform.system():
        subprocess.run(["open", f'zoommtg://zoom.us/join?confno={ID}&pwd={PASS}&zc=0&browser=chrome'])
        time.sleep(60)
    else:
      time.sleep(1)
  time.sleep(1)