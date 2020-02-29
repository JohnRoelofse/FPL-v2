def populate_initial_tables():
    """
    This function:
        1. Extracts gameweek info, football player and football team data from the FPL API;
        2. Loads this data into gameweek_info, football_players, and football_teams tables. 
    """
    
    # Load libraries
    import requests
    import sqlite3
    import os

    # Specify url 
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

    # Start session
    session = requests.session()

    # Retrieve data from url
    get_request = session.get(url)

    # Deserialise (decode) JSON to Python objects
    js = get_request.json()

    # Extract event, team and player data from JSON
    gameweek_info = js['events']
    football_teams = js['teams']
    football_players = js['elements']    # players referred to as elements

    ### Store data in fpl sqlite3 database
    # Change directory
    os.chdir('/home/ubuntu/venv/sqlite_db/')
    
    # Connect to database
    conn = sqlite3.connect('fpl.sqlite')
    cur = conn.cursor()

    # Events 
    for item in gameweek_info:
        cur.execute("INSERT INTO gameweek_info (gw_id, gw_name, gw_deadline) VALUES ( ?, ?, ? )", 
                    (item['id'], item['name'], item['deadline_time']))

    # Teams
    for item in football_teams:
        cur.execute("INSERT INTO football_teams (fb_team_id, fb_team_name, fb_short_name) VALUES ( ?, ?, ? )", 
                    (item['id'], item['name'], item['short_name']))

    # Players
    for item in football_players:
        cur.execute("INSERT INTO football_players (fb_player_id, fb_team_id, first_name, second_name) VALUES ( ?, ?, ? , ? )", 
                    (item['id'], item['team'], item['first_name'], item['second_name']))

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()
