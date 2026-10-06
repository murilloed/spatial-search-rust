import argparse,json,random,time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from .core import search,rust_search
def task(args): return search(*args)
def main():
    p=argparse.ArgumentParser(); p.add_argument('--size',type=int,default=30); p.add_argument('--seed',type=int,default=7)
    p.add_argument('--rust-binary'); a=p.parse_args()
    if a.size<2: p.error('size must be >=2')
    rng=random.Random(a.seed); n=a.size
    blocked=[(x,y) for x in range(n) for y in range(n) if x>0 and y<n-1 and rng.random()<.2]
    args=(n,n,blocked,(0,0),(n-1,n-1)); start=time.perf_counter(); astar=search(*args); at=time.perf_counter()-start
    start=time.perf_counter(); dijkstra=search(*args,heuristic=False); dt=time.perf_counter()-start
    start=time.perf_counter()
    with ProcessPoolExecutor(max_workers=2) as pool: batch=list(pool.map(task,[args]*4))
    report={'synthetic':True,'seed':a.seed,'size':n,'astar':{'length':len(astar['path'])-1 if astar['path'] else None,'expanded':astar['expanded'],'seconds':at},
            'dijkstra':{'length':len(dijkstra['path'])-1 if dijkstra['path'] else None,'expanded':dijkstra['expanded'],'seconds':dt},
            'parallel_batch_seconds':time.perf_counter()-start,'parallel_jobs':len(batch),
            'rust_validated':False}
    if a.rust_binary:
        length=rust_search(a.rust_binary,*args); report['rust_length']=length
        expected=report['astar']['length']; report['rust_validated']=length==(-1 if expected is None else expected)
        if not report['rust_validated']: raise RuntimeError('Python/Rust mismatch')
    Path('artifacts').mkdir(exist_ok=True); Path('artifacts/report.json').write_text(json.dumps(report,indent=2)); print(json.dumps(report,indent=2))
if __name__=='__main__': main()
