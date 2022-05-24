"""
In this module you should store all system entites, like:
- static dropdown values
- queue names
- ws events
- etc
"""

CONNECTED_LOG_STRING = 'Received: connect_response {"data":"Connected","count":0}'


class WsEvents:
    SOME_SERVER_PUSH_EVENT = 'some_server_push_event'
    GET_CAPITAL = 'get_capital'
    GET_COUNTRY = 'get_capital'
