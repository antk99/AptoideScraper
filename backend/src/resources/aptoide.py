import falcon
import requests
from src.validators.scrapers import validate_aptoide_url
from src.webscrapers.aptoide.scraper import AptoideScraper

API_ERROR_RESPONSES: dict[str, tuple[str, dict[str, str]]] = {
    'missing_url': (falcon.HTTP_400, {'error': '"url" query parameter is required.'}),
    'invalid_url': (falcon.HTTP_400, {'error': 'Invalid Aptoide URL.'}),
    'not_found': (falcon.HTTP_404, {'error': 'App not found.'}),
    'server_error': (falcon.HTTP_500, {'error': 'Something went wrong.'}),
}

class AptoideResource:
    def __init__(self) -> None:
        self.scraper: AptoideScraper = AptoideScraper() # Initialize the AptoideScraper

    async def on_get(self, req: falcon.Request, res: falcon.Response) -> None:
        try:
            url = req.get_param('url')
            if url is None:
                res.status, res.media = API_ERROR_RESPONSES['missing_url']
                return
            url = url.strip()
            if not validate_aptoide_url(url):
                res.status, res.media = API_ERROR_RESPONSES['invalid_url']
                return

            response = AptoideScraper.query(url)
            if response is None:
                res.status, res.media = API_ERROR_RESPONSES['server_error']
                return
            elif response.status_code == 404:
                res.status, res.media = API_ERROR_RESPONSES['not_found']
                return

            data = self.scraper.get_info(response.content)
            if data is None:
                res.status, res.media = API_ERROR_RESPONSES['server_error']
                return
            
            res.status = falcon.HTTP_200
            res.media = data

        except requests.exceptions.SSLError as e:
            # SSL certificate error occurs when an invalid language is used in the URL
            res.status, res.media = API_ERROR_RESPONSES['invalid_url']

        except requests.exceptions.RequestException as e:
            # Any other requests exception
            res.status, res.media = API_ERROR_RESPONSES['server_error']

        except Exception:
            # Any other exception
            res.status, res.media = API_ERROR_RESPONSES['server_error']
