import datetime
import subprocess
from datetime import datetime, timedelta

#idとpasswordを引数で受け取ってzoomにアクセスする関数
def zoom_access(id, password):
    id = id.replace(' ', '')
    password = password.replace(' ', '')
    url = 'zoommtg:"//zoom.us/join?confno=' + id + '&pwd=' + password + '"'
    cmd = "open %s" %url
    subprocess.check_output(cmd, shell=True)

#開始時間の一分前までの'秒数'を求める
def convert_second(timedlt):
    now = datetime.now()
    one_minute_before = timedlt - timedelta(minutes=1) - timedelta(seconds=40)
    wait_time = one_minute_before - now
    return wait_time.total_seconds()

#秒数から何時間何分何秒を求める関数(strで返す)
def convert_second_to_hms(sec):
    h,m,s = 0,0,0
    h = sec //3600
    tmp = sec % 3600
    m = tmp // 60
    s = tmp - 60*m
    return [str(h), str(m), str(s)]