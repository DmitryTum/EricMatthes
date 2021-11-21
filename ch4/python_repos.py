import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code:", r.status_code)

"""Сохранение ответа API в переменной"""
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

"""Анализ информации о репозиторих"""
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

plot_dict = {
    'value': repo_dict['stargazers_count'],
    'label': repo_dict['description'],
}
plot_dicts.append(plot_dict)

my_style = LS('#333366', base_style=LCS)

chart = pygal.Bar(style=my_style)
chart.title = 'Most-Starred Python'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

