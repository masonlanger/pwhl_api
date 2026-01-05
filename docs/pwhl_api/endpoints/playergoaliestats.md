# PlayerGoalieStats
##### pwhl_api/endpoints/playergoaliestats.py

##### Endpoint URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players)

##### Valid URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players&season=6&team=all&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1&position=goalies&qualified=qualified&rookies=0&statsType=standard&rosterstatus=undefined&activeOnly=0&limit=500](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players&season=6&team=all&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1&position=goalies&qualified=qualified&rookies=0&statsType=standard&rosterstatus=undefined&activeOnly=0&limit=500)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Options | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| **season** | season                 |         |          |   `Y`    | 
| **team** | team                   | "all" or team_id |          |   `Y`    | 
| **qualified** | qualified             | qualified, unqualified |          |   `Y`    | 
| **rookies** | rookies                | 0, 1    |          |   `Y`    | 
| **statsType** | statsType              | standard, expanded |          |   `Y`    | 
| **limit** | limit                  | integer |          |   `Y`    | 

## Methods
#### `get_raw_json`
* Returns raw JSON object containing goalie statistics, as returned by API endpoint.
```json
[{
    "sections": [{
        "data": [{
            "row": {
                "player_id": 456,
                ...
            }
        }]
    }]
}]
```

#### `get_data_frame`
* Returns pandas DataFrame of goalie statistics.
* Each row represents one goalie with their season statistics.
```text
['player_id', 'rookie', 'name', 'active', 'team_code', 'games_played', 'minutes_played', 'saves', 'shots'.'save_percentage', 'goals_against','shutouts', 'wins', 'losses', 'ot_losses', ...]
```

## Usage Examples

#### Get All Qualified Goalies
```python
from pwhl_api.endpoints.playergoaliestats import PlayerGoalieStats

goalies = PlayerGoalieStats(season="6")
df = goalies.get_data_frame()
# Returns all qualified goalies for the season
```

#### Get Goalies for a Specific Team
```python
from pwhl_api.endpoints.playergoaliestats import PlayerGoalieStats

team_goalies = PlayerGoalieStats(season="6", team="1")
df = team_goalies.get_data_frame()
# Returns all goalies for team with ID 1
```

#### Find Best Performing Goalies
```python
from pwhl_api.endpoints.playergoaliestats import PlayerGoalieStats

goalies = PlayerGoalieStats(season="6")
df = goalies.get_data_frame()

# Convert to numeric for analysis
df['save_percentage'] = df['save_percentage'].astype(float)
df['goals_against_average'] = df['goals_against_average'].astype(float)
df['games_played'] = df['games_played'].astype(int)
df['shutouts'] = df['shutouts'].astype(int)

# Best save percentage (minimum 5 games)
df_min_games = df[df['games_played'] >= 5]
best_goalies = df_min_games.nlargest(5, 'save_percentage')[['name', 'team_code', 'save_percentage', 'games_played']]

# Most shutouts
shutout_leaders = df.nlargest(5, 'shutouts')[['name', 'team_code', 'shutouts', 'games_played']]
```

Last validated 2026-01-05
