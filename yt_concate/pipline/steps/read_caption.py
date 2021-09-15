from .step import Step


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exists(yt):  # 如果沒有找到這個檔案，就跳過下一回
                continue

            captions = {}
            with open(yt.caption_filepath, 'r') as f:
                time_line = False  # 還沒拿到time時，為False
                time = None  # 存time的文字用
                caption = None  # 存caption的文字用
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line  # 拿到time
                        continue
                    if time_line:  # 跟寫time_line == True是相同的結果
                        caption = line  # 拿到caption
                        captions[caption] = time  # 這時已經拿到了time、caption了，就把它存到字典
                        time_line = False  # 再把time_line設值為False，再重從開始下個迴圈時，才能繼續再判斷
            yt.captions = captions  # yt.captions 設值為 captions

        print('completed to read captions')
        print(len(data))

        return data
