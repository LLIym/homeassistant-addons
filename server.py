from fastapi import FastAPI
import asyncio
from playwright.async_api import async_playwright
import os

app = FastAPI()
SAVE_PATH = "/share/bills"
os.makedirs(SAVE_PATH, exist_ok=True)

@app.get("/download")
async def download_invoice():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.rnparvaldnieks.lv/klientiem")

        # TODO: тут вставить шаги логина + скачивания PDF

        await browser.close()
    return {"status": "done", "saved_to": SAVE_PATH}
