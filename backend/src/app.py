import falcon.asgi

from resources.aptoide import AptoideResource

# Create the Falcon app
app = falcon.asgi.App(cors_enable=True)

# Add the Aptoide resource
aptoide = AptoideResource()
app.add_route('/api/aptoide', aptoide)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)