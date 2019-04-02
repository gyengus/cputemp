# Show Raspberry Pi's or Orange Pi's CPU temperature

It reads CPU temperature from `/sys/class/thermal/thermal_zone0/temp`.

Install:
```bash
# pip install cputemp
```

Usage: 
```bash
$ cputemp [option]
```

Options: | &nbsp;
:--- | ---:
-h, --help | display this help and exit
-f, --format telegraf\|n | setting output format
-c, --continuous | refresh every 10 seconds

Tested on Raspberry Pi Zero W and Orange Pi Zero

Project page: https://github.com/gyengus/cputemp
