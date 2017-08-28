from Board import Card
testCases = [
        [
            [Card(2,8),Card(2,6),Card(0,9),Card(0,4),Card(3,None)],
            [Card(1,6),Card(1,9),Card(1,1),Card(2,2),Card(2,9)],
            [Card(0,7),Card(5,None),Card(5,None),Card(1,7),Card(1,5)],
            [Card(3,None),Card(1,8),Card(1,3),Card(4,None),Card(0,5)],
            [Card(5,None),Card(4,None),Card(4,None),Card(2,5),Card(0,3)],
            [Card(6,None),Card(5,None),Card(2,3),Card(4,None),Card(1,4)],
            [Card(0,2),Card(2,4),Card(0,8),Card(3,None),Card(3,None)],
            [Card(2,7),Card(2,1),Card(0,1),Card(1,2),Card(0,6)]
            ],
        [
            [Card(1,6),Card(1,8),Card(2,2),Card(5,None),Card(1,2)],
            [Card(1,9),Card(0,3),Card(5,None),Card(5,None),Card(1,5)],
            [Card(2,1),Card(3,None),Card(2,5),Card(2,4),Card(0,2)],
            [Card(4,None),Card(3,None),Card(2,7),Card(1,7),Card(2,6)],
            [Card(4,None),Card(0,1),Card(2,8),Card(5,None),Card(0,9)],
            [Card(1,1),Card(1,3),Card(4,None),Card(0,6),Card(2,9)],
            [Card(0,7),Card(6,None),Card(0,5),Card(3,None),Card(1,4)],
            [Card(0,8),Card(0,4),Card(3,None),Card(2,3),Card(4,None)]
            ],
        [
            [Card(1,9),Card(2,2),Card(1,4),Card(2,6),Card(5,None)],
            [Card(5,None),Card(5,None),Card(0,3),Card(2,9),Card(0,7)],
            [Card(4,None),Card(1,7),Card(5,None),Card(3,None),Card(0,9)],
            [Card(2,4),Card(4,None),Card(1,1),Card(0,8),Card(1,6)],
            [Card(1,3),Card(2,1),Card(2,3),Card(0,2),Card(0,6)],
            [Card(0,1),Card(2,7),Card(0,5),Card(3,None),Card(4,None)],
            [Card(1,2),Card(3,None),Card(2,5),Card(1,8),Card(3,None)],
            [Card(1,5),Card(6,None),Card(0,4),Card(4,None),Card(2,8)]
            ],
        [
            [Card(0,1),Card(2,6),Card(0,5),Card(3,None),Card(1,6)],
            [Card(2,2),Card(6,None),Card(2,4),Card(1,4),Card(1,1)],
            [Card(2,8),Card(4,None),Card(5,None),Card(2,9),Card(2,5)],
            [Card(4,None),Card(0,4),Card(5,None),Card(2,1),Card(1,8)],
            [Card(0,3),Card(5,None),Card(0,6),Card(3,None),Card(3,None)],
            [Card(1,7),Card(1,9),Card(3,None),Card(1,5),Card(5,None)],
            [Card(4,None),Card(0,7),Card(0,2),Card(1,2),Card(0,9)],
            [Card(2,7),Card(1,3),Card(0,8),Card(2,3),Card(4,None)]
            ],
        [
            [Card(5,None),Card(2,8),Card(2,3),Card(0,9),Card(2,5)],
            [Card(0,8),Card(0,3),Card(1,8),Card(3,None),Card(2,9)],
            [Card(3,None),Card(1,1),Card(2,6),Card(4,None),Card(5,None)],
            [Card(2,1),Card(6,None),Card(0,5),Card(0,2),Card(1,7)],
            [Card(1,3),Card(3,None),Card(2,7),Card(2,4),Card(0,4)],
            [Card(1,2),Card(3,None),Card(4,None),Card(0,1),Card(1,9)],
            [Card(1,6),Card(4,None),Card(4,None),Card(0,6),Card(1,4)],
            [Card(0,7),Card(5,None),Card(1,5),Card(2,2),Card(5,None)]
            ],
        # Hard one
        [
                [Card(2,1),Card(2,7),Card(5,None),Card(1,5),Card(3,None)],
                [Card(1,6),Card(5,None),Card(0,1),Card(1,1),Card(2,9)],
                [Card(1,2),Card(4,None),Card(2,2),Card(3,None),Card(0,8)],
                [Card(0,4),Card(2,5),Card(2,3),Card(0,5),Card(2,4)],
                [Card(3,None),Card(0,9),Card(0,2),Card(3,None),Card(1,8)],
                [Card(4,None),Card(0,6),Card(0,7),Card(4,None),Card(1,7)],
                [Card(1,9),Card(0,3),Card(2,6),Card(5,None),Card(5,None)],
                [Card(1,3),Card(6,None),Card(4,None),Card(1,4),Card(2,8)]
                ],
        # Didn't make it
        [
                [Card(1,3),Card(3,None),Card(4,None),Card(1,4),Card(4,None)],
                [Card(1,8),Card(1,9),Card(0,5),Card(2,6),Card(1,1)],
                [Card(1,6),Card(0,9),Card(3,None),Card(5,None),Card(5,None)],
                [Card(3,None),Card(1,2),Card(2,9),Card(2,8),Card(2,5)],
                [Card(2,4),Card(6,None),Card(0,2),Card(4,None),Card(0,8)],
                [Card(2,3),Card(0,1),Card(0,4),Card(1,5),Card(2,7)],
                [Card(0,7),Card(5,None),Card(3,None),Card(2,2),Card(2,1)],
                [Card(4,None),Card(0,3),Card(0,6),Card(1,7),Card(5,None)]
                ],
        [
                [Card(0,2),Card(1,6),Card(5,None),Card(2,6),Card(2,5)],
                [Card(0,1),Card(0,6),Card(0,4),Card(3,None),Card(4,None)],
                [Card(4,None),Card(2,4),Card(2,2),Card(1,7),Card(0,7)],
                [Card(0,5),Card(2,3),Card(1,2),Card(6,None),Card(4,None)],
                [Card(5,None),Card(1,3),Card(3,None),Card(5,None),Card(0,8)],
                [Card(3,None),Card(1,8),Card(1,1),Card(1,4),Card(1,5)],
                [Card(5,None),Card(2,1),Card(0,9),Card(2,9),Card(2,7)],
                [Card(1,9),Card(2,8),Card(0,3),Card(4,None),Card(3,None)]
                ],
        [
                [Card(1,3),Card(0,1),Card(0,4),Card(4,None),Card(0,5)],
                [Card(2,7),Card(1,9),Card(5,None),Card(0,7),Card(0,8)],
                [Card(2,5),Card(1,4),Card(1,6),Card(6,None),Card(0,6)],
                [Card(0,2),Card(1,5),Card(3,None),Card(0,9),Card(2,1)],
                [Card(3,None),Card(2,9),Card(1,2),Card(4,None),Card(4,None)],
                [Card(3,None),Card(2,8),Card(5,None),Card(2,3),Card(1,7)],
                [Card(0,3),Card(5,None),Card(5,None),Card(3,None),Card(2,2)],
                [Card(1,1),Card(1,8),Card(2,4),Card(2,6),Card(4,None)]
                ]
        ]

