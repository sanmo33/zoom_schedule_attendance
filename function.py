import datetime
import subprocess

def time_check():
    dt_now = datetime.datetime.now()
    return dt_now.year, dt_now.month, dt_now.day, dt_now.hour, dt_now.minute

def zoom_access(id, password):
    id = id.replace(' ', '')
    password = password.replace(' ', '')
    url = 'zoommtg:"//zoom.us/join?confno=' + id + '&pwd=' + password + '"'
    cmd = "open %s" %url
    subprocess.check_output(cmd, shell=True)

