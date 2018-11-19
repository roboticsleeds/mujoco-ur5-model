#!/usr/bin/env python

# Copyright (C) 2018 The University of Leeds.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Rafael Papallas (rpapallas.com)

from pyquaternion import Quaternion
from xml.dom import minidom
import math

class UR5:
    def __init__(self, base_joint_value, shoulder_joint_value, elbow_joint_value,
                 wrist_1_joint_value, wrist_2_joint_value, wrist_3_joint_value):
        self.base_joint_value = base_joint_value
        self.base_quat = None

        self.shoulder_joint_value = shoulder_joint_value
        self.shoulder_quat = None

        self.elbow_joint_value = elbow_joint_value
        self.elbow_quat = None

        self.wrist_1_joint_value = wrist_1_joint_value
        self.wrist_1_quat = None

        self.wrist_2_joint_value = wrist_2_joint_value
        self.wrist_2_quat = None

        self.wrist_3_joint_value = wrist_3_joint_value
        self.wrist_3_quat = None

    def apply_joint_angles(self):
        self._set_desired_quaternion_for_base_joint()
        self._set_desired_quaternion_for_shoulder_joint()
        self._set_desired_quaternion_for_elbow_joint()
        self._set_desired_quaternion_for_wrist_1_joint()
        self._set_desired_quaternion_for_wrist_2_joint()
        self._set_desired_quaternion_for_wrist_3_joint()

    @property
    def base_quaternion_str(self):
        return "{} {} {} {}".format(self.base_quat[0], self.base_quat[1],
                                    self.base_quat[2], self.base_quat[3])

    @property
    def shoulder_quaternion_str(self):
        return "{} {} {} {}".format(self.shoulder_quat[0], self.shoulder_quat[1],
                                    self.shoulder_quat[2], self.shoulder_quat[3])

    @property
    def elbow_quaternion_str(self):
        return "{} {} {} {}".format(self.elbow_quat[0], self.elbow_quat[1],
                                    self.elbow_quat[2], self.elbow_quat[3])

    @property
    def wrist_1_quaternion_str(self):
        return "{} {} {} {}".format(self.wrist_1_quat[0], self.wrist_1_quat[1],
                                    self.wrist_1_quat[2], self.wrist_1_quat[3])

    @property
    def wrist_2_quaternion_str(self):
        return "{} {} {} {}".format(self.wrist_2_quat[0], self.wrist_2_quat[1],
                                    self.wrist_2_quat[2], self.wrist_2_quat[3])

    @property
    def wrist_3_quaternion_str(self):
        return "{} {} {} {}".format(self.wrist_3_quat[0], self.wrist_3_quat[1],
                                    self.wrist_3_quat[2], self.wrist_3_quat[3])

    def _set_desired_quaternion_for_base_joint(self):
        original_quaternion = Quaternion(0.681998, 0, 0, -0.731354)
        self.base_quat = self._apply_rotation(original_quaternion, axis=[0, 0, 1], angle=self.base_joint_value)

    def _set_desired_quaternion_for_shoulder_joint(self):
        original_quaternion = Quaternion(0.707107, 0, 0.707107, 0)
        self.shoulder_quat = self._apply_rotation(original_quaternion, axis=[0, 1, 0], angle=self.shoulder_joint_value)

    def _set_desired_quaternion_for_elbow_joint(self):
        original_quaternion = Quaternion(1.0, 0, 0, 0)
        self.elbow_quat = self._apply_rotation(original_quaternion, axis=[0, 1, 0], angle=self.elbow_joint_value)

    def _set_desired_quaternion_for_wrist_1_joint(self):
        original_quaternion = Quaternion(0.707107, 0, 0.707107, 0)
        self.wrist_1_quat = self._apply_rotation(original_quaternion, axis=[0, 1, 0], angle=self.wrist_1_joint_value)

    def _set_desired_quaternion_for_wrist_2_joint(self):
        original_quaternion = Quaternion(1.0, 0.0, 0.0, 0.0)
        self.wrist_2_quat = self._apply_rotation(original_quaternion, axis=[0, 0, 1], angle=self.wrist_2_joint_value)

    def _set_desired_quaternion_for_wrist_3_joint(self):
        original_quaternion = Quaternion(1.0, 0.0, 0.0, 0.0)
        self.wrist_3_quat = self._apply_rotation(original_quaternion, axis=[0, 1, 0], angle=self.wrist_3_joint_value)

    @staticmethod
    def _apply_rotation(q1, axis, angle):
        angle_in_radians = math.radians(angle)
        q2 = Quaternion(axis=axis, angle=angle_in_radians)
        result = q1 * q2
        return result.elements


def update_xml_with_desired_joint_values(file_path, ur5):
    xml_document = minidom.parse(file_path)
    bodies = xml_document.getElementsByTagName("body")

    for body in bodies:
        if body.attributes["name"].value == "base_link":
            body.setAttribute("quat", ur5.base_quaternion_str)

        if body.attributes["name"].value == "shoulder_link":
            body.setAttribute("quat", ur5.shoulder_quaternion_str)

        if body.attributes["name"].value == "elbow_link":
            body.setAttribute("quat", ur5.elbow_quaternion_str)

        if body.attributes["name"].value == "wrist_1_link":
            body.setAttribute("quat", ur5.wrist_1_quaternion_str)

        if body.attributes["name"].value == "wrist_2_link":
            body.setAttribute("quat", ur5.wrist_2_quaternion_str)

        if body.attributes["name"].value == "wrist_3_link":
            body.setAttribute("quat", ur5.wrist_3_quaternion_str)
 
    file_writer = open(file_path, "w")
    xml_document.writexml(file_writer)


if __name__ == "__main__":
    desired_base_joint_angle = float(input("Enter the desired joint angle for the base joint in terms of degrees: "))
    desired_shoulder_joint_angle = float(input("Enter the desired joint angle for the shoulder joint in terms of degrees: "))
    desired_elbow_joint_angle = float(input("Enter the desired joint angle for the elbow joint in terms of degrees: "))
    desired_wrist1_joint_angle = float(input("Enter the desired joint angle for the wrist 1 joint in terms of degrees: "))
    desired_wrist2_joint_angle = float(input("Enter the desired joint angle for the wrist 2 joint in terms of degrees: "))
    desired_wrist3_joint_angle = float(input("Enter the desired joint angle for the wrist 3 joint in terms of degrees: "))

    model_file_path = input("Please type the path to the xml file to be updated: ")

    ur5 = UR5(desired_base_joint_angle, desired_shoulder_joint_angle,
              desired_elbow_joint_angle, desired_wrist1_joint_angle,
              desired_wrist2_joint_angle, desired_wrist3_joint_angle)

    # Do the required calculations to convert the desired joint angles into
    # correct quaternions to set the MuJoCo model.
    ur5.apply_joint_angles()

    # Now update the model file on disk.
    update_xml_with_desired_joint_values(model_file_path, ur5)

