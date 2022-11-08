# Dijkstra-s-algorithm-application-in-Path-Planning
Path Planning using Dijkstra Algorithm
-  By:Farkad Adnan فرقد عدنان -
- https://linktr.ee/farkadadnan

 - E-mail: farkad.hpfa95@gmail.com 
- inst : farkadadnan 
- #farkadadnan , #farkad_adnan , فرقد عدنان# 
- FaceBook: كتاب عالم الاردوينو 
- inst : arduinobook
1. #كتاب_عالم_الاردوينو
2. #كتاب_عالم_الآردوينو 

* facebook : https://www.facebook.com/profile.php?id=100002145048612
* instagram:  https://www.instagram.com/farkadadnan/
* linkedin : https://www.linkedin.com/in/farkad-adnan-499972121/

 <p>
 <a href='https://mobile.twitter.com/farkadadnan'>
        <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/farkadadnan?label=%40farkadadnan&style=social" alt='Twitter' align="center"/>
    </a>
</p>


# Introduction to the Project
In this project, the Dijkstra motion planning algorithm was used on a point robot and rigid robot to navigate in a configuration space consisting of static obstacles.


# Dijkstra's algorithm
- (ˈdaɪkstrəz/ DYKE-strəz) is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.

- The algorithm exists in many variants. Dijkstra's original algorithm found the shortest path between two given nodes,[6] but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

# Description
Suppose you would like to find the shortest path between two intersections on a city map: a starting point and a destination. Dijkstra's algorithm initially marks the distance (from the starting point) to every other intersection on the map with infinity. This is done not to imply that there is an infinite distance, but to note that those intersections have not been visited yet. Some variants of this method leave the intersections' distances unlabeled. Now select the current intersection at each iteration. For the first iteration, the current intersection will be the starting point, and the distance to it (the intersection's label) will be zero. For subsequent iterations (after the first), the current intersection will be a closest unvisited intersection to the starting point (this will be easy to find).



# Results
![Capture1](https://user-images.githubusercontent.com/35774039/200636319-d0ec076f-c9ea-4c4d-a5d3-65606bf2501a.PNG)

![Capture2](https://user-images.githubusercontent.com/35774039/200636366-e325d353-0ecc-4145-a329-5abea8ba4195.PNG)

```

1  function Dijkstra(Graph, source):
2      dist[source] ← 0                           // Initialization
3
4      create vertex priority queue Q
5
6      for each vertex v in Graph.Vertices:
7          if v ≠ source
8              dist[v] ← INFINITY                 // Unknown distance from source to v
9              prev[v] ← UNDEFINED                // Predecessor of v
10
11         Q.add_with_priority(v, dist[v])
12
13
14     while Q is not empty:                      // The main loop
15         u ← Q.extract_min()                    // Remove and return best vertex
16         for each neighbor v of u:              // Go through all v neighbors of u
17             alt ← dist[u] + Graph.Edges(u, v)
18             if alt < dist[v]:
19                 dist[v] ← alt
20                 prev[v] ← u
21                 Q.decrease_priority(v, alt)
22
23     return dist, prev
```

# Code
![Capture](https://user-images.githubusercontent.com/35774039/200636416-02bfb691-550e-40e0-bf3f-74d1f8f52c5d.PNG)



# REFERENCES
- [1] Controversial, see Moshe Sniedovich (2006). "Dijkstra's algorithm revisited: the dynamic programming connexion". Control and Cybernetics. 35: 599–620. and below part. Cormen et al. 2001
- [2] Richards, Hamilton. "Edsger Wybe Dijkstra". A.M. Turing Award. Association for Computing Machinery. Retrieved 16 October 2017. At the Mathematical Centre a major project was building the ARMAC computer. For its official inauguration in 1956, Dijkstra devised a program to solve a problem interesting to a nontechnical audience: Given a network of roads connecting cities, what is the shortest route between two designated cities?
 - [3]Frana, Phil (August 2010). "An Interview with Edsger W. Dijkstra". Communications of the ACM. 53 (8): 41–47. doi:10.1145/1787234.1787249.
 - [4]Dijkstra, E. W. (1959). "A note on two problems in connexion with graphs" (PDF). Numerische Mathematik. 1: 269–271. doi:10.1007/BF01386390. S2CID 123284777.
 - [5]Mehlhorn, Kurt; Sanders, Peter (2008). "Chapter 10. Shortest Paths" (PDF). Algorithms and Data Structures: The Basic Toolbox. Springer. doi:10.1007/978-3-540-77978-0. ISBN 978-3-540-77977-3.
