import matplotlib.pyplot as plt
regions=['North','South','East','West']
revenue=[2000,3000,5800,1288]
plt.pie(revenue, labels=regions, colors=['gold','pink','gray','yellow'],autopct='%1.1f%%')
plt.legend()
plt.show()