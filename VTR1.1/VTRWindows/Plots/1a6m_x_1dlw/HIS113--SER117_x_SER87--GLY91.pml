load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mHIS113,model 1a6m_rotate and resi 113
select 1a6mSER117,model 1a6m_rotate and resi 117
show sticks, 1a6mHIS113 1a6mSER117
select 1dlwSER87,model 1dlw and resi 87
select 1dlwGLY91,model 1dlw and resi 91
show sticks, 1dlwSER87 1dlwGLY91
sele resn HOH
hide (sele)
set_color 61_0_193, [61,0,193]
select 1a6m967,model 1a6m_rotate and id 967
select 1a6m1009,model 1a6m_rotate and id 1009
distance 1a6m967-1a6m1009, 1a6m967, 1a6m1009
color 61_0_193, 1a6m967-1a6m1009
select 1dlw642,model 1dlw and id 642
select 1dlw665,model 1dlw and id 665
distance 1dlw642-1dlw665, 1dlw642, 1dlw665
color 61_0_193, 1dlw642-1dlw665
