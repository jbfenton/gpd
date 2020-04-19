"""
Model definitions.
"""


class MediaItemBase:
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
        return self._filename

    @property
    def mime_type(self) -> str:
        return self._mime_type


class MediaItem(MediaItemBase):
    def __init__(self, media_item: dict):
        """
        Instantiate MediaItem.

        :param media_item:
        :type media_item:
        """

        super(MediaItem, self).__init__(
            identifier=media_item['id'],
            filename=media_item['filename'],
            mime_type=media_item['mimeType']
        )


class AlbumBase:
    def __init__(self, identifier: str, media_count: str, title: str):
        self._identifier = identifier
        self._media_count = int(media_count)
        self._title = title

    @property
    def identifier(self):
        return self._identifier

    @property
    def media_count(self):
        return self._media_count

    @property
    def title(self):
        return self._title


class Album(AlbumBase):
    def __init__(self, album: dict):
        super(Album, self).__init__(
            identifier=album['id'],
            media_count=album['mediaItemsCount'],
            title=album['title']
        )
