# Show Raspberry Pi's or Orange Pi's CPU temperature

[![PyPI - License](https://img.shields.io/pypi/l/cputemp.svg?color=green)](https://opensource.org/licenses/MPL-2.0)
[![PyPI](https://img.shields.io/pypi/v/cputemp.svg)](https://pypi.org/project/cputemp/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/cputemp.svg)](https://pypi.org/project/cputemp/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cputemp.svg)](https://pypi.org/project/cputemp/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/cputemp.svg)](https://pypi.org/project/cputemp/)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=K5PAV5V7WGWFL)

It reads CPU temperature from `/sys/class/thermal/thermal_zone0/temp`.

### Install
```bash
# pip install cputemp
```

### Usage
```bash
$ cputemp [option]
```

### Options
* -h, --help display this help and exit
* -f, --format telegraf\|n setting output format
* -c, --continuous refresh every 10 seconds

### Donations
If you like this program, please donate me!
- PayPal: https://paypal.me/gyengus
- Bitcoin: 1QJzLBK9uQP4RthmKJRQwy3v5sd4XS4S7P
- Bitcoin Cash: qp04tazu4fe7lv6zr99suu40swqqp747nsm0kcfckv
- Ethereum: 0x2bD68120A56acBf6Dbd11da2060228b8912C1e3C

Tested on Raspberry Pi Zero W and Orange Pi Zero

Project page: https://github.com/gyengus/cputemp
