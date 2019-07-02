import requests

url = "http://codeforces.com/api"
options = '/contest.list'
link = 'http://codeforces.com/contest/'

data = requests.get(url+options)
data = data.json()

edu = []
if data['status'] == 'OK':
    data = data['result']
    for i in data:
        if 'Educational' in i['name']:
            edu.append(int(i['id']))

    edu.sort()

    f = open("educational.txt","w+")
    cnt = 1
    for i in edu:
        temp = 'Educational Round '
        temp += str(cnt)
        temp += ':  '
        temp += link+str(i)
        temp += '\n'
        f.write(temp)
        cnt+=1
    f.close()
else:
    print('There may be some issues on Codeforces or the servers or not responding');
    print('Please Wait and try it after few minutes');
