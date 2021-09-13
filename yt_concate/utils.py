import os

from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR


class Utils:
    def __init__(self):
        pass

    # 建立放檔案的資料夾
    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)  # 使用os的makedirs建立資料夾，第一個為資料夾名，第二個意思為如果有這個資料夾就不再作成資料夾
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):  # 影片清單的路徑重組，return出完整路徑的.txt
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')  # 影片檔名使用channel_id命名

    def video_list_file_exists(self, channel_id):  # 檢查檔案是否存在，而且檔案容量要大於0
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def caption_file_exists(self, yt):  # 檢查字幕檔是否存在，而且檔案容量要大於0
        filepath = yt.caption_filepath
        # os.path.exists(path) 檢查檔案在不在
        # os.path.getsize(path) > 0 檢查這個檔案容量要大於0
        # and 邏輯運算子 要兩個都成立，才會回傳 True
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def video_file_exists(self, yt):  # 檢查影片檔是否存在，而且檔案容量要大於0
        filepath = yt.video_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0