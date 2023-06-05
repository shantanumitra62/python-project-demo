import datetime
import wmi

wmiob = wmi.WMI()
sdata = wmiob.Win32_PerfFormattedData_PerfOS_System()
uptime = sdata[-1].SystemUpTime
tnow = datetime.datetime.now()
utime = datetime.timedelta(seconds=int(uptime))

print("System is up since:", utime)
boot = tnow-utime
bootime = "Boot time was around {}:{}:{}".format(boot.hour, boot.minute, boot.second)
print(bootime)