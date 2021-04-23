STEPS TO GET REPO TO RUN ON COMPUTER:

1. Follow the README instructions of the ur5_ROS-Gazebo repo
  - make sure to clone the melodic-devel branch of universal robot
  - copy the files 'ur5.urdf.xacro' and 'common.gazebo.xacro' files found in the src/ur_description/
  folder over to the cloned universal-robot repo

2. Run catkin_make and source devel/setup.bash
3. Run the roslaunch file
`roslaunch ur5_notebook initialize.launch`

which should then give you a working and running Gazebo simulation!

Any errors that pop up from this point on are likely dependency issues. If you spot an error, read it closely,
maybe google it, and then just
`sudo apt install ros-melodic-[package-name]`
until the simulation runs smoothly
