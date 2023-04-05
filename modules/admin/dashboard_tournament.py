def get_tournament_details(username, request):
    if request.method == 'POST':
        # INSERT to Tournament table
        if 'name' in request.form:
            name = request.form['name']
            print(name)
        if 'venue' in request.form:
            venue = request.form['venue']
            print(venue)
        if 'location' in request.form:
            location = request.form['location']
            print(location)
        if 'registration_open' in request.form:
            registration_open = request.form['registration_open']
            print(registration_open)
        if 'registration_deadline' in request.form:
            registration_deadline = request.form['registration_deadline']
            print(registration_deadline)
        if 'withdraw_deadline' in request.form:
            withdraw_deadline = request.form['withdraw_deadline']
            print(withdraw_deadline)
        if 'tournament_start_date' in request.form:
            tournament_start_date = request.form['tournament_start_date']
            print(tournament_start_date)
        if 'tournament_end_date' in request.form:
            tournament_end_date = request.form['tournament_end_date']
            print(tournament_end_date)
        if 'events' in request.form:
            events = request.form['events']
            print(events)
        if 'Regulations' in request.form:
            Regulations = request.form['Regulations']
            print(Regulations)
        if 'announcements' in request.form:
            announcements = request.form['announcements']
            print(announcements)

        # need to write data to DB.

    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM accounts WHERE username = username)
    # account = cursor.fetchone()
    tournament_details = {
        'name': '2023 Smashcat Tournament',
        'venue': 'UoArizona Recreation Center, South Gym',
        'location': 'Tucson, USA',
        'contact': 'Julie Fan',
        'contact_email': 'juliefan@arizona.edu',
        'contact_phone': '520-123-3344',
        'registration_open': '2023-08-01T10:00',
        'registration_deadline': '2023-08-15T10:00',
        'withdraw_deadline': '2023-08-20T10:00',
        'tournament_start_date': '2023-08-25T10:00',
        'tournament_end_date': '2023-09-01T10:00',
        'events': 'MS, MD, WS, WD',
        'Regulations': 'Fee per player: Fee includes rec center access, shuttles, lunch, and refreshments.',
        'announcements': '-The registration deadline is on 04/15/2023. -MD and WD events are currently full.'
    }

    return tournament_details
