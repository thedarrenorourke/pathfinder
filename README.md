# Pathfinder

This code is my attempt to understand the breadth first search algorithm
by printing the algorithms outputs to the console.


## Breadth First Search
Demo maze:

    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]

Start at position 0,0 and then look at neighbour points

Expand and look at the neighours of the neighbours

Breadth since we expand outwards, i.e. in a queue from the original node

Once we have reached the end, we stop as we know this is the shortest route (all others in queue by definition, will be longer)

Steps:

* Pop top of queue
* Check if adjacent nodes are end 
  * if end - done
  * if not - check if is valid point in path, if so add to queue
* Add current element to 'done' queue/set
* pop next element of queue and repeat

    