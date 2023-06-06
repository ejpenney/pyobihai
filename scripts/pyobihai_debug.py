"""Retrieve PyObihai files."""

import logging
import os
from urllib.parse import urljoin

import requests

# Update these:
USERNAME = "admin"
PASSWORD = "admin"
HOST = "http://<TODO>"

# You shouldn't need to touch any of this:
DEFAULT_STATUS_PATH = "DI_S_.xml"
DEFAULT_LINE_PATH = "PI_FXS_1_Stats.xml"
# DEFAULT_CALL_STATUS_PATH = "callstatus.htm"

LOGGER = logging.getLogger(__name__)


def _get_request(api_url: str) -> str:
    """Get a URL from the Obihai."""

    url = urljoin(HOST, api_url)
    try:
        response = requests.get(
            url,
            auth=requests.auth.HTTPDigestAuth(USERNAME, PASSWORD),
            timeout=2,
        )
    except requests.RequestException as exc:
        LOGGER.error(exc)

    return response.content.decode()


def get_xml(xml_name: str) -> None:
    """Write an XML from Obihai."""

    filename = os.path.join(os.path.dirname(__file__), xml_name)
    with open(filename, "w", encoding="utf8") as xml_fh:
        xml_fh.write(_get_request(xml_name))


def main():
    """Entry point."""
    get_xml(DEFAULT_STATUS_PATH)
    get_xml(DEFAULT_LINE_PATH)


if __name__ == "__main__":
    main()
