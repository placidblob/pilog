#!/usr/bin/env bash

echo `date "+%Y/%m/%d %T"` `/opt/vc/bin/vcgencmd measure_temp | awk -F"=|'" '{print $2}'` >> $1

# for raspi:
# /opt/vc/bin/vcgencmd measure_temp
# or
# cat /sys/class/thermal/thermal_zone0/temp
