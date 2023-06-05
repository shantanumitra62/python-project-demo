#import winotify as win

#print(dir(win))

from winotify import Notification, audio

import time

import psutil

import sysinfo

import uptime

# ctypes required for using GetTickCount64()
import ctypes



toast = Notification(app_id="Shan's Script", duration="long", title="Hey buddy!!", 
                        msg="Hello Folk you are about to experie magic")

toast.set_audio(audio.LoopingCall, loop=False)

toast.add_actions(label="Click me!", launch="https://google.com", )

## Adding time to get the system time

sys_time = time.localtime()
curr_time = time.strftime("%H:%M:%S", sys_time)
print(curr_time)

# this give an epoch format time which is a complex one
boot_time =  psutil.boot_time()

# Display the system info of the machine
print(sysinfo.getsysinfo())

## Getting the uptime of the last boot in time
up_since = uptime._uptime_windows()

print(up_since/1000)

## finding the time since the PC is powered on
## For Windows, we would be using an inbuilt API function 
## found in Windows OS under the name gettickcount64(). 

# getting the library in which GetTickCount64() resides
lib =  ctypes.windll.kernel32

# calling the function amd storing the return value
t = lib.GetTickCount64()

# since the time is in milliseconds i.e. 1000 * seconds
# therefore truncating the value
t= int(str(t)[:-3])

# extracting hours, minutes, seconds & days from t
# variable (which stores total time in seconds)
mins, sec = divmod(t, 60)
hours, mins = divmod(mins, 60)
days, hours = divmod(hours, 24)

# formatting the time in readable form
# (format = x days , HH:MM:SS)

print(f"{days} days, {hours:02}:{mins:02}:{sec:02}", "up simce these days")






#print(boot_time)

##toast.show()