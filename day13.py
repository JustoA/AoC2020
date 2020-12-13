import inp  # my [REDACTED] input parser


def main():
    instream = inp.parse_file_str()
    base_time = int(instream[0])
    busses = instream[1].split(',')
    best = (0, 9999999999999999999999999999999999999)
    for bus in busses:
        if bus != 'x':
            cycletime = int(bus)
            while cycletime <= base_time:
                cycletime += int(bus)
            if cycletime - base_time < best[1]:
                best = (bus, cycletime - base_time)
    return best


def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_euclidean(b % a, a)
        return g, x - (b // a) * y, y


def modular_inverse(a, m):
    return extended_euclidean(a, m)[1] % m  # mod m for negative results


# reference: https://en.wikipedia.org/wiki/Chinese_remainder_theorem#General_case

def crt(a_s, n_s):
    while len(a_s) > 1:  # we still got work to do!

        # solve the system two steps at a time.
        # bezout's:
        # n1 m1 +  m2 n2 = 1 <-- compute with extended euclid
        # n2m2 = 1 mod n1     m2 = inverse(n2,n1)
        # n1m1 = 1 mod n2     m1 = inverse(n1,n2)
        # thanks wikipedia,
        # solution a1 m2 n2 + a2 m1 n1
        new_a = a_s[0] * modular_inverse(n_s[1], n_s[0]) * n_s[1] +  \
                a_s[1] * modular_inverse(n_s[0], n_s[1]) * n_s[0]
        new_n = n_s[0] * n_s[1]
        # we have the new equation
        # x = a_1,2 mod n1n2
        # now iterate on the algorithm: remove the old n's
        # and a's and place our new ones, and run again. This works because coprime magic. Crypto finally paying off
        n_s = [new_n] + n_s[2:]
        a_s = [new_a % new_n] + a_s[2:]

    # only thing left is our result.
    return a_s[0]


def main2():
    instream = inp.parse_file_str()[1]
    busses = instream.split(',')

    # i just did this in crypto lol

    a_s = []
    n_s = []

    for bus in busses:
        if bus == 'x':
            continue
        # print(f'x = {-busses.index(bus)} mod {bus}')
        a_s.append(-(busses.index(bus)))
        n_s.append(int(bus))

    return crt(a_s, n_s)


print(f'part 1: {main()}')
print(f'part 2: {main2()}')  # i learned the power of python 3.6 format strings
