def get_event_details(username):
    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM accounts WHERE username = username)
    # account = cursor.fetchone()
    ms_events_details = [
        {
            'id': 1,
            'player1': 'Joe',
            'seed': '9'
        },
        {
            'id': 2,
            'player1': 'Michael',
            'seed': '10'
        }
    ]
    ws_events_details = [
        {
            'id': 1,
            'player1': 'Zoey',
            'seed': '12'
        },
        {
            'id': 2,
            'player1': 'Hanna',
            'seed': '10'
        }
    ]
    md_events_details = [
        {
            'id': 1,
            'player1': 'Neil',
            'player2': 'Jon',
            'seed': '15'
        },
        {
            'id': 2,
            'player1': 'Joey',
            'player2': 'Dan',
            'seed': '14'
        }
    ]
    wd_events_details = [
        {
            'id': 1,
            'player1': 'Jill',
            'player2': 'Rebecca',
            'seed': '18'
        },
        {
            'id': 2,
            'player1': 'Rina',
            'player2': 'Jennifer',
            'seed': '15'
        }
    ]
    xd_events_details = [
        {
            'id': 1,
            'player1': 'Kaden',
            'player2': 'Luna',
            'seed': '20'
        },
        {
            'id': 1,
            'player1': 'Lilly',
            'player2': 'Bruce',
            'seed': '22'
        }
    ]
    u19_events_details = [
        {
            'id': 1,
            'player1': 'Grace',
            'seed': '9'
        },
        {
            'id': 2,
            'player1': 'Malaya',
            'seed': '10'
        }
    ]
    u17_events_details = [
        {
            'id': 1,
            'player1': 'Mike',
            'seed': '10'
        }
    ]

    return {"ms_events_details": ms_events_details,
            "ws_events_details": ws_events_details,
            "md_events_details": md_events_details,
            "wd_events_details": wd_events_details,
            "xd_events_details": xd_events_details,
            "u19_events_details": u19_events_details,
            "u17_events_details": u17_events_details
            }
