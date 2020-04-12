import requests
from plotly.graph_objs import Bar
from plotly import offline

#Make an API call and store the response.
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3.json'}
r = requests.get(url, headers=headers)


#Store API response in a variable
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names ,repo_links, stars, labels = [], [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href= '{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)


#Make Visulization
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    }]
my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size':14},
    },
    'yaxis' : {
        'title': 'Stars',
        'titlefont': {'size':24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
