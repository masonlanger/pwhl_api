# GamePreview
##### pwhl_api/endpoints/gamepreview.py

##### Endpoint URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameCenterPreview](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameCenterPreview)

##### Valid URL
>[https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameCenterPreview&game_id=248&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1](https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=gameCenterPreview&game_id=248&key=446521baf8c38984&client_code=pwhl&site_id=0&league_id=1)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Pattern | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| **game_id** | game_id                 |         |   `Y`    |    `N`   | 

## Methods
#### `get_raw_json`
* Returns raw JSON object containing game preview information, as returned by API endpoint.
```json
{
    "game": {
        "id": 248,
        "status": "Scheduled",
        "homeTeam": {
            "id": 1,
            "code": "BOS",
            "name": "Boston Fleet"
        },
        "visitingTeam": {
            "id": 2,
            "code": "TOR",
            "name": "Toronto Sceptres"
        },
        "gameDateTime": "2025-01-05T19:00:00",
        "venue": {
            "id": 1,
            "name": "Agganis Arena"
        }
    },
    "lineupPairingReport": [...],
    ...
}
```

## Usage Examples

#### Get Game Preview Information
```python
from pwhl_api.endpoints.gamepreview import GamePreview

game_preview = GamePreview(game_id="248")
preview_data = game_preview.get_raw_json()

# Access game keys
preview_data.keys()

# Access specific information
lineup_pairings = preview_data['lineupPairingReport']
```

Last validated 2026-01-05
