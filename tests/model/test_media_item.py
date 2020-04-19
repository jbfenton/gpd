"""
MediaItem model test cases.
"""

import pytest

from gpd.model import MediaItem, MediaItemBase


MEDIA_ITEM_IDENTIFIER = "media_item_identifier"
MEDIA_ITEM_FILENAME = "test_filename.jpg"
MEDIA_ITEM_MIME_TYPE = "jpg"


@pytest.fixture
def media_item_dict() -> MediaItem:
    """
    Generate an MediaItem model.

    :return: MediaItem model.
    :rtype: MediaItem
    """

    return MediaItem(
        {
            "id": MEDIA_ITEM_IDENTIFIER,
            "filename": MEDIA_ITEM_FILENAME,
            "mimeType": MEDIA_ITEM_MIME_TYPE
        }
    )


@pytest.fixture
def media_item_base() -> MediaItemBase:
    """
    Generate an MediaItemBase model.

    :return: MediaItemBase model.
    :rtype: MediaItemBase
    """

    return MediaItemBase(
        identifier=MEDIA_ITEM_IDENTIFIER,
        filename=MEDIA_ITEM_FILENAME,
        mime_type=MEDIA_ITEM_MIME_TYPE
    )


class TestMediaItemBase:
    """
    Test MediaItemBase model.
    """

    @pytest.fixture(autouse=True)
    def _media_item_fixture(self, media_item_base: MediaItemBase) -> None:
        """
        Set test class media_item instance using a fixture.

        :param media_item_base: MediaItemBase instance.
        :type media_item_base: MediaItemBase
        :return: None.
        :rtype: None
        """

        self.media_item = media_item_base

    def test_identifier(self) -> None:
        """
        Test media_items 'identifier' property is correctly set.

        :return: None.
        :rtype: None
        """

        assert self.media_item.identifier == MEDIA_ITEM_IDENTIFIER

    def test_filename(self) -> None:
        """
        Test media_items 'filename' property is correctly set.

        :return: None.
        :rtype: None
        """

        assert self.media_item.filename == MEDIA_ITEM_FILENAME

    def test_mime_type(self) -> None:
        """
        Test media_items 'mime_type' property is correctly set.

        :return: None.
        :rtype: None
        """

        assert self.media_item.mime_type == MEDIA_ITEM_MIME_TYPE


class TestMediaItem(TestMediaItemBase):
    """
    Test MediaItem model.
    """

    @pytest.fixture(autouse=True)
    def _media_item_fixture(self, media_item_dict) -> None:
        """
        Set test class media_item instance using a fixture.

        :param media_item_dict: MediaItem instance.
        :type media_item_dict: MediaItem
        :return: None.
        :rtype: None
        """

        self.media_item = media_item_dict
