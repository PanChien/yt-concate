import os

from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR

class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url(self.url)  # 影片id
        self.caption_filepath = self.get_caption_filepath()  # 字幕檔(絕對路徑)
        self.video_filepath = self.get_video_filepath()  # 影片檔(絕對路徑)
        self.capiton = None

    @staticmethod  # 可以不須要使用self的method
    def get_video_id_from_url(url):  # 拿到video的id
        return url.split('watch?v=')[-1]  # 使用split分割，會切出兩個list，而[-1]為倒數第一個的意思

    def get_caption_filepath(self):  # 字幕的檔案的位置重組，return出完整路徑的.txt
        return os.path.join(CAPTIONS_DIR, self.id + '.txt')

    def get_video_filepath(self):  # 字幕的檔案的位置重組，return出完整路徑的.txt
        return os.path.join(VIDEOS_DIR, self.id + '.mp4')

    def __str__(self):
        return '<YT(' + self.id + ')>'

    def __repr__(self):
        content = ' : '.join([  # .join功能是用在字串上的，字串上join的這個method，每一個清單裡的字串之間會配上「:」
            'id=' + str(self.id),
            'caption_filepath=' + str(self.caption_filepath),
            'video_filepath=' + str(self.video_filepath),
        ])
        return '<YT(' + content + ')>'