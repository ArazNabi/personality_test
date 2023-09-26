import matplotlib.pyplot as plt
import numpy as np
import dummy_users as du


categories = ['Feeling', 'Perceiving', 'Introversion', 'Sensing', 'Thinking', 'Judging', 'Extroversion', 'Intuition']
#data = [4, 3, 5, 2, 4, 3, 5, 2]  

dummy_data = du.user_feelings.iloc[75]

user_name = dummy_data['Name']
data = dummy_data[categories]

num_categories = len(categories)

angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]  


plt.figure(figsize=(8, 6))
ax = plt.subplot(111, polar=True)

# data += data[:1] 
data = np.concatenate((data, [data[0]])) #closed shape of dummy_data
ax.fill(angles, data, 'b', alpha=0.1) 
ax.plot(angles, data, 'o-', linewidth=2)  


ax.set_rlabel_position(90)  
ax.set_thetagrids(np.degrees(angles[:-1]), labels=categories)


plt.title(user_name)

plt.show()
