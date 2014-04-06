instagram_client_key = 'f4c597a88f114c0ba8eb949d54336a58'
instagram_client_secret = 'c4b0f208cda64720b534fc14b126007b'

api = InstagramAPI(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
popular_media = api.media_popular(count=20)
for media in popular_media:
    print media.images['standard_resolution'].url


api.create_subscription(object='location', object_id='1257285', aspect='media', callback_url='http://mydomain.com/hook/instagram')
# Subscribe to all media in a geographic area
api.create_subscription(object='geography', lat=35.657872, lng=139.70232, radius=1000, aspect='media', callback_url='http://mydomain.com/hook/instagram')