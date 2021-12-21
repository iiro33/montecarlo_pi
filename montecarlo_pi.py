import math, random

SIZE = 4
r = SIZE/2
center = [SIZE/2, SIZE/2]

for i in range(8):
    sample_size = 10**i
    print("Sample size: " + str(sample_size))
    in_circle = 0
    
    for j in range(sample_size):
        x = random.uniform(0, SIZE)
        y = random.uniform(0, SIZE)
        rand_point = [x, y]
        distance_from_center = math.sqrt( ((center[0]-rand_point[0])**2) + ((center[1]-rand_point[1])**2) )
        
        if distance_from_center <= r:
            in_circle += 1

    pi_est = in_circle * 4 / sample_size
    accuracy = 1 - pi_est/math.pi
    if i == 0:
        best_accuracy = accuracy
        smallest = sample_size
    else:
        if abs(accuracy) < abs(best_accuracy):
            best_accuracy = accuracy
            smallest = sample_size
    
    print("Estimated pi value in Monte Carlo simulation: " + str(pi_est))
    print("Accuracy = " + str(accuracy) + "\n") 

print("Real pi: " + str(math.pi))
print("Best accuracy of sample size of: " + str(smallest) + "\n")
