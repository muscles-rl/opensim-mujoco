python vtp.stl
cd mujoco-rl/models/Geometry/
for f in *.stl; do admesh --remove-unconnected $f -b $f; done
cd ../../..
