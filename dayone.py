dayone = [sum(map(int,x.split())) for x in open("day_one.txt","rt").read().strip().split("\n\n")]
print(max(dayone),sum(sorted(dayone)[-3:]))
