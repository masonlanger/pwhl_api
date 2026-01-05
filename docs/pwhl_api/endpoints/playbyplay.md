# PlayByPlay
##### pwhl_api/endpoints/playbyplay.py

##### Endpoint URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameCenterPlayByPlay](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameCenterPlayByPlay)

##### Valid URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameCenterPlayByPlay&game_id=215&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameCenterPlayByPlay&game_id=215&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Pattern | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| **game_id** | game_id                 |         |   `Y`    |    `N`   | 

## Methods
#### `get_raw_json`
* Returns raw JSON array of events, as returned by API endpoint.
```json
[
    {
        "event": "period_start",
        "details": {
            "period": {
                "id": 1,
                "shortName": "1st"
            },
            "time": "0:00",
            "xLocation": null,
            "yLocation": null
        }
    },
    {
        "event": "shot",
        "details": {
            "period": {
                "id": 1,
                "shortName": "1st"
            },
            "time": "2:35",
            "xLocation": 85,
            "yLocation": 20,
            "shooter": {
                "id": 123,
                "firstName": "Jane",
                "lastName": "Doe"
            },
            "goalie": {
                "id": 456,
                "firstName": "Mary",
                "lastName": "Smith"
            },
            "isGoal": false,
            "shotQuality": "High Danger",
            "shotType": "Snap Shot"
        }
    },
    {
        "event": "goal",
        "details": {
            "period": {
                "id": 1,
                "shortName": "1st"
            },
            "time": "5:12",
            "xLocation": 89,
            "yLocation": 15,
            "scoredBy": {
                "id": 789,
                "firstName": "Sarah",
                "lastName": "Johnson"
            },
            "assists": [
                {
                    "id": 234,
                    "firstName": "Emma",
                    "lastName": "Williams"
                }
            ],
            "properties": {
                "isPowerPlay": false,
                "isShortHanded": false,
                "isEmptyNet": false,
                "isPenaltyShot": false,
                "isInsuranceGoal": false,
                "isGameWinningGoal": false
            }
        }
    }
]
```

#### `get_data_frame`
* Returns pandas DataFrame of game events with basic information.
```text
['event_id', 'event_type', 'period_id', 'time', 'x_location', 'y_location']
```

#### `get_data_frames`
* Returns dictionary of pandas DataFrames with normalized tables for different event types.
* Provides a normalized relational structure of play-by-play data.

**Returned dictionary keys:**
* `events` - Main events table with all events
* `shots` - Detailed shot information (shots and blocked shots)
* `goals` - Detailed goal information with goal properties
* `assists` - Assist information linked to goals
* `penalties` - Penalty information linked to penalty events

**Events DataFrame columns:**
```text
['event_id', 'event_type', 'period_id', 'time', 'x_location', 'y_location']
```

**Shots DataFrame columns:**
```text
['event_id', 'time', 'period_type', 'shooter_id', 'shooter_name', 'goalie_id', 
 'goalie_name', 'is_goal', 'shot_quality', 'shot_type', 'xLocation', 'yLocation',
 'blocker_id', 'blocker_name']
```

**Goals DataFrame columns:**
```text
['event_id', 'scorer_id', 'scorer_name', 'time', 'period_type', 'xLocation', 
 'yLocation', 'isPowerPlay', 'isShortHanded', 'isEmptyNet', 'isPenaltyShot', 
 'isInsuranceGoal', 'isGameWinningGoal']
```

**Assists DataFrame columns:**
```text
['event_id', 'assist_number', 'player_id', 'player_name']
```

**Penalties DataFrame columns:**
```text
['event_id', 'minutes', 'description', 'player_id']
```

## Usage Examples

#### Basic Usage
```python
from pwhl_api.endpoints.playbyplay import PlayByPlay

pbp = PlayByPlay(game_id="215")
pbp.response  # HTTP response object
```

#### Get Events as DataFrame
```python
pbp = PlayByPlay(game_id="215")
events_df = pbp.get_data_frame()
# Returns DataFrame with columns: event_id, event_type, period_id, time, x_location, y_location
```

#### Get Normalized Tables
```python
pbp = PlayByPlay(game_id="215")
dfs = pbp.get_data_frames()

# Access individual tables
events = dfs['events']      # All events
shots = dfs['shots']        # All shot attempts
goals = dfs['goals']        # All goals scored
assists = dfs['assists']    # All assists
penalties = dfs['penalties']  # All penalties
```

#### Analyze Shot Data
```python
pbp = PlayByPlay(game_id="215")
dfs = pbp.get_data_frames()
shots_df = dfs['shots']

# Filter for goals
goals_only = shots_df[shots_df['is_goal'] == True]

# Get shots by specific player
player_shots = shots_df[shots_df['shooter_id'] == 169]
```

#### Analyze Goals and Assists
```python
pbp = PlayByPlay(game_id="215")
dfs = pbp.get_data_frames()

goals_df = dfs['goals']
assists_df = dfs['assists']

# Find goals with assists
goals_with_assists = goals_df.merge(
    assists_df, 
    on='event_id', 
    how='left'
)
goals_with_assists.head()
```
Expected output:
```plain
     11         58  Brianne Jenner   2:25           1        165   
1        11         58  Brianne Jenner   2:25           1        165   
2        83        220  Mannon McMahon  14:03           2         93   
3        83        220  Mannon McMahon  14:03           2         93   
4       110         72  Rebecca Leslie   1:19           3         51   

   yLocation isPowerPlay isShortHanded isEmptyNet isPenaltyShot  \
0         61           1             0          0             0   
1         61           1             0          0             0   
2        155           0             0          0             0   
3        155           0             0          0             0   
4        112           0             0          0             0   

  isInsuranceGoal isGameWinningGoal  assist_number  player_id  \
0               0                 0              1         57   
1               0                 0              2        242   
2               0                 1              1         57   
3               0                 1              2        219   
4               1                 0              1         58   

           player_name  
0        Gabbie Hughes  
1         Rory Guilday  
2        Gabbie Hughes  
3  Stephanie Markowski  
4       Brianne Jenner  
```

Last validated 2026-01-05
