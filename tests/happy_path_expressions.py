happy_path_expressions = {
    "* * * * * /user": {
        'MIN': [i for i in range(0, 60)],
        'HOUR': [i for i in range(0, 24)],
        'DAY-OF-MONTH': [i for i in range(1, 32)],
        'MONTH': [i for i in range(1, 13)],
        'DAY-OF-WEEK': [i for i in range(1, 8)],
        'COMMAND': "/user"
    },
    "0 0 12 6 5 /user": {
        'MIN': [0],
        'HOUR': [0],
        'DAY-OF-MONTH': [12],
        'MONTH': [6],
        'DAY-OF-WEEK': [5],
        'COMMAND': "/user"
    },
    "0,1 1,4 12,13 2,3 4,7 /user": {
        'MIN': [0, 1],
        'HOUR': [1,4],
        'DAY-OF-MONTH': [12,13],
        'MONTH': [2, 3],
        'DAY-OF-WEEK': [4, 7],
        'COMMAND': "/user"
    },
    "6-10 0-3 12-15 3-7 1-4 /user/bin": {
        'MIN': [6, 7, 8, 9, 10],
        'HOUR': [0, 1, 2, 3],
        'DAY-OF-MONTH': [12, 13, 14, 15],
        'MONTH': [3, 4, 5, 6, 7],
        'DAY-OF-WEEK': [1, 2, 3, 4],
        'COMMAND': "/user/bin"
    },
    "0/15 */3 4/10 2/2 1/3 /user": {
        'MIN': [0, 15, 30, 45],
        'HOUR': [0, 3, 6, 9, 12, 15, 18, 21],
        'DAY-OF-MONTH': [4, 14, 24],
        'MONTH': [2, 4, 6, 8, 10, 12],
        'DAY-OF-WEEK': [1, 4, 7],
        'COMMAND': "/user"
    }
}