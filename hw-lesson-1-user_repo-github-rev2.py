import requests
import json

url = 'https://api.github.com/users/jessfraz/repos'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
#params = {'page': 2, 'per_page': 100}
r = []
data = requests.get(url, headers=header)
print(data.status_code)
j_data = data.json()
for i in j_data:
    r.append(i['html_url'])
print(r)


# url = j_data.get('next')
# result_data.extend(j_data.get('results'))

# filename = 'out\list_users_repo.json'
# with open(filename, 'w') as j_file:
#     j_file.write(json.dumps(data))


