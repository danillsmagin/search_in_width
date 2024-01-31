from collections import deque


def person_is_seller(people_name):
    if people_name[0] == 'm':
        return people_name


def search(name):
    search_queue = deque()
    graph = {'you': ['alice', 'miha', 'claire'],
             'bob': ['anuj', 'peggy'],
             'alice': ['peggy'],
             'claire': ['mom', 'johny'],
             'anuj': [],
             'peggy': [],
             'thom': [],
             'johny': []}
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search('you')
