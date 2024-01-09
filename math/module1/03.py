import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start='2021-09-01', freq='D', periods=8)
fig, axs = plt.subplots(2,1)
axs[0].plot(date, [23, 17, 17, 16, 15, 14, 17, 20], label='day temperature')
axs[1].plot(date, [19, 11, 16, 11, 10, 10, 11, 16], label='night temperature')
# plt.plot(date, [23, 17, 17, 16, 15, 14, 17, 20],label='day temperature')
plt.xlabel('Date', fontsize='large', color='teal')
plt.ylabel('Temp', fontsize='small', color='tomato')
axs[0].set_title('Forecast in Limassol Day', fontsize=18)
axs[1].set_title('Forecast in Limassol Night', fontsize=18)

plt.text(date[0], 15, 'Осінь досить тепла', color="blue")
plt.legend()
plt.show()