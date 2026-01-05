# PlayerCareerStats
##### pwhl_api/endpoints/playercareerstats.py

##### Endpoint URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=player](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=player)

##### Valid URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=player&player_id=21&season_id=8&site_id=0&key=446521baf8c38984&client_code=pwhl&league_id=1&lang=en&statsType=standard](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=player&player_id=21&season_id=8&site_id=0&key=446521baf8c38984&client_code=pwhl&league_id=1&lang=en&statsType=standard)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Pattern | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| **player_id** | player_id                 |         |   `Y`    |    `N`   | 
| **season_id** | season_id                 |         |          |   `Y`    | 
| **statsType** | statsType                 |         |          |   `Y`    | 

## Methods
#### `get_raw_json`
* Returns raw JSON object containing player career and season statistics, as returned by API endpoint.
```json
{
    "careerStats": [{
        "sections": [
            {
                "title": "Regular Season",
                "data": [{
                    "row": {
                        "season": "2024-2025",
                        "games_played": 12,
                        "goals": 5,
                        "assists": 8,
                        "points": 13,
                        "plus_minus": 3
                    }
                }]
            },
            {
                "title": "Playoffs",
                "data": [{
                    "row": {
                        "season": "2024-2025",
                        "games_played": 3,
                        "goals": 1,
                        "assists": 2,
                        "points": 3,
                        "plus_minus": 1
                    }
                }]
            }
        ]
    }],
    "gameByGame": [{
        "sections": [{
            "data": [{
                "row": {
                    "date": "2024-10-15",
                    "opponent": "BOS",
                    "goals": 1,
                    "assists": 1,
                    "points": 2
                },
                "prop": {
                    "game": {
                        "gameLink": "12345"
                    }
                }
            }]
        }]
    }],
    "currentSeasonStats": [{
        "sections": [{
            "data": [{
                "row": {
                    "games_played": "12",
                    "goals": "5",
                    "assists": "8",
                    "points": "13"
                }
            }]
        }]
    }],
    "playerShots": [
        {
            ...
        }
    ]
}
```

#### `get_data_frames`
* Returns dictionary of pandas DataFrames with normalized tables for player career and season statistics.
* Provides a comprehensive view of a player's career and current season performance.

**Returned dictionary keys:**
* `playerStats` - Dictionary containing career statistics by season
  * `regularSeason` - DataFrame of regular season stats by season
  * `playoffs` - DataFrame of playoff stats by season
* `gameByGame` - DataFrame of game-by-game statistics for the season
* `currentSeasonStats` - DataFrame of aggregated current season statistics
* `playerShots` - DataFrame of shot data for the player

**PlayerStats Regular Season DataFrame columns:**
Row structure varies by player type (skater/goalie), but typically includes:
```text
['season_name', 'goals', 'games_played', 'assists', 'points', ...]
```

**PlayerStats Playoffs DataFrame columns:**
Same structure as Regular Season:
```text
['season_name', 'goals', 'games_played', 'assists', 'points', ...]
```

**GameByGame DataFrame columns:**
```text
['date_played', 'shots', 'goals', 'pp', 'sh', 'gw',
'ice_time_minutes_seconds', 'hits','shots_blocked_by_player', 'plusminus', ...]
```

**CurrentSeasonStats DataFrame columns:**
```text
['season_name', 'games_played', 'goals', 'assists', 'points','penalty_minutes']
```
(Single row DataFrame with aggregate stats for current season)

**PlayerShots DataFrame columns:**
```text
['game_id', 'x_location', 'y_location', 'orientation']
```

## Usage Examples

#### Basic Usage
```python
from pwhl_api.endpoints.playercareerstats import PlayerCareerStats

player_stats = PlayerCareerStats(player_id="21", season_id="8")
player_stats.response  # HTTP response object
```

#### Get All Player Data Frames
```python
player_stats = PlayerCareerStats(player_id="21", season_id="8", statsType="standard")
dfs = player_stats.get_data_frames()

# Access individual DataFrames
career_regular = dfs['playerStats']['regularSeason']
career_playoffs = dfs['playerStats']['playoffs']
game_by_game = dfs['gameByGame']
current_season = dfs['currentSeasonStats']
player_shots = dfs['playerShots']
```

#### View Career Regular Season Statistics
```python
player_stats = PlayerCareerStats(player_id="115", season_id="8", statsType="standard")
dfs = player_stats.get_data_frames()
regular_season_df = dfs['playerStats']['regularSeason']

# View all seasons
print(regular_season_df)

# Filter for a specific season
season_2024 = regular_season_df[regular_season_df['season_name'].str.contains('2024')]
```

#### Analyze Game-by-Game Performance
```python
player_stats = PlayerCareerStats(player_id="21", season_id="8")
dfs = player_stats.get_data_frames()
game_by_game_df = dfs['gameByGame']

# Filter for games with points
games_with_points = game_by_game_df[game_by_game_df['points'] > 0]

# Get points per game average
total_points = game_by_game_df['points'].sum()
games_played = len(game_by_game_df)
ppg = total_points / games_played if games_played > 0 else 0
```

#### View Current Season Statistics
```python
player_stats = PlayerCareerStats(player_id="21", season_id="8")
dfs = player_stats.get_data_frames()
current_season_df = dfs['currentSeasonStats']

# Current season stats (single row DataFrame)
print(current_season_df)

# Access specific stats
games_played = current_season_df['games_played'].values[0]
total_points = current_season_df['points'].values[0]
```

#### Compare Playoff and Regular Season Performance
```python
player_stats = PlayerCareerStats(player_id="21", season_id="8")
dfs = player_stats.get_data_frames()

regular_season = dfs['playerStats']['regularSeason']
playoffs = dfs['playerStats']['playoffs']

# Compare points in most recent season
if not regular_season.empty:
    last_rs_points = regular_season.iloc[-1]['points']
    print(f"Regular Season Points: {last_rs_points}")

if not playoffs.empty:
    last_poff_points = playoffs.iloc[-1]['points']
    print(f"Playoff Points: {last_poff_points}")
```

Last validated 2026-01-05
