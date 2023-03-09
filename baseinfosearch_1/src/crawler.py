import asyncio

import aiofiles
import aiohttp
from bs4 import BeautifulSoup


class Spider:
    def __init__(self, urls):
        self.urls = urls
        self.memory = {}
        self.limit = asyncio.Semaphore(3)

    async def process_page_content(self, page):
        soup = BeautifulSoup(page, "html.parser")
        [tag.decompose() for tag in soup(["script","style","link"])]

        return str(soup)

    async def get_page(self, session, url):
        try:
            # async with self.limit:
            async with session.get(url) as response:
                html = await response.text()
                return url, await self.process_page_content(html)
        except Exception as e:
            print(e)

    async def go_spider_go(self):
        tasks = []

        headers = {"user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
        async with aiohttp.ClientSession(headers=headers) as session:
            for url in self.urls:
                tasks.append(self.get_page(session, url))

            htmls = await asyncio.gather(*tasks)
            for html in htmls:
                if html:
                    self.memory[html[0]] = html[1]

    def run(self):
        asyncio.run(self.go_spider_go())