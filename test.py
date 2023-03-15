# -*- coding: utf-8 -*-
from py.Twitch.api import Helix


api = Helix(
    # app_id
    "bimzrzt2lbjmdhb9zkurs6fycsot5u",
    # app_secret
    "20pq3ea1ab01keq5jh7f83a48vwqmf",
    # user_token
    "nemsygeqt47p16l7xg80hqg2tvqj27"
)
user_id = api.users.get_user(login = "30_old_man_dev").id

all_followed_users = api.users.get_users([
    channel.broadcaster_id
    for channel in api.channels.get_all_followed_channels(user_id)
])
# print(all_followed_users)

# ## analytics
# extension_analytics = api.analytics.get_extension_analytics()
# print(extension_analytics)
# game_analytics = api.analytics.get_game_analytics()
# print(game_analytics)

# ## channels
# followed_channels = api.channels.get_followed_channels(user_id)
# print(followed_channels)
# all_followed_channels = api.channels.get_all_followed_channels(user_id)
# print(all_followed_channels)

# ## streams
# stream = api.streams.get_stream(user_id)
# print(stream)
# streams = api.streams.get_streams()
# print(streams)

# ## users
# # get users(multiple)
# users = api.users.get_users(login = [ "30_old_man_dev" ])
# print(users)
# # get user(single)
# user = api.users.get_user(login = "30_old_man_dev")
# print(user)
# # get banned users
# banned_users = api.users.get_banned_users(broadcaster_id = "30_old_man_dev")
# print(banned_users)
