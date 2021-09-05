import os

from pprint import pprint  # python內建的功能

from .step import Step
from yt_concate.settings import CAPTIONS_DIR

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}  # key為檔名、value為字幕
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}  # key為其中一行的字幕、value為其中一行的時間，將儲存檔案裡的全部的字幕跟時間
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                time_line = False  # 還沒拿到time時，為False
                time = None  # 存time的文字用
                caption = None  # 存caption的文字用
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:  # 跟寫time_line == True是相同的結果
                        caption = line
                        captions[caption] = time  # 這時已經拿到了time、caption了，就把它存到字典
                        time_line = False  # 再把time_line設值為False，再重從開始下個迴圈時，才能繼續再判斷
            data[caption_file] = captions  # caption_file為key、captions為value
        pprint(data)
        return data
