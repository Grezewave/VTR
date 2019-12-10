load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mHIS36,model 1a6m_rotate and resi 36
select 1a6mTHR39,model 1a6m_rotate and resi 39
show sticks, 1a6mHIS36 1a6mTHR39
select 1dlwASP26,model 1dlw and resi 26
select 1dlwALA30,model 1dlw and resi 30
show sticks, 1dlwASP26 1dlwALA30
sele resn HOH
hide (sele)
set_color 18_0_236, [18,0,236]
select 1a6m305,model 1a6m_rotate and id 305
select 1a6m333,model 1a6m_rotate and id 333
distance 1a6m305-1a6m333, 1a6m305, 1a6m333
color 18_0_236, 1a6m305-1a6m333
select 1dlw189,model 1dlw and id 189
select 1dlw213,model 1dlw and id 213
distance 1dlw189-1dlw213, 1dlw189, 1dlw213
color 18_0_236, 1dlw189-1dlw213
