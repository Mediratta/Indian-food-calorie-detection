import open3d as o3d
import numpy as np 
import matplotlib.pyplot as plt 
import os 
import sys
# monkey patches visualization and provides helpers to Load geometries
sys.path.append ('..')
import open3d_tutorial as o3dtut
#change to True when interact with the visualization windows
o3dtut.interactive = not "CI" in os.environ

#A dataset Named redwood/ depth image from you 
print("Read Redwood dataset")
color_raw = o3d.io.read_image("../../test_data/RGBD/color/08000-jpg") #("colorImg-jpg")
depth_raw = o3d.io.read_image("/./test_data/RGBD/depth/00000.png") #("depthImg.png")
rgbd_image = o3d.geometry.RGBDImage. create_from_color_and_depth(color_raw, depth_raw)
print(rgbd_image)

plt.subplot (1, 2, 1)
plt.title('Redwood grayscale image')
plt. imshow(rgbd_image.color)
plt. subplot(1, 2, 2)
plt.title('Redwood depth image') 
plt.imshow(rgbd_image.depth)
plt. show()

pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image,o3d.camera.PinholeCameraIntrinsic(
o3d. camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
# Flip it, otherwise the pointcloud will be upside down
o3d.visualization.draw_geometries([pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])], zoom=0.5)