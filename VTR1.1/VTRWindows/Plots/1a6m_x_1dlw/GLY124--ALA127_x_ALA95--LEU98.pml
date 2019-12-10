load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mGLY124,model 1a6m_rotate and resi 124
select 1a6mALA127,model 1a6m_rotate and resi 127
show sticks, 1a6mGLY124 1a6mALA127
select 1dlwALA95,model 1dlw and resi 95
select 1dlwLEU98,model 1dlw and resi 98
show sticks, 1dlwALA95 1dlwLEU98
sele resn HOH
hide (sele)
set_color 42_0_212, [42,0,212]
select 1a6m1078,model 1a6m_rotate and id 1078
select 1a6m1096,model 1a6m_rotate and id 1096
distance 1a6m1078-1a6m1096, 1a6m1078, 1a6m1096
color 42_0_212, 1a6m1078-1a6m1096
select 1dlw688,model 1dlw and id 688
select 1dlw700,model 1dlw and id 700
distance 1dlw688-1dlw700, 1dlw688, 1dlw700
color 42_0_212, 1dlw688-1dlw700
