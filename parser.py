import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os

from headers import cookies, headers, params




async def generate_url(text: str, session):
    params['q'] = text
    url = 'https://www.motionelements.com/v2/search/video'
    async with session.get(url=url, params=params, cookies=cookies, headers=headers) as response:
        if response.status == 200:
            return await response.json()
        else:
            print(f"Failed to retrieve data: {response.status}")
            return None


async def parse_data(data: dict):
    items = data.get("data", [])
    for item in items:
        previews = item.get("previews", {})
        mp4 = previews.get("mp4", {})
        url = mp4.get("url")
        if url:
            yield url
        else:
            raise ValueError("None url")


async def download_video(session, url, folder_path, index):
    async with session.get(url) as response:
        if response.status == 200:
            video_content = await response.read()
            file_path = os.path.join(folder_path, f"{index}.mp4")
            with open(file_path, "wb") as f:
                f.write(video_content)
            print(f"Downloaded {url} to {file_path}")
        else:
            print(f"Failed to download {url}")


async def main():
    text = input("Enter key-word: ")
    folder_path = os.path.join("Videos", text.capitalize())
    os.makedirs(folder_path, exist_ok=True)
    
    async with aiohttp.ClientSession() as session:
        data = await generate_url(text, session)
        if data:
            tasks = []
            index = 0
            async for url in parse_data(data):
                index += 1
                tasks.append(download_video(session, url, folder_path, index))

            await asyncio.gather(*tasks)
        else:
            print("Error with getting data")



