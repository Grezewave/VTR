load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mPHE106,model 1a6m_rotate and resi 106
select 1a6mGLU109,model 1a6m_rotate and resi 109
show sticks, 1a6mPHE106 1a6mGLU109
select 1dlwTHR80,model 1dlw and resi 80
select 1dlwGLY83,model 1dlw and resi 83
show sticks, 1dlwTHR80 1dlwGLY83
sele resn HOH
hide (sele)
set_color 26_0_228, [26,0,228]
select 1a6m907,model 1a6m_rotate and id 907
select 1a6m929,model 1a6m_rotate and id 929
distance 1a6m907-1a6m929, 1a6m907, 1a6m929
color 26_0_228, 1a6m907-1a6m929
select 1dlw587,model 1dlw and id 587
select 1dlw606,model 1dlw and id 606
distance 1dlw587-1dlw606, 1dlw587, 1dlw606
color 26_0_228, 1dlw587-1dlw606
