def create_tables():
    """
    This function creates the initial set of tables to be populated:
        - Gameweek_info
        - Football_players
        - Football_teams
    """

    import sqlite3
    import os
    
    ### Change working directory
    os.chdir("/home/ubuntu/venv/sqlite_db/")

    ### Create a database connection
    conn = sqlite3.connect('fpl.sqlite')
    cur = conn.cursor()
    
    ### Drop tables if they exist
    cur.execute("DROP TABLE IF EXISTS gameweek_info")
    cur.execute("DROP TABLE IF EXISTS football_players")
    cur.execute("DROP TABLE IF EXISTS football_teams")
    
    ### Create tables
    # Gameweek info table
    cur.execute("""
                CREATE TABLE gameweek_info (
                    gw_id INTEGER,
                    gw_name TEXT,
                    gw_deadline TEXT
                    )
                """)
    
    # (Football) player table
    cur.execute("""
                CREATE TABLE football_players (
                    fb_player_id INTEGER,
                    fb_team_id INTEGER,
                    first_name TEXT,
                    second_name TEXT
                    )
                """)
    
    # Football teams table
    cur.execute("""
                CREATE TABLE football_teams (
                    fb_team_id INTEGER,
                    fb_team_name TEXT,
                    fb_short_name TEXT
                    )
                """)

