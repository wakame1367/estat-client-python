from urllib.parse import urljoin

ESTAT_BASE_URL = 'http://api.e-stat.go.jp'
API_VERSION = '3.0'
BASE_PATH = f'/rest/{API_VERSION}/app/'
BASE_URL = urljoin(ESTAT_BASE_URL, BASE_PATH)