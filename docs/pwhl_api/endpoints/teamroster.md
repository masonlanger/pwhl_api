# TeamRoster
##### pwhl_api/endpoints/teamroster.py

##### Endpoint URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=roster](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=roster)

##### Valid URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=roster&team_id=2&season_id=7&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=roster&team_id=2&season_id=7&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Pattern | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| **team_id** | team_id                   |         |   `Y`    |    `N`   | 
| **season** | season                    |         |          |   `Y`    | 

## Methods
#### `get_raw_json`
* Returns raw JSON object containing team roster data, as returned by API endpoint.
```json
{
    "roster": [{
        "sections": [
            {
                "title": "Forwards",
                "data": [{
                    "row": {
                        ...
                    }
                }]
            },
            {
                "title": "Defenders",
                "data": [{
                    "row": {
                        ...
                    }
                }]
            },
            {
                "title": "Goalies",
                "data": [{
                    "row": {
                        ...
                    }
                }]
            }
        ]
    }]
}
```

#### `get_data_frames`
* Returns dictionary of pandas DataFrames with player information organized by position.
* Dictionary keys correspond to position groups (e.g., "Forwards", "Defenders", "Goalies").
* Each DataFrame contains roster information for players in that position group.

**Returned dictionary keys (typical):**
* `Forwards` - All forwards on the team
* `Defenders` - All defensemen on the team
* `Goalies` - All goaltenders on the team
* `Coaches` - All coaches, managers on the team

**DataFrame columns (typical):**
```text
['shoots', 'hometown', 'player_id', 'birthdate', 'tp_jersey_number','position', 'name']
```

## Usage Examples

#### Get All Team Rosters
```python
from pwhl_api.endpoints.teamroster import TeamRoster

roster = TeamRoster(team_id="2", season="7")
roster_dfs = roster.get_data_frames()
# Returns dictionary with position groups as keys
```

#### Access Forwards by Position
```python
from pwhl_api.endpoints.teamroster import TeamRoster

roster = TeamRoster(team_id="2", season="7")
roster_dfs = roster.get_data_frames()

forwards = roster_dfs['Forwards']
# View first few forwards
print(forwards.head(5))

# Get specific forward info
selected = forwards[['name', 'jersey_number', 'hometown', 'birthdate']]
```

#### Compare Roster Sizes Across Positions
```python
from pwhl_api.endpoints.teamroster import TeamRoster

roster = TeamRoster(team_id="2", season="7")
roster_dfs = roster.get_data_frames()

# Get roster sizes by position
for position, df in roster_dfs.items():
    print(f"{position}: {len(df)} players")
```

Last validated 2026-01-05
