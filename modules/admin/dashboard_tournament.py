def get_tournament_details(username):
    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM accounts WHERE username = username)
    # account = cursor.fetchone()
    tournament_details = {
        'id': 1,
        'name': 'player',
        'location': 'First name',
        'registration_open': '04/01/2023',
        'registration_closed': '04/15/2023',
        'withdraw_deadline': '04/20/2023',
        'tournament_start_date': '04/25/2023',
        'tournament_end_date': '06/01/2023',
        'events': 'MS, MD, WS, WD',
        'Regulations': 'The timeline of the events wll be posted soon.',
        'announcements': 'No updated yet'
    }

    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM player WHERE userid = user_account['username'])
    # player_account = cursor.fetchone()

    # annoucements = {
    #     'player_id': 123,
    #     'seeding_score': 123,
    #     'social_media_consent': True,
    #     'competing_gender': 'f',
    #     'phone_number': '5203360140',
    #     'dob': '09-14-1998',  # MM-DD-YYYY
    #     'club_name': 'club_name_placeholder'
    # }

    return tournament_details #| player_account
