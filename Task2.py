"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""


# Read file into texts and calls.

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

longest_time = 0
longest_time_number = None

# extract all numbers and add call duration
call_duration = {}

for record in calls:
    if record[0].replace(' ', '') not in call_duration.keys():
        call_duration.update({record[0].replace(' ', '') : int(record[3])})
    else:
        value = call_duration[record[0].replace(' ', '')]
        total_time = value + int(record[3])
        call_duration.update({record[0].replace(' ', '') : total_time})

    if record[1].replace(' ', '') not in call_duration.keys():
        call_duration.update({record[1].replace(' ', '') : int(record[3])})
    else:
        value = call_duration[record[1].replace(' ', '')]
        total_time = value + int(record[3])
        call_duration.update({record[1].replace(' ', '') : total_time})

max_call_duration = max(call_duration, key=call_duration.get)

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(max_call_duration,
                                                                                          call_duration[max_call_duration]))

# Time complexity : O(n)
