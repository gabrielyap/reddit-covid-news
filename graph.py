# Run to display the line graph of day of the year vs. frequency of COVID-related posts.
# The graph is dynamic so the x-axis range changes dependent on the first to last day reddit.py was ran.
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import pandas as pd
df = pd.read_csv('dates.csv', header = None)
days = df[0]
freq = df[1]
plt.plot(days,freq)
plt.title('Day of the Year vs. Frequency of COVID-related posts on /r/worldnews')
plt.xlabel('Day of the Year (Jan 10 = 10)')
plt.ylabel('Frequency')
plt.ylim(0,100)
plt.show()
