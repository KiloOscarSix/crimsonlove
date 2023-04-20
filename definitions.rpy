### VARIABLE DEFINITIONS ###
default zena_affection = 0
default amari_affection = 0
default angela_affection = 0
default mora_affection = 0
default month1_week1_day2_avail = False
default month1_week1_day3_avail = False
default month1_week1_day4_avail = False
default month1_week1_day5_avail = False
default month1_week1_day6_avail = False
default mora_death = False
default mora_almost_kill = False
default mora_push = False
default month1_week1_day3_moraumbrella = False
define flash = Fade(.25, 0.0, .75, color="#fff")
transform t_xpos(x):
  xpos x
default mora_hobbies_unlock = False
default mora_job_unlock = False
default mora_workenjoy_failed_unlock = False

### CHARACTER DEFINITIONS ###
define my = Character("Myself", image="mc")
image side mc = "images/mc_side_normal.png"
### ZENA ###
define zena = Character("Zena", image="zena")
image side zena idol = "images/zena/idol/side_normal.png"
image side zena = "images/zena/newstudent/side_normal.png"
# IDOL #
image zena idol:
    "images/zena/idol/idol.png"
    zoom 1.75
image zena idol normal:
    "images/zena/idol/normal.png"
    zoom 1.75
image zena idol talk:
    "images/zena/idol/talk.png"
    zoom 1.75
image zena idol eyes_closed normal:
    "images/zena/idol/eyes_closed_normal.png"
    zoom 1.75
image zena idol eyes_closed talk:
    "images/zena/idol/eyes_closed_talk.png"
    zoom 1.75
# NEW STUDENT #
image zena newstudent normal:
    "images/zena/newstudent/normal.png"
    zoom 1.75
image zena newstudent talk:
    "images/zena/newstudent/talk.png"
    zoom 1.75
image zena newstudent eyes_closed normal:
    "images/zena/newstudent/eyes_closed_normal.png"
    zoom 1.75
image zena newstudent eyes_closed talk:
    "images/zena/newstudent/eyes_closed_talk.png"
    zoom 1.75
# STUDENT #
image zena student normal:
    "images/zena/student/normal.png"
    zoom 1.75
image zena student talk:
    "images/zena/student/talk.png"
    zoom 1.75
image zena student eyes_closed normal:
    "images/zena/student/eyes_closed_normal.png"
    zoom 1.75
image zena student eyes_closed talk:
    "images/zena/student/eyes_closed_talk.png"
    zoom 1.75

### ALESSA ###
define alessa = Character("Alessa")
# STUDENT #
image alessa student normal:
    "images/alessa/student/normal.png"
    zoom 1.75
image alessa student talk:
    "images/alessa/student/talk.png"
    zoom 1.75
image alessa student sad:
    "images/alessa/student/sad.png"
    zoom 1.75

### ANGELA ###
define angela = Character("Angela", image="angela")
image side angela idol = "images/angela/idol/side_normal.png"
image side angela = "images/angela/casual/side_normal.png"
# IDOL #
image angela idol normal:
    "images/angela/idol/normal.png"
    zoom 1.75
image angela idol talk:
    "images/angela/idol/talk.png"
    zoom 1.75
image angela idol eyes_closed normal:
    "images/angela/idol/eyes_closed_normal.png"
    zoom 1.75
image angela idol eyes_closed talk:
    "images/angela/idol/eyes_closed_talk.png"
    zoom 1.75
# CASUAL #
image angela casual normal:
    "images/angela/casual/normal.png"
    zoom 1.75
image angela casual talk:
    "images/angela/casual/talk.png"
    zoom 1.75
image angela casual eyes_closed normal:
    "images/angela/casual/eyes_closed_normal.png"
    zoom 1.75
image angela casual eyes_closed talk:
    "images/angela/casual/eyes_closed_talk.png"
    zoom 1.75

### AMARI ###
define amari = Character("Amari", image="amari")
image side amari idol = "images/amari/idol/side_normal.png"
image side amari = "images/amari/casual/side_normal.png"
# IDOL #
image amari idol normal:
    "images/amari/idol/normal.png"
    zoom 1.75
image amari idol talk:
    "images/amari/idol/talk.png"
    zoom 1.75
image amari idol eyes_closed normal:
    "images/amari/idol/eyes_closed_normal.png"
    zoom 1.75
image amari idol eyes_closed talk:
    "images/amari/idol/eyes_closed_talk.png"
    zoom 1.75
# CASUAL #
image amari casual normal:
    "images/amari/casual/normal.png"
    zoom 1.75
image amari casual talk:
    "images/amari/casual/talk.png"
    zoom 1.75
image amari casual eyes_closed normal:
    "images/amari/casual/eyes_closed_normal.png"
    zoom 1.75
image amari casual eyes_closed talk:
    "images/amari/casual/eyes_closed_talk.png"
    zoom 1.75

### ELI ###
define eli = Character("Eli", image="eli")
image side eli = "images/employees/eli/side_normal.png"
# WORK #
image eli work normal:
    "images/employees/eli/normal.png"
    zoom 1.75
image eli work eyes_closed normal:
    "images/employees/eli/eyes_closed_normal.png"
    zoom 1.75

### CARA ###
define cara = Character("Cara", image="cara")
image side cara = "images/employees/cara/side_normal.png"
# WORK #
image cara work normal:
    "images/employees/cara/normal.png"
    zoom 1.75
image cara work eyes_closed normal:
    "images/employees/cara/eyes_closed_normal.png"
    zoom 1.75

### MORA ###
define mora = Character("Mora", image="mora")
image side mora = "images/mora/arbiter/side_normal.png"
# ARBITER #
image mora arbiter normal:
    "images/mora/arbiter/normal.png"
    zoom 1.75
image mora arbiter eyes_closed normal:
    "images/mora/arbiter/eyes_closed_normal.png"
    zoom 1.75
image mora arbiter no_coat normal:
    "images/mora/arbiter/no_coat/normal.png"
    zoom 1.75
image mora arbiter no_coat eyes_closed normal:
    "images/mora/arbiter/no_coat/eyes_closed_normal.png"
    zoom 1.75
# UNDERWEAR #
image mora underwear coat normal:
    "images/mora/underwear/coat/normal.png"
    zoom 1.75
image mora underwear coat eyes_closed normal:
    "images/mora/underwear/coat/eyes_closed_normal.png"
    zoom 1.75
image mora underwear normal:
    "images/mora/underwear/normal.png"
    zoom 1.75
image mora underwear eyes_closed normal:
    "images/mora/underwear/eyes_closed_normal.png"
    zoom 1.75
# CASUAL #
image mora casual normal:
    "images/mora/casual/normal.png"
    zoom 1.75
image mora casual eyes_closed normal:
    "images/mora/casual/eyes_closed_normal.png"
    zoom 1.75
image mora casual ponytail normal:
    "images/mora/casual/ponytail/normal.png"
    zoom 1.75
image mora casual ponytail eyes_closed normal:
    "images/mora/casual/ponytail/eyes_closed_normal.png"
    zoom 1.75
image mora casual coat normal:
    "images/mora/casual/coat/normal.png"
    zoom 1.75
image mora casual coat eyes_closed normal:
    "images/mora/casual/coat/eyes_closed_normal.png"
    zoom 1.75
image mora casual coat ponytail normal:
    "images/mora/casual/coat/ponytail/normal.png"
    zoom 1.75
image mora casual coat ponytail eyes_closed normal:
    "images/mora/casual/coat/ponytail/eyes_closed_normal.png"
    zoom 1.75

### BACKGROUND DEFINITIONS ###
image bg apartment exterior = "images/backgrounds/Apartment_Exterior.png"
image bg apartment exterior night = "images/backgrounds/Apartment_Exterior_Night.png"
image bg bathroom = "images/backgrounds/Bathroom.png"
image bg bathroom foggy = "images/backgrounds/Bathroom_Foggy.png"
image bg bedroom day = "images/backgrounds/Bedroom_Day.png"
image bg bedroom evening = "images/backgrounds/Bedroom_Evening.png"
image bg bedroom night = "images/backgrounds/Bedroom_Night.png"
image bg bedroom night dark = "images/backgrounds/Bedroom_Night_Dark.png"
image bg cafeteria day = "images/backgrounds/Cafeteria_Day.png"
image bg city afternoon = "images/backgrounds/City_Afternoon.png"
image bg city morning = "images/backgrounds/City_Morning.png"
image bg city night = "images/backgrounds/City_Night.png"
image bg city raining = "images/backgrounds/City_Raining.png"
image bg classroom day = "images/backgrounds/Classroom_Day.png"
image bg futon room = "images/backgrounds/Futon_Room.png"
image bg futon room night = "images/backgrounds/Futon_Room_Night.png"
image bg kitchen day = "images/backgrounds/Kitchen_Day.png"
image bg kitchen night = "images/backgrounds/Kitchen_Night.png"
image bg laundromat = "images/backgrounds/Laundromat.png"
image bg living room dark = "images/backgrounds/Livingroom_Dark.png"
image bg living room day = "images/backgrounds/Livingroom_Day.png"
image bg living room night = "images/backgrounds/Livingroom_Night.png"
image bg onsen building = "images/backgrounds/Onsen_Building.png"
image bg onsen building night = "images/backgrounds/Onsen_Building_Night.png"
image bg outdoor stairs = "images/backgrounds/Outdoor_Stairs.png"
image bg restaurant a = "images/backgrounds/Restaurant_A.png"
image bg restaurant b = "images/backgrounds/Restaurant_B.png"
image bg school hallway = "images/backgrounds/School_Hallway_Day.png"
image bg sitting room = "images/backgrounds/Sitting_Room.png"
image bg sitting room dark = "images/backgrounds/Sitting_Room_Dark.png"
image bg small apartment kitchen = "images/backgrounds/Small_Apartment_Kitchen.png"
image bg small apartment kitchen night = "images/backgrounds/Small_Apartment_Kitchen_Night.png"
image bg street autumn day = "images/backgrounds/Street_Autumn_Day.png"
image bg street autumn evening = "images/backgrounds/Street_Autumn_Evening.png"
image bg street autumn night = "images/backgrounds/Street_Autumn_Night.png"
image bg street spring day = "images/backgrounds/Street_Spring_Day.png"
image bg street spring evening = "images/backgrounds/Street_Spring_Evening.png"
image bg street spring night = "images/backgrounds/Street_Spring_Night.png"
image bg street spring rain = "images/backgrounds/Street_Spring_Rain.png"
image bg street summer day = "images/backgrounds/Street_Summer_Day.png"
image bg street summer evening = "images/backgrounds/Street_Summer_Evening.png"
image bg street summer night = "images/backgrounds/Street_Summer_Night.png"
image bg street summer rain = "images/backgrounds/Street_Summer_Rain.png"
image bg street summer stars = "images/backgrounds/Street_Summer_Stars.png"
image bg train beach = "images/backgrounds/Train_beach.png"
image bg train day = "images/backgrounds/Train_Day.png"
image bg train day rain = "images/backgrounds/Train_Day_Rain.png"
image bg train evening = "images/backgrounds/Train_Evening.png"
image bg train night = "images/backgrounds/Train_Night.png"
image bg train night rain = "images/backgrounds/Train_Night_Rain.png"
image bg train tunnel = "images/backgrounds/Train_Tunnel.png"
image bg stage = "images/backgrounds/stage.png"
image bg backstage = "images/backgrounds/backstage.png"
