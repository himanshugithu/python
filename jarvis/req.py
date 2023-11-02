import requests
import time
while 1:

    response = requests.post("http://192.168.43.98/ledon")
    time.sleep(1)
    response = requests.post("http://192.168.43.98/ledoff")
    time.sleep(1)
    