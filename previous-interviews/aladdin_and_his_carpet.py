# Gas station problem
# Greedy problem

# Aladdin wants to travel around the world and will choose a circular path to fly on his magical carpet.
# The carpet needs enough magic to take hom from one place to another.
# He knows that after travelling some distance,
# he can find a magic source that will enable the carpet to travel a further distance.

# There are 'n' magical sources along the circular path numbered from 0 to n-1.
# Initially, the carpet has no magic and Aladdin can use a portal to jump to any magical source and start his journey.
# The carpet consumes units of magic equal to the units of distance travelled.
# He needs to choose a point to start hos journey that will allow him to complete his journey
# and visit all the places in the circular path in order.
# Determine the lowest index of the starting points from which Aladdin can start his journey and visit all the places
# in the circular path in order. If there is no solution return -1.

# For example, there are n=4 sources of magic along his route:
# magic = [3, 2, 5, 4] and dist = [2, 3, 4, 2].
# The first attempt is starting at the first source, magic[0] = 3.
# He transports there without cost and collects 3 units of magic.
# The distance to the next point is dist[0] = 2.
# It takes 2 units of magic to get there, and he collects magic[1] = 2 units upon arrival, so he has 3 - 2 + 2 = 3
# units of magic after making his first carpet ride. Continuing along the journey:
# 3 - dist[1] + magic[2] = 3 - 3 + 5 = 5
# 5 - dist[2] + magic[3] = 5 - 4 + 4 = 5
# 5 - dist[3] = 5 - 2 = 3

# At this point, he is back to the first source.
# Because he can complete this journey starting at source magic[0], there is no reason to continue with the analysis
# so its index, 0, is returned.
# To illustrate a point from the same example, if he starts at position 2, where magic[1] = 2 and dist[1] = 3,
# he will not be able to proceed to the next point because the distance is greater than this magic units.
# Note that the list is circular, so from magic[3] in this example, the next source on the path is magic[0].

# Function Description
# Complete the function optimal_point.
# The function must return an integer that denotes the min index of magic from which he can start a successful journey.
# If no such starting point exists, return -1.
# optimal_point has the following parameter(s):
# magic[magic[0], ..., magic[n-1]] - an array of integers where magic[i] denotes the amount of magic in the i-th source
# dist[dist[0], ..., dist[n-1]] - an array of integers where dist[i] denotes the distance to the next magical source

# Constraints
# 1 <= n <= 100 000
# 0 <= magic[i] <= 10 000
# 0 <= dist[i] <= 10 000

def optimal_point(magic: list, dist: list) -> int:
    if sum(magic) < sum(dist):
        return -1

    total = 0
    result = 0

    for i in range(len(magic)):
        total += (magic[i] - dist[i])
        if total < 0:
            total = 0
            result = i + 1

    return result


print(optimal_point([3, 2, 5, 4], [2, 3, 4, 2]))
print(optimal_point([2,3,4], [3,4,3]))
