#!/usr/bin/env bash

acpi -t | awk '{print $4}' >> $1