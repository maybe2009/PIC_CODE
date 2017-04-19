critics={
'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},

'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},

'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},

'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},

'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},

'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
''
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}
}

movies = ['Lady in the Water', 'Snakes on a Plane', 'Just My Luck', 'Superman Returns',
'You, Me and Dupree', 'The Night Listener']

names = [
'Lisa Rose',
'Michael Phillips',
'Claudia Puig',
'Mick LaSalle',
'Gene Seymour',
'Jack Matthews',
'Toby']

import math
import copy
import pprint

def sim_distance(src, dst, keys):
    powSum = 0;
    for k in keys:
        try:
            #print("caculate key ", k)
            tmp = math.pow(src[k] - dst[k], 2)
            #print("x is ", src[k], " y is ", dst[k], " pow is ", tmp)
            powSum = powSum + tmp
        except KeyError as e:
            #print("Not exist key trigger a exception:", e)
            continue

    dis =  math.sqrt(powSum)
    #print("powSum is ", powSum, " distance is ", dis)
    return dis

def sim_with_others(data, myName, otherNames, keys):
    dis = {}
    for n in otherNames:
        dis[n] = sim_distance(data[myName], data[n], keys)
        #print("other name is ", n, " distance is ", dis[n])
    return sorted(dis.items(), key=lambda d: d[1])

def sim_all(data, names, keys):
    dis = {}
    otherNames = copy.deepcopy(names);
    for n in names:
        #print("my name is ", n)
        otherNames.remove(n)
        dis[n] = sim_with_others(data, n, otherNames, keys)
    return dis

#sim_distance(critics['Lisa Rose'], critics['Gene Seymour'], movies)
#dis = sim_with_others(critics, 'Lisa Rose', names, movies)
dis = sim_all(critics, names, movies)

pprint.PrettyPrinter(indent=2).pprint(dis)


#print("@@@ ", sorted(dis.items(), key=lambda d: d[1]))