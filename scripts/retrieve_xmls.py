"""Looking for Obihai stuff."""

import os
import time
from urllib.parse import urljoin

import requests

USERNAME = "admin"
PASSWORD = "admin"
HOST = "192.168.86.39"

# List from: https://github.com/whee/dumpobi
DOCUMENTS = [
    # "favicon.ico",
    "VS_1_VP_1_.xml",
    # "listexpander.js",
    # "green.png",
    "VS_1_CODEC_2_.xml",
    "VS_1_X_STAR_2_.xml",
    "VS_1_VP_1_L_2_R_.xml",
    "VS_1_.xml",
    # "backup.xml",
    # "index.htm",
    # "HIDDEN.xml",
    "VS_1_VP_1_L_1_.xml",
    "VS_1_VP_1_SIP_.xml",
    # "left.htm",
    # "obihai-logo.png",
    "DI_S_.xml",
    # "expanded.gif",
    "DM_S_.xml",
    "SPEEDDIAL_.xml",
    "VS_1_VP_1_L_2_.xml",
    # "default.xsl",
    "VS_1_VP_2_.xml",
    "VS_1_VP_2_T_.xml",
    # "header_bg.jpg",
    # "submit.htm",
    "SetupWizard.xml",
    "VS_1_X_FXS_1_.xml",
    # "style.css",
    "DM_MISC_.xml",
    "VS_1_VP_1_T_.xml",
    "VS_1_VP_2_RTP_.xml",
    # "caution.png",
    "VS_1_X_STAR_1_.xml",
    "VS_1_CODEC_1_.xml",
    # "upload.jpg",
    # "listexpander.css",
    # "menu-obi100.htm",
    # "menu.htm",
    "VS_1_VP_1_RTP_.xml",
    "VS_1_VP_1_L_1_R_.xml",
    # "q.gif",
    # "rowcolors.js",
    "VS_1_X_AA_1_.xml",
    # "collapsed.gif",
    "VS_1_X_P2P_1_.xml",
    "DI_NS_.xml",
    # "rebootconfig.htm",
    "VS_1_VP_1_L_1_Stats.xml",
    "VS_1_VP_2_SIP_.xml",
    "VS_1_X_FXO_1_.xml",
    "PI_FXS_1_Stats.xml",
    "DIGITMAPS_.xml",
    "VS_1_X_GW_.xml",
]

def _get_request(api_url: str):
    """Get a URL from the Obihai."""

    url = urljoin(f"http://{HOST}", api_url)
    try:
        response = requests.get(
            url,
            auth=requests.auth.HTTPDigestAuth(USERNAME, PASSWORD),
            timeout=2,
        )
        if response.status_code == 200:
            return response.content.decode()
    except requests.RequestException as exc:
        print(f"ERROR: {exc}")

    return False


def get_all_xmls(output_dir: str):
    """Downloads an XML from the Obihai."""
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    for doc in DOCUMENTS:
        print(f"Processing {doc}")
        with open(os.path.join(output_dir, doc), "w",  encoding="utf8") as xml_fh:
            result = False
            for _ in range(5):
                result = _get_request(doc)

                if result:
                    print("SUCCESS!")
                    xml_fh.write(result)
                    if DOCUMENTS[-1] != doc:
                        # This isn't the last doc, wait before diving into the next one
                        time.sleep(10)
                    break
                else:
                    # Attempt failed, sleep before trying again
                    time.sleep(10)

            if not result:
                print("FAILURE!")


def main():
    """Entry point."""
    get_all_xmls("on_hook")
    input("Press Enter to continue...")
    get_all_xmls("outgoing")
    input("Press Enter to continue...")
    get_all_xmls("incoming")


if __name__ == "__main__":
    main()
