load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mGLU109,model 1a6m_rotate and resi 109
select 1a6mHIS113,model 1a6m_rotate and resi 113
show sticks, 1a6mGLU109 1a6mHIS113
select 1dlwGLY83,model 1dlw and resi 83
select 1dlwSER87,model 1dlw and resi 87
show sticks, 1dlwGLY83 1dlwSER87
sele resn HOH
hide (sele)
set_color 48_0_206, [48,0,206]
select 1a6m932,model 1a6m_rotate and id 932
select 1a6m964,model 1a6m_rotate and id 964
distance 1a6m932-1a6m964, 1a6m932, 1a6m964
color 48_0_206, 1a6m932-1a6m964
select 1dlw609,model 1dlw and id 609
select 1dlw639,model 1dlw and id 639
distance 1dlw609-1dlw639, 1dlw609, 1dlw639
color 48_0_206, 1dlw609-1dlw639
