import json

USERS = {}


def getUserInfo(userID: str) -> list:
    if userID not in USERS:
        USERS[userID] = [
            'фабричная',  # Home Station
            'выхино',     # Work Station
            20,           # From Home To Train
            60,           # From Work To Train
            4,            # Count Of Items
        ]
    return USERS[userID]


def editUserInfo(userID: str, index: int, value):
    USERS[userID][index] = value


def getStations():
    with open('stations.json', 'r', encoding='utf-8') as f:
        stations = json.loads(f.read())
        return stations


def getStationsCodes(forth, back):
    stations = getStations()
    return stations[forth], stations[back]