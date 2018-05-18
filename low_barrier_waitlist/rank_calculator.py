
def calc_rank(age, is_veteran=False, has_disability=False):
    """
    Calculate a participant's rank. A higher number is higher ranked (top of the list).
    (i.e., Reverse this when sorting.)

    Change this function to change the ranking algorithm.
    """
    # This is the base vulnerability score
    factor = 1.0

    age_multiplier = {
        range(0, 29): 1,
        range(30, 39): 1.04,
        range(40, 49): 1.63,
        range(50, 59): 2.7,
        range(60, 69): 4.28,
        range(70, 120): 11.67
    }

    # find and apply the age rr multiplier
    factor *= [age_multiplier[key] for key in age_multiplier if age in key][0]

    # is the participant a vet? Apply the vet rr multiple
    if is_veteran:
        factor *= 1.23

    # is the participant disabled? Apply the disabled rr multipler
    if has_disability:
        factor *= 1.5

    # result is a number between 1 and about 22
    return factor
