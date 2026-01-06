# GameSummary
##### pwhl_api/endpoints/gamesummary.py

##### Endpoint URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameSummary](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameSummary)

##### Valid URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameSummary&game_id=227&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameSummary&game_id=227&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Pattern | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| **game_id** | game_id                 |         |   `Y`    |    `N`   | 

## Methods
#### `get_raw_json`
* Returns raw JSON object containing comprehensive game summary information, as returned by API endpoint.
* Includes game details, team information, statistics, player stats, and period-by-period breakdown.

```json
{
    "details": {
        "gameId": "227",
        "gameDate": "2025-01-04",
        "status": "Final",
        "homeTeam": {...},
        "visitingTeam": {...}
    },
    "homeTeam": {
        "info": {...},
        "stats": {...},
        "seasonStats": {...},
        "skaters": [...],
        "goalies": [...]
    },
    "visitingTeam": {
        "info": {...},
        "stats": {...},
        "seasonStats": {...},
        "skaters": [...],
        "goalies": [...]
    },
    "periods": [...],
    "mostValuablePlayers": [...],
    "penalties": [...]
}
```

#### `get_data_frames`
* Returns dictionary of nested pandas DataFrames with organized game summary data.
* Provides a structured relational view of all game information including team, player, and period statistics.

**Returned dictionary structure:**
```text
{
    'details': DataFrame,                    # Game details (date, status, etc.)
    'homeTeam': {
        'TeamInfo': DataFrame,               # Home team information
        'TeamStats': DataFrame,              # Home team game statistics
        'TeamRecord': DataFrame,             # Home team season record
        'SkaterStats': DataFrame,            # Home team skater statistics
        'GoalieStats': DataFrame             # Home team goalie statistics
    },
    'visitingTeam': {
        'TeamInfo': DataFrame,               # Visiting team information
        'TeamStats': DataFrame,              # Visiting team game statistics
        'TeamRecord': DataFrame,             # Visiting team season record
        'SkaterStats': DataFrame,            # Visiting team skater statistics
        'GoalieStats': DataFrame             # Visiting team goalie statistics
    },
    'periods': {
        'goals': DataFrame,                  # Goals by period and team
        'shots': DataFrame                   # Shots by period and team
    },
    'mostValuablePlayers': DataFrame,        # Game MVPs with stats
    'penalties': DataFrame                   # Game penalties with details
}
```

## Usage Examples

#### Get Game Summary Data
```python
from pwhl_api.endpoints.gamesummary import GameSummary

gs = GameSummary(game_id="227")
dfs = gs.get_data_frames()

# Access game details
game_details = dfs['details']
print(game_details)
```

#### Get Team Information and Statistics
```python
gs = GameSummary(game_id="227")
dfs = gs.get_data_frames()

# Home team info and stats
home_info = dfs['homeTeam']['TeamInfo']
home_stats = dfs['homeTeam']['TeamStats']
home_record = dfs['homeTeam']['TeamRecord']

# Visiting team info and stats
away_info = dfs['visitingTeam']['TeamInfo']
away_stats = dfs['visitingTeam']['TeamStats']
away_record = dfs['visitingTeam']['TeamRecord']
```

#### Analyze Player Statistics
```python
gs = GameSummary(game_id="227")
dfs = gs.get_data_frames()

# Home team players
home_skaters = dfs['homeTeam']['SkaterStats']  # Forwards and defensemen
home_goalies = dfs['homeTeam']['GoalieStats']  # Goalies

# Visiting team players
away_skaters = dfs['visitingTeam']['SkaterStats']
away_goalies = dfs['visitingTeam']['GoalieStats']

# Find top performers
home_points = home_skaters.nlargest(5, 'points')[['player_id', 'name', 'position', 'points', 'goals', 'assists']]
```

#### View Period-by-Period Scoring and Shots
```python
gs = GameSummary(game_id="227")
dfs = gs.get_data_frames()

# Goals by period
goals_by_period = dfs['periods']['goals']
# Columns: 1st, 2nd, 3rd, OT (if applicable), T (total)

# Shots by period
shots_by_period = dfs['periods']['shots']
# Rows: Home and Away team abbreviations

print(goals_by_period)
print(shots_by_period)
```

#### Analyze Game Penalties
```python
gs = GameSummary(game_id="227")
dfs = gs.get_data_frames()

penalties = dfs['penalties']
# Columns: game_penalty_id, period_id, time, description, against_team_id, 
#          against_team_abbreviation, minutes, taken_by_id, taken_by_name, 
#          is_power_play, is_bench

# Filter for power play penalties
pp_penalties = penalties[penalties['is_power_play'] == True]

# Count penalties by team
penalty_counts = penalties.groupby('against_team_abbreviation').size()
```

Last validated 2026-01-06
