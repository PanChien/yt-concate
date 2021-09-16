from .step import Step

from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips


class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            print(found.time)
            start, end = self.parse_caption_time(found.time)  # start/end為tuple裡面裝著時間(h, m, s)
            if self.parse_during_time_str(start, end) < 1:
                continue
            video = VideoFileClip(found.yt.video_filepath).subclip(start, end)
            clips.append(video)  # 將video存入clips清單裡
            if len(clips) >= inputs['limit']:  # 如果清單大於等於limit，就break不要再存了
                break

        final_clip = concatenate_videoclips(clips)
        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        final_clip.write_videofile(output_filepath)


    def parse_caption_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        # 用split分割後，如果只用一個變數設值會存成一個清單裝著不同的資料
        # 使用兩個變數設值，就能分別設值在不同變數內
        # return回傳的值為((0, 16, 49.78), (0, 16, 52.919))
        return self.parse_time_str(start), self.parse_time_str(end)

    def parse_time_str(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        # return的資料，沒有用()也能回傳為tuple的資料形式
        return int(h), int(m), int(s) + int(ms) / 1000

    def parse_during_time_str(self, start_time, end_time):
        start_time = start_time[0] * 60 * 60 + start_time[1] * 60 + start_time[2]
        end_time = end_time[0] * 60 * 60 + end_time[1] * 60 + end_time[2]
        return end_time - start_time
