"""LOOPS
While you're here
The while loop is similar to an if statement: it executes the code inside of it if some condition is true. The difference is that the while loop will continue to execute as long as the condition is true. In other words, instead of executing if something is true, it executes while that thing is true.

Line 6 decides when the loop will be executed. So, "as long as count is less than 5," the loop will continue to execute. Line 8 increases count by 1. This happens over and over until count equals 5."""


count = 0

if count < 5:
    print "Hello, I am an if statement and count is", count

while count < 10:
    print "Hello, I am a while and count is", count
    count += 1