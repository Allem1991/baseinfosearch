import asyncio

from crawler import Spider
from utils import save_to_file


async def main(memory):
    filewrite = []
    with open("index.txt", "w") as f:
        i = 0
        for url, content in memory.items():
            i += 1
            filewrite.append(asyncio.ensure_future(save_to_file(content, f"save_pages/{i}.html")))
            f.write(f"{i}.html - {url}\n")
    await asyncio.gather(*filewrite)


urls = []
with open("urls.txt", "r") as f:
    for line in f:
        urls.append(line)

urls = [url.replace('\n','') for url in urls]
spider = Spider(urls)

spider.run()

asyncio.run(main(spider.memory))