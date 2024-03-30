# Autonomous Mobile Robot Navigation using sensor fusion

## Indoor Navigation (Map Based)
### 1. Manual Keyboard Teleoperation:
```bash
$ roslaunch husky_gazebo husky_playpen.launch
// For running the gazebo world

$ roslaunch husky_control teleop_keyboard.launch
// For running teleop Keyboard

$ roslaunch husky_viz husky_display.launch
// For running rviz to visualize the robot model
```
### 2. Map Generation( SLAM Gmapping) :
```bash
$ roslaunch husky_gazebo husky_playpen.launch

$ roslaunch husky_control teleop_keyboard.launch

$ roslaunch husky_navigation gmapping_navigation.launch
// For running slam gmapping to generate the map

$ roslaunch husky_viz husky_mapping.launch
// For running rviz to visualize the generating map

$ roslaunch husky_navigation map_saver.launch map_name:=<give_your_map_name>
// For saving the generated map
```
### 3. Autonomous Navigation :
```bash
$ roslaunch husky_gazebo husky_playpen.launch

$ roslaunch husky_navigation amcl_navigation.launch
// For running amcl to navigate autonomously

$ roslaunch husky_viz husky_navigation.launch
// For running rviz to visualize the autonomous navigation

```


## Outdoor Navigation (GPS Based)
