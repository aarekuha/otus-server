from enum import IntEnum


class Status(IntEnum):
    OK = 200
    FORBIDDEN = 403
    NOT_FOUND = 404
    NOT_ALLOWED = 405
