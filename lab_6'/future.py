def future(a, *mass, **const, ):
    crit_mass = sum(const.values()) + a

    total_mass = sum(mass)

    if total_mass < crit_mass:
        return "ACCELERATION"
    elif total_mass > crit_mass:
        return "DECELERATION"
    else:
        return "UNCHANGED"