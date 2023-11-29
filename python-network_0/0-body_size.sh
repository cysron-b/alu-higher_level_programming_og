<<<<<<< HEAD
#!/bin/bash
# takes URL and displays the size of the response body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
=======
#!/bin/bash
# takes URL and displays the size of the response body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
>>>>>>> 99b8c190bdb9c890b1842a7265f69242eca2195e
