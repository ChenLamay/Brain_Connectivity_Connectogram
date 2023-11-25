
from mne.viz import plot_connectivity_circle, circular_layout
from matplotlib.colors import ListedColormap
import matplotlib as mpl
from numpy.random.mtrand import f
import pandas as pd
import numpy as np


# create list of brain areas as given in txt file 
df = pd.read_excel(r'Brain_region_names.xlsx',header=0)
node_names = df[df.columns[2]].values.tolist()



from mne.viz import plot_connectivity_circle, circular_layout
from matplotlib.colors import ListedColormap
import matplotlib as mpl
from numpy.random.mtrand import f
import pandas as pd
import numpy as np

# create list of brain areas as given in txt file 
df = pd.read_excel(r'Brain_region_names.xlsx',header=0)
node_names = df[df.columns[2]].values.tolist()

# import excel contant, create headline of nums and convert to numpy 
exprt_mat = pd.read_excel(r'results_experimental.xlsx',header=None).to_numpy()
control_mat = pd.read_excel(r'results_control.xlsx',header=None).to_numpy()

# combine numpy
combined_numpy = np.where(exprt_mat == -1,control_mat,exprt_mat)

# take only pvalue<0.05
con = np.where(combined_numpy<=0.05,combined_numpy,np.nan)
lh_nodes = node_names[:24]
rh_nodes = node_names[24:48]
node_order = list()
node_order = lh_nodes[::-1] + rh_nodes
node_angles = circular_layout(node_names,node_order, start_pos=90, group_boundaries=[0, len(node_names) / 2])

# creat figure
new_blues = mpl.colormaps['Blues_r']
fig, axes = plot_connectivity_circle(con,node_names,node_angles=node_angles,colorbar=True, node_colors= ['deepskyblue'],colormap=ListedColormap(new_blues(np.linspace(0.01, 0.75, 128)))
,
title='Number Of Fibers \n\n         Left Hemisphere               Right Hemisphere     ', facecolor='white',textcolor='black',linewidth=3)

