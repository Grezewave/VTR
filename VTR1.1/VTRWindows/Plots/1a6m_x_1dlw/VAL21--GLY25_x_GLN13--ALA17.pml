load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mVAL21,model 1a6m_rotate and resi 21
select 1a6mGLY25,model 1a6m_rotate and resi 25
show sticks, 1a6mVAL21 1a6mGLY25
select 1dlwGLN13,model 1dlw and resi 13
select 1dlwALA17,model 1dlw and resi 17
show sticks, 1dlwGLN13 1dlwALA17
sele resn HOH
hide (sele)
set_color 80_0_174, [80,0,174]
select 1a6m177,model 1a6m_rotate and id 177
select 1a6m200,model 1a6m_rotate and id 200
distance 1a6m177-1a6m200, 1a6m177, 1a6m200
color 80_0_174, 1a6m177-1a6m200
select 1dlw89,model 1dlw and id 89
select 1dlw114,model 1dlw and id 114
distance 1dlw89-1dlw114, 1dlw89, 1dlw114
color 80_0_174, 1dlw89-1dlw114
