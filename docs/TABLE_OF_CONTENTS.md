# PWHL API Documentation - Table of Contents

## Overview
Complete API documentation for the PWHL (Professional Women's Hockey League) API wrapper, organized by module type with descriptions of available endpoints and utilities.

---

## Folder Structure

### `/pwhl_api/endpoints/` - API Endpoints
Documented API endpoints for accessing PWHL data.

| Document | Description |
|----------|-------------|
| [gamepreview.md](pwhl_api/endpoints/gamepreview.md) | Pre-game information and matchup data |
| [gamesummary.md](pwhl_api/endpoints/gamesummary.md) | Comprehensive game results and statistics |
| [leagueschedule.md](pwhl_api/endpoints/leagueschedule.md) | Season schedule and upcoming games |
| [leaguestandings.md](pwhl_api/endpoints/leaguestandings.md) | Team rankings and point standings |
| [playbyplay.md](pwhl_api/endpoints/playbyplay.md) | Detailed game events and play-by-play |
| [playercareerstats.md](pwhl_api/endpoints/playercareerstats.md) | Career and season player statistics |
| [playergoaliestats.md](pwhl_api/endpoints/playergoaliestats.md) | Goaltender performance and statistics |
| [playerleagueleaders.md](pwhl_api/endpoints/playerleagueleaders.md) | Top statistical performers and leaders |
| [playerskaterstats.md](pwhl_api/endpoints/playerskaterstats.md) | Skater statistics with filtering options |
| [teamroster.md](pwhl_api/endpoints/teamroster.md) | Team rosters with player information |

### `/pwhl_api/static/` - Utility Modules
Static data utilities for accessing registry information.

| Document | Description |
|----------|-------------|
| [players.md](pwhl_api/static/players.md) | Player registry lookup and search utilities |
| [teams.md](pwhl_api/static/teams.md) | Team registry lookup and search utilities |

---

## Quick Links by Use Case

**Getting Started:**
- [Players](pwhl_api/static/players.md) - Look up player information
- [Teams](pwhl_api/static/teams.md) - Look up team information

**Game Data:**
- [GameSummary](pwhl_api/endpoints/gamesummary.md) - Full game results
- [GamePreview](pwhl_api/endpoints/gamepreview.md) - Upcoming game info
- [PlayByPlay](pwhl_api/endpoints/playbyplay.md) - Event-by-event game data

**Player Statistics:**
- [PlayerSkaterStats](pwhl_api/endpoints/playerskaterstats.md) - Season skater data
- [PlayerCareerStats](pwhl_api/endpoints/playercareerstats.md) - Career player data
- [PlayerGoalieStats](pwhl_api/endpoints/playergoaliestats.md) - Goaltender data
- [PlayerLeagueLeaders](pwhl_api/endpoints/playerleagueleaders.md) - Top performers

**League Information:**
- [LeagueSchedule](pwhl_api/endpoints/leagueschedule.md) - Season schedule
- [LeagueStandings](pwhl_api/endpoints/leaguestandings.md) - Team standings
- [TeamRoster](pwhl_api/endpoints/teamroster.md) - Team player lists
