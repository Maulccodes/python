kilometers = 5.5

# To take kilometers from the user, uncomment the code below
kilometers = input("Enter the value in kilometers")

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.3f kilometers is equal to %0.3f miles' %(kilometers,miles))
