import datetime
import subprocess
from datetime import datetime, timedelta

def zoom_access(id, password):
    id = id.replace(' ', '')
    password = password.replace(' ', '')
    url = 'zoommtg:"//zoom.us/join?confno=' + id + '&pwd=' + password + '"'
    cmd = "open %s" %url
    subprocess.check_output(cmd, shell=True)

#開始時間の一分前までの秒数を求める
def convert_second(timedlt):
    now = datetime.now()
    one_minute_before = timedlt - timedelta(minutes=1) - timedelta(seconds=40)
    wait_time = one_minute_before - now
    return wait_time.total_seconds()
