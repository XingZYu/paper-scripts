import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from common import *

font["font.size"] = 32
plt.rcParams.update(font)

fig, ax = plt.subplots()
fig.set_size_inches(12,6)
plt.subplots_adjust(top=1.8, right=0.9,left=0.1,bottom=0.25)
labels = ["Apache", "OLTP (RO)", "OLTP (RW)", "Redis (GET)", "Redis (GET/SET)"]

xrange = np.arange(len(labels))

vanilla_avg = [1.732, 0.78, 17.48, 27.81, 23.76]
vanilla_tail = [3, 0.93, 22.87, 5, 5]
vm_live_avg = [1.815, 0.86, 18.18, 26.25, 28.19]
vm_live_tail = [3, 1.27, 25.28, 11, 6]
yanni_avg = [1.789, 0.83, 17.51, 28.84, 32.39]
yanni_tail = [3, 1.03, 28.67, 5, 6]

for i in range(len(labels)):
    vm_live_avg[i], vm_live_tail[i], yanni_avg[i], yanni_tail[i] = \
        vm_live_avg[i] / vanilla_avg[i], \
        vm_live_tail[i] / vanilla_tail[i], \
        yanni_avg[i] / vanilla_avg[i], \
        yanni_tail[i] / vanilla_tail[i]


title = "Text-Processing\nComparison with Spark"
colors = ["#f5f7c8", "#c3ddbd"]
dot_style = ['s', 'x', 'd', '^', '.', 'D']
line_style = [':', '-.', '--', '-']
hatches = ['///', '\\\\\\', '----', '//////',
           '++++', 'xxxxxx', '\\\\\\\\\\\\', '----']

bar_width = 0.5
bar_interval = 0.20
bar_zoom = 0.2
linewidth = 4

#ax.set_title(title,fontdict=font)

plt.xticks(xrange, labels, rotation=15)
ax.set_ylabel("Relative Latency")
ax.tick_params(axis='both', which='major')
ax.set_ylim([0, 4.3])
#ax.set_xlabel("Program", fontdict=font)

ax.axhline(y=1, color='grey', linestyle='--')
for i in xrange:
    vmlive_avg_bar = ax.bar(i - bar_interval, vm_live_avg[i], width=bar_width * bar_zoom,
                          bottom=0, color=colors[0],
                          label="vm live avg", edgecolor="black")
    vmlive_tail_bar = ax.bar(i - bar_interval / 2, vm_live_tail[i], width=bar_width * bar_zoom,
                          bottom=0, color=colors[0],
                          label="vm live tail", hatch="//", edgecolor="black")
    yanni_avg_bar = ax.bar(i + bar_interval / 2, yanni_avg[i], width=bar_width * bar_zoom,
                       bottom=0, color=colors[1],
                       label="yanni avg", edgecolor="black")
    yanni_tail_bar = ax.bar(i + bar_interval, yanni_tail[i], width=bar_width * bar_zoom,
                       bottom=0, color=colors[1],
                       label="yanni tail", hatch="//", edgecolor="black")

ax.legend((vmlive_avg_bar, vmlive_tail_bar, yanni_avg_bar, yanni_tail_bar),
        ("vm live avg", "vm live tail", "yanni avg", "yanni tail"),
        loc=0, frameon=True,ncol=2)
plt.subplots_adjust(top=0.86)

plt.grid(True)
plt.savefig('/Users/snake0/yanni-img/application_perf.pdf', dpi=300)
plt.show()

