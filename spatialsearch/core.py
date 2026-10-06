import heapq
def search(width,height,blocked,start,goal,heuristic=True):
    if width<1 or height<1: raise ValueError('positive grid required')
    def inside(p): return 0<=p[0]<width and 0<=p[1]<height
    if not inside(start) or not inside(goal): raise ValueError('endpoints outside grid')
    blocked=set(map(tuple,blocked))
    if start in blocked or goal in blocked: return {'path':None,'expanded':0}
    def h(p): return abs(p[0]-goal[0])+abs(p[1]-goal[1]) if heuristic else 0
    queue=[(h(start),0,start)]; dist={start:0}; parent={}; expanded=0
    while queue:
        _,g,p=heapq.heappop(queue)
        if g!=dist[p]: continue
        expanded+=1
        if p==goal:
            path=[p]
            while p in parent: p=parent[p]; path.append(p)
            return {'path':list(reversed(path)),'expanded':expanded}
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            n=(p[0]+dx,p[1]+dy)
            if inside(n) and n not in blocked and g+1<dist.get(n,float('inf')):
                dist[n]=g+1; parent[n]=p; heapq.heappush(queue,(g+1+h(n),g+1,n))
    return {'path':None,'expanded':expanded}

def rust_search(binary,width,height,blocked,start,goal):
    import subprocess
    points=list(map(tuple,blocked))
    payload=' '.join(map(str,[width,height,*start,*goal,len(points),*[v for p in points for v in p]]))
    result=subprocess.run([str(binary)],input=payload,text=True,capture_output=True,check=True,timeout=30)
    return int(result.stdout.strip())  # -1 indicates no path; otherwise shortest length.
