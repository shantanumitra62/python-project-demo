import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "*Break Time*",
            message = "Your screen is on for 50 minutes. Its time for break. Break time of 10 minutes is recommended.",
            app_name = "Break Reminder",
            #app_icon = "C:\Users\SreySha\Downloads\cofee-break.png",
            ticker = "notification coming ...",
            timeout = 600
        )
        time.sleep(3)