label start:
    jump chapter_select

label chapter_select:
    menu month_select:
        "Please choose a chapter."
        "Chapter 1.":
            jump chapter1_select
        "Chapter 2." if chapter2_avail:
            jump chapter2_select
    menu chapter1_select:
        "Please choose a day."
        "Day 1.":
            jump chapter1_day1
        "Day 2." if chapter1_day2_avail:
            jump chapter1_day2
        "Day 3." if chapter1_day3_avail:
            jump chapter1_day3
        "Day 4." if chapter1_day4_avail:
            jump chapter1_day4
        "Day 5." if chapter1_day5_avail:
            jump chapter1_day5
    menu chapter2_select:
        "Please choose a day."
        "Day 1.":
            jump chapter2_day1
###
# DAY LOG FOR DEVS #
# CHAPTER 1 - DAYS 1-5 #
# CHAPTER 2 - DAYS #
###
# MONTH 1 #
# Day 1 - Monday 1st January
# Day 2 - Tuesday 2nd January
# Day 3 - Wednesday 3rd January
# Day 4 - Thursday 4th January
# Day 5 - Friday 5th January
# Day 6 - Saturday 6th January
# Day 7 - Sunday 7th January
###
# Day 8 - Monday 8th January
# Day 9 - Tuesday 9th January
# Day 10 - Wednesday 10th January
# Day 11 - Thursday 11th January
# Day 12 - Friday 12th January
# Day 13 - Saturday 13th January
# Day 14 - Sunday 14th January
###
# Day 15 - Monday 15th January
# Day 16 - Tuesday 16th January
# Day 17 - Wednesday 17th January
# Day 18 - Thursday 18th January
# Day 19 - Friday 19th January
# Day 20 - Saturday 20th January
# Day 21 - Sunday 21st January
###
# Day 22 - Monday 22nd January
# Day 23 - Tuesday 23rd January
# Day 24 - Wednesday 24th January
# Day 25 - Thursday 25th January
# Day 26 - Friday 26th January
# Day 27 - Saturday 27th January
# Day 28 - Sunday 28th January
###
# MONTH 2 #
# Day 29 - Monday 29th January
# Day 30 - Tuesday 30th January
# Day 31 - Wednesday 31st January
# Day 32 - Thursday 1st February
# Day 33 - Friday 2nd February
# Day 34 - Saturday 3rd February
# Day 35 - Sunday 4th February
###
# Day 36 - Monday 5th February
# Day 37 - Tuesday 6th February
# Day 38 - Wednesday 7th February
# Day 39 - Thursday 8th February
# Day 40 - Friday 9th February
# Day 41 - Saturday 10th February
# Day 42 - Sunday 11th February
###
# Day 43 - Monday 12th February
# Day 44 - Tuesday 13th February
# Day 45 - Wednesday 14th February
# Day 46 - Thursday 15th February
# Day 47 - Friday 16th February
# Day 48 - Saturday 17th February
# Day 49 - Sunday 18th February
###
# Day 50 - Monday 19th February
# Day 51 - Tuesday 20th February
# Day 52 - Wednesday 21st February
# Day 53 - Thursday 22nd February
# Day 54 - Friday 23rd February
# Day 55 - Saturday 24th February
# Day 56 - Sunday 25th February