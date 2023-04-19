def get_matches_details():
    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM accounts WHERE username = username)
    # account = cursor.fetchone()
    in_progress_matches = [
        {
            'id': 1,
            'court_no': '',
            'match_up': 'John-Rich',
            'event': 'MS',
            'score': '',
            'status': 'Not yet played'
        },
        {
            'id': 2,
            'court_no': '1',
            'match_up': 'Kimsila-Rossye',
            'event': 'WS',
            'score': '',
            'status': 'In-progress'
        },
        {
            'id': 3,
            'court_no': '2',
            'match_up': 'Jacob/John - Wrapel/Kimsila',
            'event': 'MD',
            'score': '',
            'status': 'In-progress'
        }
    ]

    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM player WHERE userid = user_account['username'])
    # player_account = cursor.fetchone()

    finished_matches = [
        {
            'id': 1,
            'match_up': 'John-Derek',
            'event': 'MS',
            'score': '20-21',
            'winner': 'Derek'
        },
        {
            'id': 2,
            'match_up': 'Kimsila-Daisy',
            'event': 'WS',
            'score': '19-21',
            'winner': 'Daisy'
        },
        {
            'id': 3,
            'match_up': 'John - Jack',
            'event': 'MS',
            'score': '20-21',
            'winner': 'Jack'
        }
    ]

    return {"in_progress_matches": in_progress_matches, "finished_matches": finished_matches}
