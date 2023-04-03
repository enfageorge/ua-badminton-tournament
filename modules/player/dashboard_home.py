def get_player_profile_details(username, request):

    if request.method == 'POST':
        # INSERT to accounts table
        if 'email' in request.form:
            input_email = request.form['email']
            print(input_email)

        # INSERT to player table
        if 'phone_number' in request.form:
            input_phone_number = request.form['phone_number']
            print(input_phone_number)
        if 'dob' in request.form:
            input_dob = request.form['dob']
            print(input_dob)
        if 'club_name' in request.form:
            input_club_name = request.form['club_name']
            print(input_club_name)
        if 'gender_optionsRadios' in request.form:
            input_gender = request.form['gender_optionsRadios']
            print(input_gender)

        # INSERT to event table
        if 'event1' in request.form:
            input_event1 = request.form['event1']
            print(input_event1)

        # need to write data to DB.

    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM accounts WHERE username = username)
    # account = cursor.fetchone()
    user_account = {
        'id': 100,
        'username': 'player',
        'first_name': 'First name',
        'last_name': 'Last name',
        'email': 'email'
    }

    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM player WHERE userid = user_account['username'])
    # player_account = cursor.fetchone()

    player_account = {
        'player_id': 123,
        'seeding_score': 123,
        'social_media_consent': True,
        'competing_gender': 'f',
        'phone_number': '5203360140',
        'dob': '09-14-1998',  # MM-DD-YYYY
        'club_name': 'club_name_placeholder'

    }

    # need to send event information to front end too

    return_account = {**user_account, **player_account}

    return return_account
