"""
Album model test cases.
"""

import pytest

from gpd.model import Album, AlbumBase


ALBUM_IDENTIFIER = "album_identifier"
ALBUM_TITLE = "album title"
ALBUM_MEDIA_COUNT = "9000"


@pytest.fixture
def album_dict() -> Album:
    """
    Generate an Album model.

    :return: Album model.
    :rtype: Album
    """

    return Album(
        {
            "id": ALBUM_IDENTIFIER,
            "mediaItemsCount": ALBUM_MEDIA_COUNT,
            "title": ALBUM_TITLE
        }
    )


@pytest.fixture
def album_base() -> AlbumBase:
    """
    Generate an AlbumBase model.

    :return: AlbumBase model.
    :rtype: AlbumBase
    """

    return AlbumBase(
        identifier=ALBUM_IDENTIFIER,
        media_count=ALBUM_MEDIA_COUNT,
        title=ALBUM_TITLE
    )


class TestAlbumBase:
    """
    Test AlbumBase model.
    """

    @pytest.fixture(autouse=True)
    def _album_fixture(self, album_base) -> None:
        """
        Set test class album instance using a fixture.

        :param album_base: AlbumBase instance.
        :type album_base: AlbumBase
        :return: None.
        :rtype: None
        """

        self.album = album_base

    def test_id(self) -> None:
        """
        Test albums 'identifier' property is correctly set.

        :return: None.
        :rtype: None
        """

        assert self.album.identifier == ALBUM_IDENTIFIER
        assert type(self.album.identifier) == str

    def test_media_count(self) -> None:
        """
        Test albums 'media_count' property is correctly set.

        :return: None.
        :rtype: None
        """

        assert self.album.media_count == int(ALBUM_MEDIA_COUNT)
        assert type(self.album.media_count) == int

    def test_title(self) -> None:
        """
        Test albums 'title' property is correctly set.

        :return: None.
        :rtype: None
        """

        assert self.album.title == ALBUM_TITLE
        assert type(self.album.title) == str


class TestAlbum(TestAlbumBase):
    """
    Test Album model.
    """

    @pytest.fixture(autouse=True)
    def _album_fixture(self, album_dict: Album) -> None:
        """
        Set test class album instance using a fixture.

        :param album_dict: Album instance.
        :type album_dict: Album
        :return: None.
        :rtype: None
        """

        self.album = album_dict
