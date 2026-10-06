use std::io::{self, Read};
use std::collections::HashSet;
fn main() {
    let mut input=String::new(); io::stdin().read_to_string(&mut input).expect("stdin");
    let v:Vec<i32>=input.split_whitespace().map(|s|s.parse().expect("integer expected")).collect();
    if v.len()<7 || v[6]<0 || v.len()!=7+2*v[6] as usize { eprintln!("invalid input"); std::process::exit(2); }
    let blocked:HashSet<_>=v[7..].chunks_exact(2).map(|p|(p[0],p[1])).collect();
    let answer=spatial_search::astar(v[0],v[1],&blocked,(v[2],v[3]),(v[4],v[5]));
    println!("{}",answer.map(|n|n as i64).unwrap_or(-1));
}
