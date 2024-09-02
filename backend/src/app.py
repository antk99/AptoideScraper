import falcon.asgi

from resources.aptoide import AptoideResource

# Create the Falcon app
app = falcon.asgi.App(cors_enable=True)

# Add the Aptoide resource
aptoide = AptoideResource()
app.add_route('/api/aptoide', aptoide)