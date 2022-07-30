import random
import math


# {
#    "all_wheels_on_track": Boolean,        # flag to indicate if the agent is on the track
#    "x": float,                            # agent's x-coordinate in meters
#    "y": float,                            # agent's y-coordinate in meters
#    "closest_objects": [int, int],         # zero-based indices of the two closest objects to the agent's current position of (x, y).
#    "closest_waypoints": [int, int],       # indices of the two nearest waypoints.
#    "distance_from_center": float,         # distance in meters from the track center
#    "is_crashed": Boolean,                 # Boolean flag to indicate whether the agent has crashed.
#    "is_left_of_center": Boolean,          # Flag to indicate if the agent is on the left side to the track center or not.
#    "is_offtrack": Boolean,                # Boolean flag to indicate whether the agent has gone off track.
#    "is_reversed": Boolean,                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
#    "heading": float,                      # agent's yaw in degrees
#    "objects_distance": [float, ],         # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
#    "objects_heading": [float, ],          # list of the objects' headings in degrees between -180 and 180.
#    "objects_left_of_center": [Boolean, ], # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
#    "objects_location": [(float, float),], # list of object locations [(x,y), ...].
#    "objects_speed": [float, ],            # list of the objects' speeds in meters per second.
#    "progress": float,                     # percentage of track completed
#    "speed": float,                        # agent's speed in meters per second (m/s)
#    "steering_angle": float,               # agent's steering angle in degrees
#    "steps": int,                          # number steps completed
#    "track_length": float,                 # track length in meters.
#    "track_width": float,                  # width of the track
#    "waypoints": [(float, float), ]        # list of (x,y) as milestones along the track center
#
# }


def reward_function(params):
    # get the input variable
    global reward
    all_wheels_on_track = params[all_wheels_on_track]
    x = data[x]
    y = data[y]
    closest_objects = params[closest_objects]
    closest_waypoints = params[closest_waypoints]
    distance_from_center = params[distance_from_center]
    is_crashed = params[is_crashed]
    is_left_of_center = params[is_left_of_center]
    is_offtrack = params[is_offtrack]
    is_offtrack = params[is_offtrack]
    heading = params[heading]
    objects_distance = params[objects_distance]
    objects_distance = params[objects_distance]
    objects_left_of_center = params[objects_left_of_center]
    objects_location = params[objects_location]
    objects_speed = params[objects_speed]
    progress = params[progress]
    speed = params[speed]
    steering_angle = params[steering_angle]
    steps = params[steps]
    track_length = params[track_length]
    track_width = params[track_width]
    waypoints = params[waypoints]

    # def the marker
    marker_1 = track_width * 0.1
    marker_2 = track_width * 0.25
    marker_3 = track_width * 0.5
    SPEED_THESEHOLD = 1.0

    # reward
    if not all_wheels_on_track:
        reward = 1e-3
    elif speed < SPEED_THESEHOLD:
        reward = + 1e-3
    elif distance_from_center <= marker_1:
        reward = + 1
    elif distance_from_center <= marker_2:
        reward = + 0.25
    elif distance_from_center <= marker_3:
        reward = + 1e-3
    elif is_offtrack:
        reward = + 1e-3
    elif is_reversed:
        reward =+ 1e-3
    elif is_crashed:
        reward = 0.0
    elif progress<90:
        reward =+ 1e-3
    else:
        reward = + 1

    return float(reward)


#############################################################################
'''data =["all_wheels_on_track":,        # flag to indicate if the agent is on the track
    "x",                            # agent's x-coordinate in meters
    "y",                            # agent's y-coordinate in meters
    "closest_objects",         # zero-based indices of the two closest objects to the agent's current position of (x, y).
    "closest_waypoints",       # indices of the two nearest waypoints.
    "distance_from_center",         # distance in meters from the track center
    "is_crashed",                 # Boolean flag to indicate whether the agent has crashed.
    "is_left_of_center",          # Flag to indicate if the agent is on the left side to the track center or not.
    "is_offtrack",                # Boolean flag to indicate whether the agent has gone off track.
    "is_offtrack",                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    "heading",                      # agent's yaw in degrees
    "objects_distance",         # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
    "objects_heading",          # list of the objects' headings in degrees between -180 and 180.
    "objects_left_of_center", # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
    "objects_location", # list of object locations [(x,y), ...].
    "objects_speed",            # list of the objects' speeds in meters per second.
    "progress",                     # percentage of track completed
    "speed",                        # agent's speed in meters per second (m/s)
    "steering_angle",               # agent's steering angle in degrees
    "steps",                          # number steps completed
    "track_length"                 # track length in meters.
    "track_width",                  # width of the track
    "waypoints"]'''
