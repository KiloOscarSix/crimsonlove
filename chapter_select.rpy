label start:
    jump chapter_select

label chapter_select:
    menu month_select:
        "Please choose a month."
        "Month 1 (January).":
            jump month1_week_select
### MONTH 1 ###
    menu month1_week_select:
        "Please choose a week."
        "Week 1.":
            jump month1_week1_select
    menu month1_week1_select:
        "Please choose a day."
        "Day 1.":
            jump month1_week1_day1
        "Day 2." if month1_week1_day2_avail:
            jump month1_week1_day2
        "Day 3." if month1_week1_day3_avail:
            jump month1_week1_day3
        "Day 4." if month1_week1_day4_avail:
            jump month1_week1_day4
        "Day 5." if month1_week1_day5_avail:
            jump month1_week1_day5
