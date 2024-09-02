import requests
import json
from lxml import html, etree
import os

DEFAULT_XPATHS_FILE_PATH: str = os.path.join(os.path.dirname(__file__), 'xpaths.json')

class AptoideScraper:
    """
    A class to scrape app information from the Aptoide website.
    """
    
    def __init__(self, xpaths_file_path: str = DEFAULT_XPATHS_FILE_PATH) -> None:
        """
        Initialize the Aptoide scraper with the xpaths file.

        Args:
            xpaths_file (str): The path to the xpaths file. Default is the xpaths.json file in the same directory.
        """
        try:   
            with open(xpaths_file_path, 'r') as f:
                self.xpaths: dict[str, str] = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError('Xpaths file not found for Aptoide scraper')
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON in xpaths file for Aptoide scraper')
        except Exception as e:
            raise Exception(f'Error loading xpaths for Aptoide scraper: {e}')
        
    @staticmethod
    def query(url: str) -> requests.Response:
        """
        Query the Aptoide URL and return the response.

        Args:
            url (str): The Aptoide URL

        Returns:
            requests.Response: The response object

        Raises:
            requests.exceptions.RequestException: If a request error occurs
        """
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        return response
        
    def get_info(self, response_content: bytes) -> dict[str, str] | None:
        """
        Extract the app information from the Aptoide webpage.

        Args:
            response_content (str): The response content of the webpage from a requests.Response object.

        Returns:
            dict: The app information extracted from the webpage or None if an error occurs.
        """
        try:
            tree: html.HtmlElement = html.fromstring(response_content)
            data = {}

            custom_extract = { 'icon_url': self._extract_icon_url, 'release_date': self._extract_release_date, 'description': self._extract_description }
            for key, value in self.xpaths.items():
                if key in custom_extract:
                    data[key] = custom_extract[key](tree)
                else:
                    result = tree.xpath(value)
                    if isinstance(result, list) and len(result) > 0:
                        element = result[0]
                        if isinstance(element, etree._Element) and hasattr(element, 'text_content'):
                            data[key] = element.text_content()
                        else:
                            data[key] = str(element)
                    else:
                        data[key] = ''

            return data 
        except etree.XPathEvalError as e:
            # Xpath evaluation failed --> invalid xpath expression in the xpaths file
            print('ERROR: Aptoide scraper failed. Invalid xpath expression found.\n', e)
            return None
        except IndexError as e:
            # Xpath search failed --> webpage structure has changed --> xpaths needs to be updated
            print('ERROR: Aptoide scraper failed. Webpage structure has changed. Update the xpaths.\n', e)
            return None
        except Exception as e:
            print('ERROR: Aptoide scraper failed.\n', e)
            return None

    def _extract_icon_url(self, tree: html.HtmlElement) -> str:
        """
        Extract the icon URL from the webpage.

        Args:
            tree (html.HtmlElement): The webpage tree

        Returns:
            str: The icon URL
        """
        result = tree.xpath(self.xpaths['icon_url'])[0].get('src')
        return result if type(result) == str else ''
    
    def _extract_release_date(self, tree: html.HtmlElement) -> str:
        """
        Extract the release date from the webpage.

        Args:
            tree (html.HtmlElement): The webpage tree

        Returns:
            str: The release date
        """
        result = tree.xpath(self.xpaths['release_date'])[0].text_content().replace('Release Date: ', '').split(' ')[0]
        return result if type(result) == str else ''

    def _extract_description(self, tree: html.HtmlElement) -> str:
        """
        Extract the description from the webpage by joining the paragraphs.

        Args:
            tree (html.HtmlElement): The webpage tree

        Returns:
            str: The description text joined with newlines
        """
        # Join the paragraphs of the description with newlines and remove the last newline
        return ''.join(
            [f'{s.text_content()}\n' for s in tree.xpath(self.xpaths['description'])[0]]
        )[:-1]

    
