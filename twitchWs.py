from twitchAPI.helper import first
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticationStorageHelper
from twitchAPI.object.eventsub import ChannelPointsCustomRewardRedemptionAddEvent
from twitchAPI.eventsub.websocket import EventSubWebsocket
from twitchAPI.type import AuthScope

from pranks import invertScreen, blockInput

APP_ID        = '5zgc2191pzj62feufvjls7s3kds4qh'
APP_SECRET    = '55vote4rlp7r0symljg18gy388pymn'
TARGET_SCOPES = [AuthScope.CHANNEL_READ_REDEMPTIONS]


async def on_redeem(data: ChannelPointsCustomRewardRedemptionAddEvent):
    if data.event.reward.title == "Перевернуть экран":
        await invertScreen()
    elif data.event.reward.title == "Отключить клавиатуру/мышь":
        await blockInput()


async def run():
    twitch = await Twitch(APP_ID, APP_SECRET)
    helper = UserAuthenticationStorageHelper(twitch, TARGET_SCOPES)
    await helper.bind()


    user = await first(twitch.get_users())

    eventsub = EventSubWebsocket(twitch)
    eventsub.start()

    await eventsub.listen_channel_points_custom_reward_redemption_add(user.id, on_redeem)
    try:
        input('press Enter to shut down...')
    except KeyboardInterrupt:
        pass
    finally:
        await eventsub.stop()
        await twitch.close()

