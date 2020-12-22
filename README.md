# CS580 Assignment 1

## Program Requirements

- Python version 3.7+

## Execution Instructions

The `main.py` file is the file specified to be run; attempting to run any other file will result in no output. The program should be run following this format:

```bash
# Linux
python3 main.py [search algorithm]

# Windows
py .\main.py [search algorithm]
```

The following arguements are valid:

| Arguement      | Search Algorithm    
| :------------: | :-----------: 
| `breadth`      | Breadth First Search   
| `depth`        | Depth First Search
| `greedy`       | Greedy Best First Search  
| `a_star`       | A* Search 

Then, you will be asked to input an integer, representing the size of the pegboard to be generated. For example, inputting a 4 will generate a 4x4 pegboard. Afterwards, the chosen search algorithm will run.

- Pegboard sizes **must** be greater than or equal to **4**, but less than or equal to **8**.

## Solutions

> Solution times for larger boards will vary greatly.

### Breadth First Search

Breadth First Search took the longest to find a solution (if there was one), as it works its was down the fringe with no heuristic or path cost in mind. Running a size greater than **four** takes a considerable amount of time. I let a 5x5 board run for approximately **3 days**, and the program was still running; however, it was possible that there was no solution. Typically for 4x4 boards, if there was no solution, the algorithm explored **1686** or **2114** unique nodes; this was the same thoughout all search algorithms. If there was a solution to be found, it was found after **1869** unique nodes.

*4x4 Pegboard - Example solutions*

```
0010
0000
0000
0000

-- Goal state found! --
                        
Unique nodes visited: 1869
Execution Time: 0.44266295433044434 seconds


0000
0000
0000
0010

-- Goal state found! --
                        
Unique nodes visited: 1870
Execution Time: 0.4429311752319336 seconds
```

### Depth First Search

Depth First Search took much less time than Breadth First Search. The search algorithm is generally much more memory efficient, as you are very likely to find a solution without having to traverse throughout all branches like Breadth First Search. In some instances, the solution was found extremely fast. This held true for the larger pegboards as well.

*4x4 Pegboard - Example solution*

```
0010
0000
0000
0000

-- Goal state found! --
                        
Unique nodes visited: 37
Execution Time: 0.005750179290771484 seconds
```

*5x5, 6x6, and 7x7 Pegboards - Example solutions*

```
00000
00000
00001
00000
00000

-- Goal state found! --
                        
Unique nodes visited: 4693
Execution Time: 1.916182279586792 seconds
```

```
000000
000000
000000
100000
000000
000000

-- Goal state found! --
                        
Unique nodes visited: 1291
Execution Time: 0.29334592819213867 seconds
```

```
0010000
0000000
0000000
0000000
0000000
0000000
0000000

-- Goal state found! --
                        
Unique nodes visited: 7072
Execution Time: 8.628918170928955 seconds
```

### Greedy Best First Search

Greedy Best First Search is Depth First Search with an admissible heuristic. This heuristic makes the search algorithm able to find the solution even **faster** in some instances, but a heuristic can be wrong and make it take much longer to find a solution. This was not particularly an issue with the 4x4 boards however. The admissible heuristic selected for this search algorithm was **Manhatten Distance**, which is the sum of all pegs' approximate distance from the center of the board.

*4x4 Pegboard - Example solutions*

```
0000
0000
1000
0000

-- Goal state found! --

Unique nodes visited: 14
Execution Time: 0.0018162727355957031 seconds
```

```
0000
1000
0000
0000

-- Goal state found! --

Unique nodes visited: 85
Execution Time: 0.007805585861206055 seconds
```

*5x5 and 6x6 Pegboards - Example solutions*

```
00000
00000
00000
00000
00100

-- Goal state found! --

Unique nodes visited: 711
Execution Time: 0.11204791069030762 seconds
```

```
000000
000000
000000
001000
000000
000000

-- Goal state found! --
                        
Unique nodes visited: 665
Execution Time: 0.17257356643676758 seconds
```

### A* Search

A* Search makes use of an admissible heuristic, such as **Manhatten Distance**, as well as a method to determine the **path cost**. This path cost method keeps track of how far the current state is from the initial state. Pairing these two methods results in finding the optimal solution. Typically, A* runs like Greedy Best First Search for 4x4 boards as there is not as much path cost to consider; however, in larger boards, the path cost implementation becomes more relevant.

*4x4 Pegboard - Example solutions*

```
0000
0000
0001
0000

-- Goal state found! --
                        
Unique nodes visited: 20
Execution Time: 0.002652406692504883 seconds
```

```
0100
0000
0000
0000

-- Goal state found! --
                        
Unique nodes visited: 27
Execution Time: 0.003367185592651367 seconds
```

*5x5 and 6x6 Pegboards - Example solutions*

```
00000
00000
00000
00000
00100

-- Goal state found! --
                        
Unique nodes visited: 4818
Execution Time: 2.366917848587036 seconds
```

```
000000
000000
000000
000000
000000
010000

-- Goal state found! --
                        
Unique nodes visited: 925
Execution Time: 0.2054908275604248 seconds
```