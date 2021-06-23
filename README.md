# Dijkstra's Algorithm - Optimal Delivery
In this task, we wish to travel from one city to another. Traveling is costly, so we want to get
to our destination as cheaply as possible. However, there is a way we can make some money on
our way. We can pick up an item from one particular city, and deliver it to another particular
city. We want to determine whether it will be cheaper to perform this delivery during our
journey, or just go directly to our destination.

## Input
**n** is the number of cities. The cities are numbered [0..n-1].

**roads** is a list of tuples. Each tuple is of the form (u,v,w). Each tuple represents an road
between cities u and v. w is the cost of traveling along that road, which is always non-negative.
Note that roads can be traveled in either direction, and the cost is the same. There is at most
1 road between any pair of cities. roads will represent a simple, connected graph

**start and end** are each an integer in the range [0..n-1]. They represent the city you start
(from now on called the "start city") and the city you need to reach (from now on called the
"end city"), respectively.

**delivery** is a tuple containing 3 values. The first value is the city where we can pick up the
item (from now on called the "pickup city"). The second value is the city where we can deliver
the item (from now on called the "delivery city"). The third value is the amount of money we
can make if we deliver the item from the pickup city to the delivery city.

## Output
**opt_delivery** returns a tuple containing 2 elements. The first element is the cost of travelling
from the start city to the end city. This cost includes the profit we make from the delivery, if
we choose to make the delivery (so it could be negative, in the event that the delivery is worth
more than the total travelling cost).

The second element of the tuple is a list of integers. This list represents the cities we need to
travel to in order to achieve the cheapest cost (in order). It should start with the start city,
and end with the end city. As seen in the example below, it is possible to need to visit a city
twice.

## Example
```
n = 4
roads = [(0,1,3),(0,2,5),(2,3,7),(1,3,20)]
start = 0
end = 1
delivery = (2,3,25)
profit = 25
opt_delivery(n, roads, start, end, delivery)
>>> (2, [0,2,3,2,0,1])
delivery = (2,3,20)
opt_delivery(n, roads, start, end, delivery)
>>> (3, [0,1])
delivery = (2,3,100)
opt_delivery(n, roads, start, end, delivery)
>>>(-73, [0,2,3,2,0,1])

```

## Complexity
opt_delivery must run in O(Rlog(N)) where
- R is the total number of roads
- N is the total number of cities

### Disclaimer
1. This case study derives from my school assignment.
2. Details of the actual case study has been sanitized and changed.

