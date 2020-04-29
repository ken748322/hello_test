""" Captopril 表面モデルの.plyファイルを作成 """
import sys
import subprocess
import open3d as o3d
sys.path.append('/usr/local/Cellar/pymol/2.3.0/libexec/lib/python3.8/site-packages/') # pymolをインポートするためにpath追加
import pymol

""" pymol による分子表面の.wrlファイルの作成 """
pymol.cmd.load('Conformer3D_CID_44093.sdf') # pubchemからダウンロードした.sdfファイル
# pymol.cmd.show('surface')
pymol.cmd.show('spheres')  # 空間充填(CPK)モデル
# pymol.cmd.set('surface_quality', '3')
pymol.cmd.color('gray70', 'elem C')
pymol.cmd.save('Captopril_surface.wrl')

""" meshlab による.plyファイルへの変換 """
subprocess.call('/Applications/meshlab.app/Contents/MacOS/meshlabserver -i Captopril_surface.wrl -o Captopril_surface.ply -m vc ff'.split()) # meshlabのインストール先にあるmeshlabserverをパスで指定する必要がある

""" open3d による表示 """
giom=o3d.io.read_point_cloud('Captopril_surface.ply')
o3d.visualization.draw_geometries([giom])
