'''
Last Load

Daily Coding Challenge
June 7, 2026

Given the number of scoops of laundry detergent you have remaining and an array of how many scoops you used in each of the previous days, return the number of full days of detergent you have remaining.

Calculate your average daily usage from the usage history and assume that amount of usage each day going forward.
'''

#  the number of full days of detergent remaining = last_load_date(remaining number of scoops of laundry detergent, [scoops we used in each of the previous days]))
def last_load_date(remaining_det, list_num):
    list_sum = 0
    for degit in list_num:
        list_sum += degit
    list_avg = list_sum/len(list_num)
    remain_day = remaining_det // list_avg
    return int(remain_day)

#Tests:

print(last_load_date(10, [2, 2, 2, 2, 2, 2, 2])) # 5.
print(last_load_date(16, [2, 3, 0, 3, 4, 2, 1])) # 7.
print(last_load_date(33, [5, 0, 4, 3, 3, 2])) # 11.
print(last_load_date(50, [2, 0, 2, 9, 12, 0, 2])) # 12.
print(last_load_date(20, [13, 9, 12, 10, 8])) # 1.
