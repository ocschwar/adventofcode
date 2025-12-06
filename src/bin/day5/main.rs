use vstd::prelude::*;
/* day 5*/


verus! {
//    extern crate serde;
    use std::io::BufRead;
//    use serde::Deserialize;
    use std::fs::File;

    fn min(a:u64, b:u64) -> u64 {
	if a < b {
	    a
	} else {

	    b
	}
    }
    fn max(a:u64, b:u64) -> u64 {
	if a > b {
	    a
	} else {

	    b
	}
    }
    
#[derive(Clone, Copy, PartialEq, Eq, Debug)]
    struct Range {
	start:u64,
	end:u64
    }

    impl Range {
	fn new(start:u64, end:u64) -> Range
	    requires start <= end
	{
	    Range {start:start, end:end}
	}
	
	fn inrange(self, point:u64) -> (r:bool)
	    ensures match r {
		true => self.start <= point && point <= self.end,
		false => point < self.start || point > self.end
	    }
	{
	    self.start <= point && point <= self.end
	}

	fn overlap(self, other:Range) -> (r:bool)
	    ensures match r {
		true => {
		    self.end >= other.start ||
			other.end >= self.start
		},
		false => {
		    self.end < other.start ||
			other.end < self.start
		}
	    }
	{
	    (self.end >= other.start && self.start <= other.end ) ||
		(other.end >= self.start  && other.start <= self.end)
	}

	fn merge (self, other:Range) -> Range {
	    Range {
		start: min(self.start,other.start),
		end: max(self.end, other.end)
	    }
	}

    }
    
    proof fn test(x:int, y:int)
	ensures x+y==y+x
    {}
// #[verifier::external_body]
    fn merge_ranges(ranges:& Vec<Range>) -> (Vec<Range>,bool)
	ensures |merged:Vec<Range>, changed:bool| {
	    // postcondition: all ranges in merged are non-overlapping
	    forall|i:usize, j:usize| 0 <= i && i < merged.len() && 0 <= j && j < merged.len() && i != j ==> !merged[i@].overlap(merged[j@])
	}

    {
    let mut merged:Vec<Range> = Vec::new();
    let mut changed = false;
    for r in ranges
	invariant merged.len() <= ranges.len(),
    
    {

//	println!("Considering range: {:?}\n", r);
	let mut to_merge:Option<usize> = None;
	let mut i = 0 ;
	for mr in merged.iter() {
//	    println!("  Comparing to merged range: {:?}\n", mr);
	    if mr.overlap(*r) {
//		println!("found overlap between {:?} and {:?}\n", mr, r);
		to_merge = Some(i);
		break;
	    }
	    i+=1;
	}
	if let Some(i) = to_merge {
//	    println!("  Merging with range: {:?}\n", merged[i]);
	    let new_range = merged[i].merge(*r);
	    merged[i] = new_range;
	} else {
	    merged.push(r.clone());
	}
    }
    (merged, changed)
}

    
// src/bin/my_program.rs
 #[verifier::external_body]
 fn main() {
     println!("Hello from my new binary!");
     let args: Vec<String> = std::env::args().collect();
     
     // args[0] is typically the program's executable path
     // Subsequent elements are the command-line arguments
     let filename = match args.get(1) {
	 Some(f) => f,
	 None => panic!("No filename provided"),
     };
     let part = match args.get(2) {
	 Some(p) => p.parse::<u64>().unwrap_or(0),
	 None => 0,
     };
     let file = File::open(&filename).expect("Unable to open file");
     let reader = std::io::BufReader::new(file);
     let mut ranges:Vec<Range> = Vec::new();
     let mut candidates:Vec<u64>  =  Vec::new();
     for line in reader.lines() {
	 let l = line.expect("Unable to read line");
	 if l.contains("-") {	     
	     let parts:Vec<&str> = l.trim().split("-").collect();
	     let start = parts[0].parse::<u64>().unwrap();
	     let end = parts[1].parse::<u64>().unwrap();
	     ranges.push(Range{start:start, end:end});
	 } else if l.len() > 0 {
	     let num = l.trim().parse::<u64>().unwrap();
	     candidates.push(num);
	 }
     }
     ranges.sort_by(|a, b| a.start.cmp(&b.start));
     println!("Read {} ranges and {} candidates", ranges.len(), candidates.len());
     
     if part == 0 {
	 let mut merged = ranges.clone();
	 let mut changed = true;
	 while changed {
	     (merged, changed) = merge_ranges(&merged);
	 }
	 println!("Read {} ranges and {} candidates", merged.len(), candidates.len());
	 let mut total:u64 = 0;
	 for r in merged {
	     total += r.end - r.start + 1;
	 }
	 println!("Total: {}", total);
     } else {
	 let mut count:u64 = 0;
	 for c in candidates {
	     for r in &ranges {
		 if r.inrange(c) {
		     count += 1;
		     break;
		 }
	     }
	 }
	 println!("Allowed candidates: {}", count);
     }

 }
} // verus!    
