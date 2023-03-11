import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 5
cost_per_class = cost_per_week/classes_per_week
print("Cost per class:", cost_per_class)
print(
   classes_per_week, type(classes_per_week),
   cost_per_class, type(cost_per_class),
   weeks, type(weeks),
   classes, type(classes),
   tuition, type(tuition),
   cost_per_week, type(cost_per_week)
)

#Part B
jeremy_list = ["hi", "3.3", "cs 110", "100", "2", "bye"]
rand_result = random.choice(jeremy_list)
print(rand_result)