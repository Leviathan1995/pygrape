from pygrape.pygrape import pygrape
import time


def main():
    writer = pygrape(0.05)
    print("Downloading pygrape.whl (2 MB)")
    bar = "█"
    for i in range(101):
        time.sleep(0.05)
        if i % 2 == 0:
            bar += "█"
        writer.writer(" " + str(i) + "% |" + bar + "|")
        writer.flush()
    writer.stop()


if __name__ == '__main__':
    main()
