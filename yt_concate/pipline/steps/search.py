from .step import Step
from yt_concate.model.found import Found

class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']

        found = []
        for yt in data:
            captions = yt.captions  # 是一個字典，key為字幕、value為時間
            if not captions:  # 如果沒有這個物件，跳下一回(因為有些沒有下載到字幕檔，使用forloop迴圈時會當掉)
                continue

            for caption in captions:
                if search_word in caption:
                    time = captions[caption]  # 存下時間
                    f = Found(yt, caption, time)  # 作成一個Found實例
                    found.append(f)

        print(len(found))
        return found
