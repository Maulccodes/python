import matplotlib.pyplot as ply


students = ['john', 'love', 'Tony', 'Momo', 'jamal', 'tiff']

marks = [60, 30,196, 75, 184, 148]

plt.bar(students, marks, color="green")
plt.grid(color='yellow', linestyle='--', alpha=0.3, axis='y')
plt.xlabel('Students')
plt.ylabel('Obtained Marks')
plt.title('Students marks details')
plt.show()
