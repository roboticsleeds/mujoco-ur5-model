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
- Note that we had to apply some rotations to some bodies such that they match our configuration at the lab.
In specific we changed the body `upper_arm_link` from `<body name="upper_arm_link" pos="0 0.13585 0" quat="0.707107 0 0.707107 0">` to `<body name="upper_arm_link" pos="0 0.13585 0" quat="0.73727758 0.0 0.6755904 0">`
and `forearm_link` from `<body name="forearm_link" pos="0 -0.1197 0.425">` to `<body name="forearm_link" pos="0 -0.1197 0.425" quat="0.99904822 0. 0.04361941 0.">`.

