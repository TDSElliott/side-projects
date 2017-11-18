# For renaming my pay statements so they sort into chronological order
# rather than grouping themselves into a (useless) split of mid-month and end-month pay

import os
import re

path = '########'

for filename in os.listdir(path):
    # Split the filename by dash and underscore, as they denote dates
    sN = re.split(r'[-_]', filename)
    # Simple solution to see if the filename has already had the operation performed
    # If it has not it will return length of 4 (year) rather than 2 (day)
    if len(sN[0]) == 2:
        day = sN[0]
        month = sN[1]
        year = sN[2]
        remainder = sN[3]

        # print('Day',day,'month',month,'year',year)

        newFilename = year + '-' + month + '-' + day + '_' + remainder

        # print('new filename is', newFilename)

        # Rename the filename from the original path and filename to the same path and new filename
        os.rename(os.path.join(path, filename), os.path.join(path, newFilename))
        # Confirmation of above running successfully
        print('Renamed from', filename, 'to', newFilename)
