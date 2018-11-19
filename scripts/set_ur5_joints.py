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
from xml.etree.ElementTree import XML, SubElement, Element, tostring
import math

def apply_rotation(q1, axis, angle):
    angle_in_radians = math.radians(angle)
    q2 = Quaternion(axis=axis, angle=angle_in_radians)
    result = q1 * q2
    return result.elements

def get_desired_quaternion_for_base_joint_from(angle_in_degrees):
    original_quaternion = Quaternion(0.681998, 0, 0, -0.731354)
    desired_quaternion = apply_rotation(original_quaternion,
                                        axis=[0, 0, 1],
                                        angle=angle_in_degrees)
    return desired_quaternion

def get_desired_quaternion_for_shoulder_joint_from(angle_in_degrees):
    original_quaternion = Quaternion(0.707107, 0, 0.707107, 0)
    desired_quaternion = apply_rotation(original_quaternion,
                                        axis=[0, 1, 0],
                                        angle=angle_in_degrees)
    return desired_quaternion

def get_desired_quaternion_for_elbow_joint_from(angle_in_degrees):
    original_quaternion = Quaternion(1.0, 0, 0, 0)
    desired_quaternion = apply_rotation(original_quaternion,
                                        axis=[0, 1, 0],
                                        angle=angle_in_degrees)
    return desired_quaternion

def get_desired_quaternion_for_wrist1_joint_from(angle_in_degrees):
    original_quaternion = Quaternion(0.707107, 0, 0.707107, 0)
    desired_quaternion = apply_rotation(original_quaternion,
                                        axis=[0, 1, 0],
                                        angle=angle_in_degrees)
    return desired_quaternion

def get_desired_quaternion_for_wrist2_joint_from(angle_in_degrees):
    original_quaternion = Quaternion(1.0, 0.0, 0.0, 0.0)
    desired_quaternion = apply_rotation(original_quaternion,
                                        axis=[0, 0, 1],
                                        angle=angle_in_degrees)
    return desired_quaternion

def get_desired_quaternion_for_wrist3_joint_from(angle_in_degrees):
    original_quaternion = Quaternion(1.0, 0.0, 0.0, 0.0)
    desired_quaternion = apply_rotation(original_quaternion,
                                        axis=[0, 1, 0],
                                        angle=angle_in_degrees)
    return desired_quaternion

def update_xml_with_desired_joint_values(file_path, base_joint_quaternion, shoulder_joint_quaternion, elbow_joint_quaternion, wrist1_joint_quaternion, wrist2_joint_quaternion, wrist3_joint_quaternion):
    from xml.dom import minidom
    xmldoc = minidom.parse(file_path)
    bodies = xmldoc.getElementsByTagName("body")
    for body in bodies:
        if body.attributes["name"].value == "shoulder_link":
            body.setAttribute("quat", "{} {} {} {}".format(base_joint_quaternion[0], base_joint_quaternion[1], base_joint_quaternion[2], base_joint_quaternion[3]))

        if body.attributes["name"].value == "upper_arm_link":
            body.setAttribute("quat", "{} {} {} {}".format(shoulder_joint_quaternion[0], shoulder_joint_quaternion[1], shoulder_joint_quaternion[2], shoulder_joint_quaternion[3]))

        if body.attributes["name"].value == "forearm_link":
            body.setAttribute("quat", "{} {} {} {}".format(elbow_joint_quaternion[0], elbow_joint_quaternion[1], elbow_joint_quaternion[2], elbow_joint_quaternion[3]))

        if body.attributes["name"].value == "wrist_1_link":
            body.setAttribute("quat", "{} {} {} {}".format(wrist1_joint_quaternion[0], wrist1_joint_quaternion[1], wrist1_joint_quaternion[2], wrist1_joint_quaternion[3]))

        if body.attributes["name"].value == "wrist_2_link":
            body.setAttribute("quat", "{} {} {} {}".format(wrist2_joint_quaternion[0], wrist2_joint_quaternion[1], wrist2_joint_quaternion[2], wrist2_joint_quaternion[3]))

        if body.attributes["name"].value == "wrist_3_link":
            body.setAttribute("quat", "{} {} {} {}".format(wrist3_joint_quaternion[0], wrist3_joint_quaternion[1], wrist3_joint_quaternion[2], wrist3_joint_quaternion[3]))
 
    file_writer = open(file_path, "w")
    xmldoc.writexml(file_writer)


if __name__ == "__main__":
    desired_base_joint_angle = float(input("Enter the desired joint angle for the base joint in terms of degrees: "))
    desired_shoulder_joint_angle = float(input("Enter the desired joint angle for the shoulder joint in terms of degrees: "))
    desired_elbow_joint_angle = float(input("Enter the desired joint angle for the elbow joint in terms of degrees: "))
    desired_wrist1_joint_angle = float(input("Enter the desired joint angle for the wrist 1 joint in terms of degrees: "))
    desired_wrist2_joint_angle = float(input("Enter the desired joint angle for the wrist 2 joint in terms of degrees: "))
    desired_wrist3_joint_angle = float(input("Enter the desired joint angle for the wrist 3 joint in terms of degrees: "))

    base_joint_quaternion = get_desired_quaternion_for_base_joint_from(desired_base_joint_angle)
    shoulder_joint_quaternion = get_desired_quaternion_for_shoulder_joint_from(desired_shoulder_joint_angle)
    elbow_joint_quaternion = get_desired_quaternion_for_elbow_joint_from(desired_elbow_joint_angle)
    wrist1_joint_quaternion = get_desired_quaternion_for_wrist1_joint_from(desired_wrist1_joint_angle)
    wrist2_joint_quaternion = get_desired_quaternion_for_wrist2_joint_from(desired_wrist2_joint_angle)
    wrist3_joint_quaternion = get_desired_quaternion_for_wrist3_joint_from(desired_wrist3_joint_angle)

    model_file_path = input("Please type the path to the xml file to be updated: ")

    update_xml_with_desired_joint_values(model_file_path,
                                         base_joint_quaternion,
                                         shoulder_joint_quaternion,
                                         elbow_joint_quaternion,
                                         wrist1_joint_quaternion,
                                         wrist2_joint_quaternion,
                                         wrist3_joint_quaternion)

