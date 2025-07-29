import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/api-sports/api/api-football'

mcp = FastMCP('api-football')

@mcp.tool()
def v3_timezone() -> dict:
    '''Get the list of available timezone to be used in the fixtures endpoint. > This endpoint does not require any parameters. **Update Frequency** : This endpoint contains all the existing timezone, it is not updated. **Recommended Calls** : 1 call when you need.'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/timezone'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_predictions(fixture: Annotated[Union[int, float], Field(description='The id of the fixture Default: 198772')]) -> dict:
    '''Get predictions about a fixture. The predictions are made using several algorithms including the poisson distribution, comparison of team statistics, last matches, players etc… Bookmakers odds are not used to make these predictions Also provides some comparative statistics between teams **Available Predictions** * Match winner : Id of the team that can potentially win the fixture * Win or Draw : If `True` indicates that the designated team can win or draw * Under / Over : -1.5 / -2.5 / -3.5 / -4.5 / +1.5 / +2.5 / +3.5 / +4.5 `*` * Goals Home : -1.5 / -2.5 / -3.5 / -4.5 `*` * Goals Away -1.5 / -2.5 / -3.5 / -4.5 `*` * Advice *(Ex : Deportivo Santani or draws and -3.5 goals)* `*` **-1.5** means that there will be a maximum of **1.5** goals in the fixture, i.e : **1** goal **Update Frequency** : This endpoint is updated every hour. **Recommended Calls** : 1 call per hour for the fixtures in progress otherwise 1 call per day. >Here is an example of what can be achieved ![demo-prediction](https://www.api-football.com/public/img/demo/demo-prediction.png) **Use Cases** Get all available predictions from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/predictions?fixture=198772`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/predictions'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_head_to_head_between_two_teams(h2h: Annotated[str, Field(description='The ids of the teams id-id')],
                                               date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                               league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                                               season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020; 2021 ... Default: 0')] = None,
                                               last: Annotated[Union[int, float, None], Field(description='For the X last fixtures <= 2 characters Default: 0')] = None,
                                               next: Annotated[Union[int, float, None], Field(description='For the X next fixtures <= 2 characters Default: 0')] = None,
                                               _from: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                               to: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                               venue: Annotated[Union[int, float, None], Field(description='The venue id of the fixture Default: 0')] = None,
                                               status: Annotated[Union[str, None], Field(description='One or more fixture status short Like NS or NS-FT-CANC')] = None,
                                               timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None) -> dict:
    '''Get heads to heads between two teams. **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day. > Here is an example of what can be achieved ![demo-h2h](https://www.api-football.com/public/img/demo/demo-h2h.png) **Use Cases** Get all head to head between two {team} `https://api-football-v1.p.rapidapi.com/v3/fixtures/headtohead?h2h=33-34` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures/headtohead?h2h=33-34` `https://api-football-v1.p.rapidapi.com/v3/fixtures/headtohead?h2h=33-34&status=ns` `https://api-football-v1.p.rapidapi.com/v3/fixtures/headtohead?h2h=33-34&from=2019-10-01&to=2019-10-31` `https://api-football-v1.p.rapidapi.com/v3/fixtures/headtohead?league=39&season=2019&h2h=33-34&last=5` `https://api-football-v1.p.rapidapi.com/v3/fixtures/headtohead?league=39&season=2019&h2h=33-34&next=10&from=2019-10-01&to=2019-10-31` `https://api-football-v1.p.rapidapi.com/v3/fixtures/headtohead?league=39&season=2019&h2h=33-34&last=5&timezone=Europe/London`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/headtohead'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'h2h': h2h,
        'date': date,
        'league': league,
        'season': season,
        'last': last,
        'next': next,
        'from': _from,
        'to': to,
        'venue': venue,
        'status': status,
        'timezone': timezone,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures(id: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                live: Annotated[Union[str, None], Field(description='Enum: all or id-id for filter by league id')] = None,
                date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020; 2021 ... Default: 0')] = None,
                team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                last: Annotated[Union[int, float, None], Field(description='For the X last fixtures <= 2 characters Default: 0')] = None,
                next: Annotated[Union[int, float, None], Field(description='For the X next fixtures <= 2 characters Default: 0')] = None,
                _from: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                to: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                round: Annotated[Union[str, None], Field(description='The round of the fixture')] = None,
                timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                status: Annotated[Union[str, None], Field(description='One or more fixture status short Like NS or NS-FT-CANC')] = None,
                venue: Annotated[Union[int, float, None], Field(description='The venue id of the fixture Default: 0')] = None,
                ids: Annotated[Union[str, None], Field(description='One or more fixture ids id-id-id Maximum of 20 fixtures ids')] = None) -> dict:
    '''For all requests to fixtures you can add the query parameter `timezone` to your request in order to retrieve the list of matches in the time zone of your choice like *“Europe/London“* To know the list of available time zones you have to use the endpoint `timezone` > Some leagues have only final result check our coverage page to know which ones **Available fixtures status** * TBD : Time To Be Defined * NS : Not Started * 1H : First Half, Kick Off * HT : Halftime * 2H : Second Half, 2nd Half Started * ET : Extra Time * P : Penalty In Progress * FT : Match Finished * AET : Match Finished After Extra Time * PEN : Match Finished After Penalty * BT : Break Time (in Extra Time) * SUSP : Match Suspended * INT : Match Interrupted * PST : Match Postponed * CANC : Match Cancelled * ABD : Match Abandoned * AWD : Technical Loss * WO : WalkOver **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day. > Here are several examples of what can be achieved ![demo-fixtures](https://www.api-football.com/public/img/demo/demo-fixtures.jpg) **Use Cases** Get fixture from one fixture {id} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?id=215662` Get fixture from severals fixtures {ids} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?ids=215662-215663-215664-215665-215666-215667` Get all available fixtures in play In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all` Get all available fixtures in play filter by several {league} In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=39-61-48` Get all available fixtures from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2019` Get all available fixtures from one {date} `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2019-10-22` Get next X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?next=15` Get last X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?last=15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2020-01-30&league=61&season=2019` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&next=10` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&last=10&status=ft` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&last=10&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&season=2019&from=2019-07-01&to=2020-10-31` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&from=2019-07-01&to=2020-10-31&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&round=Regular Season - 1`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'live': live,
        'date': date,
        'league': league,
        'season': season,
        'team': team,
        'last': last,
        'next': next,
        'from': _from,
        'to': to,
        'round': round,
        'timezone': timezone,
        'status': status,
        'venue': venue,
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_rounds(league: Annotated[Union[int, float], Field(description='The id of the league Default: 39')],
                       season: Annotated[Union[int, float], Field(description='The season of the league 4 characters Like 2020, 2021 ... Default: 2020')],
                       current: Annotated[Union[str, None], Field(description='Retrun the current round only Enum: true or false')] = None) -> dict:
    '''Get the rounds for a league or a cup. The `round` can be used in endpoint fixtures as filters **Update Frequency** : This endpoint is updated every day. **Recommended Calls** : 1 call per day. **Use Cases** Get all available rounds from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/rounds?league=39&season=2019` Get current round from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/rounds?league=39&season=2019&current=true`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/rounds'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'current': current,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_current_round(league: Annotated[Union[int, float], Field(description='The id of the league Default: 39')],
                              season: Annotated[Union[int, float], Field(description='The season of the league 4 characters Like 2020, 2021 ... Default: 2020')],
                              current: Annotated[Union[str, None], Field(description='Retrun the current round only Enum: true or false')] = None) -> dict:
    '''Get the rounds for a league or a cup. The `round` can be used in endpoint fixtures as filters **Update Frequency** : This endpoint is updated every day. **Recommended Calls** : 1 call per day. **Use Cases** Get all available rounds from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/rounds?league=39&season=2019` Get current round from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/rounds?league=39&season=2019&current=true`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/rounds'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'current': current,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_by_fixture_id(id: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 157201')] = None,
                              live: Annotated[Union[str, None], Field(description='Enum: all or id-id for filter by league id')] = None,
                              date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                              league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                              season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020; 2021 ... Default: 0')] = None,
                              team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                              last: Annotated[Union[int, float, None], Field(description='For the X last fixtures <= 2 characters Default: 0')] = None,
                              next: Annotated[Union[int, float, None], Field(description='For the X next fixtures <= 2 characters Default: 0')] = None,
                              _from: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                              to: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                              round: Annotated[Union[str, None], Field(description='The round of the fixture')] = None,
                              timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                              status: Annotated[Union[str, None], Field(description='One or more fixture status short Like NS or NS-FT-CANC')] = None,
                              venue: Annotated[Union[int, float, None], Field(description='The venue id of the fixture Default: 0')] = None,
                              ids: Annotated[Union[str, None], Field(description='One or more fixture ids id-id-id Maximum of 20 fixtures ids')] = None) -> dict:
    '''For all requests to fixtures you can add the query parameter `timezone` to your request in order to retrieve the list of matches in the time zone of your choice like *“Europe/London“* To know the list of available time zones you have to use the endpoint `timezone` > Some leagues have only final result check our coverage page to know which ones **Available fixtures status** * TBD : Time To Be Defined * NS : Not Started * 1H : First Half, Kick Off * HT : Halftime * 2H : Second Half, 2nd Half Started * ET : Extra Time * P : Penalty In Progress * FT : Match Finished * AET : Match Finished After Extra Time * PEN : Match Finished After Penalty * BT : Break Time (in Extra Time) * SUSP : Match Suspended * INT : Match Interrupted * PST : Match Postponed * CANC : Match Cancelled * ABD : Match Abandoned * AWD : Technical Loss * WO : WalkOver **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day. > Here are several examples of what can be achieved ![demo-fixtures](https://www.api-football.com/public/img/demo/demo-fixtures.jpg) **Use Cases** Get fixture from one fixture {id} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?id=215662` Get fixture from severals fixtures {ids} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?ids=215662-215663-215664-215665-215666-215667` Get all available fixtures in play In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all` Get all available fixtures in play filter by several {league} In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=39-61-48` Get all available fixtures from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2019` Get all available fixtures from one {date} `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2019-10-22` Get next X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?next=15` Get last X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?last=15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2020-01-30&league=61&season=2019` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&next=10` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&last=10&status=ft` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&last=10&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&season=2019&from=2019-07-01&to=2020-10-31` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&from=2019-07-01&to=2020-10-31&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&round=Regular Season - 1`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'live': live,
        'date': date,
        'league': league,
        'season': season,
        'team': team,
        'last': last,
        'next': next,
        'from': _from,
        'to': to,
        'round': round,
        'timezone': timezone,
        'status': status,
        'venue': venue,
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_in_progress(id: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                            live: Annotated[Union[str, None], Field(description='Enum: all or id-id for filter by league id')] = None,
                            date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                            league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                            season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020; 2021 ... Default: 0')] = None,
                            team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                            last: Annotated[Union[int, float, None], Field(description='For the X last fixtures <= 2 characters Default: 0')] = None,
                            next: Annotated[Union[int, float, None], Field(description='For the X next fixtures <= 2 characters Default: 0')] = None,
                            _from: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                            to: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                            round: Annotated[Union[str, None], Field(description='The round of the fixture')] = None,
                            timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                            status: Annotated[Union[str, None], Field(description='One or more fixture status short Like NS or NS-FT-CANC')] = None,
                            venue: Annotated[Union[int, float, None], Field(description='The venue id of the fixture Default: 0')] = None,
                            ids: Annotated[Union[str, None], Field(description='One or more fixture ids id-id-id Maximum of 20 fixtures ids')] = None) -> dict:
    '''For all requests to fixtures you can add the query parameter `timezone` to your request in order to retrieve the list of matches in the time zone of your choice like *“Europe/London“* To know the list of available time zones you have to use the endpoint `timezone` > Some leagues have only final result check our coverage page to know which ones **Available fixtures status** * TBD : Time To Be Defined * NS : Not Started * 1H : First Half, Kick Off * HT : Halftime * 2H : Second Half, 2nd Half Started * ET : Extra Time * P : Penalty In Progress * FT : Match Finished * AET : Match Finished After Extra Time * PEN : Match Finished After Penalty * BT : Break Time (in Extra Time) * SUSP : Match Suspended * INT : Match Interrupted * PST : Match Postponed * CANC : Match Cancelled * ABD : Match Abandoned * AWD : Technical Loss * WO : WalkOver **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day. > Here are several examples of what can be achieved ![demo-fixtures](https://www.api-football.com/public/img/demo/demo-fixtures.jpg) **Use Cases** Get fixture from one fixture {id} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?id=215662` Get fixture from severals fixtures {ids} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?ids=215662-215663-215664-215665-215666-215667` Get all available fixtures in play In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all` Get all available fixtures in play filter by several {league} In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=39-61-48` Get all available fixtures from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2019` Get all available fixtures from one {date} `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2019-10-22` Get next X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?next=15` Get last X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?last=15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2020-01-30&league=61&season=2019` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&next=10` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&last=10&status=ft` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&last=10&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&season=2019&from=2019-07-01&to=2020-10-31` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&from=2019-07-01&to=2020-10-31&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&round=Regular Season - 1`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'live': live,
        'date': date,
        'league': league,
        'season': season,
        'team': team,
        'last': last,
        'next': next,
        'from': _from,
        'to': to,
        'round': round,
        'timezone': timezone,
        'status': status,
        'venue': venue,
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_by_date(id: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                        live: Annotated[Union[str, None], Field(description='Enum: all or id-id for filter by league id')] = None,
                        date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                        league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                        season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020; 2021 ... Default: 0')] = None,
                        team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                        last: Annotated[Union[int, float, None], Field(description='For the X last fixtures <= 2 characters Default: 0')] = None,
                        next: Annotated[Union[int, float, None], Field(description='For the X next fixtures <= 2 characters Default: 0')] = None,
                        _from: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                        to: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                        round: Annotated[Union[str, None], Field(description='The round of the fixture')] = None,
                        timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                        status: Annotated[Union[str, None], Field(description='One or more fixture status short Like NS or NS-FT-CANC')] = None,
                        venue: Annotated[Union[int, float, None], Field(description='The venue id of the fixture Default: 0')] = None,
                        ids: Annotated[Union[str, None], Field(description='One or more fixture ids id-id-id Maximum of 20 fixtures ids')] = None) -> dict:
    '''For all requests to fixtures you can add the query parameter `timezone` to your request in order to retrieve the list of matches in the time zone of your choice like *“Europe/London“* To know the list of available time zones you have to use the endpoint `timezone` > Some leagues have only final result check our coverage page to know which ones **Available fixtures status** * TBD : Time To Be Defined * NS : Not Started * 1H : First Half, Kick Off * HT : Halftime * 2H : Second Half, 2nd Half Started * ET : Extra Time * P : Penalty In Progress * FT : Match Finished * AET : Match Finished After Extra Time * PEN : Match Finished After Penalty * BT : Break Time (in Extra Time) * SUSP : Match Suspended * INT : Match Interrupted * PST : Match Postponed * CANC : Match Cancelled * ABD : Match Abandoned * AWD : Technical Loss * WO : WalkOver **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day. > Here are several examples of what can be achieved ![demo-fixtures](https://www.api-football.com/public/img/demo/demo-fixtures.jpg) **Use Cases** Get fixture from one fixture {id} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?id=215662` Get fixture from severals fixtures {ids} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?ids=215662-215663-215664-215665-215666-215667` Get all available fixtures in play In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all` Get all available fixtures in play filter by several {league} In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=39-61-48` Get all available fixtures from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2019` Get all available fixtures from one {date} `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2019-10-22` Get next X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?next=15` Get last X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?last=15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2020-01-30&league=61&season=2019` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&next=10` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&last=10&status=ft` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&last=10&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&season=2019&from=2019-07-01&to=2020-10-31` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&from=2019-07-01&to=2020-10-31&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&round=Regular Season - 1`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'live': live,
        'date': date,
        'league': league,
        'season': season,
        'team': team,
        'last': last,
        'next': next,
        'from': _from,
        'to': to,
        'round': round,
        'timezone': timezone,
        'status': status,
        'venue': venue,
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_by_league_id(id: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                             live: Annotated[Union[str, None], Field(description='Enum: all or id-id for filter by league id')] = None,
                             date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                             league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 39')] = None,
                             season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020; 2021 ... Default: 2020')] = None,
                             team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                             last: Annotated[Union[int, float, None], Field(description='For the X last fixtures <= 2 characters Default: 0')] = None,
                             next: Annotated[Union[int, float, None], Field(description='For the X next fixtures <= 2 characters Default: 0')] = None,
                             _from: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                             to: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                             round: Annotated[Union[str, None], Field(description='The round of the fixture')] = None,
                             timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                             status: Annotated[Union[str, None], Field(description='One or more fixture status short Like NS or NS-FT-CANC')] = None,
                             venue: Annotated[Union[int, float, None], Field(description='The venue id of the fixture Default: 0')] = None,
                             ids: Annotated[Union[str, None], Field(description='One or more fixture ids id-id-id Maximum of 20 fixtures ids')] = None) -> dict:
    '''For all requests to fixtures you can add the query parameter `timezone` to your request in order to retrieve the list of matches in the time zone of your choice like *“Europe/London“* To know the list of available time zones you have to use the endpoint `timezone` > Some leagues have only final result check our coverage page to know which ones **Available fixtures status** * TBD : Time To Be Defined * NS : Not Started * 1H : First Half, Kick Off * HT : Halftime * 2H : Second Half, 2nd Half Started * ET : Extra Time * P : Penalty In Progress * FT : Match Finished * AET : Match Finished After Extra Time * PEN : Match Finished After Penalty * BT : Break Time (in Extra Time) * SUSP : Match Suspended * INT : Match Interrupted * PST : Match Postponed * CANC : Match Cancelled * ABD : Match Abandoned * AWD : Technical Loss * WO : WalkOver **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day. > Here are several examples of what can be achieved ![demo-fixtures](https://www.api-football.com/public/img/demo/demo-fixtures.jpg) **Use Cases** Get fixture from one fixture {id} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?id=215662` Get fixture from severals fixtures {ids} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?ids=215662-215663-215664-215665-215666-215667` Get all available fixtures in play In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all` Get all available fixtures in play filter by several {league} In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=39-61-48` Get all available fixtures from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2019` Get all available fixtures from one {date} `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2019-10-22` Get next X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?next=15` Get last X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?last=15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2020-01-30&league=61&season=2019` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&next=10` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&last=10&status=ft` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&last=10&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&season=2019&from=2019-07-01&to=2020-10-31` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&from=2019-07-01&to=2020-10-31&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&round=Regular Season - 1`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'live': live,
        'date': date,
        'league': league,
        'season': season,
        'team': team,
        'last': last,
        'next': next,
        'from': _from,
        'to': to,
        'round': round,
        'timezone': timezone,
        'status': status,
        'venue': venue,
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_by_team_id(id: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                           live: Annotated[Union[str, None], Field(description='Enum: all or id-id for filter by league id')] = None,
                           date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                           league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                           season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020; 2021 ... Default: 2020')] = None,
                           team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 33')] = None,
                           last: Annotated[Union[int, float, None], Field(description='For the X last fixtures <= 2 characters Default: 0')] = None,
                           next: Annotated[Union[int, float, None], Field(description='For the X next fixtures <= 2 characters Default: 0')] = None,
                           _from: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                           to: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                           round: Annotated[Union[str, None], Field(description='The round of the fixture')] = None,
                           timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                           status: Annotated[Union[str, None], Field(description='One or more fixture status short Like NS or NS-FT-CANC')] = None,
                           venue: Annotated[Union[int, float, None], Field(description='The venue id of the fixture Default: 0')] = None,
                           ids: Annotated[Union[str, None], Field(description='One or more fixture ids id-id-id Maximum of 20 fixtures ids')] = None) -> dict:
    '''For all requests to fixtures you can add the query parameter `timezone` to your request in order to retrieve the list of matches in the time zone of your choice like *“Europe/London“* To know the list of available time zones you have to use the endpoint `timezone` > Some leagues have only final result check our coverage page to know which ones **Available fixtures status** * TBD : Time To Be Defined * NS : Not Started * 1H : First Half, Kick Off * HT : Halftime * 2H : Second Half, 2nd Half Started * ET : Extra Time * P : Penalty In Progress * FT : Match Finished * AET : Match Finished After Extra Time * PEN : Match Finished After Penalty * BT : Break Time (in Extra Time) * SUSP : Match Suspended * INT : Match Interrupted * PST : Match Postponed * CANC : Match Cancelled * ABD : Match Abandoned * AWD : Technical Loss * WO : WalkOver **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day. > Here are several examples of what can be achieved ![demo-fixtures](https://www.api-football.com/public/img/demo/demo-fixtures.jpg) **Use Cases** Get fixture from one fixture {id} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?id=215662` Get fixture from severals fixtures {ids} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?ids=215662-215663-215664-215665-215666-215667` Get all available fixtures in play In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all` Get all available fixtures in play filter by several {league} In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=39-61-48` Get all available fixtures from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2019` Get all available fixtures from one {date} `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2019-10-22` Get next X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?next=15` Get last X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?last=15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2020-01-30&league=61&season=2019` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&next=10` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&last=10&status=ft` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&last=10&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&season=2019&from=2019-07-01&to=2020-10-31` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&from=2019-07-01&to=2020-10-31&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&round=Regular Season - 1`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'live': live,
        'date': date,
        'league': league,
        'season': season,
        'team': team,
        'last': last,
        'next': next,
        'from': _from,
        'to': to,
        'round': round,
        'timezone': timezone,
        'status': status,
        'venue': venue,
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_between_two_dates(id: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                                  live: Annotated[Union[str, None], Field(description='Enum: all or id-id for filter by league id')] = None,
                                  date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                  league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 39')] = None,
                                  season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020; 2021 ... Default: 2020')] = None,
                                  team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                                  last: Annotated[Union[int, float, None], Field(description='For the X last fixtures <= 2 characters Default: 0')] = None,
                                  next: Annotated[Union[int, float, None], Field(description='For the X next fixtures <= 2 characters Default: 0')] = None,
                                  _from: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                  to: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                  round: Annotated[Union[str, None], Field(description='The round of the fixture')] = None,
                                  timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                                  status: Annotated[Union[str, None], Field(description='One or more fixture status short Like NS or NS-FT-CANC')] = None,
                                  venue: Annotated[Union[int, float, None], Field(description='The venue id of the fixture Default: 0')] = None,
                                  ids: Annotated[Union[str, None], Field(description='One or more fixture ids id-id-id Maximum of 20 fixtures ids')] = None) -> dict:
    '''For all requests to fixtures you can add the query parameter `timezone` to your request in order to retrieve the list of matches in the time zone of your choice like *“Europe/London“* To know the list of available time zones you have to use the endpoint `timezone` > Some leagues have only final result check our coverage page to know which ones **Available fixtures status** * TBD : Time To Be Defined * NS : Not Started * 1H : First Half, Kick Off * HT : Halftime * 2H : Second Half, 2nd Half Started * ET : Extra Time * P : Penalty In Progress * FT : Match Finished * AET : Match Finished After Extra Time * PEN : Match Finished After Penalty * BT : Break Time (in Extra Time) * SUSP : Match Suspended * INT : Match Interrupted * PST : Match Postponed * CANC : Match Cancelled * ABD : Match Abandoned * AWD : Technical Loss * WO : WalkOver **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day. > Here are several examples of what can be achieved ![demo-fixtures](https://www.api-football.com/public/img/demo/demo-fixtures.jpg) **Use Cases** Get fixture from one fixture {id} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?id=215662` Get fixture from severals fixtures {ids} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?ids=215662-215663-215664-215665-215666-215667` Get all available fixtures in play In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all` Get all available fixtures in play filter by several {league} In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=39-61-48` Get all available fixtures from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2019` Get all available fixtures from one {date} `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2019-10-22` Get next X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?next=15` Get last X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?last=15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2020-01-30&league=61&season=2019` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&next=10` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&last=10&status=ft` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&last=10&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&season=2019&from=2019-07-01&to=2020-10-31` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&from=2019-07-01&to=2020-10-31&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&round=Regular Season - 1`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'live': live,
        'date': date,
        'league': league,
        'season': season,
        'team': team,
        'last': last,
        'next': next,
        'from': _from,
        'to': to,
        'round': round,
        'timezone': timezone,
        'status': status,
        'venue': venue,
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_filtered_by_round(id: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                                  live: Annotated[Union[str, None], Field(description='Enum: all or id-id for filter by league id')] = None,
                                  date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                  league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 39')] = None,
                                  season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020; 2021 ... Default: 2020')] = None,
                                  team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                                  last: Annotated[Union[int, float, None], Field(description='For the X last fixtures <= 2 characters Default: 0')] = None,
                                  next: Annotated[Union[int, float, None], Field(description='For the X next fixtures <= 2 characters Default: 0')] = None,
                                  _from: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                  to: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                  round: Annotated[Union[str, None], Field(description='The round of the fixture')] = None,
                                  timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                                  status: Annotated[Union[str, None], Field(description='One or more fixture status short Like NS or NS-FT-CANC')] = None,
                                  venue: Annotated[Union[int, float, None], Field(description='The venue id of the fixture Default: 0')] = None,
                                  ids: Annotated[Union[str, None], Field(description='One or more fixture ids id-id-id Maximum of 20 fixtures ids')] = None) -> dict:
    '''For all requests to fixtures you can add the query parameter `timezone` to your request in order to retrieve the list of matches in the time zone of your choice like *“Europe/London“* To know the list of available time zones you have to use the endpoint `timezone` > Some leagues have only final result check our coverage page to know which ones **Available fixtures status** * TBD : Time To Be Defined * NS : Not Started * 1H : First Half, Kick Off * HT : Halftime * 2H : Second Half, 2nd Half Started * ET : Extra Time * P : Penalty In Progress * FT : Match Finished * AET : Match Finished After Extra Time * PEN : Match Finished After Penalty * BT : Break Time (in Extra Time) * SUSP : Match Suspended * INT : Match Interrupted * PST : Match Postponed * CANC : Match Cancelled * ABD : Match Abandoned * AWD : Technical Loss * WO : WalkOver **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day. > Here are several examples of what can be achieved ![demo-fixtures](https://www.api-football.com/public/img/demo/demo-fixtures.jpg) **Use Cases** Get fixture from one fixture {id} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?id=215662` Get fixture from severals fixtures {ids} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?ids=215662-215663-215664-215665-215666-215667` Get all available fixtures in play In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all` Get all available fixtures in play filter by several {league} In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=39-61-48` Get all available fixtures from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2019` Get all available fixtures from one {date} `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2019-10-22` Get next X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?next=15` Get last X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?last=15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2020-01-30&league=61&season=2019` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&next=10` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&last=10&status=ft` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&last=10&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&season=2019&from=2019-07-01&to=2020-10-31` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&from=2019-07-01&to=2020-10-31&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&round=Regular Season - 1`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'live': live,
        'date': date,
        'league': league,
        'season': season,
        'team': team,
        'last': last,
        'next': next,
        'from': _from,
        'to': to,
        'round': round,
        'timezone': timezone,
        'status': status,
        'venue': venue,
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_filtered_by_status(id: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                                   live: Annotated[Union[str, None], Field(description='Enum: all or id-id for filter by league id')] = None,
                                   date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                   league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 39')] = None,
                                   season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020; 2021 ... Default: 2020')] = None,
                                   team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                                   last: Annotated[Union[int, float, None], Field(description='For the X last fixtures <= 2 characters Default: 0')] = None,
                                   next: Annotated[Union[int, float, None], Field(description='For the X next fixtures <= 2 characters Default: 0')] = None,
                                   _from: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                   to: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                   round: Annotated[Union[str, None], Field(description='The round of the fixture')] = None,
                                   timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                                   status: Annotated[Union[str, None], Field(description='One or more fixture status short Like NS or NS-FT-CANC')] = None,
                                   venue: Annotated[Union[int, float, None], Field(description='The venue id of the fixture Default: 0')] = None,
                                   ids: Annotated[Union[str, None], Field(description='One or more fixture ids id-id-id Maximum of 20 fixtures ids')] = None) -> dict:
    '''For all requests to fixtures you can add the query parameter `timezone` to your request in order to retrieve the list of matches in the time zone of your choice like *“Europe/London“* To know the list of available time zones you have to use the endpoint `timezone` > Some leagues have only final result check our coverage page to know which ones **Available fixtures status** * TBD : Time To Be Defined * NS : Not Started * 1H : First Half, Kick Off * HT : Halftime * 2H : Second Half, 2nd Half Started * ET : Extra Time * P : Penalty In Progress * FT : Match Finished * AET : Match Finished After Extra Time * PEN : Match Finished After Penalty * BT : Break Time (in Extra Time) * SUSP : Match Suspended * INT : Match Interrupted * PST : Match Postponed * CANC : Match Cancelled * ABD : Match Abandoned * AWD : Technical Loss * WO : WalkOver **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day. > Here are several examples of what can be achieved ![demo-fixtures](https://www.api-football.com/public/img/demo/demo-fixtures.jpg) **Use Cases** Get fixture from one fixture {id} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?id=215662` Get fixture from severals fixtures {ids} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?ids=215662-215663-215664-215665-215666-215667` Get all available fixtures in play In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all` Get all available fixtures in play filter by several {league} In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=39-61-48` Get all available fixtures from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2019` Get all available fixtures from one {date} `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2019-10-22` Get next X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?next=15` Get last X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?last=15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2020-01-30&league=61&season=2019` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&next=10` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&last=10&status=ft` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&last=10&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&season=2019&from=2019-07-01&to=2020-10-31` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&from=2019-07-01&to=2020-10-31&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&round=Regular Season - 1`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'live': live,
        'date': date,
        'league': league,
        'season': season,
        'team': team,
        'last': last,
        'next': next,
        'from': _from,
        'to': to,
        'round': round,
        'timezone': timezone,
        'status': status,
        'venue': venue,
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_next_xfixtures_to_come(id: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                              live: Annotated[Union[str, None], Field(description='Enum: all or id-id for filter by league id')] = None,
                              date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                              league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                              season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020; 2021 ... Default: 0')] = None,
                              team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                              last: Annotated[Union[int, float, None], Field(description='For the X last fixtures <= 2 characters Default: 0')] = None,
                              next: Annotated[Union[int, float, None], Field(description='For the X next fixtures <= 2 characters Default: 50')] = None,
                              _from: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                              to: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                              round: Annotated[Union[str, None], Field(description='The round of the fixture')] = None,
                              timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                              status: Annotated[Union[str, None], Field(description='One or more fixture status short Like NS or NS-FT-CANC')] = None,
                              venue: Annotated[Union[int, float, None], Field(description='The venue id of the fixture Default: 0')] = None,
                              ids: Annotated[Union[str, None], Field(description='One or more fixture ids id-id-id Maximum of 20 fixtures ids')] = None) -> dict:
    '''For all requests to fixtures you can add the query parameter `timezone` to your request in order to retrieve the list of matches in the time zone of your choice like *“Europe/London“* To know the list of available time zones you have to use the endpoint `timezone` > Some leagues have only final result check our coverage page to know which ones **Available fixtures status** * TBD : Time To Be Defined * NS : Not Started * 1H : First Half, Kick Off * HT : Halftime * 2H : Second Half, 2nd Half Started * ET : Extra Time * P : Penalty In Progress * FT : Match Finished * AET : Match Finished After Extra Time * PEN : Match Finished After Penalty * BT : Break Time (in Extra Time) * SUSP : Match Suspended * INT : Match Interrupted * PST : Match Postponed * CANC : Match Cancelled * ABD : Match Abandoned * AWD : Technical Loss * WO : WalkOver **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day. > Here are several examples of what can be achieved ![demo-fixtures](https://www.api-football.com/public/img/demo/demo-fixtures.jpg) **Use Cases** Get fixture from one fixture {id} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?id=215662` Get fixture from severals fixtures {ids} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?ids=215662-215663-215664-215665-215666-215667` Get all available fixtures in play In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all` Get all available fixtures in play filter by several {league} In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=39-61-48` Get all available fixtures from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2019` Get all available fixtures from one {date} `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2019-10-22` Get next X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?next=15` Get last X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?last=15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2020-01-30&league=61&season=2019` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&next=10` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&last=10&status=ft` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&last=10&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&season=2019&from=2019-07-01&to=2020-10-31` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&from=2019-07-01&to=2020-10-31&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&round=Regular Season - 1`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'live': live,
        'date': date,
        'league': league,
        'season': season,
        'team': team,
        'last': last,
        'next': next,
        'from': _from,
        'to': to,
        'round': round,
        'timezone': timezone,
        'status': status,
        'venue': venue,
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_last_xfixtures_that_were_played(id: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                                       live: Annotated[Union[str, None], Field(description='Enum: all or id-id for filter by league id')] = None,
                                       date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                       league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                                       season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020; 2021 ... Default: 0')] = None,
                                       team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                                       last: Annotated[Union[int, float, None], Field(description='For the X last fixtures <= 2 characters Default: 50')] = None,
                                       next: Annotated[Union[int, float, None], Field(description='For the X next fixtures <= 2 characters Default: 0')] = None,
                                       _from: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                       to: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                       round: Annotated[Union[str, None], Field(description='The round of the fixture')] = None,
                                       timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                                       status: Annotated[Union[str, None], Field(description='One or more fixture status short Like NS or NS-FT-CANC')] = None,
                                       venue: Annotated[Union[int, float, None], Field(description='The venue id of the fixture Default: 0')] = None,
                                       ids: Annotated[Union[str, None], Field(description='One or more fixture ids id-id-id Maximum of 20 fixtures ids')] = None) -> dict:
    '''For all requests to fixtures you can add the query parameter `timezone` to your request in order to retrieve the list of matches in the time zone of your choice like *“Europe/London“* To know the list of available time zones you have to use the endpoint `timezone` > Some leagues have only final result check our coverage page to know which ones **Available fixtures status** * TBD : Time To Be Defined * NS : Not Started * 1H : First Half, Kick Off * HT : Halftime * 2H : Second Half, 2nd Half Started * ET : Extra Time * P : Penalty In Progress * FT : Match Finished * AET : Match Finished After Extra Time * PEN : Match Finished After Penalty * BT : Break Time (in Extra Time) * SUSP : Match Suspended * INT : Match Interrupted * PST : Match Postponed * CANC : Match Cancelled * ABD : Match Abandoned * AWD : Technical Loss * WO : WalkOver **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day. > Here are several examples of what can be achieved ![demo-fixtures](https://www.api-football.com/public/img/demo/demo-fixtures.jpg) **Use Cases** Get fixture from one fixture {id} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?id=215662` Get fixture from severals fixtures {ids} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?ids=215662-215663-215664-215665-215666-215667` Get all available fixtures in play In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all` Get all available fixtures in play filter by several {league} In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=39-61-48` Get all available fixtures from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2019` Get all available fixtures from one {date} `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2019-10-22` Get next X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?next=15` Get last X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?last=15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2020-01-30&league=61&season=2019` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&next=10` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&last=10&status=ft` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&last=10&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&season=2019&from=2019-07-01&to=2020-10-31` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&from=2019-07-01&to=2020-10-31&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&round=Regular Season - 1`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'live': live,
        'date': date,
        'league': league,
        'season': season,
        'team': team,
        'last': last,
        'next': next,
        'from': _from,
        'to': to,
        'round': round,
        'timezone': timezone,
        'status': status,
        'venue': venue,
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_from_severals_fixtures_ids(id: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                                           live: Annotated[Union[str, None], Field(description='Enum: all or id-id for filter by league id')] = None,
                                           date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                           league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                                           season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020; 2021 ... Default: 0')] = None,
                                           team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                                           last: Annotated[Union[int, float, None], Field(description='For the X last fixtures <= 2 characters Default: 0')] = None,
                                           next: Annotated[Union[int, float, None], Field(description='For the X next fixtures <= 2 characters Default: 0')] = None,
                                           _from: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                           to: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                           round: Annotated[Union[str, None], Field(description='The round of the fixture')] = None,
                                           timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                                           status: Annotated[Union[str, None], Field(description='One or more fixture status short Like NS or NS-FT-CANC')] = None,
                                           venue: Annotated[Union[int, float, None], Field(description='The venue id of the fixture Default: 0')] = None,
                                           ids: Annotated[Union[str, None], Field(description='One or more fixture ids id-id-id Maximum of 20 fixtures ids')] = None) -> dict:
    '''For all requests to fixtures you can add the query parameter `timezone` to your request in order to retrieve the list of matches in the time zone of your choice like *“Europe/London“* To know the list of available time zones you have to use the endpoint `timezone` > Some leagues have only final result check our coverage page to know which ones **Available fixtures status** * TBD : Time To Be Defined * NS : Not Started * 1H : First Half, Kick Off * HT : Halftime * 2H : Second Half, 2nd Half Started * ET : Extra Time * P : Penalty In Progress * FT : Match Finished * AET : Match Finished After Extra Time * PEN : Match Finished After Penalty * BT : Break Time (in Extra Time) * SUSP : Match Suspended * INT : Match Interrupted * PST : Match Postponed * CANC : Match Cancelled * ABD : Match Abandoned * AWD : Technical Loss * WO : WalkOver **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the leagues, teams, fixtures who have at least one fixture in progress otherwise 1 call per day. > Here are several examples of what can be achieved ![demo-fixtures](https://www.api-football.com/public/img/demo/demo-fixtures.jpg) **Use Cases** Get fixture from one fixture {id} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?id=215662` Get fixture from severals fixtures {ids} In this request events, lineups, statistics fixture and players fixture are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?ids=215662-215663-215664-215665-215666-215667` Get all available fixtures in play In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=all` Get all available fixtures in play filter by several {league} In this request events are returned in the response `https://api-football-v1.p.rapidapi.com/v3/fixtures?live=39-61-48` Get all available fixtures from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2019` Get all available fixtures from one {date} `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2019-10-22` Get next X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?next=15` Get last X available fixtures `https://api-football-v1.p.rapidapi.com/v3/fixtures?last=15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2020-01-30&league=61&season=2019` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&next=10` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&last=10&status=ft` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&last=10&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?team=85&season=2019&from=2019-07-01&to=2020-10-31` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&from=2019-07-01&to=2020-10-31&timezone=Europe/london` `https://api-football-v1.p.rapidapi.com/v3/fixtures?league=61&season=2019&round=Regular Season - 1`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'live': live,
        'date': date,
        'league': league,
        'season': season,
        'team': team,
        'last': last,
        'next': next,
        'from': _from,
        'to': to,
        'round': round,
        'timezone': timezone,
        'status': status,
        'venue': venue,
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_rounds_with_dates(league: Annotated[Union[int, float], Field(description='The id of the league Default: 39')],
                                  season: Annotated[Union[int, float], Field(description='The season of the league 4 characters Like 2020, 2021 ... Default: 2020')],
                                  current: Annotated[Union[str, None], Field(description='Retrun the current round only Enum: true or false')] = None,
                                  dates: Annotated[Union[str, None], Field(description='Default: false Enum: "true" "false" Add the dates of each round in the response')] = None) -> dict:
    '''Get the rounds for a league or a cup. The `round` can be used in endpoint fixtures as filters **Update Frequency** : This endpoint is updated every day. **Recommended Calls** : 1 call per day. **Use Cases** Get all available rounds from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/rounds?league=39&season=2019` // Get all available rounds from one {league} & {season} With the dates of each round get("https://v3.football.api-sports.io/fixtures/rounds?league=39&season=2019&dates=true"); Get current round from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/rounds?league=39&season=2019&current=true`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/rounds'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'current': current,
        'dates': dates,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_statistics_with_halftime_data(fixture: Annotated[Union[int, float], Field(description='The id of the fixture Default: 1234266')],
                                              team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                                              type: Annotated[Union[str, None], Field(description='The type of statistics Like Fouls, Offsides...')] = None,
                                              half: Annotated[Union[str, None], Field(description='Default: false Enum: "true" "false" Add the halftime statistics in the response Data start from 2024 season for half parameter')] = None) -> dict:
    '''Get the statistics for one fixture with halftime data. **Available statistics** * Shots on Goal * Shots off Goal * Shots insidebox * Shots outsidebox * Total Shots * Blocked Shots * Fouls * Corner Kicks * Offsides * Ball Possession * Yellow Cards * Red Cards * Goalkeeper Saves * Total passes * Passes accurate * Passes % **Update Frequency** : This endpoint is updated every minute. **Recommended Calls** : 1 call every minute for the teams or fixtures who have at least one fixture in progress otherwise 1 call per day. > Here is an example of what can be achieved ![demo-statistics](https://www.api-football.com/public/img/demo/demo-statistics.png) **Use Cases** Get all available statistics from one {fixture} `https://v3.football.api-sports.io/fixtures/statistics?fixture=215662` // Get all available statistics from one {fixture} with Fulltime, First & Second Half data get("https://v3.football.api-sports.io/fixtures/statistics?fixture=215662&half=true"); Get all available statistics from one {fixture} & {type} `https://v3.football.api-sports.io/fixtures/statistics?fixture=215662&type=Total Shots` Get all available statistics from one {fixture} & {team} `v3.football.api-sports.io/fixtures/statistics?fixture=215662&team=463`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/statistics'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'team': team,
        'type': type,
        'half': half,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_teams_statistics(league: Annotated[Union[int, float], Field(description='The id of the league Default: 39')],
                        season: Annotated[Union[int, float], Field(description='The season of the league 4 charactersLike 2020, 2021 ... Default: 2020')],
                        team: Annotated[Union[int, float], Field(description='The id of the team Default: 33')],
                        date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None) -> dict:
    '''**Update Frequency** : This endpoint is updated twice a day. **Recommended Calls** : 1 call per day for the teams who have at least one fixture during the day otherwise 1 call per week. > Here is an example of what can be achieved ![demo-teams-statistics](https://www.api-football.com/public/img/demo/demo-teams-statistics.png) **Use Cases** Get all statistics for a {team} in a {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/teams/statistics?league=39&team=33&season=2019` Get all statistics for a {team} in a {league} & {season} with a end {date} `https://api-football-v1.p.rapidapi.com/v3/teams/statistics?league=39&team=33&season=2019&date=2019-10-08`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/teams/statistics'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'team': team,
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_teams_informations(id: Annotated[Union[int, float, None], Field(description='The id of the team Default: 33')] = None,
                          name: Annotated[Union[str, None], Field(description='The name of the team')] = None,
                          league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                          season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2019, 2020, 2021 ... Default: 0')] = None,
                          country: Annotated[Union[str, None], Field(description='The country name of the team')] = None,
                          search: Annotated[Union[str, None], Field(description='The name or the country name of the team >= 3 characters')] = None,
                          code: Annotated[Union[str, None], Field(description='The code of the team')] = None,
                          venue: Annotated[Union[int, float, None], Field(description='The id of the venue Default: 0')] = None) -> dict:
    '''Get the list of available teams. The team `id` are **unique** in the API and teams keep it among all the leagues/cups in which they participate. > All the parameters of this endpoint can be used together. **This endpoint requires at least one parameter.** **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get one team from one team {id} `https://api-football-v1.p.rapidapi.com/v3/teams?id=33` Get one team from one team {name} `https://api-football-v1.p.rapidapi.com/v3/teams?name=manchester united` Get all teams from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/teams?league=39&season=2019` Get teams from one team {country} `https://api-football-v1.p.rapidapi.com/v3/teams?country=england` Allows you to search for a team in relation to a team {name} or {country} `https://api-football-v1.p.rapidapi.com/v3/teams?search=manches` `https://api-football-v1.p.rapidapi.com/v3/teams?search=England`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/teams'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'league': league,
        'season': season,
        'country': country,
        'search': search,
        'code': code,
        'venue': venue,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_teams_seasons(team: Annotated[Union[int, float], Field(description='The id of the team Default: 33')]) -> dict:
    '''Get the list of seasons available for a team. **This endpoint requires at least one parameter.** **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all seasons available for a team from one team {id} `https://api-football-v1.p.rapidapi.com/v3/teams/seasons?team=33`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/teams/seasons'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team': team,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_teams_countries() -> dict:
    '''Get the list of countries available for the `teams` endpoint. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all countries available for the teams endpoints `https://api-football-v1.p.rapidapi.com/v3/teams/countries`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/teams/countries'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_seasons() -> dict:
    '''Get the list of available seasons. All seasons are only **4-digit keys**, so for a league whose season is `2018-2019` like the English Premier League (EPL), the `2018-2019` season in the API will be `2018`. All `seasons` can be used in other endpoints as filters. > This endpoint does not require any parameters. **Update Frequency** : This endpoint is updated each time a new league is added. **Recommended Calls** : 1 call per day.'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/leagues/seasons'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_countries(name: Annotated[Union[str, None], Field(description='The name of the country')] = None,
                 code: Annotated[Union[str, None], Field(description='The Alpha2 code of the country 2 characters Like FR, GB, IT…')] = None,
                 search: Annotated[Union[str, None], Field(description='The name of the country >= 3 characters')] = None) -> dict:
    '''Get the list of available countries. The `name` and `code` fields can be used in other endpoints as filters. > Examples available in Request samples "Use Cases". All the parameters of this endpoint can be used together. **Update Frequency** : This endpoint is updated each time a new league from a country not covered by the API is added. **Recommended Calls** : 1 call per day. **Use Cases** Get all available countries across all {seasons} and competitions `https://api-football-v1.p.rapidapi.com/v3/countries` Get all available countries from one country {name} `https://api-football-v1.p.rapidapi.com/v3/countries?name=england` Get all available countries from one country {code} `https://api-football-v1.p.rapidapi.com/v3/countries?code=fr` Allows you to search for a countries in relation to a country {name} `https://api-football-v1.p.rapidapi.com/v3/countries?search=engl`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/countries'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
        'code': code,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_leagues(id: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
               name: Annotated[Union[str, None], Field(description='The name of the league')] = None,
               country: Annotated[Union[str, None], Field(description='The country name of the league')] = None,
               code: Annotated[Union[str, None], Field(description='The Alpha2 code of the country 2 characters Like FR, GB, IT…')] = None,
               season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2018, 2019 etc... Default: 0')] = None,
               team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
               type: Annotated[Union[str, None], Field(description='The type of the league Enum: league or cup')] = None,
               current: Annotated[Union[str, None], Field(description='The state of the league Enum: true or false')] = None,
               search: Annotated[Union[str, None], Field(description='The name or the country of the league >= 3 characters')] = None,
               last: Annotated[Union[int, float, None], Field(description='The X last leagues/cups added in the API <= 2 characters Default: 0')] = None) -> dict:
    '''Get the list of available leagues and cups. The league `id` are **unique** in the API and leagues keep it across all `seasons` > Most of the parameters of this endpoint can be used together. **Update Frequency** : This endpoint is updated several times a day. **Recommended Calls** : 1 call per hour. **Use Cases** Allows to retrieve all the seasons available for a league/cup `https://api-football-v1.p.rapidapi.com/v3/leagues?id=39` Get all leagues from one league {name} `https://api-football-v1.p.rapidapi.com/v3/leagues?name=premier league` Get all leagues from one {country} You can find the available {country} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?country=england` Get all leagues from one country {code} (GB, FR, IT etc..) You can find the available country {code} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?code=gb` Get all leagues from one {season} You can find the available {season} by using the endpoint seasons `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019` Get one league from one league {id} & {season} `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&id=39` Get all leagues in which the {team} has played at least one match `https://api-football-v1.p.rapidapi.com/v3/leagues?team=33` Allows you to search for a league in relation to a league {name} or {country} `https://api-football-v1.p.rapidapi.com/v3/leagues?search=premier league` `https://api-football-v1.p.rapidapi.com/v3/leagues?search=England` Get all leagues from one {type} `https://api-football-v1.p.rapidapi.com/v3/leagues?type=league` Get all leagues where the season is in progress or not `https://api-football-v1.p.rapidapi.com/v3/leagues?current=true` Get the last 99 leagues or cups added to the API `https://api-football-v1.p.rapidapi.com/v3/leagues?last=99` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&country=england&type=league` `https://api-football-v1.p.rapidapi.com/v3/leagues?team=85&season=2019` `https://api-football-v1.p.rapidapi.com/v3/leagues?id=61&current=true&type=league`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/leagues'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'country': country,
        'code': code,
        'season': season,
        'team': team,
        'type': type,
        'current': current,
        'search': search,
        'last': last,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_leagues_by_league_id(id: Annotated[Union[int, float, None], Field(description='The id of the league Default: 39')] = None,
                            name: Annotated[Union[str, None], Field(description='The name of the league')] = None,
                            country: Annotated[Union[str, None], Field(description='The country name of the league')] = None,
                            code: Annotated[Union[str, None], Field(description='The Alpha2 code of the country 2 characters Like FR, GB, IT…')] = None,
                            season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2018, 2019 etc... Default: 0')] = None,
                            team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                            type: Annotated[Union[str, None], Field(description='The type of the league Enum: league or cup')] = None,
                            current: Annotated[Union[str, None], Field(description='The state of the league Enum: true or false')] = None,
                            search: Annotated[Union[str, None], Field(description='The name or the country of the league >= 3 characters')] = None,
                            last: Annotated[Union[int, float, None], Field(description='The X last leagues/cups added in the API <= 2 characters Default: 0')] = None) -> dict:
    '''Get the list of available leagues and cups. The league `id` are **unique** in the API and leagues keep it across all `seasons` > Most of the parameters of this endpoint can be used together. **Update Frequency** : This endpoint is updated several times a day. **Recommended Calls** : 1 call per hour. **Use Cases** Allows to retrieve all the seasons available for a league/cup `https://api-football-v1.p.rapidapi.com/v3/leagues?id=39` Get all leagues from one league {name} `https://api-football-v1.p.rapidapi.com/v3/leagues?name=premier league` Get all leagues from one {country} You can find the available {country} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?country=england` Get all leagues from one country {code} (GB, FR, IT etc..) You can find the available country {code} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?code=gb` Get all leagues from one {season} You can find the available {season} by using the endpoint seasons `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019` Get one league from one league {id} & {season} `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&id=39` Get all leagues in which the {team} has played at least one match `https://api-football-v1.p.rapidapi.com/v3/leagues?team=33` Allows you to search for a league in relation to a league {name} or {country} `https://api-football-v1.p.rapidapi.com/v3/leagues?search=premier league` `https://api-football-v1.p.rapidapi.com/v3/leagues?search=England` Get all leagues from one {type} `https://api-football-v1.p.rapidapi.com/v3/leagues?type=league` Get all leagues where the season is in progress or not `https://api-football-v1.p.rapidapi.com/v3/leagues?current=true` Get the last 99 leagues or cups added to the API `https://api-football-v1.p.rapidapi.com/v3/leagues?last=99` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&country=england&type=league` `https://api-football-v1.p.rapidapi.com/v3/leagues?team=85&season=2019` `https://api-football-v1.p.rapidapi.com/v3/leagues?id=61&current=true&type=league`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/leagues'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'country': country,
        'code': code,
        'season': season,
        'team': team,
        'type': type,
        'current': current,
        'search': search,
        'last': last,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_leagues_by_country_name(id: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                               name: Annotated[Union[str, None], Field(description='The name of the league')] = None,
                               country: Annotated[Union[str, None], Field(description='The country name of the league')] = None,
                               code: Annotated[Union[str, None], Field(description='The Alpha2 code of the country 2 characters Like FR, GB, IT…')] = None,
                               season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2018, 2019 etc... Default: 0')] = None,
                               team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                               type: Annotated[Union[str, None], Field(description='The type of the league Enum: league or cup')] = None,
                               current: Annotated[Union[str, None], Field(description='The state of the league Enum: true or false')] = None,
                               search: Annotated[Union[str, None], Field(description='The name or the country of the league >= 3 characters')] = None,
                               last: Annotated[Union[int, float, None], Field(description='The X last leagues/cups added in the API <= 2 characters Default: 0')] = None) -> dict:
    '''Get the list of available leagues and cups. The league `id` are **unique** in the API and leagues keep it across all `seasons` > Most of the parameters of this endpoint can be used together. **Update Frequency** : This endpoint is updated several times a day. **Recommended Calls** : 1 call per hour. **Use Cases** Allows to retrieve all the seasons available for a league/cup `https://api-football-v1.p.rapidapi.com/v3/leagues?id=39` Get all leagues from one league {name} `https://api-football-v1.p.rapidapi.com/v3/leagues?name=premier league` Get all leagues from one {country} You can find the available {country} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?country=england` Get all leagues from one country {code} (GB, FR, IT etc..) You can find the available country {code} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?code=gb` Get all leagues from one {season} You can find the available {season} by using the endpoint seasons `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019` Get one league from one league {id} & {season} `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&id=39` Get all leagues in which the {team} has played at least one match `https://api-football-v1.p.rapidapi.com/v3/leagues?team=33` Allows you to search for a league in relation to a league {name} or {country} `https://api-football-v1.p.rapidapi.com/v3/leagues?search=premier league` `https://api-football-v1.p.rapidapi.com/v3/leagues?search=England` Get all leagues from one {type} `https://api-football-v1.p.rapidapi.com/v3/leagues?type=league` Get all leagues where the season is in progress or not `https://api-football-v1.p.rapidapi.com/v3/leagues?current=true` Get the last 99 leagues or cups added to the API `https://api-football-v1.p.rapidapi.com/v3/leagues?last=99` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&country=england&type=league` `https://api-football-v1.p.rapidapi.com/v3/leagues?team=85&season=2019` `https://api-football-v1.p.rapidapi.com/v3/leagues?id=61&current=true&type=league`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/leagues'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'country': country,
        'code': code,
        'season': season,
        'team': team,
        'type': type,
        'current': current,
        'search': search,
        'last': last,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_leagues_by_country_code(id: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                               name: Annotated[Union[str, None], Field(description='The name of the league')] = None,
                               country: Annotated[Union[str, None], Field(description='The country name of the league')] = None,
                               code: Annotated[Union[str, None], Field(description='The Alpha2 code of the country 2 characters Like FR, GB, IT…')] = None,
                               season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2018, 2019 etc... Default: 0')] = None,
                               team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                               type: Annotated[Union[str, None], Field(description='The type of the league Enum: league or cup')] = None,
                               current: Annotated[Union[str, None], Field(description='The state of the league Enum: true or false')] = None,
                               search: Annotated[Union[str, None], Field(description='The name or the country of the league >= 3 characters')] = None,
                               last: Annotated[Union[int, float, None], Field(description='The X last leagues/cups added in the API <= 2 characters Default: 0')] = None) -> dict:
    '''Get the list of available leagues and cups. The league `id` are **unique** in the API and leagues keep it across all `seasons` > Most of the parameters of this endpoint can be used together. **Update Frequency** : This endpoint is updated several times a day. **Recommended Calls** : 1 call per hour. **Use Cases** Allows to retrieve all the seasons available for a league/cup `https://api-football-v1.p.rapidapi.com/v3/leagues?id=39` Get all leagues from one league {name} `https://api-football-v1.p.rapidapi.com/v3/leagues?name=premier league` Get all leagues from one {country} You can find the available {country} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?country=england` Get all leagues from one country {code} (GB, FR, IT etc..) You can find the available country {code} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?code=gb` Get all leagues from one {season} You can find the available {season} by using the endpoint seasons `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019` Get one league from one league {id} & {season} `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&id=39` Get all leagues in which the {team} has played at least one match `https://api-football-v1.p.rapidapi.com/v3/leagues?team=33` Allows you to search for a league in relation to a league {name} or {country} `https://api-football-v1.p.rapidapi.com/v3/leagues?search=premier league` `https://api-football-v1.p.rapidapi.com/v3/leagues?search=England` Get all leagues from one {type} `https://api-football-v1.p.rapidapi.com/v3/leagues?type=league` Get all leagues where the season is in progress or not `https://api-football-v1.p.rapidapi.com/v3/leagues?current=true` Get the last 99 leagues or cups added to the API `https://api-football-v1.p.rapidapi.com/v3/leagues?last=99` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&country=england&type=league` `https://api-football-v1.p.rapidapi.com/v3/leagues?team=85&season=2019` `https://api-football-v1.p.rapidapi.com/v3/leagues?id=61&current=true&type=league`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/leagues'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'country': country,
        'code': code,
        'season': season,
        'team': team,
        'type': type,
        'current': current,
        'search': search,
        'last': last,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_leagues_by_season(id: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                         name: Annotated[Union[str, None], Field(description='The name of the league')] = None,
                         country: Annotated[Union[str, None], Field(description='The country name of the league')] = None,
                         code: Annotated[Union[str, None], Field(description='The Alpha2 code of the country 2 characters Like FR, GB, IT…')] = None,
                         season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2018, 2019 etc... Default: 2020')] = None,
                         team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                         type: Annotated[Union[str, None], Field(description='The type of the league Enum: league or cup')] = None,
                         current: Annotated[Union[str, None], Field(description='The state of the league Enum: true or false')] = None,
                         search: Annotated[Union[str, None], Field(description='The name or the country of the league >= 3 characters')] = None,
                         last: Annotated[Union[int, float, None], Field(description='The X last leagues/cups added in the API <= 2 characters Default: 0')] = None) -> dict:
    '''Get the list of available leagues and cups. The league `id` are **unique** in the API and leagues keep it across all `seasons` > Most of the parameters of this endpoint can be used together. **Update Frequency** : This endpoint is updated several times a day. **Recommended Calls** : 1 call per hour. **Use Cases** Allows to retrieve all the seasons available for a league/cup `https://api-football-v1.p.rapidapi.com/v3/leagues?id=39` Get all leagues from one league {name} `https://api-football-v1.p.rapidapi.com/v3/leagues?name=premier league` Get all leagues from one {country} You can find the available {country} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?country=england` Get all leagues from one country {code} (GB, FR, IT etc..) You can find the available country {code} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?code=gb` Get all leagues from one {season} You can find the available {season} by using the endpoint seasons `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019` Get one league from one league {id} & {season} `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&id=39` Get all leagues in which the {team} has played at least one match `https://api-football-v1.p.rapidapi.com/v3/leagues?team=33` Allows you to search for a league in relation to a league {name} or {country} `https://api-football-v1.p.rapidapi.com/v3/leagues?search=premier league` `https://api-football-v1.p.rapidapi.com/v3/leagues?search=England` Get all leagues from one {type} `https://api-football-v1.p.rapidapi.com/v3/leagues?type=league` Get all leagues where the season is in progress or not `https://api-football-v1.p.rapidapi.com/v3/leagues?current=true` Get the last 99 leagues or cups added to the API `https://api-football-v1.p.rapidapi.com/v3/leagues?last=99` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&country=england&type=league` `https://api-football-v1.p.rapidapi.com/v3/leagues?team=85&season=2019` `https://api-football-v1.p.rapidapi.com/v3/leagues?id=61&current=true&type=league`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/leagues'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'country': country,
        'code': code,
        'season': season,
        'team': team,
        'type': type,
        'current': current,
        'search': search,
        'last': last,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_leagues_by_team_id(id: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                          name: Annotated[Union[str, None], Field(description='The name of the league')] = None,
                          country: Annotated[Union[str, None], Field(description='The country name of the league')] = None,
                          code: Annotated[Union[str, None], Field(description='The Alpha2 code of the country 2 characters Like FR, GB, IT…')] = None,
                          season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2018, 2019 etc... Default: 0')] = None,
                          team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 33')] = None,
                          type: Annotated[Union[str, None], Field(description='The type of the league Enum: league or cup')] = None,
                          current: Annotated[Union[str, None], Field(description='The state of the league Enum: true or false')] = None,
                          search: Annotated[Union[str, None], Field(description='The name or the country of the league >= 3 characters')] = None,
                          last: Annotated[Union[int, float, None], Field(description='The X last leagues/cups added in the API <= 2 characters Default: 0')] = None) -> dict:
    '''Get the list of available leagues and cups. The league `id` are **unique** in the API and leagues keep it across all `seasons` > Most of the parameters of this endpoint can be used together. **Update Frequency** : This endpoint is updated several times a day. **Recommended Calls** : 1 call per hour. **Use Cases** Allows to retrieve all the seasons available for a league/cup `https://api-football-v1.p.rapidapi.com/v3/leagues?id=39` Get all leagues from one league {name} `https://api-football-v1.p.rapidapi.com/v3/leagues?name=premier league` Get all leagues from one {country} You can find the available {country} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?country=england` Get all leagues from one country {code} (GB, FR, IT etc..) You can find the available country {code} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?code=gb` Get all leagues from one {season} You can find the available {season} by using the endpoint seasons `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019` Get one league from one league {id} & {season} `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&id=39` Get all leagues in which the {team} has played at least one match `https://api-football-v1.p.rapidapi.com/v3/leagues?team=33` Allows you to search for a league in relation to a league {name} or {country} `https://api-football-v1.p.rapidapi.com/v3/leagues?search=premier league` `https://api-football-v1.p.rapidapi.com/v3/leagues?search=England` Get all leagues from one {type} `https://api-football-v1.p.rapidapi.com/v3/leagues?type=league` Get all leagues where the season is in progress or not `https://api-football-v1.p.rapidapi.com/v3/leagues?current=true` Get the last 99 leagues or cups added to the API `https://api-football-v1.p.rapidapi.com/v3/leagues?last=99` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&country=england&type=league` `https://api-football-v1.p.rapidapi.com/v3/leagues?team=85&season=2019` `https://api-football-v1.p.rapidapi.com/v3/leagues?id=61&current=true&type=league`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/leagues'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'country': country,
        'code': code,
        'season': season,
        'team': team,
        'type': type,
        'current': current,
        'search': search,
        'last': last,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_leagues_by_type(id: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                       name: Annotated[Union[str, None], Field(description='The name of the league')] = None,
                       country: Annotated[Union[str, None], Field(description='The country name of the league')] = None,
                       code: Annotated[Union[str, None], Field(description='The Alpha2 code of the country 2 characters Like FR, GB, IT…')] = None,
                       season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2018, 2019 etc... Default: 0')] = None,
                       team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                       type: Annotated[Union[str, None], Field(description='The type of the league Enum: league or cup')] = None,
                       current: Annotated[Union[str, None], Field(description='The state of the league Enum: true or false')] = None,
                       search: Annotated[Union[str, None], Field(description='The name or the country of the league >= 3 characters')] = None,
                       last: Annotated[Union[int, float, None], Field(description='The X last leagues/cups added in the API <= 2 characters Default: 0')] = None) -> dict:
    '''Get the list of available leagues and cups. The league `id` are **unique** in the API and leagues keep it across all `seasons` > Most of the parameters of this endpoint can be used together. **Update Frequency** : This endpoint is updated several times a day. **Recommended Calls** : 1 call per hour. **Use Cases** Allows to retrieve all the seasons available for a league/cup `https://api-football-v1.p.rapidapi.com/v3/leagues?id=39` Get all leagues from one league {name} `https://api-football-v1.p.rapidapi.com/v3/leagues?name=premier league` Get all leagues from one {country} You can find the available {country} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?country=england` Get all leagues from one country {code} (GB, FR, IT etc..) You can find the available country {code} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?code=gb` Get all leagues from one {season} You can find the available {season} by using the endpoint seasons `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019` Get one league from one league {id} & {season} `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&id=39` Get all leagues in which the {team} has played at least one match `https://api-football-v1.p.rapidapi.com/v3/leagues?team=33` Allows you to search for a league in relation to a league {name} or {country} `https://api-football-v1.p.rapidapi.com/v3/leagues?search=premier league` `https://api-football-v1.p.rapidapi.com/v3/leagues?search=England` Get all leagues from one {type} `https://api-football-v1.p.rapidapi.com/v3/leagues?type=league` Get all leagues where the season is in progress or not `https://api-football-v1.p.rapidapi.com/v3/leagues?current=true` Get the last 99 leagues or cups added to the API `https://api-football-v1.p.rapidapi.com/v3/leagues?last=99` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&country=england&type=league` `https://api-football-v1.p.rapidapi.com/v3/leagues?team=85&season=2019` `https://api-football-v1.p.rapidapi.com/v3/leagues?id=61&current=true&type=league`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/leagues'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'country': country,
        'code': code,
        'season': season,
        'team': team,
        'type': type,
        'current': current,
        'search': search,
        'last': last,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_leagues_whose_season_is_running(id: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                                       name: Annotated[Union[str, None], Field(description='The name of the league')] = None,
                                       country: Annotated[Union[str, None], Field(description='The country name of the league')] = None,
                                       code: Annotated[Union[str, None], Field(description='The Alpha2 code of the country 2 characters Like FR, GB, IT…')] = None,
                                       season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2018, 2019 etc... Default: 0')] = None,
                                       team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                                       type: Annotated[Union[str, None], Field(description='The type of the league Enum: league or cup')] = None,
                                       current: Annotated[Union[str, None], Field(description='The state of the league Enum: true or false')] = None,
                                       search: Annotated[Union[str, None], Field(description='The name or the country of the league >= 3 characters')] = None,
                                       last: Annotated[Union[int, float, None], Field(description='The X last leagues/cups added in the API <= 2 characters Default: 0')] = None) -> dict:
    '''Get the list of available leagues and cups. The league `id` are **unique** in the API and leagues keep it across all `seasons` > Most of the parameters of this endpoint can be used together. **Update Frequency** : This endpoint is updated several times a day. **Recommended Calls** : 1 call per hour. **Use Cases** Allows to retrieve all the seasons available for a league/cup `https://api-football-v1.p.rapidapi.com/v3/leagues?id=39` Get all leagues from one league {name} `https://api-football-v1.p.rapidapi.com/v3/leagues?name=premier league` Get all leagues from one {country} You can find the available {country} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?country=england` Get all leagues from one country {code} (GB, FR, IT etc..) You can find the available country {code} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?code=gb` Get all leagues from one {season} You can find the available {season} by using the endpoint seasons `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019` Get one league from one league {id} & {season} `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&id=39` Get all leagues in which the {team} has played at least one match `https://api-football-v1.p.rapidapi.com/v3/leagues?team=33` Allows you to search for a league in relation to a league {name} or {country} `https://api-football-v1.p.rapidapi.com/v3/leagues?search=premier league` `https://api-football-v1.p.rapidapi.com/v3/leagues?search=England` Get all leagues from one {type} `https://api-football-v1.p.rapidapi.com/v3/leagues?type=league` Get all leagues where the season is in progress or not `https://api-football-v1.p.rapidapi.com/v3/leagues?current=true` Get the last 99 leagues or cups added to the API `https://api-football-v1.p.rapidapi.com/v3/leagues?last=99` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&country=england&type=league` `https://api-football-v1.p.rapidapi.com/v3/leagues?team=85&season=2019` `https://api-football-v1.p.rapidapi.com/v3/leagues?id=61&current=true&type=league`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/leagues'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'country': country,
        'code': code,
        'season': season,
        'team': team,
        'type': type,
        'current': current,
        'search': search,
        'last': last,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_bets(id: Annotated[Union[int, float, None], Field(description='The id of the bet Default: 0')] = None,
            search: Annotated[Union[str, None], Field(description='The name of the bet')] = None) -> dict:
    '''Get all available bets. All bets `id` can be used in endpoint odds as filters. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all available bets `https://api-football-v1.p.rapidapi.com/v3/odds/bets` Get bet from one {id} `https://api-football-v1.p.rapidapi.com/v3/odds/bets?id=1` Allows you to search for a bet in relation to a bets {name} `https://api-football-v1.p.rapidapi.com/v3/odds/bets?search=winner`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/odds/bets'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_bookmakers(id: Annotated[Union[int, float, None], Field(description='The id of the bookmaker Default: 0')] = None,
                  search: Annotated[Union[str, None], Field(description='The name of the bookmaker')] = None) -> dict:
    '''Get all available bookmakers. All bookmakers `id` can be used in endpoint odds as filters. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all available bookmakers `https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers` Get bookmaker from one {id} `https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers?id=1` Allows you to search for a bookmaker in relation to a bookmakers {name} `https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers?search=Betfair`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_odds_mapping(page: Annotated[Union[int, float, None], Field(description='Use for the pagination Default: 1 Default: 0')] = None) -> dict:
    '''Get the list of available odds. All fixtures, leagues `id` and `date` can be used in endpoint odds as filters. This endpoint uses a **pagination system**, you can navigate between the different pages thanks to the `page` parameter. > **Pagination** : 100 results per page. **Update Frequency** : This endpoint is updated every day. **Recommended Calls** : 1 call per day.'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/odds/mapping'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_odds_by_date(fixture: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                    league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                    season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020, 2021 ... Default: 0')] = None,
                    date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                    timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                    page: Annotated[Union[int, float, None], Field(description='Use for the pagination Default: 1 Default: 0')] = None,
                    bookmaker: Annotated[Union[int, float, None], Field(description='The id of the bookmaker Default: 0')] = None,
                    bet: Annotated[Union[int, float, None], Field(description='The id of the bet Default: 0')] = None) -> dict:
    '''Get odds from fixtures, leagues or date. This endpoint uses a **pagination system**, you can navigate between the different pages with to the `page` parameter. > **Pagination** : 10 results per page. We provide pre-match odds between 1 and 14 days before the fixture. We keep a 7-days history *(The availability of odds may vary according to the leagues, seasons, fixtures and bookmakers)* **Update Frequency** : This endpoint is updated every 3 hours. **Recommended Calls** : 1 call every 3 hours. **Use Cases** Get all available odds from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/odds?fixture=164327` Get all available odds from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/odds?league=39&season=2019` Get all available odds from one {date} `https://api-football-v1.p.rapidapi.com/v3/odds?date=2020-05-15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/odds?bookmaker=1&bet=4&league=39&season=2019` `https://api-football-v1.p.rapidapi.com/v3/odds?bet=4&fixture=164327` `https://api-football-v1.p.rapidapi.com/v3/odds?bookmaker=1&league=39&season=2019` `https://api-football-v1.p.rapidapi.com/v3/odds?date=2020-05-15&page=2&bet=4`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/odds'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'league': league,
        'season': season,
        'date': date,
        'timezone': timezone,
        'page': page,
        'bookmaker': bookmaker,
        'bet': bet,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_odds_filtered_by_bet_id(fixture: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 568987')] = None,
                               league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                               season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020, 2021 ... Default: 0')] = None,
                               date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                               timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                               page: Annotated[Union[int, float, None], Field(description='Use for the pagination Default: 1 Default: 0')] = None,
                               bookmaker: Annotated[Union[int, float, None], Field(description='The id of the bookmaker Default: 0')] = None,
                               bet: Annotated[Union[int, float, None], Field(description='The id of the bet Default: 1')] = None) -> dict:
    '''Get odds from fixtures, leagues or date. This endpoint uses a **pagination system**, you can navigate between the different pages with to the `page` parameter. > **Pagination** : 10 results per page. We provide pre-match odds between 1 and 14 days before the fixture. We keep a 7-days history *(The availability of odds may vary according to the leagues, seasons, fixtures and bookmakers)* **Update Frequency** : This endpoint is updated every 3 hours. **Recommended Calls** : 1 call every 3 hours. **Use Cases** Get all available odds from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/odds?fixture=164327` Get all available odds from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/odds?league=39&season=2019` Get all available odds from one {date} `https://api-football-v1.p.rapidapi.com/v3/odds?date=2020-05-15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/odds?bookmaker=1&bet=4&league=39&season=2019` `https://api-football-v1.p.rapidapi.com/v3/odds?bet=4&fixture=164327` `https://api-football-v1.p.rapidapi.com/v3/odds?bookmaker=1&league=39&season=2019` `https://api-football-v1.p.rapidapi.com/v3/odds?date=2020-05-15&page=2&bet=4`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/odds'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'league': league,
        'season': season,
        'date': date,
        'timezone': timezone,
        'page': page,
        'bookmaker': bookmaker,
        'bet': bet,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_odds_filtered_by_bookmaker_id(fixture: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 568987')] = None,
                                     league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                                     season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020, 2021 ... Default: 0')] = None,
                                     date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                     timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                                     page: Annotated[Union[int, float, None], Field(description='Use for the pagination Default: 1 Default: 0')] = None,
                                     bookmaker: Annotated[Union[int, float, None], Field(description='The id of the bookmaker Default: 1')] = None,
                                     bet: Annotated[Union[int, float, None], Field(description='The id of the bet Default: 0')] = None) -> dict:
    '''Get odds from fixtures, leagues or date. This endpoint uses a **pagination system**, you can navigate between the different pages with to the `page` parameter. > **Pagination** : 10 results per page. We provide pre-match odds between 1 and 14 days before the fixture. We keep a 7-days history *(The availability of odds may vary according to the leagues, seasons, fixtures and bookmakers)* **Update Frequency** : This endpoint is updated every 3 hours. **Recommended Calls** : 1 call every 3 hours. **Use Cases** Get all available odds from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/odds?fixture=164327` Get all available odds from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/odds?league=39&season=2019` Get all available odds from one {date} `https://api-football-v1.p.rapidapi.com/v3/odds?date=2020-05-15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/odds?bookmaker=1&bet=4&league=39&season=2019` `https://api-football-v1.p.rapidapi.com/v3/odds?bet=4&fixture=164327` `https://api-football-v1.p.rapidapi.com/v3/odds?bookmaker=1&league=39&season=2019` `https://api-football-v1.p.rapidapi.com/v3/odds?date=2020-05-15&page=2&bet=4`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/odds'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'league': league,
        'season': season,
        'date': date,
        'timezone': timezone,
        'page': page,
        'bookmaker': bookmaker,
        'bet': bet,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_odds_by_league_id(fixture: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                         league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 287')] = None,
                         season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020, 2021 ... Default: 2020')] = None,
                         date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                         timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                         page: Annotated[Union[int, float, None], Field(description='Use for the pagination Default: 1 Default: 0')] = None,
                         bookmaker: Annotated[Union[int, float, None], Field(description='The id of the bookmaker Default: 0')] = None,
                         bet: Annotated[Union[int, float, None], Field(description='The id of the bet Default: 0')] = None) -> dict:
    '''Get odds from fixtures, leagues or date. This endpoint uses a **pagination system**, you can navigate between the different pages with to the `page` parameter. > **Pagination** : 10 results per page. We provide pre-match odds between 1 and 14 days before the fixture. We keep a 7-days history *(The availability of odds may vary according to the leagues, seasons, fixtures and bookmakers)* **Update Frequency** : This endpoint is updated every 3 hours. **Recommended Calls** : 1 call every 3 hours. **Use Cases** Get all available odds from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/odds?fixture=164327` Get all available odds from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/odds?league=39&season=2019` Get all available odds from one {date} `https://api-football-v1.p.rapidapi.com/v3/odds?date=2020-05-15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/odds?bookmaker=1&bet=4&league=39&season=2019` `https://api-football-v1.p.rapidapi.com/v3/odds?bet=4&fixture=164327` `https://api-football-v1.p.rapidapi.com/v3/odds?bookmaker=1&league=39&season=2019` `https://api-football-v1.p.rapidapi.com/v3/odds?date=2020-05-15&page=2&bet=4`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/odds'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'league': league,
        'season': season,
        'date': date,
        'timezone': timezone,
        'page': page,
        'bookmaker': bookmaker,
        'bet': bet,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_odds_by_fixture_id(fixture: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 568987')] = None,
                          league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                          season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2020, 2021 ... Default: 0')] = None,
                          date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                          timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                          page: Annotated[Union[int, float, None], Field(description='Use for the pagination Default: 1 Default: 0')] = None,
                          bookmaker: Annotated[Union[int, float, None], Field(description='The id of the bookmaker Default: 0')] = None,
                          bet: Annotated[Union[int, float, None], Field(description='The id of the bet Default: 0')] = None) -> dict:
    '''Get odds from fixtures, leagues or date. This endpoint uses a **pagination system**, you can navigate between the different pages with to the `page` parameter. > **Pagination** : 10 results per page. We provide pre-match odds between 1 and 14 days before the fixture. We keep a 7-days history *(The availability of odds may vary according to the leagues, seasons, fixtures and bookmakers)* **Update Frequency** : This endpoint is updated every 3 hours. **Recommended Calls** : 1 call every 3 hours. **Use Cases** Get all available odds from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/odds?fixture=164327` Get all available odds from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/odds?league=39&season=2019` Get all available odds from one {date} `https://api-football-v1.p.rapidapi.com/v3/odds?date=2020-05-15` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/odds?bookmaker=1&bet=4&league=39&season=2019` `https://api-football-v1.p.rapidapi.com/v3/odds?bet=4&fixture=164327` `https://api-football-v1.p.rapidapi.com/v3/odds?bookmaker=1&league=39&season=2019` `https://api-football-v1.p.rapidapi.com/v3/odds?date=2020-05-15&page=2&bet=4`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/odds'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'league': league,
        'season': season,
        'date': date,
        'timezone': timezone,
        'page': page,
        'bookmaker': bookmaker,
        'bet': bet,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_events(fixture: Annotated[Union[int, float], Field(description='The id of the fixture Default: 215662')],
                       team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                       player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                       type: Annotated[Union[str, None], Field(description='The event type Like Goal, Card ...')] = None) -> dict:
    '''Get the events from a fixture. **Available events** * Goal : Normal Goal, Own Goal, Penalty, Missed Penalty * Card : Yellow Card, Second Yellow card, Red card * Subst : Substitution [1, 2, 3...] * Var : Goal cancelled, Penalty confirmed **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the fixtures in progress otherwise 1 call per day. You can also retrieve all the events of the fixtures in progress thanks to the endpoint `fixtures?live=all` > Here is an example of what can be achieved ![demo-events](https://www.api-football.com/public/img/demo/demo-events.png) **Use Cases** Get all available events from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662` Get all available events from one {fixture} & {team} `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&team=463` Get all available events from one {fixture} & {player} `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&player=35845` Get all available events from one {fixture} & {type} `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&type=card` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&player=35845&type=card` `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&team=463&type=goal&player=35845`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/events'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'team': team,
        'player': player,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_events_filtered_by_player_id(fixture: Annotated[Union[int, float], Field(description='The id of the fixture Default: 215662')],
                                             team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                                             player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 6126')] = None,
                                             type: Annotated[Union[str, None], Field(description='The event type Like Goal, Card ...')] = None) -> dict:
    '''Get the events from a fixture. **Available events** * Goal : Normal Goal, Own Goal, Penalty, Missed Penalty * Card : Yellow Card, Second Yellow card, Red card * Subst : Substitution [1, 2, 3...] * Var : Goal cancelled, Penalty confirmed **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the fixtures in progress otherwise 1 call per day. You can also retrieve all the events of the fixtures in progress thanks to the endpoint `fixtures?live=all` > Here is an example of what can be achieved ![demo-events](https://www.api-football.com/public/img/demo/demo-events.png) **Use Cases** Get all available events from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662` Get all available events from one {fixture} & {team} `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&team=463` Get all available events from one {fixture} & {player} `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&player=35845` Get all available events from one {fixture} & {type} `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&type=card` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&player=35845&type=card` `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&team=463&type=goal&player=35845`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/events'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'team': team,
        'player': player,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_events_filtered_by_team_id(fixture: Annotated[Union[int, float], Field(description='The id of the fixture Default: 215662')],
                                           team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 463')] = None,
                                           player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                                           type: Annotated[Union[str, None], Field(description='The event type Like Goal, Card ...')] = None) -> dict:
    '''Get the events from a fixture. **Available events** * Goal : Normal Goal, Own Goal, Penalty, Missed Penalty * Card : Yellow Card, Second Yellow card, Red card * Subst : Substitution [1, 2, 3...] * Var : Goal cancelled, Penalty confirmed **Update Frequency** : This endpoint is updated every 15 seconds. **Recommended Calls** : 1 call per minute for the fixtures in progress otherwise 1 call per day. You can also retrieve all the events of the fixtures in progress thanks to the endpoint `fixtures?live=all` > Here is an example of what can be achieved ![demo-events](https://www.api-football.com/public/img/demo/demo-events.png) **Use Cases** Get all available events from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662` Get all available events from one {fixture} & {team} `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&team=463` Get all available events from one {fixture} & {player} `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&player=35845` Get all available events from one {fixture} & {type} `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&type=card` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&player=35845&type=card` `https://api-football-v1.p.rapidapi.com/v3/fixtures/events?fixture=215662&team=463&type=goal&player=35845`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/events'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'team': team,
        'player': player,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_standings_by_league_id(season: Annotated[Union[int, float], Field(description='The season of the league 4 characters Like 2020, 2021 ... Default: 2020')],
                              league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 39')] = None,
                              team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None) -> dict:
    '''Get the standings for a league or a team. Return a table of one or more rankings according to the league / cup. Some competitions have several rankings in a year, group phase, opening ranking, closing ranking etc… > Most of the parameters of this endpoint can be used together. **Update Frequency** : This endpoint is updated every hour. **Recommended Calls** : 1 call per hour for the leagues or teams who have at least one fixture in progress otherwise 1 call per day. **Use Cases** Get all Standings from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/standings?league=39&season=2019` Get all Standings from one {league} & {season} & {team} `https://api-football-v1.p.rapidapi.com/v3/standings?league=39&team=33&season=2019` Get all Standings from one {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/standings?team=33&season=2019`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/standings'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'season': season,
        'league': league,
        'team': team,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_standings_by_team_id(season: Annotated[Union[int, float], Field(description='The season of the league 4 characters Like 2020, 2021 ... Default: 2020')],
                            league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                            team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 33')] = None) -> dict:
    '''Get the standings for a league or a team. Return a table of one or more rankings according to the league / cup. Some competitions have several rankings in a year, group phase, opening ranking, closing ranking etc… > Most of the parameters of this endpoint can be used together. **Update Frequency** : This endpoint is updated every hour. **Recommended Calls** : 1 call per hour for the leagues or teams who have at least one fixture in progress otherwise 1 call per day. **Use Cases** Get all Standings from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/standings?league=39&season=2019` Get all Standings from one {league} & {season} & {team} `https://api-football-v1.p.rapidapi.com/v3/standings?league=39&team=33&season=2019` Get all Standings from one {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/standings?team=33&season=2019`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/standings'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'season': season,
        'league': league,
        'team': team,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_statistics(fixture: Annotated[Union[int, float], Field(description='The id of the fixture Default: 215662')],
                           team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                           type: Annotated[Union[str, None], Field(description='The type of statistics Like Fouls, Offsides...')] = None) -> dict:
    '''Get the statistics for one fixture. **Available statistics** * Shots on Goal * Shots off Goal * Shots insidebox * Shots outsidebox * Total Shots * Blocked Shots * Fouls * Corner Kicks * Offsides * Ball Possession * Yellow Cards * Red Cards * Goalkeeper Saves * Total passes * Passes accurate * Passes % **Update Frequency** : This endpoint is updated every minute. **Recommended Calls** : 1 call every minute for the teams or fixtures who have at least one fixture in progress otherwise 1 call per day. > Here is an example of what can be achieved ![demo-statistics](https://www.api-football.com/public/img/demo/demo-statistics.png) **Use Cases** Get all available statistics from one {fixture} `https://v3.football.api-sports.io/fixtures/statistics?fixture=215662` Get all available statistics from one {fixture} & {type} `https://v3.football.api-sports.io/fixtures/statistics?fixture=215662&type=Total Shots` Get all available statistics from one {fixture} & {team} `v3.football.api-sports.io/fixtures/statistics?fixture=215662&team=463`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/statistics'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'team': team,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_statistics_filtered_by_type(fixture: Annotated[Union[int, float], Field(description='The id of the fixture Default: 215662')],
                                            team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                                            type: Annotated[Union[str, None], Field(description='The type of statistics Like Fouls, Offsides...')] = None) -> dict:
    '''Get the statistics for one fixture. **Available statistics** * Shots on Goal * Shots off Goal * Shots insidebox * Shots outsidebox * Total Shots * Blocked Shots * Fouls * Corner Kicks * Offsides * Ball Possession * Yellow Cards * Red Cards * Goalkeeper Saves * Total passes * Passes accurate * Passes % **Update Frequency** : This endpoint is updated every minute. **Recommended Calls** : 1 call every minute for the teams or fixtures who have at least one fixture in progress otherwise 1 call per day. > Here is an example of what can be achieved ![demo-statistics](https://www.api-football.com/public/img/demo/demo-statistics.png) **Use Cases** Get all available statistics from one {fixture} `https://v3.football.api-sports.io/fixtures/statistics?fixture=215662` Get all available statistics from one {fixture} & {type} `https://v3.football.api-sports.io/fixtures/statistics?fixture=215662&type=Total Shots` Get all available statistics from one {fixture} & {team} `v3.football.api-sports.io/fixtures/statistics?fixture=215662&team=463`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/statistics'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'team': team,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_statistics_filtered_by_team_id(fixture: Annotated[Union[int, float], Field(description='The id of the fixture Default: 215662')],
                                               team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 463')] = None,
                                               type: Annotated[Union[str, None], Field(description='The type of statistics Like Fouls, Offsides...')] = None) -> dict:
    '''Get the statistics for one fixture. **Available statistics** * Shots on Goal * Shots off Goal * Shots insidebox * Shots outsidebox * Total Shots * Blocked Shots * Fouls * Corner Kicks * Offsides * Ball Possession * Yellow Cards * Red Cards * Goalkeeper Saves * Total passes * Passes accurate * Passes % **Update Frequency** : This endpoint is updated every minute. **Recommended Calls** : 1 call every minute for the teams or fixtures who have at least one fixture in progress otherwise 1 call per day. > Here is an example of what can be achieved ![demo-statistics](https://www.api-football.com/public/img/demo/demo-statistics.png) **Use Cases** Get all available statistics from one {fixture} `https://v3.football.api-sports.io/fixtures/statistics?fixture=215662` Get all available statistics from one {fixture} & {type} `https://v3.football.api-sports.io/fixtures/statistics?fixture=215662&type=Total Shots` Get all available statistics from one {fixture} & {team} `v3.football.api-sports.io/fixtures/statistics?fixture=215662&team=463`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/statistics'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'team': team,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_players_statistics_by_player_id(id: Annotated[Union[int, float, None], Field(description='The id of the player Default: 276')] = None,
                                       team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                                       league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                                       season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Requires the fields Id, League or Team Default: 2020')] = None,
                                       search: Annotated[Union[str, None], Field(description='The name of the player >= 4 characters Requires the fields League or Team')] = None,
                                       page: Annotated[Union[int, float, None], Field(description='Use for the pagination Default: 1 Default: 0')] = None) -> dict:
    '''Get players statistics. The players `id` are unique in the API and players keep it among all the teams they have been in The statistics are calculated according to the team `id`, league `id` and `season`. You can find the available `seasons` by using the endpoint players seasons. This endpoint uses a **pagination system**, you can navigate between the different pages thanks to the `page` parameter. > **Pagination** : 20 results per page. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all players statistics from one player {id} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?id=19088&season=2018` Get all players statistics from one {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&team=33` `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&team=33&page=2` Get all players statistics from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61` `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61&page=4` Get all players statistics from one {league}, {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61&team=33` `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61&team=33&page=5` Allows you to search for a player in relation to a player {name} `https://api-football-v1.p.rapidapi.com/v3/players?team=85&search=cavani` `https://api-football-v1.p.rapidapi.com/v3/players?league=61&search=cavani` `https://api-football-v1.p.rapidapi.com/v3/players?team=85&search=cavani&season=2018`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/players'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'team': team,
        'league': league,
        'season': season,
        'search': search,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_players_seasons() -> dict:
    '''Get all available seasons for players statistics. **Update Frequency** : This endpoint is updated every day. **Recommended Calls** : 1 call per day.'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/players/seasons'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_players_statistics_by_fixture_id(fixture: Annotated[Union[int, float], Field(description='The id of the fixture Default: 169080')],
                                        team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None) -> dict:
    '''Get the players statistics from one fixture. **Update Frequency** : This endpoint is updated every minute. **Recommended Calls** : 1 call every minute for the fixtures in progress otherwise 1 call per day. **Use Cases** Get all available players statistics from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/fixtures/players?fixture=169080` Get all available players statistics from one {fixture} & {team} `https://api-football-v1.p.rapidapi.com/v3/fixtures/players?fixture=169080&team=2284`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/players'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'team': team,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_players_statistics_by_league_id(id: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                                       team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                                       league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 39')] = None,
                                       season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Requires the fields Id, League or Team Default: 2020')] = None,
                                       search: Annotated[Union[str, None], Field(description='The name of the player >= 4 characters Requires the fields League or Team')] = None,
                                       page: Annotated[Union[int, float, None], Field(description='Use for the pagination Default: 1 Default: 0')] = None) -> dict:
    '''Get players statistics. The players `id` are unique in the API and players keep it among all the teams they have been in The statistics are calculated according to the team `id`, league `id` and `season`. You can find the available `seasons` by using the endpoint players seasons. This endpoint uses a **pagination system**, you can navigate between the different pages thanks to the `page` parameter. > **Pagination** : 20 results per page. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all players statistics from one player {id} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?id=19088&season=2018` Get all players statistics from one {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&team=33` `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&team=33&page=2` Get all players statistics from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61` `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61&page=4` Get all players statistics from one {league}, {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61&team=33` `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61&team=33&page=5` Allows you to search for a player in relation to a player {name} `https://api-football-v1.p.rapidapi.com/v3/players?team=85&search=cavani` `https://api-football-v1.p.rapidapi.com/v3/players?league=61&search=cavani` `https://api-football-v1.p.rapidapi.com/v3/players?team=85&search=cavani&season=2018`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/players'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'team': team,
        'league': league,
        'season': season,
        'search': search,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_players_statistics_by_team_id(id: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                                     team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 33')] = None,
                                     league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                                     season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Requires the fields Id, League or Team Default: 2020')] = None,
                                     search: Annotated[Union[str, None], Field(description='The name of the player >= 4 characters Requires the fields League or Team')] = None,
                                     page: Annotated[Union[int, float, None], Field(description='Use for the pagination Default: 1 Default: 0')] = None) -> dict:
    '''Get players statistics. The players `id` are unique in the API and players keep it among all the teams they have been in The statistics are calculated according to the team `id`, league `id` and `season`. You can find the available `seasons` by using the endpoint players seasons. This endpoint uses a **pagination system**, you can navigate between the different pages thanks to the `page` parameter. > **Pagination** : 20 results per page. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all players statistics from one player {id} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?id=19088&season=2018` Get all players statistics from one {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&team=33` `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&team=33&page=2` Get all players statistics from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61` `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61&page=4` Get all players statistics from one {league}, {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61&team=33` `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61&team=33&page=5` Allows you to search for a player in relation to a player {name} `https://api-football-v1.p.rapidapi.com/v3/players?team=85&search=cavani` `https://api-football-v1.p.rapidapi.com/v3/players?league=61&search=cavani` `https://api-football-v1.p.rapidapi.com/v3/players?team=85&search=cavani&season=2018`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/players'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'team': team,
        'league': league,
        'season': season,
        'search': search,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_players_seasons_by_player_id(player: Annotated[Union[int, float, None], Field(description='Default: 276')] = None) -> dict:
    '''Get all available seasons for players statistics filtered by a player {id}. **Update Frequency** : This endpoint is updated every day. **Recommended Calls** : 1 call per day. **Use Cases** Get all seasons available for a player {id} `https://api-football-v1.p.rapidapi.com/v3/players/seasons?player=276`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/players/seasons'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_players_squads(team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 33')] = None,
                      player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None) -> dict:
    '''Return the current squad of a team when the `team` parameter is used. When the `player` parameter is used the endpoint returns the set of teams associated with the player. > The response format is the same regardless of the parameter sent. **This endpoint requires at least one parameter.** **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per week. **Use Cases** Get all players from one {team} `https://api-football-v1.p.rapidapi.com/v3/players/squads?team=33` Get all teams from one {player} `https://api-football-v1.p.rapidapi.com/v3/players/squads?player=276`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/players/squads'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team': team,
        'player': player,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_players_profiles(player: Annotated[Union[int, float, None], Field(description='The id of the player')] = None,
                        search: Annotated[Union[str, None], Field(description='')] = None,
                        page: Annotated[Union[int, float, None], Field(description='Default: 1 Use for the pagination')] = None) -> dict:
    '''Returns the list of all available players. It is possible to call this endpoint without parameters, but you will need to use the **pagination** to get all available players. To get the photo of a player you have to call the following url: `https://media.api-sports.io/football/players/{player_id}.png` This endpoint uses a **pagination system**, you can navigate between the different pages with to the `page` parameter. > **Pagination** : 250 results per page. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per week. // Get data from one {player} get("https://v3.football.api-sports.io/players/profiles?player=276"); // Allows you to search for a player in relation to a player {lastname} get("https://v3.football.api-sports.io/players/profiles?search=ney"); // Get all available Players (limited to 250 results, use the pagination for next ones) get("https://v3.football.api-sports.io/players/profiles"); get("https://v3.football.api-sports.io/players/profiles?page=2"); get("https://v3.football.api-sports.io/players/profiles?page=3");'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/players/profiles'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
        'search': search,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_players_teams(player: Annotated[Union[int, float], Field(description='The id of the player Default: 276')]) -> dict:
    '''Returns the list of teams and seasons in which the player played during his career. **This endpoint requires at least one parameter.** **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per week.'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/players/teams'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_lineups(fixture: Annotated[Union[int, float], Field(description='The id of the fixture Default: 215662')],
                        team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                        player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                        type: Annotated[Union[str, None], Field(description='The Lineup type Like Formation, Substitutes...')] = None) -> dict:
    '''Get the lineups for a fixture. **Available datas** * Formation * Coach * Start XI * Substitutes > Lineups are available between 20 and 40 minutes before the fixture. **Players' positions on the grid** **X** = row and **Y** = column (X:Y) Line 1 **X** being the one of the goal and then for each line this number is incremented. The column **Y** will go from left to right, and incremented for each player of the line. `As a new feature, some irregularities may occur, do not hesitate to report them on our public Roadmap` **Update Frequency** : This endpoint is updated every 15 minutes. **Recommended Calls** : 1 call every 15 minutes for the fixtures in progress otherwise 1 call per day. > Here are several examples of what can be done ![demo-lineups](https://www.api-football.com/public/img/demo/demo-lineups-1.jpg) ![demo-lineups](https://www.api-football.com/public/img/demo/demo-lineups.png) **Use Cases** Get all available lineups from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups?fixture=215662` Get all available lineups from one {fixture} & {team} `https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups?fixture=215662&team=463` Get all available lineups from one {fixture} & {player} `https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups?fixture=215662&player=35845` Get all available lineups from one {fixture} & {type} `https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups?fixture=215662&type=startXI` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups?fixture=215662&player=35845&type=startXI` `https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups?fixture=215662&team=463&type=startXI&player=35845`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'team': team,
        'player': player,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_fixtures_lineups_filtered_by_team_id(fixture: Annotated[Union[int, float], Field(description='The id of the fixture Default: 215662')],
                                            team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 463')] = None,
                                            player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                                            type: Annotated[Union[str, None], Field(description='The Lineup type Like Formation, Substitutes...')] = None) -> dict:
    '''Get the lineups for a fixture. **Available datas** * Formation * Coach * Start XI * Substitutes > Lineups are available between 20 and 40 minutes before the fixture. **Players' positions on the grid** **X** = row and **Y** = column (X:Y) Line 1 **X** being the one of the goal and then for each line this number is incremented. The column **Y** will go from left to right, and incremented for each player of the line. `As a new feature, some irregularities may occur, do not hesitate to report them on our public Roadmap` **Update Frequency** : This endpoint is updated every 15 minutes. **Recommended Calls** : 1 call every 15 minutes for the fixtures in progress otherwise 1 call per day. > Here are several examples of what can be done ![demo-lineups](https://www.api-football.com/public/img/demo/demo-lineups-1.jpg) ![demo-lineups](https://www.api-football.com/public/img/demo/demo-lineups.png) **Use Cases** Get all available lineups from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups?fixture=215662` Get all available lineups from one {fixture} & {team} `https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups?fixture=215662&team=463` Get all available lineups from one {fixture} & {player} `https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups?fixture=215662&player=35845` Get all available lineups from one {fixture} & {type} `https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups?fixture=215662&type=startXI` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups?fixture=215662&player=35845&type=startXI` `https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups?fixture=215662&team=463&type=startXI&player=35845`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'team': team,
        'player': player,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_trophies_by_player_id(player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 276')] = None,
                             coach: Annotated[Union[int, float, None], Field(description='The id of the coach Default: 0')] = None,
                             players: Annotated[Union[str, None], Field(description='Maximum of 20 players ids id-id-id')] = None,
                             coachs: Annotated[Union[str, None], Field(description='Maximum of 20 coachs ids id-id-id')] = None) -> dict:
    '''Get all available trophies for a player or a coach. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all trophies from one {player} `https://api-football-v1.p.rapidapi.com/v3/trophies?player=276` Get all trophies from several {player} ids `https://api-football-v1.p.rapidapi.com/v3/trophies?players=276-278` Get all trophies from one {coach} `https://api-football-v1.p.rapidapi.com/v3/trophies?coach=2` Get all trophies from several {coachs} ids `https://api-football-v1.p.rapidapi.com/v3/trophies?coachs=2-6`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/trophies'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
        'coach': coach,
        'players': players,
        'coachs': coachs,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_trophies_by_coach_id(player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                            coach: Annotated[Union[int, float, None], Field(description='The id of the coach Default: 276')] = None,
                            players: Annotated[Union[str, None], Field(description='Maximum of 20 players ids id-id-id')] = None,
                            coachs: Annotated[Union[str, None], Field(description='Maximum of 20 coachs ids id-id-id')] = None) -> dict:
    '''Get all available trophies for a player or a coach. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all trophies from one {player} `https://api-football-v1.p.rapidapi.com/v3/trophies?player=276` Get all trophies from several {player} ids `https://api-football-v1.p.rapidapi.com/v3/trophies?players=276-278` Get all trophies from one {coach} `https://api-football-v1.p.rapidapi.com/v3/trophies?coach=2` Get all trophies from several {coachs} ids `https://api-football-v1.p.rapidapi.com/v3/trophies?coachs=2-6`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/trophies'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
        'coach': coach,
        'players': players,
        'coachs': coachs,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_trophies_by_players_ids(player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                               coach: Annotated[Union[int, float, None], Field(description='The id of the coach Default: 0')] = None,
                               players: Annotated[Union[str, None], Field(description='Maximum of 20 players ids id-id-id')] = None,
                               coachs: Annotated[Union[str, None], Field(description='Maximum of 20 coachs ids id-id-id')] = None) -> dict:
    '''Get all available trophies for a player or a coach. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all trophies from one {player} `https://api-football-v1.p.rapidapi.com/v3/trophies?player=276` Get all trophies from several {player} ids `https://api-football-v1.p.rapidapi.com/v3/trophies?players=276-278` Get all trophies from one {coach} `https://api-football-v1.p.rapidapi.com/v3/trophies?coach=2` Get all trophies from several {coachs} ids `https://api-football-v1.p.rapidapi.com/v3/trophies?coachs=2-6`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/trophies'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
        'coach': coach,
        'players': players,
        'coachs': coachs,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_trophies_by_coachs_ids(player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                              coach: Annotated[Union[int, float, None], Field(description='The id of the coach Default: 0')] = None,
                              players: Annotated[Union[str, None], Field(description='Maximum of 20 players ids id-id-id')] = None,
                              coachs: Annotated[Union[str, None], Field(description='Maximum of 20 coachs ids id-id-id')] = None) -> dict:
    '''Get all available trophies for a player or a coach. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all trophies from one {player} `https://api-football-v1.p.rapidapi.com/v3/trophies?player=276` Get all trophies from several {player} ids `https://api-football-v1.p.rapidapi.com/v3/trophies?players=276-278` Get all trophies from one {coach} `https://api-football-v1.p.rapidapi.com/v3/trophies?coach=2` Get all trophies from several {coachs} ids `https://api-football-v1.p.rapidapi.com/v3/trophies?coachs=2-6`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/trophies'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
        'coach': coach,
        'players': players,
        'coachs': coachs,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_odds(fixture: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
            league: Annotated[Union[int, float, None], Field(description='The id of the league In this endpoint the \\\\\\\\\\\\\\"season\\\\\\\\\\\\\\" parameter is not needed Default: 0')] = None,
            bet: Annotated[Union[int, float, None], Field(description='The id of the bet Default: 0')] = None) -> dict:
    '''This endpoint returns in-play odds for fixtures in progress. Fixtures are added between 15 and 5 minutes before the start of the fixture. Once the fixture is over they are removed from the endpoint between 5 and 20 minutes. **No history is stored**. So fixtures that are about to start, fixtures in progress and fixtures that have just ended are available in this endpoint. **Update Frequency** : This endpoint is updated every 5 seconds.`*` `* This value can change in the range of 5 to 60 seconds` **INFORMATIONS ABOUT STATUS** ``` "status": { "stopped": false, // True if the fixture is stopped by the referee for X reason "blocked": false, // True if bets on this fixture are temporarily blocked "finished": false // True if the fixture has not started or if it is finished }, ``` **INFORMATIONS ABOUT VALUES** When several identical values exist for the same bet the `main` field is set to `True` for the bet being considered, the others will have the value `False`. The `main` field will be set to `True` only if several identical values exist for the same bet. When a value is unique for a bet the `main` value will always be `False` or `null`. **Example below** : ``` "id": 36, "name": "Over/Under Line", "values": [ { "value": "Over", "odd": "1.975", "handicap": "2", "main": true, // Bet to consider "suspended": false // True if this bet is temporarily suspended }, { "value": "Over", "odd": "3.45", "handicap": "2", "main": false, // Bet to no consider "suspended": false }, ]'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/odds/live'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fixture': fixture,
        'league': league,
        'bet': bet,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_odds_bets() -> dict:
    '''Get all available bets for in-play odds. All bets `id` can be used in endpoint `odds/live` as filters, **but are not compatible with endpoint `odds` for pre-match odds**. **Update Frequency** : This endpoint is updated every 60 seconds.'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/odds/live/bets'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_sidelined_by_player_id(player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 276')] = None,
                              coach: Annotated[Union[int, float, None], Field(description='The id of the coach Default: 0')] = None,
                              players: Annotated[Union[str, None], Field(description='Maximum of 20 players ids id-id-id')] = None,
                              coachs: Annotated[Union[str, None], Field(description='Maximum of 20 coachs ids id-id-id')] = None) -> dict:
    '''Get all available sidelined for a player or a coach. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all from one {player} `https://api-football-v1.p.rapidapi.com/v3/sidelined?player=276` Get all from several {player} ids `https://api-football-v1.p.rapidapi.com/v3/sidelined?players=276-278` Get all from one {coach} `https://api-football-v1.p.rapidapi.com/v3/sidelined?coach=2` Get all from several {coachs} ids `https://api-football-v1.p.rapidapi.com/v3/sidelined?coachs=2-6`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/sidelined'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
        'coach': coach,
        'players': players,
        'coachs': coachs,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_sidelined_by_coach_id(player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                             coach: Annotated[Union[int, float, None], Field(description='The id of the coach Default: 276')] = None,
                             players: Annotated[Union[str, None], Field(description='Maximum of 20 players ids id-id-id')] = None,
                             coachs: Annotated[Union[str, None], Field(description='Maximum of 20 coachs ids id-id-id')] = None) -> dict:
    '''Get all available sidelined for a player or a coach. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all from one {player} `https://api-football-v1.p.rapidapi.com/v3/sidelined?player=276` Get all from several {player} ids `https://api-football-v1.p.rapidapi.com/v3/sidelined?players=276-278` Get all from one {coach} `https://api-football-v1.p.rapidapi.com/v3/sidelined?coach=2` Get all from several {coachs} ids `https://api-football-v1.p.rapidapi.com/v3/sidelined?coachs=2-6`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/sidelined'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
        'coach': coach,
        'players': players,
        'coachs': coachs,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_sidelined_by_players_ids(player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                                coach: Annotated[Union[int, float, None], Field(description='The id of the coach Default: 0')] = None,
                                players: Annotated[Union[str, None], Field(description='Maximum of 20 players ids id-id-id')] = None,
                                coachs: Annotated[Union[str, None], Field(description='Maximum of 20 coachs ids id-id-id')] = None) -> dict:
    '''Get all available sidelined for a player or a coach. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all from one {player} `https://api-football-v1.p.rapidapi.com/v3/sidelined?player=276` Get all from several {player} ids `https://api-football-v1.p.rapidapi.com/v3/sidelined?players=276-278` Get all from one {coach} `https://api-football-v1.p.rapidapi.com/v3/sidelined?coach=2` Get all from several {coachs} ids `https://api-football-v1.p.rapidapi.com/v3/sidelined?coachs=2-6`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/sidelined'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
        'coach': coach,
        'players': players,
        'coachs': coachs,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_sidelined_by_coachs_ids(player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                               coach: Annotated[Union[int, float, None], Field(description='The id of the coach Default: 0')] = None,
                               players: Annotated[Union[str, None], Field(description='Maximum of 20 players ids id-id-id')] = None,
                               coachs: Annotated[Union[str, None], Field(description='Maximum of 20 coachs ids id-id-id')] = None) -> dict:
    '''Get all available sidelined for a player or a coach. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all from one {player} `https://api-football-v1.p.rapidapi.com/v3/sidelined?player=276` Get all from several {player} ids `https://api-football-v1.p.rapidapi.com/v3/sidelined?players=276-278` Get all from one {coach} `https://api-football-v1.p.rapidapi.com/v3/sidelined?coach=2` Get all from several {coachs} ids `https://api-football-v1.p.rapidapi.com/v3/sidelined?coachs=2-6`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/sidelined'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
        'coach': coach,
        'players': players,
        'coachs': coachs,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_transfers_by_player_id(player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 35845')] = None,
                              team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None) -> dict:
    '''Get all available transfers for players and teams **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all transfers from one {player} `https://api-football-v1.p.rapidapi.com/v3/transfers?player=35845` Get all transfers from one {team} `https://api-football-v1.p.rapidapi.com/v3/transfers?team=463`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/transfers'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
        'team': team,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_transfers_by_team_id(player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                            team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 33')] = None) -> dict:
    '''Get all available transfers for players and teams **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all transfers from one {player} `https://api-football-v1.p.rapidapi.com/v3/transfers?player=35845` Get all transfers from one {team} `https://api-football-v1.p.rapidapi.com/v3/transfers?team=463`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/transfers'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'player': player,
        'team': team,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_search_team(id: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                   name: Annotated[Union[str, None], Field(description='The name of the team')] = None,
                   league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                   season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2019, 2020, 2021 ... Default: 0')] = None,
                   country: Annotated[Union[str, None], Field(description='The country name of the team')] = None,
                   search: Annotated[Union[str, None], Field(description='The name or the country name of the team >= 3 characters')] = None) -> dict:
    '''Get the list of available teams. The team `id` are **unique** in the API and teams keep it among all the leagues/cups in which they participate. > All the parameters of this endpoint can be used together. **This endpoint requires at least one parameter.** **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get one team from one team {id} `https://api-football-v1.p.rapidapi.com/v3/teams?id=33` Get one team from one team {name} `https://api-football-v1.p.rapidapi.com/v3/teams?name=manchester united` Get all teams from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/teams?league=39&season=2019` Get teams from one team {country} `https://api-football-v1.p.rapidapi.com/v3/teams?country=england` Allows you to search for a team in relation to a team {name} or {country} `https://api-football-v1.p.rapidapi.com/v3/teams?search=manches` `https://api-football-v1.p.rapidapi.com/v3/teams?search=England`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/teams'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'league': league,
        'season': season,
        'country': country,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_search_country(name: Annotated[Union[str, None], Field(description='The name of the country')] = None,
                      code: Annotated[Union[str, None], Field(description='The Alpha2 code of the country 2 characters Like FR, GB, IT…')] = None,
                      search: Annotated[Union[str, None], Field(description='The name of the country >= 3 characters')] = None) -> dict:
    '''Get the list of available countries. The `name` and `code` fields can be used in other endpoints as filters. > Examples available in Request samples "Use Cases". All the parameters of this endpoint can be used together. **Update Frequency** : This endpoint is updated each time a new league from a country not covered by the API is added. **Recommended Calls** : 1 call per day. **Use Cases** Get all available countries across all {seasons} and competitions `https://api-football-v1.p.rapidapi.com/v3/countries` Get all available countries from one country {name} `https://api-football-v1.p.rapidapi.com/v3/countries?name=england` Get all available countries from one country {code} `https://api-football-v1.p.rapidapi.com/v3/countries?code=fr` Allows you to search for a countries in relation to a country {name} `https://api-football-v1.p.rapidapi.com/v3/countries?search=engl`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/countries'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
        'code': code,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_search_league(id: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                     name: Annotated[Union[str, None], Field(description='The name of the league')] = None,
                     country: Annotated[Union[str, None], Field(description='The country name of the league')] = None,
                     code: Annotated[Union[str, None], Field(description='The Alpha2 code of the country 2 characters Like FR, GB, IT…')] = None,
                     season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Like 2018, 2019 etc... Default: 0')] = None,
                     team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                     type: Annotated[Union[str, None], Field(description='The type of the league Enum: league or cup')] = None,
                     current: Annotated[Union[str, None], Field(description='The state of the league Enum: true or false')] = None,
                     search: Annotated[Union[str, None], Field(description='The name or the country of the league >= 3 characters')] = None,
                     last: Annotated[Union[int, float, None], Field(description='The X last leagues/cups added in the API <= 2 characters Default: 0')] = None) -> dict:
    '''Get the list of available leagues and cups. The league `id` are **unique** in the API and leagues keep it across all `seasons` > Most of the parameters of this endpoint can be used together. **Update Frequency** : This endpoint is updated several times a day. **Recommended Calls** : 1 call per hour. **Use Cases** Allows to retrieve all the seasons available for a league/cup `https://api-football-v1.p.rapidapi.com/v3/leagues?id=39` Get all leagues from one league {name} `https://api-football-v1.p.rapidapi.com/v3/leagues?name=premier league` Get all leagues from one {country} You can find the available {country} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?country=england` Get all leagues from one country {code} (GB, FR, IT etc..) You can find the available country {code} by using the endpoint country `https://api-football-v1.p.rapidapi.com/v3/leagues?code=gb` Get all leagues from one {season} You can find the available {season} by using the endpoint seasons `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019` Get one league from one league {id} & {season} `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&id=39` Get all leagues in which the {team} has played at least one match `https://api-football-v1.p.rapidapi.com/v3/leagues?team=33` Allows you to search for a league in relation to a league {name} or {country} `https://api-football-v1.p.rapidapi.com/v3/leagues?search=premier league` `https://api-football-v1.p.rapidapi.com/v3/leagues?search=England` Get all leagues from one {type} `https://api-football-v1.p.rapidapi.com/v3/leagues?type=league` Get all leagues where the season is in progress or not `https://api-football-v1.p.rapidapi.com/v3/leagues?current=true` Get the last 99 leagues or cups added to the API `https://api-football-v1.p.rapidapi.com/v3/leagues?last=99` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/leagues?season=2019&country=england&type=league` `https://api-football-v1.p.rapidapi.com/v3/leagues?team=85&season=2019` `https://api-football-v1.p.rapidapi.com/v3/leagues?id=61&current=true&type=league`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/leagues'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'country': country,
        'code': code,
        'season': season,
        'team': team,
        'type': type,
        'current': current,
        'search': search,
        'last': last,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_search_player(id: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                     team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                     league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 61')] = None,
                     season: Annotated[Union[int, float, None], Field(description='The season of the league 4 characters Requires the fields Id, League or Team Default: 0')] = None,
                     search: Annotated[Union[str, None], Field(description='The name of the player >= 4 characters Requires the fields League or Team')] = None,
                     page: Annotated[Union[int, float, None], Field(description='Use for the pagination Default: 1 Default: 0')] = None) -> dict:
    '''Get players statistics. The players `id` are unique in the API and players keep it among all the teams they have been in The statistics are calculated according to the team `id`, league `id` and `season`. You can find the available `seasons` by using the endpoint players seasons. This endpoint uses a **pagination system**, you can navigate between the different pages thanks to the `page` parameter. > **Pagination** : 20 results per page. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all players statistics from one player {id} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?id=19088&season=2018` Get all players statistics from one {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&team=33` `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&team=33&page=2` Get all players statistics from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61` `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61&page=4` Get all players statistics from one {league}, {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61&team=33` `https://api-football-v1.p.rapidapi.com/v3/players?season=2018&league=61&team=33&page=5` Allows you to search for a player in relation to a player {name} `https://api-football-v1.p.rapidapi.com/v3/players?team=85&search=cavani` `https://api-football-v1.p.rapidapi.com/v3/players?league=61&search=cavani` `https://api-football-v1.p.rapidapi.com/v3/players?team=85&search=cavani&season=2018`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/players'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'team': team,
        'league': league,
        'season': season,
        'search': search,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_search_coach(id: Annotated[Union[int, float, None], Field(description='The id of the coach Default: 0')] = None,
                    team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                    search: Annotated[Union[str, None], Field(description='The name of the coach >= 3 characters')] = None) -> dict:
    '''Get all the information about the coachs and their careers. **Update Frequency** : This endpoint is updated every day. **Recommended Calls** : 1 call per day. **Use Cases** Get coachs from one coach {id} `https://api-football-v1.p.rapidapi.com/v3/coachs?id=1` Get coachs from one {team} `https://api-football-v1.p.rapidapi.com/v3/coachs?team=33` Allows you to search for a coach in relation to a coach {name} `https://api-football-v1.p.rapidapi.com/v3/coachs?search=Klopp`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/coachs'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'team': team,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_search_venue(id: Annotated[Union[int, float, None], Field(description='The id of the venue Default: 0')] = None,
                    name: Annotated[Union[str, None], Field(description='The name of the venue')] = None,
                    city: Annotated[Union[str, None], Field(description='The city of the venue')] = None,
                    country: Annotated[Union[str, None], Field(description='The country name of the venue')] = None,
                    search: Annotated[Union[str, None], Field(description='The name, city or the country of the venue >= 3 characters')] = None) -> dict:
    '''Get the list of available venues. The venue `id` are **unique** in the API. > All the parameters of this endpoint can be used together. **This endpoint requires at least one parameter.** **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get one venue from venue {id} `https://api-football-v1.p.rapidapi.com/v3/venues?id=556` Get one venue from venue {name} `https://api-football-v1.p.rapidapi.com/v3/venues?name=Old Trafford` Get all venues from {city} `https://api-football-v1.p.rapidapi.com/v3/venues?city=manchester` Get venues from {country} `https://api-football-v1.p.rapidapi.com/v3/venues?country=england` Allows you to search for a venues in relation to a venue {name}, {city} or {country} `https://api-football-v1.p.rapidapi.com/v3/venues?search=trafford` `https://api-football-v1.p.rapidapi.com/v3/venues?search=manches` `https://api-football-v1.p.rapidapi.com/v3/venues?search=England`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/venues'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'city': city,
        'country': country,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_search_bet(id: Annotated[Union[int, float, None], Field(description='The id of the bet Default: 0')] = None,
                  search: Annotated[Union[str, None], Field(description='The name of the bet')] = None) -> dict:
    '''Get all available bets. All bets `id` can be used in endpoint odds as filters. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all available bets `https://api-football-v1.p.rapidapi.com/v3/odds/bets` Get bet from one {id} `https://api-football-v1.p.rapidapi.com/v3/odds/bets?id=1` Allows you to search for a bet in relation to a bets {name} `https://api-football-v1.p.rapidapi.com/v3/odds/bets?search=winner`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/odds/bets'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_search_bookmaker(id: Annotated[Union[int, float, None], Field(description='The id of the bookmaker Default: 0')] = None,
                        search: Annotated[Union[str, None], Field(description='The name of the bookmaker')] = None) -> dict:
    '''Get all available bookmakers. All bookmakers `id` can be used in endpoint odds as filters. **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get all available bookmakers `https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers` Get bookmaker from one {id} `https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers?id=1` Allows you to search for a bookmaker in relation to a bookmakers {name} `https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers?search=Betfair`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_top_scorers(league: Annotated[Union[int, float], Field(description='The id of the league Default: 39')],
                   season: Annotated[Union[int, float], Field(description='The season of the league 4 characters Like 2020, 2021 ... Default: 2020')]) -> dict:
    '''Get the 20 best players for a league or cup. **How it is calculated:** * 1 : The player that has scored the higher number of goals * 2 : The player that has scored the fewer number of penalties * 3 : The player that has delivered the higher number of goal assists * 4 : The player that scored their goals in the higher number of matches * 5 : The player that played the fewer minutes * 6 : The player that plays for the team placed higher on the table * 7 : The player that received the fewer number of red cards * 8 : The player that received the fewer number of yellow cards **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day.'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/players/topscorers'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_top_assists(league: Annotated[Union[int, float], Field(description='The id of the league Default: 39')],
                   season: Annotated[Union[int, float], Field(description='The season of the league 4 characters Like 2020, 2021 ... Default: 2020')]) -> dict:
    '''Get the 20 best players assists for a league or cup. **How it is calculated:** * 1 : The player that has delivered the higher number of goal assists * 2 : The player that has scored the higher number of goals * 3 : The player that has scored the fewer number of penalties * 4 : The player that assists in the higher number of matches * 5 : The player that played the fewer minutes * 6 : The player that received the fewer number of red cards * 7 : The player that received the fewer number of yellow cards **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day.'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/players/topassists'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_top_red_cards(league: Annotated[Union[int, float], Field(description='The id of the league Default: 39')],
                     season: Annotated[Union[int, float], Field(description='The season of the league 4 characters Like 2020, 2021 ... Default: 2020')]) -> dict:
    '''Get the 20 players with the most red cards for a league or cup. **How it is calculated:** * 1 : The player that received the higher number of red cards * 2 : The player that received the higher number of yellow cards * 3 : The player that assists in the higher number of matches * 4 : The player that played the fewer minutes **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day.'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/players/topredcards'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_top_yellow_cards(league: Annotated[Union[int, float], Field(description='The id of the league Default: 39')],
                        season: Annotated[Union[int, float], Field(description='The season of the league 4 characters Like 2020, 2021 ... Default: 2020')]) -> dict:
    '''Get the 20 players with the most yellow cards for a league or cup. **How it is calculated:** * 1 : The player that received the higher number of yellow cards * 2 : The player that received the higher number of red cards * 3 : The player that assists in the higher number of matches * 4 : The player that played the fewer minutes **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day.'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/players/topyellowcards'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_venues_by_venue_id(id: Annotated[Union[int, float, None], Field(description='The id of the venue Default: 556')] = None,
                          name: Annotated[Union[str, None], Field(description='The name of the venue')] = None,
                          city: Annotated[Union[str, None], Field(description='The city of the venue')] = None,
                          country: Annotated[Union[str, None], Field(description='The country name of the venue')] = None,
                          search: Annotated[Union[str, None], Field(description='The name, city or the country of the venue >= 3 characters')] = None) -> dict:
    '''Get the list of available venues. The venue `id` are **unique** in the API. > All the parameters of this endpoint can be used together. **This endpoint requires at least one parameter.** **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get one venue from venue {id} `https://api-football-v1.p.rapidapi.com/v3/venues?id=556` Get one venue from venue {name} `https://api-football-v1.p.rapidapi.com/v3/venues?name=Old Trafford` Get all venues from {city} `https://api-football-v1.p.rapidapi.com/v3/venues?city=manchester` Get venues from {country} `https://api-football-v1.p.rapidapi.com/v3/venues?country=england` Allows you to search for a venues in relation to a venue {name}, {city} or {country} `https://api-football-v1.p.rapidapi.com/v3/venues?search=trafford` `https://api-football-v1.p.rapidapi.com/v3/venues?search=manches` `https://api-football-v1.p.rapidapi.com/v3/venues?search=England`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/venues'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'city': city,
        'country': country,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_venues_by_country_name(id: Annotated[Union[int, float, None], Field(description='The id of the venue Default: 0')] = None,
                              name: Annotated[Union[str, None], Field(description='The name of the venue')] = None,
                              city: Annotated[Union[str, None], Field(description='The city of the venue')] = None,
                              country: Annotated[Union[str, None], Field(description='The country name of the venue')] = None,
                              search: Annotated[Union[str, None], Field(description='The name, city or the country of the venue >= 3 characters')] = None) -> dict:
    '''Get the list of available venues. The venue `id` are **unique** in the API. > All the parameters of this endpoint can be used together. **This endpoint requires at least one parameter.** **Update Frequency** : This endpoint is updated several times a week. **Recommended Calls** : 1 call per day. **Use Cases** Get one venue from venue {id} `https://api-football-v1.p.rapidapi.com/v3/venues?id=556` Get one venue from venue {name} `https://api-football-v1.p.rapidapi.com/v3/venues?name=Old Trafford` Get all venues from {city} `https://api-football-v1.p.rapidapi.com/v3/venues?city=manchester` Get venues from {country} `https://api-football-v1.p.rapidapi.com/v3/venues?country=england` Allows you to search for a venues in relation to a venue {name}, {city} or {country} `https://api-football-v1.p.rapidapi.com/v3/venues?search=trafford` `https://api-football-v1.p.rapidapi.com/v3/venues?search=manches` `https://api-football-v1.p.rapidapi.com/v3/venues?search=England`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/venues'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'name': name,
        'city': city,
        'country': country,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_injuries_by_team_id_and_season(league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                                      season: Annotated[Union[int, float, None], Field(description='The season of the league, required with league, team and player parameters Default: 2020')] = None,
                                      fixture: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                                      team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 33')] = None,
                                      player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                                      date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                      timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None) -> dict:
    '''Get the list of players not participating in the fixtures for various reasons such as `suspended`, `injured` for example. Being a new endpoint, the data is only available from April 2021. **There are two types:** * `Missing Fixture` : The player will not play the fixture. * `Questionable` : The information is not yet 100% sure, the player may eventually play the fixture. > Examples available in Request samples "Use Cases". > All the parameters of this endpoint can be used together. **This endpoint requires at least one parameter.** **Update Frequency** : This endpoint is updated every 4 hours. **Recommended Calls** : 1 call per day. **Use Cases** Get all available injuries from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020` Get all available injuries from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/injuries?fixture=686314` Get all available injuries from one {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?team=85&season=2020` Get all available injuries from one {player} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?player=865&season=2020` Get all available injuries from one {date} `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020&team=85` `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020&player=865` `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07&timezone=Europe/London&team=85` `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07&league=61`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/injuries'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'fixture': fixture,
        'team': team,
        'player': player,
        'date': date,
        'timezone': timezone,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_injuries_by_player_id_and_season(league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                                        season: Annotated[Union[int, float, None], Field(description='The season of the league, required with league, team and player parameters Default: 2020')] = None,
                                        fixture: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                                        team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                                        player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 276')] = None,
                                        date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                        timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None) -> dict:
    '''Get the list of players not participating in the fixtures for various reasons such as `suspended`, `injured` for example. Being a new endpoint, the data is only available from April 2021. **There are two types:** * `Missing Fixture` : The player will not play the fixture. * `Questionable` : The information is not yet 100% sure, the player may eventually play the fixture. > Examples available in Request samples "Use Cases". > All the parameters of this endpoint can be used together. **This endpoint requires at least one parameter.** **Update Frequency** : This endpoint is updated every 4 hours. **Recommended Calls** : 1 call per day. **Use Cases** Get all available injuries from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020` Get all available injuries from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/injuries?fixture=686314` Get all available injuries from one {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?team=85&season=2020` Get all available injuries from one {player} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?player=865&season=2020` Get all available injuries from one {date} `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020&team=85` `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020&player=865` `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07&timezone=Europe/London&team=85` `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07&league=61`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/injuries'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'fixture': fixture,
        'team': team,
        'player': player,
        'date': date,
        'timezone': timezone,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_injuries_by_fixture_id(league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                              season: Annotated[Union[int, float, None], Field(description='The season of the league, required with league, team and player parameters Default: 0')] = None,
                              fixture: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 686308')] = None,
                              team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                              player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                              date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                              timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None) -> dict:
    '''Get the list of players not participating in the fixtures for various reasons such as `suspended`, `injured` for example. Being a new endpoint, the data is only available from April 2021. **There are two types:** * `Missing Fixture` : The player will not play the fixture. * `Questionable` : The information is not yet 100% sure, the player may eventually play the fixture. > Examples available in Request samples "Use Cases". > All the parameters of this endpoint can be used together. **This endpoint requires at least one parameter.** **Update Frequency** : This endpoint is updated every 4 hours. **Recommended Calls** : 1 call per day. **Use Cases** Get all available injuries from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020` Get all available injuries from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/injuries?fixture=686314` Get all available injuries from one {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?team=85&season=2020` Get all available injuries from one {player} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?player=865&season=2020` Get all available injuries from one {date} `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020&team=85` `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020&player=865` `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07&timezone=Europe/London&team=85` `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07&league=61`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/injuries'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'fixture': fixture,
        'team': team,
        'player': player,
        'date': date,
        'timezone': timezone,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_injuries_by_league_id_and_season(league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 61')] = None,
                                        season: Annotated[Union[int, float, None], Field(description='The season of the league, required with league, team and player parameters Default: 2020')] = None,
                                        fixture: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                                        team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                                        player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                                        date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                        timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None) -> dict:
    '''Get the list of players not participating in the fixtures for various reasons such as `suspended`, `injured` for example. Being a new endpoint, the data is only available from April 2021. **There are two types:** * `Missing Fixture` : The player will not play the fixture. * `Questionable` : The information is not yet 100% sure, the player may eventually play the fixture. > Examples available in Request samples "Use Cases". > All the parameters of this endpoint can be used together. **This endpoint requires at least one parameter.** **Update Frequency** : This endpoint is updated every 4 hours. **Recommended Calls** : 1 call per day. **Use Cases** Get all available injuries from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020` Get all available injuries from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/injuries?fixture=686314` Get all available injuries from one {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?team=85&season=2020` Get all available injuries from one {player} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?player=865&season=2020` Get all available injuries from one {date} `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020&team=85` `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020&player=865` `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07&timezone=Europe/London&team=85` `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07&league=61`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/injuries'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'fixture': fixture,
        'team': team,
        'player': player,
        'date': date,
        'timezone': timezone,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_injuries_by_date(league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                        season: Annotated[Union[int, float, None], Field(description='The season of the league, required with league, team and player parameters Default: 0')] = None,
                        fixture: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                        team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                        player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                        date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                        timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None) -> dict:
    '''Get the list of players not participating in the fixtures for various reasons such as `suspended`, `injured` for example. Being a new endpoint, the data is only available from April 2021. **There are two types:** * `Missing Fixture` : The player will not play the fixture. * `Questionable` : The information is not yet 100% sure, the player may eventually play the fixture. > Examples available in Request samples "Use Cases". > All the parameters of this endpoint can be used together. **This endpoint requires at least one parameter.** **Update Frequency** : This endpoint is updated every 4 hours. **Recommended Calls** : 1 call per day. **Use Cases** Get all available injuries from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020` Get all available injuries from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/injuries?fixture=686314` Get all available injuries from one {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?team=85&season=2020` Get all available injuries from one {player} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?player=865&season=2020` Get all available injuries from one {date} `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020&team=85` `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020&player=865` `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07&timezone=Europe/London&team=85` `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07&league=61`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/injuries'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'fixture': fixture,
        'team': team,
        'player': player,
        'date': date,
        'timezone': timezone,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_injuries_by_multiple_fixtures_ids(league: Annotated[Union[int, float, None], Field(description='The id of the league Default: 0')] = None,
                                         season: Annotated[Union[int, float, None], Field(description='The season of the league, required with league, team and player parameters Default: 0')] = None,
                                         fixture: Annotated[Union[int, float, None], Field(description='The id of the fixture Default: 0')] = None,
                                         team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                                         player: Annotated[Union[int, float, None], Field(description='The id of the player Default: 0')] = None,
                                         date: Annotated[Union[str, datetime, None], Field(description=' Example: Date (yyyy-mm-dd)')] = None,
                                         timezone: Annotated[Union[str, None], Field(description='A valid timezone from the endpoint Timezone')] = None,
                                         ids: Annotated[Union[str, None], Field(description='Maximum of 20 fixtures ids Value: "id-id-id" One or more fixture ids')] = None) -> dict:
    '''Get the list of players not participating in the fixtures for various reasons such as `suspended`, `injured` for example. Being a new endpoint, the data is only available from April 2021. **There are two types:** * `Missing Fixture` : The player will not play the fixture. * `Questionable` : The information is not yet 100% sure, the player may eventually play the fixture. > Examples available in Request samples "Use Cases". > All the parameters of this endpoint can be used together. **This endpoint requires at least one parameter.** **Update Frequency** : This endpoint is updated every 4 hours. **Recommended Calls** : 1 call per day. **Use Cases** Get all available injuries from one {league} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020` Get all available injuries from one {fixture} `https://api-football-v1.p.rapidapi.com/v3/injuries?fixture=686314` // Get all available injuries from severals fixtures {ids} get("https://v3.football.api-sports.io/injuries?ids=686314-686315-686316-686317-686318-686319-686320"); Get all available injuries from one {team} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?team=85&season=2020` Get all available injuries from one {player} & {season} `https://api-football-v1.p.rapidapi.com/v3/injuries?player=865&season=2020` Get all available injuries from one {date} `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07` It’s possible to make requests by mixing the available parameters `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020&team=85` `https://api-football-v1.p.rapidapi.com/v3/injuries?league=2&season=2020&player=865` `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07&timezone=Europe/London&team=85` `https://api-football-v1.p.rapidapi.com/v3/injuries?date=2021-04-07&league=61`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/injuries'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'fixture': fixture,
        'team': team,
        'player': player,
        'date': date,
        'timezone': timezone,
        'ids': ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_coachs_by_team_id(id: Annotated[Union[int, float, None], Field(description='The id of the coach Default: 0')] = None,
                         team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 33')] = None,
                         search: Annotated[Union[str, None], Field(description='The name of the coach >= 3 characters')] = None) -> dict:
    '''Get all the information about the coachs and their careers. **Update Frequency** : This endpoint is updated every day. **Recommended Calls** : 1 call per day. **Use Cases** Get coachs from one coach {id} `https://api-football-v1.p.rapidapi.com/v3/coachs?id=1` Get coachs from one {team} `https://api-football-v1.p.rapidapi.com/v3/coachs?team=33` Allows you to search for a coach in relation to a coach {name} `https://api-football-v1.p.rapidapi.com/v3/coachs?search=Klopp`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/coachs'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'team': team,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_coachs_by_coach_id(id: Annotated[Union[int, float, None], Field(description='The id of the coach Default: 276')] = None,
                          team: Annotated[Union[int, float, None], Field(description='The id of the team Default: 0')] = None,
                          search: Annotated[Union[str, None], Field(description='The name of the coach >= 3 characters')] = None) -> dict:
    '''Get all the information about the coachs and their careers. **Update Frequency** : This endpoint is updated every day. **Recommended Calls** : 1 call per day. **Use Cases** Get coachs from one coach {id} `https://api-football-v1.p.rapidapi.com/v3/coachs?id=1` Get coachs from one {team} `https://api-football-v1.p.rapidapi.com/v3/coachs?team=33` Allows you to search for a coach in relation to a coach {name} `https://api-football-v1.p.rapidapi.com/v3/coachs?search=Klopp`'''
    url = 'https://api-football-v1.p.rapidapi.com/v3/coachs'
    headers = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'team': team,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")