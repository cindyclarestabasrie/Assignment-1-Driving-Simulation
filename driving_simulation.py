u = 0
t = int(input("Time:"))
print(t, "s")
a = int(input("Acceleration: "))
print(a, "m/s^2")
s = int(input("Distance: "))
print(s, "m")
v_limit = 60
x = 0

print("\nThe \"*\" indicates every 10m")

for duration in range (0, t+1):
    print("\nDuration: ", end="")
    print(duration, "s")
    d_10 = u * x + (1/2) * a * (x * x)
    d = d_10 / 10
    x += 1
    dc = 0
    import math
    dc = math.floor(d)
    print("Distance: ", "*"*dc)

v = (u**2 + 2 * a * d_10) ** 0.5

if v > v_limit:
    print("\nThe person went over the speed limit. (Max speed was " + str(v) + "m/s)")
else:
    print("\nThe person did not go over the speed limit. (Max speed was " + str(v) + "m/s)")

if d_10 >= s:
    print("The person reached the destination. (Reached " + str(d_10) + "m)")
else:
    print("The person did not reach the destination (Reached " + str(d_10) + "m)")
