################################################################################
# Description: Best Travel                                                     #
# From: https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python    #
# Author: Michael Post                                                         #
# Date Started: 20171129                                                       #
################################################################################
"""
John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between
these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary that he doesn't want to drive more
than t = 174 miles and he will visit only 3 towns.

Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible

to please Mary - but less than t - to please John- ?
Example:

With list ls and 3 towns to visit they can make a choice between:
[50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].

The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding
towns is [55, 58, 60].

The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters
t (maximum sum of distances, integer >= 0),
k (number of towns to visit, k >= 1) and
ls (list of distances, all distances are positive or null integers and this list has at least one element).
The function returns the "best" sum ie the biggest possible sum of k distances less than or equal to the given limit t,
if that sum exists, or otherwise nil, null, None, Nothing

Examples:
ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163
xs = [50] choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, Rust, Swift, Go)
ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228
"""

############################################################
#                 Program Starts Here                      #
############################################################
def cbs1(t, k, ls):
    import itertools
    """
    :param t: max distance between towns
    :param k: max number of towns to visit
    :param ls: list of distance between towns
    :return: best_sum, the largest sum of distances between towns that works
    """

    # if zero distance then No travel can be done so return None
    if t == 0:
        return None

    best_sum = None

    # if the sum of all towns is less then, eq to max then return sum all
    if sum(ls) <= t and len(ls) <= k:
        return sum(ls)

    if k > len(ls):
        k = len(ls)


    # loop through all other combinations
    for next_size_down in range(k, 1, -1):
        tmp_list = list(itertools.combinations(ls,next_size_down))
        for trip_list in tmp_list:
            if sum(trip_list) > best_sum and sum(trip_list) <= t:
                best_sum =sum(trip_list)



    return best_sum


def cbs2(t, k, ls):
    import itertools
    """
    :param t: max distance between towns
    :param k: number of towns needed to visit
    :param ls: list of distance between towns
    :return: best_sum, the largest sum of distances between towns that works
    """

    # if zero distance then No travel can be done so return None
    if t == 0:
        return None

    # if more towns to visit then towns available return None
    if k > len(ls):
        return None

    best_sum = None


    # loop through all other combinations
    tmp_list = list(itertools.combinations(ls,k))
    for trip_list in tmp_list:
        if sum(trip_list) > best_sum and sum(trip_list) <= t:
            best_sum =sum(trip_list)
            print "\n" + str(trip_list) + " is " + str(best_sum)



    return best_sum


def choose_best_sum_Turned_IN(t, k, ls):
    import itertools
    """
    :param t: max distance between towns
    :param k: number of towns needed to visit
    :param ls: list of distance between towns
    :return: best_sum, the largest sum of distances between towns that works
    """

    # # if zero distance then No travel can be done so return None
    # if t == 0:
    #     return None
    #
    # # if more towns to visit then towns available return None
    # if k > len(ls):
    #     return None

    tmp_list = [sum(trip) if sum(trip) <= t else 0 for trip in list(itertools.combinations(ls,k))]
    tmp_list.append(0)
    best_sum = max(tmp_list)
    if best_sum == 0:
        return None()
    return best_sum

def choose_best_sum(t, k, ls):
    import itertools
    """
    :param t: max distance between towns
    :param k: number of towns needed to visit
    :param ls: list of distance between towns
    :return: best_sum, the largest sum of distances between towns that works
    """

    # # if zero distance then No travel can be done so return None
    # if t == 0:
    #     return None
    #
    # # if more towns to visit then towns available return None
    # if k > len(ls):
    #     return None

    # tmp_list = [sum(trip) if sum(trip) <= t else 0 for trip in list(itertools.combinations(ls,k))]
    # tmp_list.append(0)
    best_sum = max([0] + [sum(trip) for trip in list(itertools.combinations(ls,k)) if sum(trip) <= t])
    if best_sum == 0:
        return None()
    return best_sum



import itertools
def choose_best_sum_from_them(t, k, ls):
    try:
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None





# End of File
# ==============================================================================

