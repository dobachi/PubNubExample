import os
import inspect
from PIL import Image

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

CHANNEL = "file_test"
FILENAME = "moon.jpg"

pnconfig = PNConfiguration()
pnconfig.publish_key = os.environ["PUBNUB_PUBKEY"]
pnconfig.subscribe_key = os.environ["PUBNUB_SUBKEY"]
pnconfig.uuid = "serverUUID-SUB"

pubnub = PubNub(pnconfig)

file_list = pubnub.list_files().channel(CHANNEL).sync()
file_id = file_list.result.data[0]["id"]

download_envelope = pubnub.download_file().\
    channel(CHANNEL).\
    file_id(file_id).\
    file_name(FILENAME).sync()

img = Image.frombytes(data=download_envelope.result.data, size=(499, 346), mode="RGB")
img.show()
