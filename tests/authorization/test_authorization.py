"""
Authorization tests.
"""

from json import JSONDecodeError, load
from pathlib import Path

import pytest

from gpd.authorization import Credentials, cache_credentials


def test_credentials_no_path() -> None:
    """
    Validate that a FileNotFoundError is raised if the credentials cache is not found.

    :return: None.
    :rtype: None
    """

    with pytest.raises(FileNotFoundError):
        Credentials.from_json(Path("null.json"))


def test_credentials_no_json() -> None:
    """
    Validate that a JSONDecodeError is raised if the credentials cache does not contain valid JSON.

    :return: None.
    :rtype: None
    """

    with pytest.raises(JSONDecodeError):
        Credentials.from_json(Path("authorization/credentials_cache/credentials_cache_no_json.json"))


@pytest.fixture
def normal_credentials_cache_path() -> Path:
    """
    Retrieve path to a credentials cache file that contains scopes as a list.

    :return: Path to credentials cache.
    :rtype: Path
    """

    return Path("authorization/credentials_cache/credentials_cache.json")


@pytest.fixture
def normal_credentials(normal_credentials_cache_path: Path) -> Credentials:
    """
    Load in a mock set of Credentials from a cache file.

    The cache file in question should contain a list of scopes.

    :param normal_credentials_cache_path: Path to the credentials cache file.
    :type normal_credentials_cache_path: Path
    :return: Credentials.
    :rtype: Credentials
    """

    return Credentials.from_json(normal_credentials_cache_path)


@pytest.fixture
def string_scope_credentials_cache_path() -> Path:
    """
    Retrieve path to the credentials cache file that contains scopes a string.

    :return: Path to the credentials cache.
    :rtype: Path
    """

    return Path("authorization/credentials_cache/credentials_cache_string_scopes.json")


@pytest.fixture
def credentials_string_scopes(string_scope_credentials_cache_path: Path) -> Credentials:
    """
    Load in a mock set of Credentials from a cache file.

    The cache file in question should contain a scope as a string object (not within a list).

    :param string_scope_credentials_cache_path: Path to the credentials cache file.
    :type string_scope_credentials_cache_path: Path
    :return: Credentials.
    :rtype: Credentials
    """

    return Credentials.from_json(string_scope_credentials_cache_path)


def test_save_credentials(
        normal_credentials_cache_path: Path,
        normal_credentials: Credentials,
        tmp_path: Path
) -> None:
    """
    Test caching of credentials.

    Credentials should be saved to disk as a JSON file.

    :param normal_credentials_cache_path: Path to the credentials cache file.
    :type normal_credentials_cache_path: Path
    :param normal_credentials: Credentials object.
    :type normal_credentials: Credentials
    :param tmp_path: Temporary output path.
    :type tmp_path: Path
    :return: None.
    :rtype: None
    """

    output_file = tmp_path / 'temp_cache.json'

    cache_credentials(output_file, normal_credentials)

    if output_file.is_file():
        with open(str(output_file)) as temp_cache:
            temp_cache_json = load(temp_cache)

            with open(str(normal_credentials_cache_path)) as credentials_cache:
                baseline_cache_json = load(credentials_cache)
                assert temp_cache_json == baseline_cache_json


class TestCredentials:
    """
    Verify that all properties are returning correctly after building the object from a cache file.

    In this scenario the cache file will contain scopes as a list.
    """

    @pytest.fixture(autouse=True)
    def _set_credentials(self, normal_credentials: Credentials) -> None:
        """
        Store the passed in credentials for convenient access.

        :param normal_credentials: Credentials.
        :type normal_credentials: Credentials
        :return: None
        :rtype: None
        """

        self._credentials = normal_credentials

    def test_credentials_exist(self) -> None:
        """
        Verify the Credentials were correctly loaded from the cache.

        :return: None.
        :rtype: None
        """

        assert type(self._credentials) == Credentials

    def test_credentials_token(self) -> None:
        """
        Verify that the credentials token is correctly returned.

        :return: None.
        :rtype: None
        """

        assert self._credentials.token == "mock_token"

    def test_credentials_refresh_token(self) -> None:
        """
        Verify that the credentials refresh token is correctly returned.

        :return: None.
        :rtype: None
        """

        assert self._credentials.refresh_token == "refresh_token"

    def test_token_uri(self) -> None:
        """
        Verify that the credentials token uri is correctly returned.

        :return: None.
        :rtype: None
        """

        assert self._credentials.token_uri == "https://www.googleapis.com/oauth2/v3/token"

    def test_client_id(self) -> None:
        """
        Verify that the credentials client id is correctly returned.

        :return: None.
        :rtype: None
        """

        assert self._credentials.client_id == "client_id"

    def test_client_secret(self) -> None:
        """
        Verify that the client secret is correctly returned.

        :return: None.
        :rtype: None
        """

        assert self._credentials.client_secret == "client_secret"

    def test_scopes(self) -> None:
        """
        Verify that the credentials scopes are correctly returned.

        :return: None.
        :rtype: None
        """

        assert type(self._credentials.scopes) == list
        assert self._credentials.scopes == ["https://www.googleapis.com/auth/photoslibrary"]


class TestCredentialsStringScopes(TestCredentials):
    """
    Verify that Credentials properties are returning correctly after loading from the cache.

    In this scenario the cache file will contain a scope as a string.
    """

    @pytest.fixture(autouse=True)
    def _set_credentials(self, credentials_string_scopes: Credentials) -> None:
        """
        Store credentials for convenient access.

        :param credentials_string_scopes: Credentials.
        :type credentials_string_scopes: Credentials
        :return: None
        :rtype: None
        """

        self._credentials = credentials_string_scopes
