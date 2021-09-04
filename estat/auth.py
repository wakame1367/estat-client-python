
import os
from exceptions import InvalidAppId


ENV_KEY = 'ESTAT_APP_ID'


def find_app_id() -> str:
    app_id = os.getenv(ENV_KEY)
    if app_id is None:
        raise InvalidAppId('No App id provided')
    return app_id