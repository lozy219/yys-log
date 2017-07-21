# coding=utf-8
import csv
import re
import glob
import os
import json

main = {
  2: ['攻击加成', '生命加成', '防御加成', '速度'],
  4: ['攻击加成', '生命加成', '防御加成', '效果命中', '效果抵抗'],
  6: ['攻击加成', '生命加成', '防御加成', '暴击', '暴击伤害']
}
chinese_num = ['一', '二', '三', '四', '五', '六']
temp_file = 'temp.tmp'

def run(file, write_file=False):
  if not write_file:
    write_file = file[6:]
  a = []
  j = {}
  with open(file, 'r') as c:
    r = csv.reader(c, delimiter=' ')
    all = {}
    for row in r:
      source = row[-1]
      if re.findall('御魂副本', source, re.S):
        name = row[3]
        if name not in all:
          all[name] = {
            'name': name, 
            'star_position': [],
          }
        all[name]['star_position'].append(row[5] + row[6])

    total = 0
    total_star = [0, 0]
    total_position = [0, 0, 0, 0, 0, 0]
    total_2 = [0, 0, 0, 0]
    total_4 = [0, 0, 0, 0, 0]
    total_6 = [0, 0, 0, 0, 0]
    for row in all.keys():
      yuhun = all[row]

      a.append([yuhun['name']])
      y = {}

      sp = yuhun['star_position']

      a.append(['总数', '五星', '六星'])
      star_5 = len([1 for c in sp if re.findall('5星', c, re.S)])
      star_6 = len([1 for c in sp if re.findall('6星', c, re.S)])
      
      a.append([len(sp), star_5, star_6])
      y['总数'] = len(sp)
      y['五星'] = star_5
      y['六星'] = star_6

      total += len(sp)
      total_star[0] += star_5
      total_star[1] += star_6

      pos_info = [c + '号位' for c in chinese_num]
      pos = [len([1 for c in sp if re.findall(cn + '号位', c, re.S)]) for cn in chinese_num]
      a.append(pos_info)
      a.append(pos)
      for t in zip(pos_info, pos):
        y[t[0]] = t[1]
      total_position = [total_position[c] + pos[c] for c in range(len(pos))]

      a.append(['二号位属性'])
      type = [len([1 for c in sp if re.findall('二号位.*' + m, c, re.S)]) for m in main[2]]
      a.append(main[2])
      a.append(type)
      y2 = {}
      for t in zip(main[2], type):
        y2[t[0]] = t[1]
      total_2 = [total_2[c] + type[c] for c in range(len(type))]
      
      a.append(['四号位属性'])
      type = [len([1 for c in sp if re.findall('四号位.*' + m, c, re.S)]) for m in main[4]]
      a.append(main[4])
      a.append(type)
      y4 = {}
      for t in zip(main[4], type):
        y4[t[0]] = t[1]
      total_4 = [total_4[c] + type[c] for c in range(len(type))]
      
      a.append(['六号位属性'])
      type = [len([1 for c in sp if re.findall('六号位.*' + m, c, re.S)]) for m in main[6]]
      a.append(main[6])
      a.append(type)
      y6 = {}
      for t in zip(main[6], type):
        y6[t[0]] = t[1]
      total_6 = [total_6[c] + type[c] for c in range(len(type))]
      a.append([])

      y['二号位属性'] = y2
      y['四号位属性'] = y4
      y['六号位属性'] = y6

      j[yuhun['name']] = y

  a.append([])
  k = ['金色御魂总数', '五星御魂总数', '六星御魂总数']
  v = [total, total_star[0], total_star[1]]
  a.append(k)
  a.append(v)
  for t in zip(k, v):
    j[t[0]] = t[1]

  k = [c + '号位总数' for c in chinese_num]
  v = total_position
  a.append(k)
  a.append(v)
  for t in zip(k, v):
    j[t[0]] = t[1]

  a.append(['二号位属性'])
  k = main[2]
  v = total_2
  a.append(k)
  a.append(v)
  j2 = {}
  for t in zip(k, v):
    j2[t[0]] = t[1]

  a.append(['四号位属性'])
  k = main[4]
  v = total_4
  a.append(k)
  a.append(v)
  j4 = {}
  for t in zip(k, v):
    j4[t[0]] = t[1]

  a.append(['六号位属性'])
  k = main[6]
  v = total_6
  a.append(k)
  a.append(v)
  j6 = {}
  for t in zip(k, v):
    j6[t[0]] = t[1]

  j['二号位属性'] = j2
  j['四号位属性'] = j4
  j['六号位属性'] = j6


  with open('./analysis/{0}'.format(write_file), 'w+') as c:
    w = csv.writer(c, delimiter=',')
    for row in a:
      w.writerow(row);

  with open('./analysis/{0}'.format(write_file[:-3] + 'json'), 'w+') as c:
    c.write(json.dumps(j).decode('unicode-escape').encode('utf8'))

all_files = glob.glob("./raw/*.csv")
all_ana = glob.glob("./analysis/*.csv")

for file in all_ana:
  os.remove(file)

for file in all_files:
  run(file)
  with open(file, 'r') as c:
    with open(temp_file, 'a+') as d:
      for line in c.readlines():
        d.write(line)

run(temp_file, 'overall.csv')
os.remove(temp_file)