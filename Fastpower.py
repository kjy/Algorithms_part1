
# Calculate a^b, where a & b are positive integers
# Here (b/2) denotes the floor function, that is, the largest integer less than
# or equal to x. 

def FastPower(a,b):
    if b == 1:
        return a
    else:
        c = a*a
        answer = FastPower(c,(b/2))
    if b%2 != 0:
        return (a*answer)
    else:
        return answer
                