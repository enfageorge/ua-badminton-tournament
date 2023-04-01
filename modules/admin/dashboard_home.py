def get_player_details(username):
    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM accounts WHERE username = username)
    # account = cursor.fetchone()
    player_roaster = {
        'id': 1,
        'username': 'player',
        'first_name': 'First name',
        'last_name': 'Last name',
        'email': 'email'
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

    return player_roaster #| player_account
