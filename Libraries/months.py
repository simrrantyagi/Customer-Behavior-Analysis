import matplotlib.pyplot as plt
months=['Jan','Feb','Mar','Apr','May','Jun']
sales=[2000,1100,2000,1500,1200,1234]
plt.title('Monthly Sales')
plt.barh(months,sales, label='Sales Growth',color='green')
plt.ylabel('Sales in months')
plt.xlabel('Months')
plt.xlim(1000,3000)
plt.legend()
plt.show()