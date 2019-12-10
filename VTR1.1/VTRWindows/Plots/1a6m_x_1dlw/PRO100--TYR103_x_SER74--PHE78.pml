load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mPRO100,model 1a6m_rotate and resi 100
select 1a6mTYR103,model 1a6m_rotate and resi 103
show sticks, 1a6mPRO100 1a6mTYR103
select 1dlwSER74,model 1dlw and resi 74
select 1dlwPHE78,model 1dlw and resi 78
show sticks, 1dlwSER74 1dlwPHE78
sele resn HOH
hide (sele)
set_color 36_0_218, [36,0,218]
select 1a6m854,model 1a6m_rotate and id 854
select 1a6m875,model 1a6m_rotate and id 875
distance 1a6m854-1a6m875, 1a6m854, 1a6m875
color 36_0_218, 1a6m854-1a6m875
select 1dlw541,model 1dlw and id 541
select 1dlw566,model 1dlw and id 566
distance 1dlw541-1dlw566, 1dlw541, 1dlw566
color 36_0_218, 1dlw541-1dlw566
