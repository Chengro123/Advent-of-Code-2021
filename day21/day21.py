position1, position2 = 10, 9 
points1, points2 = 0, 0
dice = list(range(1, 101))*10000
board = [1,2,3,4,5,6,7,8,9,10]*100000

n = 0
while True:

    position1 += sum(dice[3*(2*n):3*(2*n+1)])
    points1 += board[position1-1]
    if points1 >= 1000:
        print((6*n+3) * points2)
        break

    position2 += sum(dice[3*(2*n+1):3*(2*n+2)])
    points2 += board[position2-1]
    if points2 >= 1000:
        print(6*(n+1) * points1)
        break

    n += 1

p1 = 7-1
p2 = 2-1
DP = {} 
def count_win(p1, p2, s1, s2):

  if s1 >= 21:
    return (1,0)
  if s2 >= 21:
    return (0, 1)
  if (p1, p2, s1, s2) in DP:
    return DP[(p1, p2, s1, s2)]

  ans = (0,0)

  for d1 in [1,2,3]:
    for d2 in [1,2,3]:
      for d3 in [1,2,3]:
        new_p1 = (p1+d1+d2+d3)%10
        new_s1 = s1 + new_p1 + 1

        x1, y1 = count_win(p2, new_p1, s2, new_s1)
        ans = (ans[0]+y1, ans[1]+x1)
  DP[(p1, p2, s1, s2)] = ans
  return ans

print(max(count_win(p1, p2, 0, 0)))
