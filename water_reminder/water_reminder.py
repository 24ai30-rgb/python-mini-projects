import time
from plyer import notification

while True:
    print("please some sip of water!")
    notification.notify(title="please some drink drink water",message="You need to dring some water",)
    time.sleep(60*60)