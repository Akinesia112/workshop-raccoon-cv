# workshop-raccoon-cv



### KUKA prc example files
[example_robot_programming_in_Rhino](https://drive.google.com/file/d/1kzzR0gK_d3wgkkV1yESv7XUb84CfU9Pq/view?usp=sharing)


### ROS Setup
#### Ubuntu 20.04.6 LTS install of ROS Noetic
https://wiki.ros.org/noetic/Installation/Ubuntu

```
sudo apt install ros-noetic-rosbridge-server ros-noetic-ros-controllers ros-noetic-ros-control
mkdir -p catkin_ws/src
cd catkin_ws/src
git clone https://github.com/rccn-dev/compas_fab_backend.git
git clone https://github.com/rccn-dev/kuka_kr300_support.git
git clone https://github.com/rccn-dev/kuka_robot_driver_interfaces.git
git clone https://github.com/rccn-dev/rccn_robot_cell.git

# Official packages
git clone https://github.com/ros-planning/moveit_calibration.git
git clone https://github.com/introlab/rtabmap_ros.git
cd catkin_ws/src
rosdep install -y --from-paths . --ignore-src --rosdistro noetic
cd ..
catkin_make
source devel/setup.bash
roslaunch rccn_east_robot_moveit_config demo.launch
```
  
  ![image](rviz_open.png)   

  * rviz open
