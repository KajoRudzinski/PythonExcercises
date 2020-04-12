age = 24
print("My age is " + str(age) + " years")
# same below
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
# Result:
# There are 31 days in Jan, Mar, May, Jul, Aug, Oct and Dec

print("text {2}, {0}, {2}.".format("x", 1, 24))
