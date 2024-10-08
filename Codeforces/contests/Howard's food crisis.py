'''A. Howard's Food crisis
Howard is in Space, he has x
 amounts of food and y
 amounts of water. He eats m
 amount of food a day and drinks n
 amount of water a day. Find how many days he can last.

He needs both water and food to be alive.

Input
The first line of input contains t
 (1≤t≤105)
 ,no. of testcases.

First line of each test case contains x
 and y
 (1≤x,y≤105)
 ,amount of food and water Howard has resp.

Second line of each test case contains m
 and n
 (1≤m,n≤105)
 ,amount of food and water Howard needs in a day resp.

Output
For each testcase ,output a single integer denoting the number of days Howard will last.
  '''

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    m, n = map(int, input().split())
    days = min(x // m, y // n)
    print(days)
