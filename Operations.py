#p = 103  


# https://stackoverflow.com/questions/61851700/scalar-multiplication-on-elliptic-curves
a = -7
b = 10   

def add(P, Q):
    if P is None or Q is None: # check for the zero point 
        return P or Q
    xp, yp = P
    xq, yq = Q
    if xp == xq:
        return double(P)
    m = (yp - yq) / (xp - xq)
    xr = m**2 - xp - xq
    yr = yp + m * (xr - xp)
    return (xr, -yr)

def double(P): 
    if P is None:
        return None 
    xp, yp = P 
    m = (3 * xp ** 2 + a) / (2 * yp) 
    xr = m**2 - 2*xp 
    yr = yp + m * (xr - xp) 
    return (xr, -yr)

def bits(n):
    # Convert integer to binary string
    binary_string = bin(n)[2:]
    # Ensure the binary string has the desired length by padding with zeros if necessary
    binary_string = binary_string.zfill(10)
    return binary_string

# Example usage:
result = bits(10)
print(result)


def double_and_add(n, P):
    result = None # This is our zero point
    addend = P
    for b in bin(n)[2:][::-1]:
        if b:
            result = add(result, addend)
        addend = double(addend)
    return result

print(double_and_add(151, (3,4)))
