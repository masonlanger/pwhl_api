# simple method for returning a list of players
def get_players():
    return [
        {"id": 1, "name": "Alice", "position": "Forward"},
        {"id": 2, "name": "Bob", "position": "Midfielder"},
        {"id": 3, "name": "Charlie", "position": "Defender"},
        {"id": 4, "name": "Diana", "position": "Goalkeeper"},
    ]
# callable as: from pwhl_api.static.players import get_players