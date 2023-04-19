def get_player_details():
    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM accounts WHERE username = username)
    # account = cursor.fetchone()
    player_roaster = [
        {
            'id': 1,
            'username': 'John15482',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': '	name@site.com'
        },
        {
            'id': 2,
            'username': 'Kim1425',
            'first_name': 'Kimsila',
            'last_name': 'Marriye',
            'email': '	name@site.com'
        },
        {
            'id': 3,
            'username': 'Rossy1245',
            'first_name': 'Rossye',
            'last_name': 'Nermal',
            'email': '	name@site.com'
        },
        {
            'id': 4,
            'username': 'Rich5685',
            'first_name': 'Richard',
            'last_name': 'Orieal',
            'email': '	name@site.com'
        },
        {
            'id': 5,
            'username': 'Jac4587',
            'first_name': 'Jacob',
            'last_name': 'Hielsar',
            'email': '	name@site.com'
        },
        {
            'id': 6,
            'username': 'Wrap4585',
            'first_name': 'Wrapel',
            'last_name': 'Dere',
            'email': '	name@site.com'
        }
    ]

    return player_roaster
