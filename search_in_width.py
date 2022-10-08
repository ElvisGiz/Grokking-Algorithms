from collections import deque

graph = {}
graph["you"]=["alice", "bob", "claire"]
graph["alice"]=["peggy"]
graph["bob"]=["anuj","peggy"]
graph["claire"]=["tom", "jonnyM"]
graph["anuj"]=[]
graph["peggy"]=[]
graph["tom"]=[]
graph["jonnyM"]=[]

def person_is_seller(name):
    return name[-1]=='M'

def search(name):
    search_queue= deque()
    search_queue+=graph[name]
    searched=[]
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person+" is a seller!")
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False


print(search("you"))                    