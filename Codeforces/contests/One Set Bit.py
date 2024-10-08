''' B. One Set Bit
Sheldon is working on a problem involving binary numbers. Given a positive integer x
, he wants to determine if the binary representation of x
 contains exactly one 1.

For example, the number 4 (which is 1002
 in binary) has exactly one 1 in its binary representation.

Your task is to help Sheldon determine if a given number x
 has exactly one 1 in its binary representation.

Input
The first line of the input consists of a single integer T
 (1≤T≤105)
Next T
 lines consists of a single integer x
 (1≤x≤109)
 — the numbers to check.

Output
Output "YES" if the binary representation of x
 contains exactly one 1. Otherwise, output "NO".
'''
t = int(input())
 
for _ in range(t):
    x = int(input())
    count = 0
    while x > 0:
        if x % 2 == 1:
            count += 1
        if count > 1:
            break
        x = x // 2
    if count == 1:
        print("YES")
    else:
        print("NO")

