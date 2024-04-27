"""
DESCRIPTION:
This Kata is intended as a small challenge for my students

All Star Code Challenge #1

Write a function, called sumPPG, that takes two NBA player objects/struct/Hash/Dict/Class and sums their PPG

Examples:
iverson := NBAPlayer{ Team: "76ers", Ppg: 11.2 }
jordan  := NBAPlayer{ Team: "bulls", Ppg: 20.2 }
SumPpg(iverson,jordan) // => 31.4
"""

def sum_ppg(playerOne, playerTwo):
    jor = {}
    for key in playerOne:                                    
        jor = playerTwo[key] + playerOne[key]      
    a = float(jor)
    return a