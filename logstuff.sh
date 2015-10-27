#!/usr/bin/env bash

echo `date "+%Y/%m/%d %T"` `acpi -t | awk '{print $4}'` >> $1

# for raspi:
# /opt/vc/bin/vcgencmd measure_temp