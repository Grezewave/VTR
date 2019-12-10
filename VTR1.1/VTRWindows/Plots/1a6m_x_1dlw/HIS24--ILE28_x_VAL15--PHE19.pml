load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mHIS24,model 1a6m_rotate and resi 24
select 1a6mILE28,model 1a6m_rotate and resi 28
show sticks, 1a6mHIS24 1a6mILE28
select 1dlwVAL15,model 1dlw and resi 15
select 1dlwPHE19,model 1dlw and resi 19
show sticks, 1dlwVAL15 1dlwPHE19
sele resn HOH
hide (sele)
set_color 18_0_236, [18,0,236]
select 1a6m193,model 1a6m_rotate and id 193
select 1a6m226,model 1a6m_rotate and id 226
distance 1a6m193-1a6m226, 1a6m193, 1a6m226
color 18_0_236, 1a6m193-1a6m226
select 1dlw103,model 1dlw and id 103
select 1dlw128,model 1dlw and id 128
distance 1dlw103-1dlw128, 1dlw103, 1dlw128
color 18_0_236, 1dlw103-1dlw128
