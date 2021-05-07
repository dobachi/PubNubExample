import os
from PIL import Image

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconfig = PNConfiguration()
pnconfig.publish_key = os.environ["PUBNUB_PUBKEY"]
pnconfig.subscribe_key = os.environ["PUBNUB_SUBKEY"]
pnconfig.uuid = "serverUUID-PUB"

pubnub = PubNub(pnconfig)

with open("send_file/moon.jpg", "rb") as fd:
    img = Image.open(fd)
    print("# Image info")
    print("size: {}".format(img.size))
    print("mode: {}".format(img.mode))
    print("# Send a file")
    envelope = pubnub.send_file().\
        channel("file_test").\
        file_name("moon.jpg").\
        message({"test_message": "test"}).\
        should_store(True).\
        ttl(222).\
        file_object(img.tobytes()).sync()

    print("file_id: {}".format(envelope.result.file_id))
    print("name: {}".format(envelope.result.name))
