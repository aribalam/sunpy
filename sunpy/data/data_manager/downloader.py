from abc import ABCMeta, abstractmethod
from pathlib import Path

from parfive import Downloader

__all__ = ['DownloaderBase', 'DownloaderError', 'ParfiveDownloader']


class DownloaderBase(metaclass=ABCMeta):
    """
    Base class for remote data manager downloaders.
    """
    @abstractmethod
    def download(self, url, path):
        """
        Downloads a file.

        Parameters
        ----------
        url: `str`
            URL of the file to be downloaded.
        path: `pathlib.Path` or `str`
            Path where the file should be downloaded to.

        Raises
        ------
        `DownloaderError`
            DownloaderError is raised when download errors.
        """
        raise NotImplementedError


class DownloaderError(Exception):
    """
    Error to be raised when a download fails.
    """


class ParfiveDownloader(DownloaderBase):
    """
    Concrete implementation of `~sunpy.data.data_manager.downloader.DownloaderBase`
    using `parfive`.
    """

    def download(self, url, path):
        downloader = Downloader()
        path = Path(path)
        filename = path.name
        directory = path.parent
        downloader.enqueue_file(url, directory, filename)
        try:
            downloader.download()
        except Exception as e:
            raise DownloaderError from e
