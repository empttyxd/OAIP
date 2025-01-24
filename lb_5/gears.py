def gears(data, n, m):
    slv1, slv2 = {}, {}

    for i in data:

        for gear in i:
            if gear % n == 0 and gear >= n:
                a = gear // n

                if a not in slv1 and a in slv2:
                    return gear, slv2[a]
                slv1[a] = gear

            elif gear % m == 0 and gear >= m:
                rm = gear // m

                if rm not in slv2 and rm in slv2:
                    return slv2[rm], gear
                slv2[rm] = gear

    return (None, None)