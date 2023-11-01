import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import BoundaryNorm, ListedColormap

# Load dataset
df = pd.read_csv('Solar_flare_RHESSI_2004_05.csv')

# Filter data for months 1+2+3+4
m_1to4 = ((df['year'] == 2004) & (df['month'].between(1, 4)))
df_1to4 = df[m_1to4]

# Filter data for months 21+22+23+24
m_21to24 = ((df['year'] == 2005) & (df['month'].between(9, 12)))
df_21to24 = df[m_21to24]

# Define the energy ranges based on energy.kev values
energy_kev_ranges = [(6, 12), (12, 25), (25, 50), (50, 100), (100, 300), (300, 800)]

# Create a custom colormap and norm
# cmap = ListedColormap(['blue', 'magenta', 'cyan', 'purple', 'teal', 'black'])
cmap = plt.get_cmap('YlGnBu', len(energy_kev_ranges))
boundaries = [range[0] for range in energy_kev_ranges] + [energy_kev_ranges[-1][1]]
norm = BoundaryNorm(boundaries, cmap.N, clip=True)

# Set the circle radius
circle_radius = 900

# Create a heatmap for months 1+2+3+4
heatmap1, xedges1, yedges1 = np.histogram2d(df_1to4['x.pos.asec'], df_1to4['y.pos.asec'], bins=30)
extent1 = [-circle_radius, circle_radius, -circle_radius, circle_radius]
fig1, ax1 = plt.subplots(figsize=(10, 8))
sc1 = ax1.imshow(heatmap1.T, extent=extent1, origin='lower', aspect='auto', cmap=cmap, alpha=0.7, norm=norm)
colorbar_ticks1 = [range[0] for range in energy_kev_ranges] + [800]
ax1.set_title('Solar Flare Intensity Heatmap (Months 1+2+3+4)')
ax1.set_xlabel('X Position (arcseconds)')
ax1.set_ylabel('Y Position (arcseconds)')
circle1 = plt.Circle((0, 0), circle_radius, color='r', fill=False)
ax1.add_artist(circle1)
cbar1 = fig1.colorbar(sc1, ax=ax1, label='Intensity', boundaries=boundaries, ticks=colorbar_ticks1)

# Create a heatmap for months 21+22+23+24
heatmap2, xedges2, yedges2 = np.histogram2d(df_21to24['x.pos.asec'], df_21to24['y.pos.asec'], bins=30)
extent2 = [-circle_radius, circle_radius, -circle_radius, circle_radius]
fig2, ax2 = plt.subplots(figsize=(10, 8))
sc2 = ax2.imshow(heatmap2.T, extent=extent2, origin='lower', aspect='auto', cmap=cmap, alpha=0.7, norm=norm)
colorbar_ticks2 = [range[0] for range in energy_kev_ranges] + [800]
ax2.set_title('Solar Flare Intensity Heatmap (Months 21+22+23+24)')
ax2.set_xlabel('X Position (arcseconds)')
ax2.set_ylabel('Y Position (arcseconds)')
circle2 = plt.Circle((0, 0), circle_radius, color='r', fill=False)
ax2.add_artist(circle2)
cbar2 = fig2.colorbar(sc2, ax=ax2, label='Intensity', boundaries=boundaries, ticks=colorbar_ticks2)
plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# from matplotlib.colors import ListedColormap
# import matplotlib.patches as mpatches

# # Load dataset
# df = pd.read_csv('Solar_flare_RHESSI_2004_05.csv')

# # Filter data for months 1+2+3+4
# m_1to4 = ((df['year'] == 2004) & (df['month'].between(1, 4)))
# df_1to4 = df[m_1to4]

# # Filter data for months 21+22+23+24
# m_21to24 = ((df['year'] == 2005) & (df['month'].between(9, 12)))
# df_21to24 = df[m_21to24]

# # Create a custom colormap for color-coded energy ranges
# cmap = ListedColormap(['blue', 'magenta', 'cyan', 'purple', 'teal', 'black'])

# # Define the energy ranges based on energy.kev values
# energy_kev_ranges = [(6, 12), (12, 25), (25, 50), (50, 100), (100, 300), (300, 800)]

# # Create plot for months 1+2+3+4
# x_1to4 = df_1to4['x.pos.asec'].values
# y_1to4 = df_1to4['y.pos.asec'].values
# duration_1to4 = df_1to4['duration.s'].values
# energy_kev_1to4 = df_1to4['energy.kev'].apply(lambda x: (int(x.split('-')[0]) + int(x.split('-')[1])) / 2).values

# r_1to4 = np.sqrt(x_1to4 ** 2 + y_1to4 ** 2)
# t = 80  # percent

# r0_1to4 = np.percentile(r_1to4, t)

# # Determine the intensity range for each data point based on energy.kev values
# intensity_range_1to4 = np.digitize(energy_kev_1to4, [energy_range[1] for energy_range in energy_kev_ranges])

# # Create legend items
# legend_patches = []
# for i, energy_range in enumerate(energy_kev_ranges):
#     label = f'{energy_range[0]} - {energy_range[1]} KeV'
#     legend_patch = mpatches.Patch(color=cmap(i / len(energy_kev_ranges)), label=label)
#     legend_patches.append(legend_patch)

# plt.figure(figsize=(8, 6))
# sc = plt.scatter(x_1to4, y_1to4, c=intensity_range_1to4, cmap=cmap, s=15)
# circle_1to4 = plt.Circle((0, 0), r0_1to4, color='r', fill=False)
# plt.gca().add_artist(circle_1to4)
# plt.title('Solar Flare Intensity Scatter Plot (Months 1+2+3+4)')
# plt.xlabel('X Position (arcseconds)')
# plt.ylabel('Y Position (arcseconds)')
# plt.xlim(-1200, 1200)
# plt.ylim(-1200, 1200)
# plt.gca().set_aspect('equal', adjustable='box')

# # Add legend
# plt.legend(handles=legend_patches, title='Energy Range', loc='upper left')

# plt.show()

# # Create plot for months 21+22+23+24
# x_21to24 = df_21to24['x.pos.asec'].values
# y_21to24 = df_21to24['y.pos.asec'].values
# duration_21to24 = df_21to24['duration.s'].values
# energy_kev_21to24 = df_21to24['energy.kev'].apply(lambda x: (int(x.split('-')[0]) + int(x.split('-')[1])) / 2).values

# r_21to24 = np.sqrt(x_21to24 ** 2 + y_21to24 ** 2)
# t = 80  # percent

# r0_21to24 = np.percentile(r_21to24, t)

# # Determine the intensity range for each data point based on energy.kev values
# intensity_range_21to24 = np.digitize(energy_kev_21to24, [energy_range[1] for energy_range in energy_kev_ranges])

# plt.figure(figsize=(8, 6))
# sc = plt.scatter(x_21to24, y_21to24, c=intensity_range_21to24, cmap=cmap, s=15)
# circle_21to24 = plt.Circle((0, 0), r0_21to24, color='r', fill=False)
# plt.gca().add_artist(circle_21to24)
# plt.title('Solar Flare Intensity Scatter Plot (Months 21+22+23+24)')
# plt.xlabel('X Position (arcseconds)')
# plt.ylabel('Y Position (arcseconds)')
# plt.xlim(-1200, 1200)
# plt.ylim(-1200, 1200)
# plt.gca().set_aspect('equal', adjustable='box')

# # Add legend
# plt.legend(handles=legend_patches, title='Energy Range', loc='upper left')
# plt.show()


