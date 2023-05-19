from datetime import datetime
import urllib3
import json

color = {'SUCCESS': '#1AF952', 'FAILED': '#F91A1A'}
slack_url = 'https://hooks.slack.com/key'

dateDict = {0: '월요일', 1: '화요일', 2: '수요일은 정식당 삼겹살', 3: '목요일은 정식당 감자탕', 4: '금요일', 5: '', 6: ''}

def gen_slack_message(type, title, text):
        body, body_channel, body_attachments = {}, {}, {}
        body['attachments'] = []
        body_attachments["color"] = type
        body_attachments["pretext"] = title
        body_attachments["text"] = text
        body['attachments'].append(body_channel)
        body['attachments'].append(body_attachments)
        return json.dumps(body).encode('utf-8')

def send_slack_webhook_msg(slack_url, req_body):        
        req_headers = {'Content-Type': 'application/json; charset=UTF-8'}
        http = urllib3.PoolManager()
        req = http.request('POST', slack_url, headers=req_headers, body=req_body)
        result = req.data.decode('utf-8')
        return result

def update_LunchTime():
        now = datetime.now()        
        if now.weekday() > 4:
                print("주말입니다")
                return
        print(now)
        past = datetime.strptime("20230102", "%Y%m%d")
        print(past)
        diff = now - past
        print(diff.days)
        remain = int(diff.days/7)
        print(remain)

        dateDict[now.weekday()]
        text = '{}입니다'.format(dateDict[now.weekday()])

        if(remain%2 == 1):
                print("점심시간은 12시40분입니다")                
                # send_slack_webhook_msg(slack_url, gen_slack_message(color['SUCCESS'], '[점심시간] 12시 40분', '12시40분입니다.'))                
        else:
                print("점심시간은 1시입니다")
                # send_slack_webhook_msg(slack_url, gen_slack_message(color['FAILED'], '[점심시간] 1시', '1시입니다.'))                

update_LunchTime()