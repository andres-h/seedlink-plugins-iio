#!/usr/bin/env python3

import sys
import os
import glob
import struct


_doy = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365)


def _is_leap(y):
    """True if y is a leap year."""
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)


def _ldoy(y, m):
    """The day of the year of the first day of month m, in year y.

    Note: for January, m=1; for December, m=12.
    Examples:
    _ldoy(1900, 4) = 90
    _ldoy(1900, 1) = 0
    _ldoy(1999, 4) = 90
    _ldoy(2004, 4) = 91
    _ldoy(2000, 4) = 91

    """
    return _doy[m - 1] + (_is_leap(y) and m >= 3)


def _mdy2dy(month, day, year):
    return _ldoy(year, month) + day


class Seedlink(object):
    def __init__(self):
        self.__fd = os.fdopen(63, "wb")

    def send_raw3(self, sta, cha, t, usec_corr, tqual, data):
        packet = struct.pack(
            "@i10s10s9i%di" % len(data),
            8,
            sta.encode(),
            cha.encode(),
            t.year,
            _mdy2dy(t.month, t.day, t.year),
            t.hour,
            t.minute,
            t.second,
            t.microsecond,
            usec_corr,
            tqual,
            len(data),
            *data
        )

        self.__fd.write(packet)


class IIODevice(object):
    def __init__(self, name, recsize=0):
        for dev in glob.glob("/sys/bus/iio/devices/*"):
            with open(os.path.join(dev, "name")) as f:
                if f.read().strip() == name:
                    self.__dev = dev
                    break

        else:
            raise Exception("device %s not found" % name)

        self.__recsize = recsize

    def get(self, attr):
        with open(os.path.join(self.__dev, attr)) as f:
            return f.read().strip()

    def set(self, attr, value):
        found = False

        for path in glob.glob(os.path.join(self.__dev, attr)):
            found = True

            with open(path, "w") as f:
                f.write(str(value))

        if not found:
            raise Exception("%s not found" % os.path.join(self.__dev, attr))

    def __iter__(self):
        if self.__recsize == 0:
            return

        with open(os.path.join("/dev", os.path.basename(self.__dev)), "rb") as f:
            while True:
                yield f.read(self.__recsize)

