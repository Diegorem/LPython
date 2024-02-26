import math
import os
import random
import re
import sys

def timeConversion(s):
    tiempo = s.split(":")
    hr = int(tiempo[0])
    mn = tiempo[1]
    sec = tiempo[2][:2]
    AmPm = tiempo[2][2:4]

    if AmPm == 'AM' and hr == 12:
        hr = 0
    elif AmPm == 'PM' and hr != 12:
        hr += 12
    hr = str(hr)
    hr = hr.zfill(2)
    return f"{hr}:{mn}:{sec}"


def gradingStudents(grades):
    rounded_grades = []

    for grade in grades:
        if grade < 38:
            # No rounding occurs for failing grades
            rounded_grades.append(grade)
        else:
            # Round the grade to the next multiple of 5 if the difference is less than 3
            next_multiple_of_5 = (grade // 5 + 1) * 5
            if next_multiple_of_5 - grade < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                rounded_grades.append(grade)

    return rounded_grades


if __name__ == '__main__':


   ''' s = input()
    result = timeConversion(s)
    print(result)'''

   grades_count = int(input().strip())

   grades = []

   for _ in range(grades_count):
       grades_item = int(input().strip())
       grades.append(grades_item)

   result = gradingStudents(grades)
   print(grades)
   print(result)

