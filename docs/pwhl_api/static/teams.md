# Teams
##### pwhl_api/static/teams.py

## Overview
Utility module for accessing team data from the static teams registry. Provides functions to retrieve all teams or search for specific teams by ID or name.

## Data Source
Teams data is loaded from `teams.json`, a static JSON file containing team information including team ID, name, nickname, team code, division ID, and logo URL.

## Functions

#### `get_teams()`
* Returns a list of all teams in the PWHL.
* Each team object contains: `id`, `name`, `nickname`, `team_code`, `division_id`, `logo`

**Example return value:**
```json
[
    {
        "id": "1",
        "name": "Boston Fleet",
        "nickname": "Fleet",
        "team_code": "BOS",
        "division_id": "1",
        "logo": "https://assets.leaguestat.com/pwhl/logos/50x50/1.png"
    },
    {
        "id": "2",
        "name": "Minnesota Frost",
        "nickname": "Frost",
        "team_code": "MIN",
        "division_id": "1",
        "logo": "https://assets.leaguestat.com/pwhl/logos/50x50/2.png"
    }
]
```

#### `get_team(team_id)`
* Returns a single team object by team ID.
* `team_id` can be a string or integer.
* Returns `None` if team is not found.

**Parameters:**
- `team_id` (str | int) - The unique identifier for the team

#### `get_team_by_name(team_name)`
* Returns a single team object by team name or nickname (case-insensitive).
* `team_name` can be either the full team name or the team nickname.
* Returns `None` if team is not found.

**Parameters:**
- `team_name` (str) - The name or nickname of the team to search for

## Usage Examples

#### Get All Teams
```python
from pwhl_api.static.teams import get_teams

teams = get_teams()
# Returns list of all team dictionaries
print(f"Total teams: {len(teams)}")
for team in teams:
    print(f"{team['name']} ({team['team_code']})")
```

#### Search Team by ID
```python
from pwhl_api.static.teams import get_team

team = get_team("1")
# Returns Boston Fleet team object, or None if not found
```

#### Search Team by Name
```python
from pwhl_api.static.teams import get_team_by_name

team = get_team_by_name("Boston Fleet")
# Returns team named "Boston Fleet"

# Can also search by nickname
team = get_team_by_name("Fleet")
# Also returns Boston Fleet team object

# Handle not found case
if team:
    print(f"Found: {team['name']} with code {team['team_code']}")
else:
    print("Team not found")
```

Last validated 2026-01-05
