"""
Custom authorization handling.
"""

from json import load
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials as GoogleCredentials
from google_auth_oauthlib.flow import InstalledAppFlow

from constants import PHOTOS_SCOPE


class Credentials(GoogleCredentials):
    """
    Extended Credentials object to assist with credential caching.
    """

    @classmethod
    def from_json(cls, credentials_path: Path):
        """
        Load credentials from file.

        :param credentials_path: Path to credentials cache.
        :type credentials_path: Path
        :return: Credentials instance.
        :rtype: Credentials
        """

        with open(str(credentials_path)) as credentials_file:
            credentials_json = load(credentials_file)

            scopes = credentials_json["scopes"]

            if isinstance(scopes, str):
                scopes = [scopes]

            credentials = cls(
                token=credentials_json["token"],
                refresh_token=credentials_json["refresh_token"],
                token_uri=credentials_json["token_uri"],
                client_id=credentials_json["client_id"],
                client_secret=credentials_json["client_secret"],
                scopes=scopes
            )

            return credentials


def cache_credentials(credentials_cache_path: Path, credentials: Credentials) -> None:
    """
    Save credentials to a cache file.

    :param credentials_cache_path: Path to the cache file.
    :type credentials_cache_path: Path
    :param credentials: Credentials object to save.
    :type credentials: Credentials
    :return: None.
    :rtype: None
    """

    with open(str(credentials_cache_path), 'w+') as credentials_file:
        credentials_file.write(credentials.to_json())


def load_credentials(
    credentials_cache_path: Path = Path('configuration/credentials_cache.json'),
    client_identification_path: Path = Path('configuration/client_id.json')
) -> Credentials:
    """
    Load credentials from the cache.

    If no credentials can be loaded, initiate credential creation flow.

    :param credentials_cache_path: Path to credentials cache file.
    :type credentials_cache_path: Path
    :param client_identification_path: Path to client identification configuration.
    :type client_identification_path: Path
    :return: Credentials.
    :rtype: Credentials
    """

    if credentials_cache_path.is_file():
        credentials = Credentials.from_json(credentials_cache_path)
    else:
        credentials = None

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(client_identification_path), PHOTOS_SCOPE)
            credentials = flow.run_local_server()

        cache_credentials(credentials_cache_path, credentials)

    return credentials
