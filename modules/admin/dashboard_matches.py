def get_matches_details(username):
    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM accounts WHERE username = username)
    # account = cursor.fetchone()
    in_progress_matches = {
        'id': 1,
        'court_no': 1,
        'match_up': 'player',
        'event': 'First name',
        'score': 'Last name',
        'status': 'email'
    }

    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM player WHERE userid = user_account['username'])
    # player_account = cursor.fetchone()

    finished_matches = {
        'id': 1,
        'match_up': 'player',
        'event': 'First name',
        'score': 'Last name',
        'winner': 'email'
    }

    return in_progress_matches | finished_matches
