import time,sys,re
from collections import defaultdict 
tstart=time.time()

inf = sys.argv[1] if len(sys.argv) > 1 else 'input/input9.txt'
with open(inf) as fi:
    line = [int(x) for x in fi.read().strip()]
id_ = 0
mem = [] 
memd = dict()
M = dict()
freespace = defaultdict(list)

pos = 0
for i,x in enumerate(line):
    #for part1 - slow solution...
    for _ in range(x):
        if i % 2 == 0:
            mem.append(i//2)
        else:
            mem.append('.')
    #for part2
    if i % 2 == 0:
        memd[pos] = (i//2,x)
    else:
        if x > 0:
            freespace[x].append(pos)
    pos = x+pos
#part2    
P = list(memd.keys())[::-1]
for pos in P:
    id_, L = memd[pos]
    F = sorted(list(freespace.keys()))[::-1]#.sort()
    npos = dict()
    for space in F:
        if L<= space and len(freespace[space])>0:
            npos[min(freespace[space])] = space
    if len(npos)> 0:
        newpos = min(list(npos.keys()))
        if newpos<pos: 
            space = npos[newpos]
            freespace[space].remove(newpos)
            memd.pop(pos)
            memd[newpos] = (id_, L)
            if space-L > 0:
                freespace[space-L].append(newpos+L)

CS1 = 0
for pos in memd:
    id_,x = memd[pos]
    for i in range(x):
        CS1 += id_*(pos+i)
print('part2',CS1)
tend=time.time()
print(round(tend-tstart,5))

#part1
x = 0
while x < len(mem):
    if mem[x] == '.':
        mem[x] = mem[-1]
        mem = mem[:-1]
        while mem[-1]=='.':
            mem = mem[:-1]
    x += 1

CS = 0
for i,x in enumerate(mem):
    #print(f'{i} * {x} = {i*x}')
    CS += i*x
print('part1',CS)
tend=time.time()

print(round(tend-tstart,5))

