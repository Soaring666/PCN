import open3d as o3d

pcd1 = o3d.geometry.PointCloud()
pcd1.points = o3d.utility.Vector3dVector([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
pcd2 = o3d.geometry.PointCloud()
pcd2.points = o3d.utility.Vector3dVector([[1, 0, 0], [1, 1, 1], [1, 2, 2]])
distances = o3d.geometry.compute_point_cloud_distance(pcd1, pcd2)
print(distances)