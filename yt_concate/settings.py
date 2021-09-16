import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

# 寫路徑，使用os的join來合併字串
DOWNLOADS_DIR = 'downloads'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
OUTPUT_DIR = 'outputs'
