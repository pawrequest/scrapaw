import asyncio

import bs4
from aiohttp import ClientError, ClientSession


async def response_(url: str, http_session: ClientSession) -> str:
    """
    Get response from url, retry 3 times if request fails

    :param url: url to get response from
    :param http_session: aiohttp ClientSession
    :return: response text
    """
    for _ in range(3):
        try:
            async with http_session.get(url) as response:
                response.raise_for_status()
                return await response.text()
        except ClientError as e:
            print(f'Request failed: {e}')
            await asyncio.sleep(2)
            continue
    else:
        raise ClientError('Request failed 3 times')


async def soup_from_url(url: str, session: ClientSession | None = None) -> bs4.BeautifulSoup:
    html = await response_(url, session)
    return bs4.BeautifulSoup(html, 'html.parser')
