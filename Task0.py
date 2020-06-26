
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

import csv


# Read file into texts and calls.
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

first_incoming_number = texts[0][0].replace(' ', '')
first_answering_number = texts[0][1].replace(' ', '')
time_for_first_text_entry = texts[0][2][-8:]

print('First record of texts, {} texts {} at time {}'.format(first_incoming_number,
                                                             first_answering_number,
                                                             time_for_first_text_entry))

last_outgoing_call = calls[-1][0].replace(' ', '')
last_incoming_call = calls[-1][1]
time_for_last_call_entry = calls[-1][2][-8:]
last_call_duration = calls[-1][3]

print('Last record of calls, {} calls {} at time {}, lasting {} seconds'.format(last_outgoing_call,
                                                                                last_incoming_call,
                                                                                time_for_last_call_entry,
                                                                                last_call_duration))

# Time complexity : O(1)
