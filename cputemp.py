#!/usr/bin/env python3

import os, sys, getopt, array

def readTemp():
    temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
    temp = int(temp.replace("\n", ""))
    return (temp)

def convertTemp(temp):
    if temp > 200:
        return (temp / 1000)
    return (temp)

def showHelp():
    print("Show Raspberry Pi's or Orange Pi's CPU temperature\nUsage: cputemp [option]\n\nOptions:\n\t-h, --help\t\t\tdisplay this help\n\t-f, --format telegraf|n\t\tsetting output format")


temp = convertTemp(readTemp())
argv = sys.argv[1:]
opts, args = getopt.getopt(argv, "f:h", ["format=", "help"])
if len(opts) == 0:
    opts = [("-f", "n")]
for opt, arg in opts:
    if opt in ("-f", "--format"):
        if arg == "telegraf":
            print("cpu temperature=" + str(temp))
        elif arg == "n":
            print(str(temp) + " °C")
        else:
            print(str(temp))
    elif opt in ("-h", "--help"):
        showHelp()