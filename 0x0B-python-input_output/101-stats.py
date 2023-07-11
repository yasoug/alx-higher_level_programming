#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


def print_size_and_codes(size, stat_codes):
    print("File size: {:d}".format(size))
    for key, value in sorted(stat_codes.items()):
        if value:
            print("{:s}: {:d}".format(key, value))


def parse_stdin_and_compute():
    size = 0
    lines = 0
    stat_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                  "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            fields = list(map(str, line.strip().split(" ")))
            size += int(fields[-1])
            if fields[-2] in stat_codes:
                stat_codes[fields[-2]] += 1
            lines += 1
            if lines % 10 == 0:
                print_size_and_codes(size, stat_codes)
    except KeyboardInterrupt:
        print_size_and_codes(size, stat_codes)
        raise

    print_size_and_codes(size, stat_codes)


parse_stdin_and_compute()
