"""
    This module implements the simple blocks world using PAIP GPS.
"""
from gps import gps

# Formulate the problem states and actions.
problem = {

    'initial': ['space on a', 'a on b', 'b on c', 'c on table', 'space on table'],
    'goal': ['space on c', 'c on b', 'b on a', 'a on table', 'space on table'],

    'initial1': ['space on table', 'space on b', 'b on table', 'space on c', 'c on a', 'a on table'],
    'goal1': ['space on b', 'b on table', 'space on a', 'a on table', 'space on c', 'c on table'],

    'initial2': ['space on a', 'a on table', 'space on b', 'b on table', 'space on c', 'c on table'],
    'goal2': ['c on table', 'b on c', 'a on b', 'space on a'],

    'actions': [
        {
            'action': 'move a from b to c',
            'preconds': [
                'space on a',
                'space on c',
                'a on b'
            ],
            'add': [
                'a on c',
                'space on b'
            ],
            'delete': [
                'a on b',
                'space on c'
            ]
        },
        {
            'action': 'move a from table to b',
            'preconds': [
                'space on a',
                'space on b',
                'a on table'
            ],
            'add': [
                'a on b'
            ],
            'delete': [
                'a on table',
                'space on b'
            ]
        },
        {
            'action': 'move a from b to table',
            'preconds': [
                'space on a',
                'space on table',
                'a on b'
            ],
            'add': [
                'a on table',
                'space on b'
            ],
            'delete': [
                'a on b'
            ]
        },
        {
            'action': 'move a from c to b',
            'preconds': [
                'space on a',
                'space on b',
                'a on c'
            ],
            'add': [
                'a on b',
                'space on c'
            ],
            'delete': [
                'a on c',
                'space on b'
            ]
        },
        {
            'action': 'move a from table to c',
            'preconds': [
                'space on a',
                'space on c',
                'a on table'
            ],
            'add': [
                'a on c'
            ],
            'delete': [
                'a on table',
                'space on c'
            ]
        },
        {
            'action': 'move a from c to table',
            'preconds': [
                'space on a',
                'space on table',
                'a on c'
            ],
            'add': [
                'a on table',
                'space on c'
            ],
            'delete': [
                'a on c'
            ]
        },
        {
            'action': 'move b from a to c',
            'preconds': [
                'space on b',
                'space on c',
                'b on a'
            ],
            'add': [
                'b on c',
                'space on a'
            ],
            'delete': [
                'b on a',
                'space on c'
            ]
        },
        {
            'action': 'move b from table to a',
            'preconds': [
                'space on b',
                'space on a',
                'b on table'
            ],
            'add': [
                'b on a'
            ],
            'delete': [
                'b on table',
                'space on a'
            ]
        },
        {
            'action': 'move b from a to table',
            'preconds': [
                'space on b',
                'space on table',
                'b on a'
            ],
            'add': [
                'b on table',
                'space on a'
            ],
            'delete': [
                'b on a'
            ]
        },
        {
            'action': 'move b from c to a',
            'preconds': [
                'space on b',
                'space on a',
                'b on c'
            ],
            'add': [
                'b on a',
                'space on c'
            ],
            'delete': [
                'b on c',
                'space on a'
            ]
        },
        {
            'action': 'move b from table to c',
            'preconds': [
                'space on b',
                'space on c',
                'b on table'
            ],
            'add': [
                'b on c'
            ],
            'delete': [
                'b on table',
                'space on c'
            ]
        },
        {
            'action': 'move b from c to table',
            'preconds': [
                'space on b',
                'space on table',
                'b on c'
            ],
            'add': [
                'b on table',
                'space on c'
            ],
            'delete': [
                'b on c'
            ]
        },
        {
            'action': 'move c from a to b',
            'preconds': [
                'space on c',
                'space on b',
                'c on a'
            ],
            'add': [
                'c on b',
                'space on a'
            ],
            'delete': [
                'c on a',
                'space on b'
            ]
        },
        {
            'action': 'move c from table to a',
            'preconds': [
                'space on c',
                'space on a',
                'c on table'
            ],
            'add': [
                'c on a'
            ],
            'delete': [
                'c on table',
                'space on a'
            ]
        },
        {
            'action': 'move c from a to table',
            'preconds': [
                'space on c',
                'space on table',
                'c on a'
            ],
            'add': [
                'c on table',
                'space on a'
            ],
            'delete': [
                'c on a'
            ]
        },
        {
            'action': 'move c from b to a',
            'preconds': [
                'space on c',
                'space on a',
                'c on b'
            ],
            'add': [
                'c on a',
                'space on b'
            ],
            'delete': [
                'c on b',
                'space on a'
            ]
        },
        {
            'action': 'move c from table to b',
            'preconds': [
                'space on c',
                'space on b',
                'c on table'
            ],
            'add': [
                'c on b'
            ],
            'delete': [
                'c on table',
                'space on b'
            ]
        },
        {
            'action': 'move c from b to table',
            'preconds': [
                'space on c',
                'space on table',
                'c on b'
            ],
            'add': [
                'c on table',
                'space on b'
            ],
            'delete': [
                'c on b'
            ]
        }
    ]
}


if __name__ == '__main__':

    # Use GPS to solve the problem formulated above.
    actionSequence = gps(
        problem['initial'],
        problem['goal'],
        problem['actions']
    )

    actionSequence1 = gps(
        problem['initial1'],
        problem['goal1'],
        problem['actions']
    )

    actionSequence2 = gps(
        problem['initial2'],
        problem['goal2'],
        problem['actions']
    )

    # Print the solution, if there is one.
    if actionSequence is not None:
        for action in actionSequence:
            print(action)
    else:
        print('plan failure...')

    print('\n')
    if actionSequence1 is not None:
        for action in actionSequence1:
            print(action)
    else:
        print('plan failure...')

    print('\n')
    if actionSequence2 is not None:
        for action in actionSequence2:
            print(action)
    else:
        print('plan failure...')

