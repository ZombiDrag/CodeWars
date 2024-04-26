"""
DESCRIPTION:
Were you ever interested in the phenomena of astrology, star signs, tarot, voodoo ? 
(ok not voodoo that's too spooky)...
Task:
Your job for today is to finish the star_sign function by finding the astrological sign,
given the birth details as a Date object.
Start and end dates for zodiac signs vary on different resources so we will use this table
to get consistent results:

Aquarius ------ 21 January - 19 February
Pisces --------- 20 February - 20 March
Aries ---------- 21 March - 20 April
Taurus -------- 21 April - 21 May
Gemini -------- 22 May - 21 June
Cancer -------- 22 June - 22 July
Leo ------------- 23 July - 23 August
Virgo ----------- 24 August - 23 September
Libra ----------- 24 September - 23 October
Scorpio -------- 24 October - 22 November
Sagittarius ---- 23 November - 21 December
Capricorn ----- 22 December - 20 January

Test info: 100 random tests (dates range from January 1st 1940 until now)
"""




import datetime
def star_sign(date):
    if date < datetime.date(date.year,1,21):
        return 'Capricorn'
    if date < datetime.date(date.year,2,20):
        return 'Aquarius'
    if date < datetime.date(date.year,3,21):
        return 'Pisces'
    if date < datetime.date(date.year,4,21):
        return 'Aries'
    if date < datetime.date(date.year,5,22):
        return 'Taurus'
    if date < datetime.date(date.year,6,22):
        return 'Gemini'
    if date < datetime.date(date.year,7,23):
        return 'Cancer'
    if date < datetime.date(date.year,8,24):
        return 'Leo'
    if date < datetime.date(date.year,9,24):
        return 'Virgo'
    if date < datetime.date(date.year,10,24):
        return 'Libra'
    if date < datetime.date(date.year,11,23):
        return 'Scorpio'
    if date < datetime.date(date.year,12,22):
        return 'Sagittarius'
    return 'Capricorn'