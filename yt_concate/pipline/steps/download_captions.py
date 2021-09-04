import os
from pytube import YouTube
import time

from .step import Step
from .step import StepException


class DownLoadCaptions(Step):
    def process(self, data, inputs, utils):
        # download the package by:  pip install pytube
        start = time.time()
        for url in data:
            if utils.caption_file_exists(url):  # 如果有字幕檔，就跳到下一迴圈
                print('found existing caption file')
                continue  # 跳到下一回

            print(url)
            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError):
                print('Error when downloading caption for', url)
                continue
            # print(en_caption_convert_to_srt)
            text_file = open(utils.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', end - start, 'seconds')