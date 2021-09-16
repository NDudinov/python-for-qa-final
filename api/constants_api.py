import enum


class Type(enum.Enum):
    Science_Fiction = "Science"
    Satire = "Satire"
    Drama = "Drama"
    Action_and_Adventure = "Adventure"
    Romance = "Romance"


class HttpCodes(enum.IntEnum):
    ok = 200
    not_found = 404
    bad_request = 400


local_url = 'http://127.0.0.1:5000/v1/books/'


