from datetime import datetime
import time

from .listener import Listener

time.sleep(2)

listener = Listener()
start_time = listener.create_connection()
t = start_time[2]
while True:
    t += 1
    if t - start_time[2] > 30 or t == start_time[2]:
        listener.renew_listen_key()
        t = start_time[2]
    if int(datetime.now().strftime('%-d')) != start_time[0] and int(datetime.now().strftime('%-H')) == start_time[1] and int(datetime.now().strftime('%M')) == start_time[2]:
        start_time = listener.create_connection()
    time.sleep(60)