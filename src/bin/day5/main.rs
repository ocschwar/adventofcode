use vstd::prelude::*;
/* day 5*/


verus! {
//    extern crate serde;
    use std::io::BufRead;
//    use serde::Deserialize;
    use std::fs::File;


    struct Range {
	start:u32,
	end:u32
    }

    impl Range {
	fn overlap(self, other) -> bool {
	    self.stop >= other.start ||
		other.stop >= self.stop
	}

	fn merge (self, other) -> Range {
	    Range {
		start: min(self.start,other.start),
		stop: max(self.stop, other.stop)
	    }
	}

    }

    
    proof fn test(x:int, y:int)
	ensures x+y==y+x
    {}

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
	 Some(p) => p.parse::<u32>().unwrap_or(0),
	 None => 0,
     };
     let file = File::open(&filename).expect("Unable to open file");
     let reader = std::io::BufReader::new(file);
     
 }
}
