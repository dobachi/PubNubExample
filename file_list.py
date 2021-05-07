import os
import inspect
import pprint

from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

CHANNEL = "file_test"

pnconfig = PNConfiguration()
pnconfig.publish_key = os.environ["PUBNUB_PUBKEY"]
pnconfig.subscribe_key = os.environ["PUBNUB_SUBKEY"]
pnconfig.uuid = "serverUUID-SUB"

pubnub = PubNub(pnconfig)

envelop = pubnub.list_files().channel(CHANNEL).sync()

pprint.pprint(envelop.result.data)
