# LeagueSchedule
##### pwhl_api/endpoints/leagueschedule.py

##### Endpoint URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=schedule](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=schedule)

##### Valid URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=schedule&team=-1&season=8&month=-1&location=homeaway&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1&conference_id=-1&division_id=-1&lang=en](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=schedule&team=-1&season=8&month=-1&location=homeaway&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1&conference_id=-1&division_id=-1&lang=en)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Options | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| **season** | season                 |         |          |   `Y`    | 
| **month** | month                  | -1 or month number (1-12) |          |   `Y`    | 
| **location** | location               | homeaway, home, away |          |   `Y`    | 
| **team** | team                   | -1 or team_id |          |   `Y`    | 

## Methods
#### `get_raw_json`
* Returns raw JSON object containing schedule data, as returned by API endpoint.
```json
[{
    "sections": [{
        "data": [{
            "prop": {
                "home_team": {
                    "teamLink": "1"
                },
                "visiting_team": {
                    "teamLink": "2"
                }
            },
            "row": {
                "game_id": "215",
                "game_status": "Final",
                "start_time_ampm": "7:00 PM",
                "visiting_team": "Toronto Sceptres",
                "home_team": "Boston Fleet",
                "visiting_team_score": "3",
                "home_team_score": "2"
            }
        }]
    }]
}]
```

#### `get_data_frame`
* Returns pandas DataFrame of league schedule with game information.
* Each row represents one scheduled game.
```text
['prop_home_team_teamLink', 'prop_visiting_team_teamLink', 'row_game_id', 
 'row_game_status', 'row_start_time_ampm', 'row_visiting_team', 'row_home_team', 
 'row_visiting_team_score', 'row_home_team_score', ...]
```

## Usage Examples

#### Get Current Season Schedule
```python
from pwhl_api.endpoints.leagueschedule import LeagueSchedule

schedule = LeagueSchedule(season="8")
df = schedule.get_data_frame()
# Returns DataFrame with all games for season 8
```

Last validated 2026-01-05
