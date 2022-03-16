# Author: Hafizul Damar Laya
# NIM: 120450028
# Affiliation: Sains Data ITERA
# Date: 13 March 2022
# Program Description: Program contains function to solve simple encryption and depcryption password problem
def check_pj(pw, limitasii):
    return False if (len(pw) > limitasii) or (len(pw) <=0) else True

def transform_1(charr,parmet):
    return chr(( ord(charr) // parmet['a'])+ parmet['c'])

def transform_2(charr, parmet):
    return chr(( ord(charr) % parmet['a'])+ parmet['c'])

def transform_3(kal1, kal2):
    return '+' if(kal1 > kal2) else '-'

def transform_(charr,parmet):
    return transform_1(charr,parmet)+ transform_2(charr,parmet)+ (transform_3(transform_1(charr,parmet), transform_2(charr,parmet) ) )

#enkripted
def enkripted(pw,parmet):
    return ''.join([ transform_( passw, parmet) for passw in pw ])

#depcrypted
def d_residu(charr, parmet):
    return ord(charr)-parmet['c']
def d_bagi(charr, parmet):
    return d_residu(charr, parmet) * parmet['a']
def dtransform_(ch1,ch2,parmet):
    return chr(d_bagi(ch1, parmet)+d_residu(ch2,parmet))
def dekripted(pw, parmet):
    return ''.join([ dtransform_(pw[i],pw[i+1], parmet) for i in range(0, len(pw), 3)])

import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def show_password(pws):
    clear()
    print("Showing password...")
    print()
    maksi = max(map( lambda x: len(x[0]), pws))
    maksi_total = max( map(lambda x:len(x[0] + x[1] ),pws) )
    aksesoris = lambda n:''.join( ['-' for i in range(n) ] )
    span= 5
    tanda_hub =': '
    print( aksesoris( maksi_total+ span+ len(tanda_hub) ) )
    for passw in pws:
        exp_space = maksi-len(passw[0])+span
        tam = ' '.join( ['' for i in range(exp_space) ] )
        print( passw[0] + tam + tanda_hub + passw[1] )
        print( aksesoris( maksi_total+ span + len(tanda_hub) ) )
