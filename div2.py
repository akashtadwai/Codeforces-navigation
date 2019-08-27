import requests

url = "http://codeforces.com/api"
options = '/contest.list'
link = 'http://codeforces.com/contest/'

data = requests.get(url+options)
data = data.json()

div2 = []

if data['status'] == 'OK':
    data = data['result']
    for i in data:
        if 'Div. 2' in i['name']:
            div2.append(int(i['id']))

    div2.sort()

    f = open("div2.txt","w+")
    cnt = 1
    for i in div2:
        temp = 'Div2 '
        temp += str(cnt)
        temp += ':  '
        temp += link+str(i)
        temp += '\n'
        f.write(temp)
        cnt+=1
    f.close()

else:
    print('There may be some issues on Codeforces or the servers are not responding');
    print('Please Wait and try it after few minutes');
