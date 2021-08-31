import urllib.request
import json

from yt_concate.pipline.steps.step import Step  # 使用絕對路徑import這個檔案裡的Step進來
from yt_concate.settings import API_KEY


class GetVideoList(Step):
    def process(self, data, inputs):
        channel_id = inputs['channel_id']

        base_video_url = 'https://www.youtube.com/watch?v='  # youtbe影片網址
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'  # 讓我們使用API的網址(API endpoint)

        # first_url組合成可被使用的網址(要有取得key、channelId)
        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY,
                                                                                                            channel_id)

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)  # 使用python內建的urllib的function，來送網址的request
            resp = json.load(inp)  # 回傳後的結果(使用json解讀)

            # 以下為結果的解讀，來把影片的Url取出
            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
        print(video_links)
        print('There are ', len(video_links), 'videos.')
        return video_links  # 回傳 儲存有所有網址的清單
