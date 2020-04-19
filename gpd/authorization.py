"""
Custom authorization handling.
"""

from json import load
from pathlib import Path
from typing import Union

from google.oauth2.credentials import Credentials as GoogleCredentials


class Credentials(GoogleCredentials):
    """
    Extended Credentials object to assist with credential caching.
    """
    
    @classmethod
    def from_json(cls, credentials_path: Union[Path, str]):
        """
        Load credentials from file.

        :param credentials_path: Path to credentials cache.
        :type credentials_path: str | Path
        :return: Credentials instance.
        :rtype: Credentials
        """

        with open(credentials_path) as credentials_file:
            credentials_json = load(credentials_file)

            credentials = cls(
                token=credentials_json["token"],
                refresh_token=credentials_json["refresh_token"],
                token_uri=credentials_json["token_uri"],
                client_id=credentials_json["client_id"],
                client_secret=credentials_json["client_secret"],
                scopes=credentials_json["scopes"]
            )

            return credentials
