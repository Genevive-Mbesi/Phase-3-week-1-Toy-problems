def check_two_integers_for_positive(a,b,c):
    count = 0
    if a > 0:
        count += 1

    if b > 0:
        count +=1

    if c > 0:
        count +=1

    if count == 2:
        return True 
    else:
        return False

print(check_two_integers_for_positive(2,4,-3))
print(check_two_integers_for_positive(-4,6,8))
print(check_two_integers_for_positive(4,-6,9))
print(check_two_integers_for_positive(-4,6,0))
print(check_two_integers_for_positive(4,6,10))
print(check_two_integers_for_positive(-14,-3,-4))
