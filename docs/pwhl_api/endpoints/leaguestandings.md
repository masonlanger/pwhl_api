# LeagueStandings
##### pwhl_api/endpoints/leaguestandings.py

##### Endpoint URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=teams](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=teams)

##### Valid URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=teams&groupTeamsBy=division&context=overall&season=8&key=446521baf8c38984&special=false&client_code=pwhl&site_id=0&league_id=1&conference_id=-1&division_id=-1&sort=points&lang=en](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=teams&groupTeamsBy=division&context=overall&season=8&key=446521baf8c38984&special=false&client_code=pwhl&site_id=0&league_id=1&conference_id=-1&division_id=-1&sort=points&lang=en)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Pattern | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| **season** | season                 |         |       |   `Y`    | 
| **context** | context        |         |          |   `Y`    | 
| **special** | special_teams        |         |          |   `Y`    | 
| **sort** | sort        |         |          |   `Y`    | 

## Methods
#### `get_raw_json`
* Returns raw JSON object, as returned by API endpoint.
```json
[{
    "sections":[
        ...
        { "data":[{
            "prop":{
                "team_code":{
                    "teamLink":"1"
                },
                "name":{"teamLink":"1"}
            },
            "row":
                {
                    "team_code":"BOS",
                    "losses":"2",
                    "regulation_wins":"6",
                    "points":"19",
                    "goals_for":"23",
                    "goals_against":"15",
                    "non_reg_wins":"0",
                    "non_reg_losses":"1",
                    "games_remaining":"21",
                    "percentage":"0.704",
                    "overall_rank":"1",
                    "games_played":"9",
                    "rank":1,
                    "name":"Boston Fleet"}}
                ...
    }}]}]}]
```

#### `get_data_frame`
* Returns pandas DataFrame of current league standings, sorted by `sort` parameter.
```text
['prop_team_code_teamLink', 'prop_name_teamLink', 'row_team_code',
       'row_losses', 'row_regulation_wins', 'row_points', 'row_goals_for',
       'row_goals_against', 'row_non_reg_wins', 'row_non_reg_losses',
       'row_games_remaining', 'row_percentage', 'row_overall_rank',
       'row_games_played', 'row_rank', 'row_name']
```

Last validated 2026-01-05