################################################################################
# Description:                                                                 #
# From:                                                                        #
# Author: Michael Post                                                         #
# Date Started: 20170815                                                       #
################################################################################


#########################
#    Imports & Setup    #
#########################
from __future__ import division

############################################################
#                 Program Starts Here                      #
############################################################

def average(array):
    my_set = set(array)
    set_len = len(my_set)
    set_sum = 0
    while my_set:
        set_sum += my_set.pop()

    return set_sum / set_len









# End of File
# ==============================================================================