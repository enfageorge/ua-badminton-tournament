def get_event_details(username):
    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM accounts WHERE username = username)
    # account = cursor.fetchone()
    ms_events_details = {
        'id': 1,
        'player1': 'Joe',
        'seed': 'First name'
    }
    ws_events_details = {
        'id': 1,
        'player1': 'Joe',
        'seed': 'First name'
    }
    md_events_details = {
        'id': 1,
        'player1': 'Joe',
        'player2': 'Joe',
        'seed': 'First name'
    }
    wd_events_details = {
        'id': 1,
        'player1': 'Joe',
        'player2': 'Joe',
        'seed': 'First name'
    }
    xd_events_details = {
        'id': 1,
        'player1': 'Joe',
        'player2': 'Joe',
        'seed': 'First name'
    }
    u19_events_details = {
        'id': 1,
        'player1': 'Joe',
        'seed': 'First name'
    }
    u17_events_details = {
        'id': 1,
        'player1': 'Joe',
        'seed': 'First name'
    }

    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM player WHERE userid = user_account['username'])
    # player_account = cursor.fetchone()

    # player_account = {
    #     'player_id': 123,
    #     'seeding_score': 123,
    #     'social_media_consent': True,
    #     'competing_gender': 'f',
    #     'phone_number': '5203360140',
    #     'dob': '09-14-1998',  # MM-DD-YYYY
    #     'club_name': 'club_name_placeholder'
    # }

    return ms_events_details | ws_events_details | md_events_details | wd_events_details | xd_events_details | u19_events_details | u17_events_details # | player_account
