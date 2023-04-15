import time
import random
import numpy as np
import pandas as pd

strnam = 'Str(Strength)'
dexnam = 'Dex(Dexterity)'
connam = 'Con(Constitution)'
intnam = 'Int(Intelligence)'
wisnam = 'Wis(Wisdom)'
chanam = 'Cha(Charisma)'

standarray = [15, 14, 13, 12, 10, 8]

print('Welcome to DSF(D&D Stat Filler) V1!')

while True:

    print('Loading...')
    time.sleep(0.5)
    zerolocation = input(f'Where should 15 be? {strnam}, {dexnam}, {connam}, {intnam}, {wisnam}, or {chanam} ')

    if zerolocation == 'Str' or zerolocation == 'str' or zerolocation == 'Strength' or zerolocation == 'strength':
        standarray[0] = 'Str: 15, '
        strnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif zerolocation == 'Dex' or zerolocation == 'dex' or zerolocation == 'Dexterity' or zerolocation == 'dexterity':
        standarray[0] = 'Dex: 15, '
        dexnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif zerolocation == 'Con' or zerolocation == 'con' or zerolocation == 'Constitution' or zerolocation == 'constitution':
        standarray[0] = 'Con: 15, '
        connam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif zerolocation == 'Int' or zerolocation == 'int' or zerolocation == 'Intelligence' or zerolocation == 'intelligence':
        standarray[0] = 'Int: 15, '
        intnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif zerolocation == 'Wis' or zerolocation == 'wis' or zerolocation == 'Wisdom' or zerolocation == 'wisdom':
        standarray[0] = 'Wis: 15, '
        wisnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif zerolocation == 'Cha' or zerolocation == 'cha' or zerolocation == 'Charisma' or zerolocation == 'charisma':
        standarray[0] = 'Cha: 15, '
        chanam = 'UNAVAILABLE(ALREADY CHOSEN)'
    else:
        print('INVALID')

#Now 14 location!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    onelocation = input(f'Where should 14 be? {strnam}, {dexnam}, {connam}, {intnam}, {wisnam}, or {chanam} ')

    if onelocation == 'Str' or onelocation == 'str' or onelocation == 'Strength' or onelocation == 'strength':
        standarray[1] = 'Str: 14, '
        strnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif onelocation == 'Dex' or onelocation == 'dex' or onelocation == 'Dexterity' or onelocation == 'dexterity':
        standarray[1] = 'Dex: 14, '
        dexnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif onelocation == 'Con' or onelocation == 'con' or onelocation == 'Constitution' or onelocation == 'constitution':
        standarray[1] = 'Con: 14, '
        connam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif onelocation == 'Int' or onelocation == 'int' or onelocation == 'Intelligence' or onelocation == 'intelligence':
        standarray[1] = 'Int: 14, '
        intnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif onelocation == 'Wis' or onelocation == 'wis' or onelocation == 'Wisdom' or onelocation == 'wisdom':
        standarray[1] = 'Wis: 14, '
        wisnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif onelocation == 'Cha' or onelocation == 'cha' or onelocation == 'Charisma' or onelocation == 'charisma':
        standarray[1] = 'Cha: 14, '
        chanam = 'UNAVAILABLE(ALREADY CHOSEN)'
    else:
        print('INVALID')

#Now 13 location!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    twolocation = input(f'Where should 13 be? {strnam}, {dexnam}, {connam}, {intnam}, {wisnam}, or {chanam} ')

    if twolocation == 'Str' or twolocation == 'str' or twolocation == 'Strength' or twolocation == 'strength':
        standarray[2] = 'Str: 13, '
        strnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif twolocation == 'Dex' or twolocation == 'dex' or twolocation == 'Dexterity' or twolocation == 'dexterity':
        standarray[2] = 'Dex: 13, '
        dexnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif twolocation == 'Con' or twolocation == 'con' or twolocation == 'Constitution' or twolocation == 'constitution':
        standarray[2] = 'Con: 13, '
        connam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif twolocation == 'Int' or twolocation == 'int' or twolocation == 'Intelligence' or twolocation == 'intelligence':
        standarray[2] = 'Int: 13, '
        intnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif twolocation == 'Wis' or twolocation == 'wis' or twolocation == 'Wisdom' or twolocation == 'wisdom':
        standarray[2] = 'Wis: 13, '
        wisnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif twolocation == 'Cha' or twolocation == 'cha' or twolocation == 'Charisma' or twolocation == twolocation == 'charisma':
        standarray[2] = 'Cha: 13, '
        chanam = 'UNAVAILABLE(ALREADY CHOSEN)'
    else:
        print('INVALID')

#Now 12 Location!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    threelocation = input(f'Where should 12 be? {strnam}, {dexnam}, {connam}, {intnam}, {wisnam}, or {chanam} ')

    if threelocation == 'Str' or threelocation == 'str' or threelocation == 'Strength' or threelocation == 'strength':
        standarray[3] = 'Str: 12, '
        strnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif threelocation == 'Dex' or threelocation == 'dex' or threelocation == 'Dexterity' or threelocation == 'dexterity':
        standarray[3] = 'Dex: 12, '
        dexnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif threelocation == 'Con' or threelocation == 'con' or threelocation == 'Constitution' or threelocation == 'constitution':
        standarray[3] = 'Con: 12, '
        connam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif threelocation == 'Int' or threelocation == 'int' or threelocation == 'Intelligence' or threelocation == 'intelligence':
        standarray[3] = 'Int: 12, '
        intnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif threelocation == 'Wis' or threelocation == 'wis' or threelocation == 'Wisdom' or threelocation == 'wisdom':
        standarray[3] = 'Wis: 12, '
        wisnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif threelocation == 'Cha' or threelocation == 'cha' or threelocation == 'Charisma' or threelocation == threelocation == 'charisma':
        standarray[3] = 'Cha: 12, '
        chanam = 'UNAVAILABLE(ALREADY CHOSEN)'
    else:
        print('INVALID')

# Now 10 location!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    fourlocation = input(f'Where should 10 be? {strnam}, {dexnam}, {connam}, {intnam}, {wisnam}, or {chanam} ')

    if fourlocation == 'Str' or fourlocation == 'str' or fourlocation == 'Strength' or fourlocation == 'strength':
        standarray[4] = 'Str: 10, '
        strnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif fourlocation == 'Dex' or fourlocation == 'dex' or fourlocation == 'Dexterity' or fourlocation == 'dexterity':
        standarray[4] = 'Dex: 10, '
        dexnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif fourlocation == 'Con' or fourlocation == 'con' or fourlocation == 'Constitution' or fourlocation == 'constitution':
        standarray[4] = 'Con: 10, '
        connam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif fourlocation == 'Int' or fourlocation == 'int' or fourlocation == 'Intelligence' or fourlocation == 'intelligence':
        standarray[4] = 'Int: 10, '
        intnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif fourlocation == 'Wis' or fourlocation == 'wis' or fourlocation == 'Wisdom' or fourlocation == 'wisdom':
        standarray[4] = 'Wis: 10, '
        wisnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif fourlocation == 'Cha' or fourlocation == 'cha' or fourlocation == 'Charisma' or fourlocation == fourlocation == 'charisma':
        standarray[4] = 'Cha: 10, '
        chanam = 'UNAVAILABLE(ALREADY CHOSEN)'
    else:
        print('INVALID')

# Now 8 location!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    finallocation = input(f'Where should 8 be? {strnam}, {dexnam}, {connam}, {intnam}, {wisnam}, or {chanam} ')

    if finallocation == 'Str' or finallocation == 'str' or finallocation == 'Strength' or finallocation == 'strength':
        standarray[5] = 'Str: 8, '
        strnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif finallocation == 'Dex' or finallocation == 'dex' or finallocation == 'Dexterity' or finallocation == 'dexterity':
        standarray[5] = 'Dex: 8, '
        dexnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif finallocation == 'Con' or finallocation == 'con' or finallocation == 'Constitution' or finallocation == 'constitution':
        standarray[5] = 'Con: 8, '
        connam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif finallocation == 'Int' or finallocation == 'int' or finallocation == 'Intelligence' or finallocation == 'intelligence':
        standarray[5] = 'Int: 8, '
        intnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif finallocation == 'Wis' or finallocation == 'wis' or finallocation == 'Wisdom' or finallocation == 'wisdom':
        standarray[5] = 'Wis: 8, '
        wisnam = 'UNAVAILABLE(ALREADY CHOSEN)'
    elif finallocation == 'Cha' or finallocation == 'cha' or finallocation == 'Charisma' or finallocation == 'charisma':
        standarray[5] = 'Cha: 8, '
        chanam = 'UNAVAILABLE(ALREADY CHOSEN)'
    else:
        print('INVALID')

    print('Final Stats! V')
    print( )
    print(f'{standarray[0]}{standarray[1]}{standarray[2]}{standarray[3]}{standarray[4]}{standarray[5]}')
    rerun = input('Rerun? Y/N ')
    if rerun == 'Y':
        strnam = 'Str(Strength)'
        dexnam = 'Dex(Dexterity)'
        connam = 'Con(Constitution)'
        intnam = 'Int(Intelligence)'
        wisnam = 'Wis(Wisdom)'
        chanam = 'Cha(Charisma)'
        print( )
    elif rerun == 'N':
        print('Thank you for using DSF V1!')
        break