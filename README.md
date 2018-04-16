if __name__ == '__main__':
main()# pygrape
[![Build Status](https://travis-ci.org/Leviathan1995/pygrape.svg?branch=master)](https://travis-ci.org/Leviathan1995/pygrape)
[![PyPI version](https://badge.fury.io/py/pygrape.svg)](https://badge.fury.io/py/pygrape)

pygrape is a python library for updating terminal output in realtime



### Usage

```python
pip3 install pygrape
```

### Example

```python
from pygrape import pygrape
import time

def main():
    #  Initialize the pygrape, 0.05 is the interval
    writer = pygrape(0.05)
    print("Downloading pygrape.whl (2 MB)")
    bar = "█"
    for i in range(101):
        time.sleep(0.05)
        # It only print fifty bars.
        if i % 2 == 0:
            bar += "█"
        writer.writer(" " + str(i) + "% |" + bar + "|")
        writer.flush()
    # Finish the printing
    writer.stop()

if __name__ == '__main__':
    main()
```

#### Result

![gif](https://github.com/Leviathan1995/pygrape/blob/master/doc/HD.gif)

### License

MIT
