import re

def validate_aptoide_url(url: str) -> bool:
    """
    Validates an Aptoide URL.
    Matches URLs like: 
    * https://APP_NAME.LANGUAGE.aptoide.com/app

    Args:
        url (str): The URL to validate

    Returns:
        bool: Whether the URL is a valid Aptoide URL
    """
    return re.fullmatch(r'(https:\/\/)[\w-]+\.\w+\.aptoide\.com\/app', url) is not None