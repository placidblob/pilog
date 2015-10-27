import daemon
import time
import logging

# from
# http://stackoverflow.com/questions/4637420/efficient-python-daemon
#   To actually run it:
#   python pylogd.py


def do_something():
    while True:
        logging.info("piiiiing...")
        time.sleep(5)


def init():
    logging.basicConfig(filename='/tmp/pilogd.log',level=logging.DEBUG)
    # logging.debug('This message should go to the log file')
    # logging.info('So should this')
    # logging.warning('And this, too')


def run():
    with daemon.DaemonContext():
        init()
        do_something()


if __name__ == "__main__":
    run()


