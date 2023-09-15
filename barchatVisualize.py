import numpy as np
import matplotlib.pyplot as plt

# groups and labels for groups
groups = ['FLARE22', 'TCIA', 'AMOS','Synapse']
subgroups = ['client_BC', 'w/o A', 'client_AC', 'w/o B', 'client_AB', 'w/o C', 'client_ABC']

# data of the first subplot
data1 = np.array([
    [54.93, 87.13, 71.39, 85.05, 83.37, 85.99, 84.77],
    [49.73, 72.65, 66.56, 75.46, 52.14, 73.59, 72.34],
    [60.53, 64.63, 55.37, 62.13, 52.40, 63.60, 66.95],
    [68.39, 77.54, 59.62, 78.66, 69.75, 75.14, 78.45]
])

# data of the second subplot
data2 = np.array([
    [80.0, 85.0, 87.0, 89.0, 90.0, 91.0, 92.0],
    [55.0, 65.0, 60.0, 63.0, 65.0, 70.0, 72.0],
    [58.0, 62.0, 57.0, 56.0, 50.0, 63.0, 61.0],
    [75.0, 80.0, 77.0, 84.0, 72.0, 78.0, 82.0]
])

color = ['#DDF2C6', '#C0D1DC', '#C8F2E9', '#CFCCE3', '#AED4CB', '#BBA8BF', '#F19C99']

# set the size of the figure
plt.figure(figsize=(20, 6))

# create first subplot
plt.subplot(1, 2, 1)

# set the width and gap of bars
bar_width = 0.1
group_spacing = 0.4
subgroup_spacing = 0.02

# calculate the position of each group
index = np.arange(len(groups))

# calculate the position of each sub group
subgroup_indices = (index[:, np.newaxis] +
                    (bar_width + subgroup_spacing) * np.arange(len(subgroups)))

# align the group1 and group2
subgroup_indices[:, 0] += subgroup_spacing
subgroup_indices[:, 2] += subgroup_spacing
subgroup_indices[:, 4] += subgroup_spacing
subgroup_indices[:, 6] += subgroup_spacing

# draw the bar chart
for i, subgroup in enumerate(subgroups):
    subgroup_data = data1[:, i]
    plt.bar(subgroup_indices[:, i], subgroup_data, bar_width, label=subgroup, color=color[i])

# set the labels of x and y axis
plt.xlabel('Stomach', fontsize=20)
plt.ylabel('Dice Value (%)', fontsize=18)

# set the ticks for x and y
plt.xticks(index + group_spacing, groups, fontsize=18)
plt.yticks(fontsize=18)

# create the second subplot
plt.subplot(1, 2, 2)

# Using different data to draw the second subplot
for i, subgroup in enumerate(subgroups):
    subgroup_data = data2[:, i]
    plt.bar(subgroup_indices[:, i], subgroup_data, bar_width, label=subgroup, color=color[i])

# set the labels for x and y axis
plt.xlabel('Pancreas', fontsize=20)
plt.ylabel('Dice Value (%)', fontsize=18)

# set the ticks for x and y axis
plt.xticks(index + group_spacing, groups, fontsize=18)
plt.yticks(fontsize=18)

# adjust tht distance from each other
plt.tight_layout()

# add the legned for whole chart
handles, labels = plt.gca().get_legend_handles_labels()
plt.figlegend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=len(subgroups), fontsize=18)

# show the plot
plt.show()