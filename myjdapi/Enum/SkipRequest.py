from enum import Enum


class SkipRequest(Enum):

    SINGLE = 1
    BLOCK_HOSTER = 2
    BLOCK_ALL_CAPTCHAS = 3
    BLOCK_PACKAGE = 4
    REFRESH = 5
    STOP_CURRENT_ACTION = 6
    TIMEOUT = 7
