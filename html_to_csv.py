import requests
import os
from requests_testadapter import Resp
from bs4 import BeautifulSoup
import pandas as pd

class LocalFileAdapter(requests.adapters.HTTPAdapter):
    def build_response_from_file(self, request):
        file_path = request.url[7:]
        with open(file_path, 'rb') as file:
            buff = bytearray(os.path.getsize(file_path))
            file.readinto(buff)
            resp = Resp(buff)
            r = self.build_response(request, resp)

            return r

    def send(self, request, stream=False, timeout=None,
             verify=True, cert=None, proxies=None):

        return self.build_response_from_file(request)

requests_session = requests.session()
requests_session.mount('file://', LocalFileAdapter())
response = requests_session.get('file:///Users/shiningsunnyday/Documents/GitHub/aiFriend/message.html')

text = response.text

html_soup = BeautifulSoup(text, 'html.parser')

messages = html_soup.find_all('div', class_ = 'pam _3-95 _2pi0 _2lej uiBoxWhite noborder')

message = messages[0]

lis = []

for i in reversed(range(len(messages))):
    message = messages[i]
    message_lis = []
    for x in message.find_all('div'):
        if x.text != "" and x.text not in message_lis:
            message_lis.append(x.text)

    if len(message_lis) == 3:
        lis.append(message_lis)

lis_dic = [{"sender": lis[i][0], "message": lis[i][1], "time": lis[i][2]} for i in range(len(lis))]

df = pd.DataFrame(lis_dic)
df.to_csv('brianli.csv')

# name = message.find('div', class_ = '_3-96 _2pio _2lek _2lel').text
# date = message.find('div', class_ = '_3-94 _2lem').text
