# Balance Board

### Project Overview

This is a ROS project developed as part of ME495 - Embedded Systems in Robotics course at Northwestern University.

The goal of this project is to control a ping-pong ball by using Franka Panda robot  to manipulate a white board. 

Github link:

### Quickstart Guide

### Package Details

`maze.launch`, the main launch file including: 

1. a launch file `pd_controller.launch`: a sub launch file.
2. a node `trajectory_manager` : take inputs of current ball pose and map parameters from `vision` node in each frame, output the target ball pose.  

`pd_controller.launch`: 

1.  `ros_control_interface.launch` : a sub launch file.
2.  `vision`: a node using OpenCV libary processing images to output a current ball pose in each frame and map parameters.
3. a node `pd_controller`: a node using a high-level tuned PD controller to calculate a desired angle update in each frame. 

 `ros_control_interface.launch` :

1. `panda_control_moveit_rviz.launch`: a launch file to initialize basic robot configurations.
2. `pos_control_spawner`: a node to spawn a position controller in ROS 
3. `ros_control_interface`: a node using a low-level tuned PD controller to give the desired effort command to robot.

### Architecture

 ![img](https://documents.lucid.app/documents/016a84d4-ee5f-441b-803b-49a0ed6e6852/pages/0_0?a=395&x=172&y=93&w=611&h=1034&store=1&accept=image%2F*&auth=LCA%206ef4b283f28e7322fce266730dc833f7660ca186-ts%3D1638816158)

### Control Loop

 ![img](https://documents.lucid.app/documents/d9cacb50-e613-4a57-96a8-e48c03650f00/pages/0_0?a=542&x=-1&y=40&w=1182&h=881&store=1&accept=image%2F*&auth=LCA%2084f4d8bb0bc569761947bb638a61287baa8fa32d-ts%3D1638817068)

