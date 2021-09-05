from pytube import YouTube

from yt_concate.pipline.steps.preflight import Preflight
from yt_concate.pipline.steps.get_video_list import GetVideoList
from yt_concate.pipline.steps.download_captions import DownLoadCaptions
from yt_concate.pipline.steps.read_caption import ReadCaption
from yt_concate.pipline.steps.postflight import Postflight
from yt_concate.pipline.steps.step import StepException
from yt_concate.pipline.pipline import Pipline
from yt_concate.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'  # 通常不會改變的東西，會使用Global variable、全大寫


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    # 使用多行式的清單格式時，建議每個後面都加入「,」
    steps = [
        Preflight(),
        GetVideoList(),
        DownLoadCaptions(),
        ReadCaption(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipline(steps)
    p.run(inputs, utils)


# main check，檢查這個程式是不是進入點
# 如果這個程式被執行的時候，檔案本身的模組紙上__name__這個屬性，就會被稱為__main__
# 否則會變成是路徑
if __name__ == '__main__':
    main()
