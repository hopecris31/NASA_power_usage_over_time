"""
Power Usage over Time Plot
Author: Hope Crisafi

 This plot shows what our FROST lander power consumption might look like
 over the course of a typical day. The time is incremented by 4 hours.  This assumes
 that the day begins with using only essential instruments on near maximal
 power.  Gradually, each science instrument (Co2 LiDAR, CheMin, and RAD) are turned on
 and used, while the other two are off.  The essential systems remain on throughout the
 whole day.  After each instrument is used (assumed a period of 4 hours per science instrument),
 they are shut off, and the essential systems power is reduced until the next day, when
 the cycle would start over again.
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("power_usage.csv")


time = data["Time"]
total_power_usage = data["Total Power Usage"]

plt.plot(time, total_power_usage)

plt.title("Power Usage Over Time (24 Hours)")
plt.xlabel("Time (Hours)")
plt.ylabel("Power Usage (W)")

plt.show()
