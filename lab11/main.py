import re
from zipfile import ZipFile

archive = 'access_log_Jul95'
regex = re.compile(
    ':(01:39:+|01:[4-5][0-9]+:|01[4-5][0-9]:|0[2-9]:[0-9]+:|1[0-1]:[0-9]+:|12:4[0-5]:|12:[0-4][0-9]:).+/shuttle/missions/([0-9A-Za-z-]+)')

with ZipFile(archive + '.zip', 'r') as _:
    _.extractall()

with open(archive, 'r', encoding='cp850') as file:

    logs = set()
    for log in file:
        groups = regex.findall(log)

        if len(groups) > 0:
            logs.add(groups[0][1])

    print(logs)