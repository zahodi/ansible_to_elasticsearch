#!/usr/bin/env python3
import json
from pprint import pprint

result_dict = {}
with open('output2.json') as data_file:
    data = json.load(data_file)
    plays = data['plays']
    play_stats = data['stats']


def parse_json():
  for play in plays:
    play_name = play['play']['name']
    for tasks in play['tasks']:
      print("this is all the hosts:", tasks['hosts'])
      for hosts in tasks['hosts']:
        print("this is the individual hosts:", hosts)
        for host in hosts['results']:
          print(host)

#pprint(data['plays'][1]['tasks'][5]['hosts'])

print(json.dumps(plays[1]['tasks'][0]['hosts']['localhost-vagrant']['results'][0], indent=4))

#parse_json()
