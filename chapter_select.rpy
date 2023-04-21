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
        "Day 2." if chapter2_day2_avail:
            jump chapter2_day2
        "Day 3." if chapter2_day3_avail:
            jump chapter2_day3
###
# DAY LOG FOR DEVS #
###
# YEAR ONE #
# Day 1 - Monday 1st January (Game start, meet Artificial Interspace)
# Day 2 - Tuesday 2nd January (Day Mora kidnapped you)
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
# Day 45 - Wednesday 14th February (Valentine's Day)
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
###
# Day 57 - Monday 26th February
# Day 58 - Tuesday 27th February
# Day 59 - Wednesday 28th February
# Day 60 - Thursday 1st March
# Day 61 - Friday 2nd March
# Day 62 - Saturday 3rd March
# Day 63 - Sunday 4th March
###
# Day 64 - Monday 5th March
# Day 65 - Tuesday 6th March
# Day 66 - Wednesday 7th March
# Day 67 - Thursday 8th March
# Day 68 - Friday 9th March
# Day 69 - Saturday 10th March
# Day 70 - Sunday 11th March (Angela's birthday)
###
# Day 71 - Monday 12th March
# Day 72 - Tuesday 13th March
# Day 73 - Wednesday 14th March
# Day 74 - Thursday 15th March
# Day 75 - Friday 16th March
# Day 76 - Saturday 17th March
# Day 77 - Sunday 18th March
###
# Day 78 - Monday 19th March
# Day 79 - Tuesday 20th March
# Day 80 - Wednesday 21st March
# Day 81 - Thursday 22nd March
# Day 82 - Friday 23rd March
# Day 83 - Saturday 24th March
# Day 84 - Sunday 25th March
###
# Day 85 - Monday 26th March
# Day 86 - Tuesday 27th March
# Day 87 - Wednesday 28th March
# Day 88 - Thursday 29th March
# Day 89 - Friday 30th March
# Day 90 - Saturday 31st March
# Day 91 - Sunday 1st April (April Fools)
###
# Day 92 - Monday 2nd April
# Day 93 - Tuesday 3rd April
# Day 94 - Wednesday 4th April
# Day 95 - Thursday 5th April
# Day 96 - Friday 6th April
# Day 97 - Saturday 7th April
# Day 98 - Sunday 8th April
###
# Day 99 - Monday 9th April
# Day 100 - Tuesday 10th April
# Day 101 - Wednesday 11th April
# Day 102 - Thursday 12th April
# Day 103 - Friday 13th April
# Day 104 - Saturday 14th April
# Day 105 - Sunday 15th April
###
# Day 106 - Monday 16th April
# Day 107 - Tuesday 17th April
# Day 108 - Wednesday 18th April
# Day 109 - Thursday 19th April
# Day 110 - Friday 20th April
# Day 111 - Saturday 21st April
# Day 112 - Sunday 22nd April
###
# Day 113 - Monday 23rd April
# Day 114 - Tuesday 24th April
# Day 115 - Wednesday 25th April
# Day 116 - Thursday 26th April
# Day 117 - Friday 27th April
# Day 118 - Saturday 28th April
# Day 119 - Sunday 29th April
###
# Day 120 - Monday 30th April
# Day 121 - Tuesday 1st May
# Day 122 - Wednesday 2nd May
# Day 123 - Thursday 3rd May
# Day 124 - Friday 4th May
# Day 125 - Saturday 5th May (Zena's birthday)
# Day 126 - Sunday 6th May
###
# Day 127 - Monday 7th May
# Day 128 - Tuesday 8th May
# Day 129 - Wednesday 9th May
# Day 130 - Thursday 10th May
# Day 131 - Friday 11th May
# Day 132 - Saturday 12th May
# Day 133 - Sunday 13th May
###
# Day 134 - Monday 14th May
# Day 135 - Tuesday 15th May
# Day 136 - Wedneaday 16th May
# Day 137 - Thursday 17th May
# Day 138 - Friday 18th May
# Day 139 - Saturday 19th May
# Day 140 - Sunday 20th May
###
# Day 141 - Monday 21st May
# Day 142 - Tuesday 22nd May
# Day 143 - Wednesday 23rd May
# Day 144 - Thursday 24th May
# Day 145 - Friday 25th May
# Day 146 - Saturday 26th May
# Day 147 - Sunday 27th May
###
# Day 148 - Monday 28th May
# Day 149 - Tuesday 29th May
# Day 150 - Wednesday 30th May
# Day 151 - Thursday 31st May
# Day 152 - Friday 1st June
# Day 153 - Saturday 2nd June
# Day 154 - Sunday 3rd June
###
# Day 155 - Monday 4th June
# Day 156 - Tuesday 5th June
# Day 157 - Wednesday 6th June
# Day 158 - Thursday 7th June
# Day 159 - Friday 8th June
# Day 160 - Saturday 9th June
# Day 161 - Sunday 10th June
###
# Day 162 - Monday 11th June
# Day 163 - Tuesday 12th June
# Day 164 - Wednesday 13th June
# Day 165 - Thursday 14th June
# Day 166 - Friday 15th June
# Day 167 - Saturday 16th June
# Day 168 - Sunday 17th June
###
# Day 169 - Monday 18th June
# Day 170 - Tuesday 19th June
# Day 171 - Wednesday 20th June
# Day 172 - Thursday 21st June
# Day 173 - Friday 22nd June
# Day 174 - Saturday 23rd June
# Day 175 - Sunday 24th June
###
# Day 176 - Monday 25th June
# Day 177 - Tuesday 26th June
# Day 178 - Wednesday 27th June (Alex/MC's birthday)
# Day 179 - Thursday 28th June
# Day 180 - Friday 29th June
# Day 181 - Saturday 30th June
# Day 182 - Sunday 1st July
###
# Day 183 - Monday 2nd July
# Day 184 - Tuesday 3rd July
# Day 185 - Wednesday 4th July
# Day 186 - Thursday 5th July
# Day 187 - Friday 6th July
# Day 188 - Saturday 7th July
# Day 189 - Sunday 8th July
###
# Day 190 - Monday 9th July
# Day 191 - Tuesday 10th July
# Day 192 - Wednesday 11th July
# Day 193 - Thursday 12th July
# Day 194 - Friday 13th July
# Day 195 - Saturday 14th July
# Day 196 - Sunday 15th July
###
# Day 197 - Monday 16th July
# Day 198 - Tuesday 17th July
# Day 199 - Wednesday 18th July
# Day 200 - Thursday 19th July
# Day 201 - Friday 20th July
# Day 202 - Saturday 21st July
# Day 203 - Sunday 22nd July
###
# Day 204 - Monday 23rd July
# Day 205 - Tuesday 24th July
# Day 206 - Wednesday 25th July
# Day 207 - Thursday 26th July
# Day 208 - Friday 27th July
# Day 209 - Saturday 28th July
# Day 210 - Sunday 29th July
###
# Day 211 - Monday 30th July
# Day 212 - Tuesday 31st July
# Day 213 - Wednesday 1st August
# Day 214 - Thursday 2nd August
# Day 215 - Friday 3rd August
# Day 216 - Saturday 4th August
# Day 217 - Sunday 5th August
###
# Day 218 - Monday 6th August
# Day 219 - Tuesday 7th August
# Day 220 - Wednesday 8th August
# Day 221 - Thursday 9th August
# Day 222 - Friday 10th August
# Day 223 - Saturday 11th August
# Day 224 - Sunday 12th August (Eli's birthday)
###
# Day 225 - Monday 13th August
# Day 226 - Tuesday 14th August
# Day 227 - Wednesday 15th August
# Day 228 - Thursday 16th August
# Day 229 - Friday 17th August
# Day 230 - Saturday 18th August
# Day 231 - Sunday 19th August
###
# Day 232 - Monday 20th August
# Day 233 - Tuesday 21st August
# Day 234 - Wednesday 22nd August
# Day 235 - Thursday 23rd August
# Day 236 - Friday 24th August
# Day 237 - Saturday 25th August
# Day 238 - Sunday 26th August
###
# Day 239 - Monday 27th August
# Day 240 - Tuesday 28th August
# Day 241 - Wednesday 29th August
# Day 242 - Thursday 30th August
# Day 243 - Friday 31st August
# Day 244 - Saturday 1st September
# Day 245 - Sunday 2nd September
###
# Day 246 - Monday 3rd September
# Day 247 - Tuesday 4th September
# Day 248 - Wednesday 5th September
# Day 249 - Thursday 6th September
# Day 250 - Friday 7th September
# Day 251 - Saturday 8th September
# Day 252 - Sunday 9th September
###
# Day 253 - Monday 10th September
# Day 254 - Tuesday 11th September
# Day 255 - Wednesday 12th September
# Day 256 - Thursday 13th September
# Day 257 - Friday 14th September
# Day 258 - Saturday 15th September
# Day 259 - Sunday 16th September
###
# Day 260 - Monday 17th September
# Day 261 - Tuesday 18th September
# Day 262 - Wednesday 19th September
# Day 263 - Thursday 20th September
# Day 264 - Friday 21st September
# Day 265 - Saturday 22nd September
# Day 266 - Sunday 23rd September
###
# Day 267 - Monday 24th September
# Day 268 - Tuesday 25th September
# Day 269 - Wednesday 26th September
# Day 270 - Thursday 27th September
# Day 271 - Friday 28th September
# Day 272 - Saturday 29th September
# Day 273 - Sunday 30th September
###
# Day 274 - Monday 1st October
# Day 275 - Tuesday 2nd October
# Day 276 - Wednesday 3rd October
# Day 277 - Thursday 4th October
# Day 278 - Friday 5th October
# Day 279 - Saturday 6th October
# Day 280 - Sunday 7th October
###
# Day 281 - Monday 8th October
# Day 282 - Tuesday 9th October
# Day 283 - Wednesday 10th October
# Day 284 - Thursday 11th October
# Day 285 - Friday 12th October
# Day 286 - Saturday 13th October
# Day 287 - Sunday 14th October
###
# Day 288 - Monday 15th October
# Day 289 - Tuesday 16th October
# Day 290 - Wednesday 17th October
# Day 291 - Thursday 18th October
# Day 292 - Friday 19th October
# Day 293 - Saturday 20th October
# Day 294 - Sunday 21st October
###
# Day 295 - Monday 22nd October
# Day 296 - Tuesday 23rd October
# Day 297 - Wednesday 24th October
# Day 298 - Thursday 25th October
# Day 299 - Friday 26th October
# Day 300 - Saturday 27th October
# Day 301 - Sunday 28th October
###
# Day 302 - Monday 29th October
# Day 303 - Tuesday 30th October
# Day 304 - Wednesday 31st October (Halloween)
# Day 305 - Thursday 1st November
# Day 306 - Friday 2nd November
# Day 307 - Saturday 3rd November
# Day 308 - Sunday 4th November
###
# Day 309 - Monday 5th November
# Day 310 - Tuesday 6th November
# Day 311 - Wednesday 7th November
# Day 312 - Thursday 8th November
# Day 313 - Friday 9th November
# Day 314 - Saturday 10th November
# Day 315 - Sunday 11th November
###
# Day 316 - Monday 12th November
# Day 317 - Tuesday 13th November
# Day 318 - Wednesday 14th November
# Day 319 - Thursday 15th November
# Day 320 - Friday 16th November
# Day 321 - Saturday 17th November
# Day 322 - Sunday 18th November
###
# Day 323 - Monday 19th November
# Day 324 - Tuesday 20th November
# Day 325 - Wednesday 21st November
# Day 326 - Thursday 22nd November
# Day 327 - Friday 23rd November
# Day 328 - Saturday 24th November
# Day 329 - Sunday 25th November
###
# Day 330 - Monday 26th November
# Day 331 - Tuesday 27th November
# Day 332 - Wednesday 28th November
# Day 333 - Thursday 29th November
# Day 334 - Friday 30th November
# Day 335 - Saturday 1st December
# Day 336 - Sunday 2nd December
###
# Day 337 - Monday 3rd December
# Day 338 - Tuesday 4th December
# Day 339 - Wednesday 5th December
# Day 340 - Thursday 6th December
# Day 341 - Friday 7th December
# Day 342 - Saturday 8th December
# Day 343 - Sunday 9th December
###
# Day 344 - Monday 10th December
# Day 345 - Tuesday 11th December
# Day 346 - Wednesday 12th December
# Day 347 - Thursday 13th December (Amari's birthday)
# Day 348 - Friday 14th December
# Day 349 - Saturday 15th December
# Day 350 - Sunday 16th December
###
# Day 351 - Monday 17th December
# Day 352 - Tuesday 18th December
# Day 353 - Wednesday 19th December
# Day 354 - Thursday 20th December
# Day 355 - Friday 21st December
# Day 356 - Saturday 22nd December
# Day 357 - Sunday 23rd December
###
# Day 358 - Monday 24th December
# Day 359 - Tuesday 25th December
# Day 360 - Wednesday 26th December
# Day 361 - Thursday 27th December
# Day 362 - Friday 28th December
# Day 363 - Saturday 29th December
# Day 364 - Sunday 30th December
###
# Day 365 - Monday 31st December
# YEAR TWO #
# Day 366 - Tuesday 1st January (New Year)
# Day 367 - Wednesday 2nd January (1 year anniversary of meeting Mora)
# Day 368 - Thursday 3rd January
# Day 369 - Friday 4th January
# Day 370 - Saturday 5th January
# Day 371 - Sunday 6th January