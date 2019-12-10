load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mVAL66,model 1a6m_rotate and resi 66
select 1a6mTHR70,model 1a6m_rotate and resi 70
show sticks, 1a6mVAL66 1a6mTHR70
select 1dlwASN43,model 1dlw and resi 43
select 1dlwALA47,model 1dlw and resi 47
show sticks, 1dlwASN43 1dlwALA47
sele resn HOH
hide (sele)
set_color 78_0_176, [78,0,176]
select 1a6m586,model 1a6m_rotate and id 586
select 1a6m612,model 1a6m_rotate and id 612
distance 1a6m586-1a6m612, 1a6m586, 1a6m612
color 78_0_176, 1a6m586-1a6m612
select 1dlw317,model 1dlw and id 317
select 1dlw343,model 1dlw and id 343
distance 1dlw317-1dlw343, 1dlw317, 1dlw343
color 78_0_176, 1dlw317-1dlw343
