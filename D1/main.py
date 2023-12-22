import seaborn as sns
import matplotlib.pyplot as plt

# Load iris data
iris = sns.load_dataset("iris")
print(iris.head())

# Plot sepal with as a function of sepal_length across days
g = sns.lmplot(x="sepal_length", y="sepal_width", hue="species",
               truncate=True, height=5, data=iris)

# Use more informative axis labels than are provided by default
g.set_axis_labels("Sepal length (mm)", "Sepal width (mm)")

# Add the legend manually
new_title = 'Species'
g.legend.set_title(new_title)

# replace labels
new_labels = ['Setosa', 'Versicolor', 'Virginica']
for t, l in zip(g.legend.texts, new_labels): t.set_text(l)

plt.show()







