# Players
##### pwhl_api/static/players.py

## Overview
Utility module for accessing player data from the static players registry. Provides functions to retrieve all players or search for specific players by ID or name.

## Data Source
Players data is loaded from `players.json`, a static JSON file containing player information including player ID, name, hometown, and birthdate.

## Functions

#### `get_players()`
* Returns a list of all players in the registry.
* Each player object contains: `player_id`, `name`, `hometown`, `birthdate`

**Example return value:**
```json
[
    {
        "player_id": "1",
        "name": "Player One",
        "hometown": "City, State",
        "birthdate": "1990-01-01"
    },
    {
        "player_id": "2",
        "name": "Player Two",
        "hometown": "City, State",
        "birthdate": "1991-02-15"
    }
]
```

#### `get_player(player_id)`
* Returns a single player object by player ID.
* `player_id` can be a string or integer.
* Returns `None` if player is not found.

**Parameters:**
- `player_id` (str | int) - The unique identifier for the player

#### `get_player_by_name(player_name)`
* Returns a single player object by player name (case-insensitive).
* `player_name` should be the full player name.
* Returns `None` if player is not found.

**Parameters:**
- `player_name` (str) - The full name of the player to search for

## Usage Examples

#### Get All Players
```python
from pwhl_api.static.players import get_players

players = get_players()
# Returns list of all player dictionaries
print(f"Total players: {len(players)}")
print(players[:5])  # First 5 players
```

#### Search Player by ID
```python
from pwhl_api.static.players import get_player

player = get_player("21")
# Returns player with ID 21, or None if not found
```

#### Search Player by Name
```python
from pwhl_api.static.players import get_player_by_name

player = get_player_by_name("Sophie Shirley")
# Returns player named "Sophie Shirley" (case-insensitive)

# Handle not found case
if player:
    print(f"Found: {player['name']} from {player['hometown']}")
else:
    print("Player not found")
```

Last validated 2026-01-05
