"""
Model definitions.
"""


class MediaItemBase:
    """
    Media item base definition.
    """

    def __init__(self, identifier: str, filename: str, mime_type: str):
        """
        Instantiate MediaItem.

        :param identifier: Media item identifier.
        :type identifier: str
        :param filename: File name.
        :type filename: str
        :param mime_type: Media item mime type
        :type mime_type: str
        """

        self._identifier = identifier
        self._filename = filename
        self._mime_type = mime_type

    @property
    def identifier(self) -> str:
        """
        Retrieve media item ID.

        :return: Media item ID.
        :rtype: str
        """

        return self._identifier

    @property
    def filename(self) -> str:
        """
        Retrieve media item filename.

        :return: Media item filename.
        :rtype: str
        """

        return self._filename

    @property
    def mime_type(self) -> str:
        """
        Retrieve media item mime type.

        :return: Media item mime type.
        :rtype: str
        """

        return self._mime_type


class MediaItem(MediaItemBase):
    """
    Media item definition.
    """

    def __init__(self, media_item: dict):
        """
        Instantiate MediaItem.

        :param media_item: Dictionary representation of a media item.
        :type media_item: dict
        """

        super(MediaItem, self).__init__(
            identifier=media_item['id'],
            filename=media_item['filename'],
            mime_type=media_item['mimeType']
        )


class AlbumBase:
    """
    Album base definition.
    """

    def __init__(self, identifier: str, media_count: str, title: str):
        """
        Instantiate Album.

        :param identifier: Album identifier.
        :type identifier: str
        :param media_count: Album media item count.
        :type media_count: str
        :param title: Album title.
        :type title: str
        """

        self._identifier = identifier
        self._media_count = int(media_count)
        self._title = title

    @property
    def identifier(self) -> str:
        """
        Retrieve album identifier.

        :return: Album identifier
        :rtype: str
        """

        return self._identifier

    @property
    def media_count(self) -> int:
        """
        Retrieve album media count.

        :return: Album media count.
        :rtype: int
        """

        return self._media_count

    @property
    def title(self) -> str:
        """
        Retrieve album title.

        :return: Album title.
        :rtype: str
        """

        return self._title


class Album(AlbumBase):
    """
    Album definition.
    """

    def __init__(self, album: dict):
        """
        Instantiate Album.

        :param album: Dictionary representation of an Album.
        :type album: dict
        """

        super(Album, self).__init__(
            identifier=album['id'],
            media_count=album['mediaItemsCount'],
            title=album['title']
        )
