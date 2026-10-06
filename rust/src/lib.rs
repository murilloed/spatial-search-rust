use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap, HashSet};
pub type Point = (i32, i32);
pub fn astar(width:i32,height:i32,blocked:&HashSet<Point>,start:Point,goal:Point)->Option<u32> {
    let inside=|p:Point| p.0>=0 && p.1>=0 && p.0<width && p.1<height;
    if !inside(start) || !inside(goal) || blocked.contains(&start) || blocked.contains(&goal) { return None; }
    let h=|p:Point| p.0.abs_diff(goal.0)+p.1.abs_diff(goal.1);
    let mut queue=BinaryHeap::new(); let mut dist=HashMap::new();
    queue.push(Reverse((h(start),0u32,start))); dist.insert(start,0u32);
    while let Some(Reverse((_,g,p)))=queue.pop() {
        if dist.get(&p)!=Some(&g) { continue; }
        if p==goal { return Some(g); }
        for (dx,dy) in [(1,0),(-1,0),(0,1),(0,-1)] {
            let n=(p.0+dx,p.1+dy);
            if inside(n) && !blocked.contains(&n) && g+1<*dist.get(&n).unwrap_or(&u32::MAX) {
                dist.insert(n,g+1); queue.push(Reverse((g+1+h(n),g+1,n)));
            }
        }
    }
    None
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn shortest() { assert_eq!(astar(5,5,&HashSet::new(),(0,0),(4,4)),Some(8)); }
    #[test] fn blocked() { let b=HashSet::from([(1,0),(0,1)]); assert_eq!(astar(3,3,&b,(0,0),(2,2)),None); }
    #[test] fn outside() { assert_eq!(astar(3,3,&HashSet::new(),(-1,0),(2,2)),None); }
}
