# PlayerLeagueLeaders
##### pwhl_api/endpoints/playerleagueleaders.py

##### Endpoint URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=leadersExtended](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=leadersExtended)

##### Valid URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=leadersExtended&season_id=8&team_id=0&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1&playerTypes=skaters,goalies&skaterStatTypes=points,goals,assists&goalieStatTypes=wins,save_percentage,goals_against_average&activeOnly=0](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=leadersExtended&season_id=8&team_id=0&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1&playerTypes=skaters,goalies&skaterStatTypes=points,goals,assists&goalieStatTypes=wins,save_percentage,goals_against_average&activeOnly=0)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Options | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| **season** | season                 |         |          |   `Y`    | 
| **team_id** | team_id                | 0 or team_id |          |   `Y`    | 

## Methods
#### `get_raw_json`
* Returns raw JSON object containing league leader statistics by category, as returned by API endpoint.
```json
{
    "skaters": {
        "points": {
            "results": [
                {
                    "player_id": 123,
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "team_code": "BOS",
                    "points": 45,
                    "rank": 1
                }
            ]
        },
        "goals": {
            "results": [...]
        },
        "assists": {
            "results": [...]
        }
    },
    "goalies": {
        "wins": {
            "results": [...]
        },
        "save_percentage": {
            "results": [...]
        },
        "goals_against_average": {
            "results": [...]
        }
    }
}
```

#### `get_data_frames`
* Returns dictionary with nested structure of pandas DataFrames organized by player type and statistic category.
* Structure: `leaders[player_type][stat_type]` returns a DataFrame with player leader information.

**Dictionary structure:**
```text
leaders['skaters']['points']        # Points leaders (DataFrame)
leaders['skaters']['goals']         # Goals leaders (DataFrame)
leaders['skaters']['assists']       # Assists leaders (DataFrame)
leaders['goalies']['wins']          # Wins leaders (DataFrame)
leaders['goalies']['save_percentage']  # Save percentage leaders (DataFrame)
leaders['goalies']['goals_against_average']  # GAA leaders (DataFrame)
```

**DataFrame columns (varies by stat):**
```text
['rank', 'player_id', 'jersey_number', 'name', 'team_id', ...]
```

## Usage Examples

#### Get All League Leaders
```python
from pwhl_api.endpoints.playerleagueleaders import PlayerLeagueLeaders

leaders = PlayerLeagueLeaders(season="8")
leaders_dfs = leaders.get_data_frames()

# Access specific leader categories
points_leaders = leaders_dfs['skaters']['Points']
goals_leaders = leaders_dfs['skaters']['Goals']
assists_leaders = leaders_dfs['skaters']['Assists']

wins_leaders = leaders_dfs['goalies']['Wins']
save_pct_leaders = leaders_dfs['goalies']['Save Percentage']
gaa_leaders = leaders_dfs['goalies']['Goals Against Average']
```

Last validated 2026-01-05
