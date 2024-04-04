#!/usr/bin/python3
"""
Module: 0-stats.py

This module reads stdin line by line
and computes metrics
"""


import sys
import re


total_file_size = 0
line_count = 0
status_code_counts = {
                         200: 0,
                         301: 0,
                         400: 0,
                         401: 0,
                         403: 0,
                         404: 0,
                         405: 0,
                         500: 0
                        }

try:
    for line in sys.stdin:
        match = re.match(
                r'\d+\.\d+\.\d+\.\d+ - \[.*\] "GET /projects/260 HTTP/1\.1"'
                r' (\d+) (\d+)',
                line
                )

        if match:
            status_code, file_size = map(int, match.groups())
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1

        if line_count % 10 == 0:
            total_file_size = sum(
                    int(size) for size in re.findall(r'\d+', line)
                    )
            print(f"File size: {total_file_size}")
            for code in sorted(status_code_counts):
                if status_code_counts[code] > 0:
                    print(f"{code}: {status_code_counts[code]}")
            line_count = 0
            total_file_size = 0
            status_code_counts = {
                                     200: 0,
                                     301: 0,
                                     400: 0,
                                     401: 0,
                                     403: 0,
                                     404: 0,
                                     405: 0,
                                     500: 0
                        }


except KeyboardInterrupt:
    pass
