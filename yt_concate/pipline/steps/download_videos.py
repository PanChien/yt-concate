from pytube import YouTube

from .step import Step
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])  # 有可能搜尋到的文字在同一個url，使用set()來將重複的淘汰
        print('videos to download=', len(yt_set))

        for found in yt_set:
            yt = found.yt
            url = yt.url

            if utils.video_file_exists(yt):  # 如果影片有在資料夾的檢查，就不要再次下載
                print(f'found existing video file for {url}, skipping')
                continue

            print('downloading:', url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)  # 下載影片，如果有發生錯誤再使用TryExcept來跳過

        return data
