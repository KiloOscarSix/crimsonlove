label start:
    jump chapter_select

label chapter_select:
    menu month_select:
        "Please choose a chapter."
        "Chapter 1.":
            jump chapter1_select
        #"Chapter 2." if chapter2_avail:
            #jump chapter2_select
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
    #menu chapter2_select:
        #"Please choose a day."
        #"Day 1.":
            #jump chapter2_day1
