load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mSER108,model 1a6m_rotate and resi 108
select 1a6mILE112,model 1a6m_rotate and resi 112
show sticks, 1a6mSER108 1a6mILE112
select 1dlwILE82,model 1dlw and resi 82
select 1dlwARG86,model 1dlw and resi 86
show sticks, 1dlwILE82 1dlwARG86
sele resn HOH
hide (sele)
set_color 31_0_223, [31,0,223]
select 1a6m926,model 1a6m_rotate and id 926
select 1a6m956,model 1a6m_rotate and id 956
distance 1a6m926-1a6m956, 1a6m926, 1a6m956
color 31_0_223, 1a6m926-1a6m956
select 1dlw601,model 1dlw and id 601
select 1dlw628,model 1dlw and id 628
distance 1dlw601-1dlw628, 1dlw601, 1dlw628
color 31_0_223, 1dlw601-1dlw628
