import urllib.request
import json
from yt_concate.settings import API_KEY


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'  # 通常不會改變的東西，會使用Global variable、全大寫


def get_all_video_in_channel(channel_id):  # channel_di是要投入的參數
    api_key = 'AIzaSyAjw8ANVConwvy1gjqDuO_X17QbcdG0sb8'  # 貼上你的API Key

    base_video_url = 'https://www.youtube.com/watch?v='  # youtbe影片網址
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'  # 讓我們使用API的網址(API endpoint)

    # first_url組合成可被使用的網址(要有取得key、channelId)
    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)  # 使用python內建的urllib的function，來送網址的request
        resp = json.load(inp)      # 回傳後的結果(使用json解讀)

        # 以下為結果的解讀，來把影片的Url取出
        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except KeyError:
            break
    return video_links  # 回傳 儲存有所有網址的清單


video_list = get_all_video_in_channel(CHANNEL_ID)
print(video_list)
print('一共有', len(video_list), '個網址。')