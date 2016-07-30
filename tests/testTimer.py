from datetime import datetime
from datetime import timedelta
import threading

def update():
    now = datetime.now()
    print("%s" % now)
    run_at = now + timedelta(seconds=1)
    delay = (run_at - now).total_seconds()
    threading.Timer(delay, update).start()

update()
