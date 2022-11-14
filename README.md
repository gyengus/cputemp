# Show Raspberry Pi's or Orange Pi's CPU temperature

[![PyPI - License](https://img.shields.io/pypi/l/cputemp.svg?color=green)](https://opensource.org/licenses/MPL-2.0)
[![PyPI](https://img.shields.io/pypi/v/cputemp.svg)](https://pypi.org/project/cputemp/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/cputemp.svg)](https://pypi.org/project/cputemp/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cputemp.svg)](https://pypi.org/project/cputemp/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/cputemp.svg)](https://pypi.org/project/cputemp/)

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
- Bitcoin: bc1qx4q5epl7nsyu9mum8edrvp2my8tut0enrz7kcn
- EVM compatible (Ethereum, Fantom, Polygon, etc.): 0x9F0a70A7306DF3fc072446cAF540F6766a4CC4E8
- Litecoin: ltc1qk2gf43u3lw6vzhvah03wns0nkgetg2c7ea0w5r
- Solana: 14SHwk3jTNYdMkEvpbq1j7Eu9iUJ3GySnaBF4kqBR8Ah
- Flux: t1T3x4HExm4nWD7gN68px9zCF3ZFQyneFSK

Tested on Raspberry Pi Zero W and Orange Pi Zero

Project page: https://github.com/gyengus/cputemp
