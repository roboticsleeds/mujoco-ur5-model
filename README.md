# MuJoCo UR5 Model

![Model](images/model.png "Robot Model")

This is currently a planar robot only with three joints (two slide joints and a hinge joint). 

## Developers and Contributors
MuJoCo UR5 Model was developed by the Robotics Lab in the School of Computing at the University of Leeds. 
- Authors: [Rafael Papallas](http://rpapallas.com), [Wisdom Agboh](https://agboh.com) 
- Current maintainors: [Rafael Papallas](http://rpapallas.com), [Wisdom Agboh](https://agboh.com).

## License
This work is licensed under GNU General Public License v3.0. The full license is available [here](https://github.com/roboticsleeds/mujoco_ur5_model/blob/master/LICENSE). 

## Notes
The current model as defined includes some custom configurations such that the arm is set to the following:
- Base: -90 degrees
- Shoulder -175 degrees
- Elbow: -5 degrees
- Wrist1: -180 degrees
- Wrist2: -90 degrees
- Wrist3: -180 degrees

If you want to change the configuration of the robot, then we will recomend to start from the following
original configuration of the arm and apply rotations as needed to the required bodies to match the 
UR5 joint values:
```xml
<body name="shoulder_link" pos="0.28 0 0.545159" quat="0.681998 0 0 -0.731354">
    <inertial pos="0 0 0" mass="3.7" diaginertia="0.0102675 0.0102675 0.00666" />
    <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="shoulder" />
    <body name="upper_arm_link" pos="0 0.13585 0" quat="0.707107 0 0.707107 0">
        <inertial pos="0 0 0.28" mass="8.393" diaginertia="0.226891 0.226891 0.0151074" />
        <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="upperarm" />
        <body name="forearm_link" pos="0 -0.1197 0.425">
            <inertial pos="0 0 0.25" mass="2.275" diaginertia="0.0494433 0.0494433 0.004095" />
            <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="forearm" />
            <body name="wrist_1_link" pos="0 0 0.39225" quat="0.707107 0 0.707107 0">
                <inertial pos="0 0 0" quat="0.5 0.5 -0.5 0.5" mass="1.219" diaginertia="0.21942 0.111173 0.111173" />
                <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="wrist1" />
                <body name="wrist_2_link" pos="0 0.093 0">
                    <inertial pos="0 0 0" quat="0.5 0.5 -0.5 0.5" mass="1.219" diaginertia="0.21942 0.111173 0.111173" />
                    <geom type="mesh" rgba="0.7 0.7 0.7 1" mesh="wrist2" />
                    <body name="wrist_3_link" pos="0 0 0.09465">
                        <inertial pos="0 0 0" quat="0.5 0.5 -0.5 0.5"  mass="0.1879" diaginertia="0.033822 0.0171365 0.0171365" />
                        <geom type="mesh" rgba="0.7 0.7 0.7 1" friction="0.8 0.8 0.8" mesh="wrist3" />
                    </body>
                </body>
            </body>
        </body>
    </body>
</body>
```
