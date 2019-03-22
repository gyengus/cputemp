from os import popen
from sys import argv, exit, stdout
from getopt import getopt
from time import sleep

def readTemp():
    try:
        file = open("/sys/class/thermal/thermal_zone0/temp", "r")
        temp = int(file.read().replace("\n", ""))
        file.close()
        return(temp)
    except:
        print("Unsupported device")
        exit()

def convertTemp(temp):
    if temp > 200:
        return (temp / 1000)
    return(temp)

def showHelp():
    print("Show Raspberry Pi's or Orange Pi's CPU temperature\n"
        + "Usage: cputemp [option]\n\n"
        + "Options:\n"
        + "\t-h, --help\t\t\tdisplay this help and exit\n"
        + "\t-f, --format telegraf|n\t\tsetting output format\n"
        + "\t-c, --continuous\t\trefresh every 10 seconds\n\n"
        + "Project page: https://github.com/gyengus/cputemp")
    exit()

def formatTemp(arg):
    temp = convertTemp(readTemp())
    if arg == "telegraf":
        return("cpu temperature=" + str(temp))
    elif arg == "n":
        return(str(temp) + " °C")
    else:
        return("CPU temperature: " + str(temp) + " °C")

def printTemp(argv):
    try:
        argv = argv[1:]
        opts, args = getopt(argv, "f:hc", ["format=", "help", "continuous"])
        format = "h"
        continuous = False
        if len(opts) == 0:
            opts = [("-f", "h")]
        for opt, arg in opts:
            if opt in ("-f", "--format"):
                format = arg
            elif opt in ("-h", "--help"):
                showHelp()
            elif opt in ("-c", "--continuous"):
                continuous = True

        while True:
            if continuous:
                stdout.write(u"\u001b[1000D")
            stdout.write(formatTemp(format))
            stdout.flush()
            if not continuous:
                break;
            sleep(10)
        print("")
    except KeyboardInterrupt:
        print("")
        exit()

def main():
    printTemp(argv)
