load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mALA22,model 1a6m_rotate and resi 22
select 1a6mVAL66,model 1a6m_rotate and resi 66
show sticks, 1a6mALA22 1a6mVAL66
select 1dlwGLN13,model 1dlw and resi 13
select 1dlwASN43,model 1dlw and resi 43
show sticks, 1dlwGLN13 1dlwASN43
sele resn HOH
hide (sele)
set_color 2_0_252, [2,0,252]
select 1a6m185,model 1a6m_rotate and id 185
select 1a6m589,model 1a6m_rotate and id 589
distance 1a6m185-1a6m589, 1a6m185, 1a6m589
color 2_0_252, 1a6m185-1a6m589
select 1dlw94,model 1dlw and id 94
select 1dlw320,model 1dlw and id 320
distance 1dlw94-1dlw320, 1dlw94, 1dlw320
color 2_0_252, 1dlw94-1dlw320
