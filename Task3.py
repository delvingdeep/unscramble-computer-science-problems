"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Read file into texts and calls.
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
--------------------------
-------> Part A <---------
--------------------------
"""
area_codes = set()
bangalore_call_counter = 0
# get all the numbers with bangalore area code
for record in calls:
    if record[0][:5] == '(080)':

        # for fixed lines number
        if record[1][:1] == '(':
           code = record[1][record[1].find("(")+1:record[1].find(")")]
           area_codes.add(code)

        # for mobile number
        else:
            area_codes.add(record[1][:4])

        if record[1][:5] == '(080)':
            bangalore_call_counter += 1

print('The numbers called by people in Bangalore have codes:')
for code in sorted(area_codes):
    print(code)


"""
--------------------------
-------> Part B <---------
--------------------------
"""
print('{:0.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(bangalore_call_counter/len(area_codes)))

# Time complexity : O(n2 + n log n)
