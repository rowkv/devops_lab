import requests


def get_pulls(state):
    pulls = list()
    if state in ('accepted', 'needs work'):
        payload = {'state': 'all', 'per_page': 100}
        response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls',
                                params=payload)
        for item in response.json():
            try:
                if item['labels'][0]['name'] == state:
                    pulls.append({'num': item['number'],
                                  'title': item['title'],
                                  'link': item['url']})
            except IndexError:
                continue
    elif state in ('open', 'closed'):
        payload = {'state': state, 'per_page': 100}
        response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls',
                                params=payload)
        for item in response.json():
            pulls.append({'num': item['number'], 'title': item['title'], 'link': item['url']})
    return pulls
