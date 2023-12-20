import numpy as np
import open3d as o3d
pcd = o3d.io.read_point_cloud("your_point_cloud.ply")
voxel_size = 0.01  # Adjust voxel size as needed
voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd, voxel_size)
voxels = voxel_grid.get_voxels()
voxel_centers = voxel_grid.get_voxel_centers()

volume = 0
for voxel in voxels:
    # Check for convexity (approximate approach):
    points_in_voxel = pcd.select_by_index(voxel)
    hull = o3d.geometry.ConvexHull(points_in_voxel)
    if hull.is_convex:
        volume += voxel_size**3

print("Estimated volume:", volume)
