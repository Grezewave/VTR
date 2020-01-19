#!/usr/bin/env pymol
load ../Data/3wcux3wcv_align/3wcu.pdb
load ../Data/3wcv.pdb
hide all
show cartoon
color red
color blue, ../Data/3wcux3wcv_align/3wcu
set stick_radius, 0.25
set sphere_scale, 0.25
show stick, not polymer
show sphere, not polymer
zoom
set ray_shadow, 0
