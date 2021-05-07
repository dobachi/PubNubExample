import os

from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

ENTRY = "Earth"
CHANNEL = "the_guide"

pnconfig = PNConfiguration()
pnconfig.publish_key = os.environ["PUBNUB_PUBKEY"]
pnconfig.subscribe_key = os.environ["PUBNUB_SUBKEY"]
pnconfig.uuid = "serverUUID-SUB"

pubnub = PubNub(pnconfig)


class MySubscribeCallback(SubscribeCallback):
  def presence(self, pubnub, event):
    print("[PRESENCE: {}]".format(event.event))
    print("uuid: {}, channel: {}".format(event.uuid, event.channel))

  def status(self, pubnub, event):
    if event.category == PNStatusCategory.PNConnectedCategory:
      print("[STATUS: PNConnectedCategory]")
      print("connected to channels: {}".format(event.affected_channels))

  def message(self, pubnub, event):
    print("[MESSAGE received]")

    if event.message["update"] == "42":
      print("The publisher has ended the session.")
      os._exit(0)
    else:
      print("{}: {}".format(event.message["entry"], event.message["update"]))

pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels(CHANNEL).with_presence().execute()

print("***************************************************")
print("* Waiting for updates to The Guide about {}... *".format(ENTRY))
print("***************************************************")

