# Log Processing

# As a programmer who has recently become familiar with regex, you have been asked to process dates, times, and the count of logs using regex and write a suitable pattern in the form of a function.

# Input
# The input consists of two values:

# Variable n representing the number of log lines.

# 1 <= n <= 10^6 

# Log lines to be processed.

# Output
# In this section, the processed log is displayed in the correct format.

# Year {year}, Hour {hour}: INFO={counts['INFO']}, WARNING={counts['WARNING']}, ERROR={counts['ERROR']}

# Example
# Sample Input 1
# 3
# [2020-07-28 08:04:19] ERROR: Alice write wrong regex.
# [2020-07-28 08:04:19] ERROR: Alice make mistake.
# [2024-01-04 23:17:55] INFO: Alice confused.

# Sample Output 1
# Year 2020, Hour 08: INFO=0, WARNING=0, ERROR=2
# Year 2024, Hour 23: INFO=1, WARNING=0, ERROR=0

# Sample Input 2
# 2
# [2024-01-04 23:17:55] INFO: Alice confused.
# [2023-09-18 12:03:18] WARNING: Alice does not use regex.

# Sample Output 2
# Year 2024, Hour 23: INFO=1, WARNING=0, ERROR=0
# Year 2023, Hour 12: INFO=0, WARNING=1, ERROR=0

# Note
# Your code must be written in the form of a function.

# Only regex should be used to solve the problem.

import re
from collections import defaultdict


def log_formatter(log_txt, pattern):
    log_dic = defaultdict(lambda: {"ERROR": 0, "WARNING": 0, "INFO": 0})

    for match in pattern.finditer(log_txt):
        year = match.group(1)
        hour = match.group(2)
        types = match.group(3)

        key = (year, hour)

        log_dic[key][types] += 1

    return log_dic


num_lines = int(input())
log_txt = ""

for ii in range(num_lines):
    line = input()
    log_txt += line + "\n"


pattern = re.compile(r"^\[(\d{4}).{7}(\d{2}).{8}([A-Z]{4,7})", flags=re.MULTILINE)

log_dic = log_formatter(log_txt, pattern)

output_str = ""
for log in log_dic:
    year = log[0]
    hour = log[1]
    info = log_dic[log].get("INFO")
    warning = log_dic[log].get("WARNING")
    error = log_dic[log].get("ERROR")

    output_str += (
        f"Year {year}, Hour {hour}: INFO={info}, WARNING={warning}, ERROR={error}\n"
    )

print(output_str)
