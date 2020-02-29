def authenticate():
    """
    This function provides authentication for the FPL API.
    """

    # Import requests module
    import requests
    
    # Start session
    session = requests.session()

    # Login url and sign in details
    url = 'https://users.premierleague.com/accounts/login/'
    payload = {
        'password': 'Superspurs1961',
        'login': 'wjroelofse@gmail.com',
        'redirect_uri': 'https://fantasy.premierleague.com/',
        'app': 'plfpl-web'
    }

    # POST request
    session.post(url, data=payload)

    return session
