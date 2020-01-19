#!/usr/bin/env pymol
load ../Data/1dlwx1a6m_align/1dlw.pdb
load ../Data/1a6m.pdb
hide all
show cartoon
color red
color blue, ../Data/1dlwx1a6m_align/1dlw
set stick_radius, 0.25
set sphere_scale, 0.25
show stick, not polymer
show sphere, not polymer
zoom
set ray_shadow, 0
