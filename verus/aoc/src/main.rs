use vstd::prelude::*;

verus! {
    use std::io::BufRead;
    use serde::Deserialize;
    use std::fs::File;

const USAGE: &'static str = "
Usage: aoc [options] filename 

Options:
    --part=<part>  part of the puzzle to rn [default: 0].
";
    //
    
    enum Sign {
	Plus,
	Minus
    }
    fn count_zero_landings( instructions:Vec<(Sign,u32)> ) -> (r:Option<u32>)
	ensures match r { Some(I) => I<instructions@.len(), None=>true}
    {
	let mut pos:u32 = 50;
	let mut hits:u32 = 0 ;
	for i in instructions {
	    let mov = i.1;
	    let sign = i.0;	    
	    let modulo = match sign {
		Sign::Plus => mov % 100,
		Sign::Minus => (100 - mov%100)%100
	    };
	    pos = pos.checked_add(modulo)?;
	    pos %= 100 ;
	    if pos == 0 {
		hits = hits.checked_add(1)?;
	    }
	}
	Some(hits)
	
    }


    fn count_zero_crossings ( instructions:Vec<(Sign,u32)> ) -> Option<(u32,u32,u32,u32)> {
	let mut pos:u32 = 50;
	let mut hits:u32 = 0 ;
	let mut twit_1: u32 = 0 ;
	let mut twit_2: u32 = 0 ;
	let mut twit_3: u32 = 0 ;
	for i in instructions {
	    let mov = i.1;
	    let sign = i.0;
	    hits = hits.checked_add( mov/100)?;	    
	    twit_3 = twit_3.checked_add( mov/100)?;
	    let modulo = match sign {
		Sign::Plus => mov % 100,
		Sign::Minus => (100 - mov%100)%100
	    };
	    match sign {
		Sign::Plus => {
		    if pos.checked_add(modulo)?%100 < pos {
			hits = hits.checked_add( 1)? ;
			twit_1 = twit_1.checked_add(1)?;
		    }
		},
		Sign::Minus => {
		    if pos > 0 && pos <= mov%100 {
			hits = hits.checked_add( 1)? ;
			twit_2 = twit_2.checked_add(1)?;
		    }
		}
	    };
	    pos = pos.checked_add(modulo)?;
	    pos %= 100 ;
	}
	Some((hits, twit_1, twit_2, twit_3))
	
    }

    #[verifier::external_body]
    fn main() {
        let args: Vec<String> = std::env::args().collect();

        // args[0] is typically the program's executable path
        // Subsequent elements are the command-line arguments
	let filename = match args.get(1) {
	    Some(f) => f,
	    None => panic!("No filename provided"),
	};
	let part = match args.get(2) {
	    Some(p) => p.parse::<u32>().unwrap_or(0),
	    None => 0,
	};
	let file = File::open(&filename).expect("Unable to open file");
	let reader = std::io::BufReader::new(file);
	let mut instructions:Vec<(Sign,u32)> = Vec::new();
	for line in reader.lines() {
	    let l = line.expect("Unable to read line");
	    let sign = match &l.chars().nth(0).expect("Empty line") {
		'R' => Sign::Plus,
		'L' => Sign::Minus,
		_ => panic!("Bad direction")
	    };
	    let mov:u32 = l[1..].parse().expect("Bad number");
	    instructions.push( (sign,mov) );
	}
	match part {
	    1 => {
		let res = count_zero_crossings(instructions).expect("Overflow during calculation");
		println!("Result: {} {} {} {}", res.0, res.1, res.2, res.3);
	    },
	    _ => {
		let res = count_zero_landings(instructions).expect("Overflow during calculation");
		println!("Result: {}", res);
	    }
	}
	assert(1 == 0 + 1);
    }


    spec fn min(x: int, y: int) -> int {
    if x <= y {
        x
    } else {
        y
    }
}

fn test() {
    assert(min(10, 20) == 10); // succeeds
    assert(min(100, 200) == 100); // succeeds
}
} // verus!
