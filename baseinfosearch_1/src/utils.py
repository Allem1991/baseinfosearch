import aiofiles


async def save_to_file(content, filepath):
    async with aiofiles.open(filepath, 'w') as f:
        await f.write(content)
