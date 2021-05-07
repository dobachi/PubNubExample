import os
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

ENTRY = "Earth"
CHANNEL = "the_guide"
the_update = None

pnconfig = PNConfiguration()
pnconfig.publish_key = os.environ["PUBNUB_PUBKEY"]
pnconfig.subscribe_key = os.environ["PUBNUB_SUBKEY"]
pnconfig.uuid = "serverUUID-PUB"

pubnub = PubNub(pnconfig)

print("*****************************************")
print("* Submit updates to The Guide for Earth *")
print("*     Enter 42 to exit this process     *")
print("*****************************************")

while the_update != "42":
    print
    the_update = input("Enter an update for Earth: ")
    the_message = {"entry": ENTRY, "update": the_update}
    envelope = pubnub.publish().channel(CHANNEL).message(the_message).sync()

    if envelope.status.is_error():
        print("[PUBLISH: fail]")
        print("error: %s" % status.error)
    else:
        print("[PUBLISH: sent]")
        print("timetoken: %s" % envelope.result.timetoken)

