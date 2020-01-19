#!/usr/bin/env pymol
load ../Data/1a6mx2mm1_align/1a6m.pdb
load ../Data/2mm1.pdb
hide all
show cartoon
color red
color blue, ../Data/1a6mx2mm1_align/1a6m
set stick_radius, 0.25
set sphere_scale, 0.25
show stick, not polymer
show sphere, not polymer
zoom
set ray_shadow, 0
