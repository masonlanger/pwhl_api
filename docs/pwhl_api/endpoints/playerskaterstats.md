# PlayerSkaterStats
##### pwhl_api/endpoints/playerskaterstats.py

##### Endpoint URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players)

##### Valid URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players&season=8&team=all&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1&position=forwards&rookies=0&statsType=standard&rosterstatus=undefined&activeOnly=0&limit=500](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players&season=8&team=all&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1&position=forwards&rookies=0&statsType=standard&rosterstatus=undefined&activeOnly=0&limit=500)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Options | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| **season** | season                 |         |          |   `Y`    | 
| **team** | team                   | "all" or team_id |          |   `Y`    | 
| **position** | position               | skaters, forwards, defenders |          |   `Y`    | 
| **rookies** | rookies                | 0, 1    |          |   `Y`    | 
| **statsType** | statsType              | standard |          |   `Y`    | 
| **limit** | limit                  | integer |          |   `Y`    | 

## Methods
#### `get_raw_json`
* Returns raw JSON object containing player statistics, as returned by API endpoint.
```json
[{
    "sections": [{
        "data": [{
            "row": {
                "player_id": 123,
                "first_name": "Jane",
                "last_name": "Doe",
                "team_code": "BOS",
                "position": "F",
                "games_played": 12,
                "goals": 5,
                "assists": 8,
                "points": 13,
                "plus_minus": 3,
                "penalty_minutes": 8,
                "power_play_goals": 1,
                "short_handed_goals": 0,
                "game_winning_goals": 1
            }
        }]
    }]
}]
```

#### `get_data_frame`
* Returns pandas DataFrame of player skater statistics.
* Each row represents one player with their season statistics.
```text
['player_id', 'name', 'active', 'position', 'rookie', 'team_code', 'games_played', 'goals', 'shots', 'hits','shots_blocked_by_player', ...]
```

## Usage Examples

#### Basic Usage - All Skaters
```python
from pwhl_api.endpoints.playerskaterstats import PlayerSkaterStats

skaters = PlayerSkaterStats(season="8")
df = skaters.get_data_frame()
# Returns all skaters for the season
```

#### Get Forwards Only
```python
from pwhl_api.endpoints.playerskaterstats import PlayerSkaterStats

forwards = PlayerSkaterStats(season="8", position="forwards")
df = forwards.get_data_frame()
# Returns only forwards
```

#### Get Defenders Only
```python
from pwhl_api.endpoints.playerskaterstats import PlayerSkaterStats

defenders = PlayerSkaterStats(season="8", position="defenders")
df = defenders.get_data_frame()
# Returns only defenders
```

#### Get Statistics for a Specific Team
```python
from pwhl_api.endpoints.playerskaterstats import PlayerSkaterStats

team_skaters = PlayerSkaterStats(season="8", team="1")
df = team_skaters.get_data_frame()
# Returns all skaters for team with ID 1
```

#### Get Rookies Only
```python
# Returns only rookies for the season
from pwhl_api.endpoints.playerskaterstats import PlayerSkaterStats

rookies = PlayerSkaterStats(season="8", rookies=1)
df = rookies.get_data_frame()
```

#### Analyze Forward Statistics
```python
from pwhl_api.endpoints.playerskaterstats import PlayerSkaterStats

forwards = PlayerSkaterStats(season="8", position="forwards")
df = forwards.get_data_frame()
df['points'] = df['points'].astype(int)
df['games_played'] = df['games_played'].astype(int)
# Top scorers
top_scorers = df.nlargest(10, 'points')[['name', 'points', 'goals', 'assists']]

# High-scoring forwards (15+ points)
productive_forwards = df[df['points'] >= 15]

# Average points per game
df['ppg'] = df['points'] / df['games_played']
df.sort_values(by='ppg', ascending=False).head(10)[['name', 'team_code','ppg']]
```

Last validated 2026-01-05
