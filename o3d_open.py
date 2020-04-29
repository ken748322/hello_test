import open3d as o3d

giom=o3d.io.read_point_cloud('surface.ply')
o3d.visualization.draw_geometries([giom])
