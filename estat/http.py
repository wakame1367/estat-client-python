import logging
from __version__ import __version__


LOGGER = logging.getLogger(__name__)


class BaseSession():
    @staticmethod
    def _get_user_agent():
        return 'estat-client-python/' + __version__

    @staticmethod
    def _log_request(request):
        LOGGER.info(f'{request.method} {request.url} - Sent')

    @staticmethod
    def _log_response(response):
        request = response.request
        LOGGER.info(
            f'{request.method} {request.url} - '
            f'Status {response.status_code}')