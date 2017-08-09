import json
import datetime
import discord

data_dict = {
    'queues': 'data/queues.json',
    'reference': 'data/reference.json',
    'small': 'data/small.json'
}
keys = {
    'small': ['item', 'event'],
    'reference': ['commands', 'queue']
}


# creates class "Boss" holding info on all boss queues and where external files are saved and their content
class Boss(object):
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.path = data_dict['queues']


# ---------- CORE COMMANDS --------------
def read_json(path):
    with open(path, 'r') as doc:
        return json.load(doc)


def write_json(path, content):
    with open(path, 'w') as doc:
        json.dump(content, doc)
# ---------- END OF CORE ----------------


# removes a name from all queues
def remove_from_queue(name):
    queues = read_json(data_dict['queues'])
    for i in queues:
        queues[i] = list(filter(name.__ne__, queues[i]))
    write_json(data_dict['queues'], queues)


# clears a single queue
def empty_queue(boss):
    queues = read_json(boss.path)
    queues[boss.name] = []
    write_json(boss.path, queues)


# adds a new name to a single queue
def append_queue(boss, user):
    queues = read_json(boss.path)
    queues[boss.name].append(user)
    if len(queues[boss.name]) >= boss.length:
        return_list = queues[boss.name]
        empty_queue(boss)
        return True, return_list
    write_json(boss.path, queues)
    return False, 'a'


# Creates empty queues and writes them (in Json) to a file
def init_queues(path, list_):
    queues = {}
    for i in list_:
        x = i.name
        queues[x] = []
    write_json(path, queues)


# Removes all data, and formats the lists correctly for {event, item} small data
def init_small(dict_):
    write_json(data_dict['small'], dict_)


def init_reference(dict_):
    write_json(data_dict['reference'], dict_)


# rewrite data - useful for updating item of the week and upcoming events
def rewrite_json(path, key, content):
    d = read_json(path)
    d[key] = content
    write_json(path, d)


def recall_json(path, key):
    d = read_json(path)
    return d[key]


def get_queue_info():
    d = read_json(data_dict['queues'])
    for i in d:
        d[i] = len(d[i])
    return d


# takes 2 ints returns xx.xx% chance to receive drop
def drop_rate(x, y):
    floater = 1-((1-1/x)**y)
    floater = floater * 100
    floater = str(floater)
    return floater[:5] + '%'


# builds embed for moderation log
def punish(target, punishment, executioner, reason):
    if punishment == 'Kick':
        em_colour = 0xffff00
    elif punishment == 'Soft Ban':
        em_colour = 0xffaa00
    elif punishment == 'Ban':
        em_colour = 0xff0000
    else:
        em_colour = 0x00FAFF
    embed = discord.Embed(colour=discord.Colour(em_colour), description=f"Punished: {target}\nAction: {punishment}"
                                                                        f"\nReason: {reason}",
                          timestamp=datetime.datetime.utcnow())
    embed.set_author(name=executioner, icon_url=executioner.avatar_url)
    return embed
