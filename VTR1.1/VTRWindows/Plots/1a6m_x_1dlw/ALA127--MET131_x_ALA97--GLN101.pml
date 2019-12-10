load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mALA127,model 1a6m_rotate and resi 127
select 1a6mMET131,model 1a6m_rotate and resi 131
show sticks, 1a6mALA127 1a6mMET131
select 1dlwALA97,model 1dlw and resi 97
select 1dlwGLN101,model 1dlw and resi 101
show sticks, 1dlwALA97 1dlwGLN101
sele resn HOH
hide (sele)
set_color 65_0_189, [65,0,189]
select 1a6m1099,model 1a6m_rotate and id 1099
select 1a6m1124,model 1a6m_rotate and id 1124
distance 1a6m1099-1a6m1124, 1a6m1099, 1a6m1124
color 65_0_189, 1a6m1099-1a6m1124
select 1dlw698,model 1dlw and id 698
select 1dlw724,model 1dlw and id 724
distance 1dlw698-1dlw724, 1dlw698, 1dlw724
color 65_0_189, 1dlw698-1dlw724
