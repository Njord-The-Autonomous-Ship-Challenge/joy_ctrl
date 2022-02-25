# joy_ctrl
This is a repository which makes it possible to navigate the Njordvessel with a joystick. The node is working on joy_node from the ROS enviroment. 

Here is the code that will install the package.
```
cd catkin_ws/src
git clone https://github.com/Njord-The-Autonomous-Ship-Challenge/joy_ctrl.git
chmod +x ~/catkin_ws/src/joy_ctrl/install_requirements.sh
chmod +x ~/catkin_ws/src/joy_ctrl/scripts/joy_ctrl_client.py
cd joy_ctrl
./install_requirements.sh
```

Here is how to launch the node (needs to be launched after a scenario is launched).
```
source catkin_ws/devel/setup.bash
roslaunch catkin_ws/src/joy_ctrl/launch/launch_joystick_stack.launch
```
