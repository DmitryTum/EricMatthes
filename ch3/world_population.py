import json
import pygal
from pygal.style import RotateStyle
from countries import get_country_code


file_name = 'population_data.json'
with open(file_name) as f:
    pop_data = json.load(f)

cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
            print(code + ": " + str(population))
        else:
            print('ERROR ' + country_name)

cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}

for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops1[cc] = pop
    elif pop < 100000000:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop
print(len(cc_pops1), len(cc_pops3), len(cc_pops3))

wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'W_P_in_2010, by Country'
wm.add('0-10m', cc_pops1)
wm.add('10-1bn', cc_pops2)
wm.add('>1bn', cc_pops3)
wm.render_to_file('world_populations3.svg')
