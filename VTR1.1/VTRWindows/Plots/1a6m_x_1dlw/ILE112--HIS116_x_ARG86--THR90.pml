load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mILE112,model 1a6m_rotate and resi 112
select 1a6mHIS116,model 1a6m_rotate and resi 116
show sticks, 1a6mILE112 1a6mHIS116
select 1dlwARG86,model 1dlw and resi 86
select 1dlwTHR90,model 1dlw and resi 90
show sticks, 1dlwARG86 1dlwTHR90
sele resn HOH
hide (sele)
set_color 34_0_220, [34,0,220]
select 1a6m959,model 1a6m_rotate and id 959
select 1a6m993,model 1a6m_rotate and id 993
distance 1a6m959-1a6m993, 1a6m959, 1a6m993
color 34_0_220, 1a6m959-1a6m993
select 1dlw631,model 1dlw and id 631
select 1dlw658,model 1dlw and id 658
distance 1dlw631-1dlw658, 1dlw631, 1dlw658
color 34_0_220, 1dlw631-1dlw658
