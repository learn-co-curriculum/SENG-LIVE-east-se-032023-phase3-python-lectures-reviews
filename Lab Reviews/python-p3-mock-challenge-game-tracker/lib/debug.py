#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    p1 = Player( 'Thomas' )
    p2 = Player( 'Princeton' )
    p3 = Player( 'Ryan' )
    p4 = Player( 'Patty' )

    g1 = Game( 'Apex Legends' )
    g2 = Game( 'Elden Ring' )
    g3 = Game( 'Breath of the Wild' )
    g4 = Game( 'Risk of Rain Returns' )
    g5 = Game( 'Patty Cakes' )

    r0 = Result( p4, g5, 5000 )
    r1 = Result( p1, g1, 5000 )
    r2 = Result( p2, g1, 4201 )
    r3 = Result( p3, g1, 4999 )
    r4 = Result( p4, g2, 2 )
    r5 = Result( p3, g2, 45 )
    r6 = Result( p1, g3, 600 )
    r7 = Result( p4, g4, 389 )
    r8 = Result( p2, g4, 567 )
    r9 = Result( p4, g5, 4000 )
    r10 = Result( p1, g1, 430 )
    r11 = Result( p1, g1, 4378 )

    ipdb.set_trace()
