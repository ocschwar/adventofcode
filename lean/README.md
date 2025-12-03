# hello

Note: This linter can be disabled with `set_option linter.unusedVariables false`
Build completed successfully (8 jobs).
➜  lean git:(main) ✗ .lake/build/bin/hello  && echo foo 
Hello, FOOBAR world!
➜  lean git:(main) ✗ .lake/build/bin/hello test.lean && echo foo  
def main : IO Unit := IO.println "Hello, world!"
foo
➜  lean git:(main) ✗ .lake/build/bin/hello test.lean && echo foo || echo $?
def main : IO Unit := IO.println "Hello, world!"
foo
➜  lean git:(main) ✗ .lake/build/bin/hello testlean && echo foo || echo $? 
File not found: testlean
File not found 
2
➜  lean git:(main) ✗ .lake/build/bin/hello  && echo foo || echo $?        
Hello, FOOBAR world!
1
➜  lean git:(main) ✗ 
