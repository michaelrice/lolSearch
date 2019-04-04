import logging
import giphy_client

from giphy_client.api_client import ApiException
from django.conf import settings

logger = logging.getLogger(__name__)


class Gclient(object):
    """
    Wrapper for giphy API
    """

    def __init__(self):
        self.api_key = settings.GIPHY_SETTINGS['api_key']
        self.rating = settings.GIPHY_SETTINGS['gif_rating']
        self.api_result_limit = settings.GIPHY_SETTINGS['api_limit']
        self.api_lang = settings.GIPHY_SETTINGS['api_lang']
        self.api_fmt = settings.GIPHY_SETTINGS['api_response_fmt']
        self.api_instance = giphy_client.DefaultApi()

    def random_image(self, tag=None):
        """
        Return a random image from giphy using a given tag

        :param tag: Tag used to filter search results on giphy
                    If multiple strings arew provided testing
                    shows the api uses the last one provided.
        :return: returns the URL of the random image or None type
                 if an error was encountered.
        """
        if not tag:
            tag = ''
        try:
            api_res = self.api_instance.gifs_random_get(
                self.api_key,
                tag=tag,
                rating=self.rating
            )
            return api_res.data.image_url
        except ApiException as e:
            logger.error("Failed to fetch image from giphy!", e)
            return None

    def search(self, query, offset=0):
        """
        Search giphy using a given query string.

        :param query: Search query term or phrase
        :param offset: An optional result offset. Defaults to 0
        :return: Giphy InlineResponse200 or None
        """
        if not query:
            logger.error("search method called with no query string which"
                         " returns an empty object from giphy.")
            return None
        # needed to workaround https://github.com/Giphy/GiphyAPI/issues/88
        if settings.GIPHY_SETTINGS['img_offset_limit']:
            limit = int(settings.GIPHY_SETTINGS['img_offset_limit'])
            if offset > limit:
                offset = limit
        try:
            api_res = self.api_instance.gifs_search_get(
                api_key=self.api_key,
                q=query,
                limit=self.api_result_limit,
                offset=offset,
                rating=self.rating,
                lang=self.api_lang,
                fmt=self.api_fmt
            )
            return api_res
        except ApiException as e:
            logger.error("Failed to fetch images from giphy.", e)
            return None
        except ValueError as e:
            logger.error("Failed ot fetch images from giphy", e)
            return None
