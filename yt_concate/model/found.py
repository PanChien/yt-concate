# 將找到的資料，作成一個Found class，來儲存資料 helper class

class Found:
    def __init__(self, yt, caption, time):
        self.yt = yt
        self.caption = caption
        self.time = time

    def __str__(self):
        return '<Found(yt=' + str(self.yt) + ')>'

    def __repr__(self):
        content = ' : '.join([  # .join功能是用在字串上的，字串上join的這個method，每一個清單裡的字串之間會配上「:」
            'yt=' + str(self.yt),  # yt有寫repr，如果要使用就把str改為repr
            'caption=' + str(self.caption),
            'time=' + str(self.time),
        ])
        return '<Found(' + content + ')>'
