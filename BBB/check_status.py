# need this to chain SysID's together
from itertools import chain

# need this to wait
import time

# need this for actuators
from actuators.actuators import F, V, M, P

print

# filter
print "Filter:"
print

print "\t"+F[1].table, "is", F[1].check_status()
print

# valves
print "Valves:"
print

for SysID in range(3, 5):

	print "\t"+V[SysID].table, "is", V[SysID].check_status()

print

# miscellaneous
SysIDs = chain(range(1, 3), range(6, 9), range(18, 19))

print "Miscellaneous components:"
print

for SysID in SysIDs:

	print "\t"+M[SysID].table, "is", M[SysID].check_status()

print

# pumps
print "Pumps:"
print

for SysID in range(1, 13):

	print "\t"+P[SysID].table, "is", P[SysID].check_status()

print
