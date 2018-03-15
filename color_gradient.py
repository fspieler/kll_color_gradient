#!/usr/bin/env python
from __future__ import division

header = \
"""
Name = "Color gradient";
Version = 0.1;
Author = "fspieler (Fred Spieler) 2018";
KLL = 0.5;

Date = 2018-03-15;

A[color_gradient] <= start, framedelay:1, framestretch, loop, replace:all, pfunc:interp;
"""
def get_color_for_frame(start, end, total_frames, frame_num):
    delta = map(lambda x: x[0]-x[1],zip(end,start))
    percent = frame_num / total_frames
    return tuple(map(lambda x: int(x[0] + percent * x[1]), zip(start, delta)))
colors = [(0,0,255),(255,0,255),(255,0,0),(255,255,0),(0,255,0),(0,255,255)]
colors.append(colors[0])
frames_per_transition = 100
frame_counter = 1
with open("color_gradient.kll",'w') as f:
    f.write(header)
    for idx, main_color in enumerate(colors):
        if idx == len(colors) - 1:
            break
        for frame in range(frames_per_transition):
            intermediate_color = get_color_for_frame(colors[idx],colors[idx+1],frames_per_transition, frame)
            frame_rows = reduce(lambda a,b:"{}, P[r:{}] {}".format(a,b,intermediate_color),range(1,8),"P[r:0] {}".format(intermediate_color))
            f.write("A[color_gradient, {}] <= {};\n".format(frame_counter, frame_rows))
            frame_counter += 1


