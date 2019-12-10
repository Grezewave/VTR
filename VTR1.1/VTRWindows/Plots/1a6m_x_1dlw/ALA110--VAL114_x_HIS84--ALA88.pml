load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mALA110,model 1a6m_rotate and resi 110
select 1a6mVAL114,model 1a6m_rotate and resi 114
show sticks, 1a6mALA110 1a6mVAL114
select 1dlwHIS84,model 1dlw and resi 84
select 1dlwALA88,model 1dlw and resi 88
show sticks, 1dlwHIS84 1dlwALA88
sele resn HOH
hide (sele)
set_color 70_0_184, [70,0,184]
select 1a6m946,model 1a6m_rotate and id 946
select 1a6m974,model 1a6m_rotate and id 974
distance 1a6m946-1a6m974, 1a6m946, 1a6m974
color 70_0_184, 1a6m946-1a6m974
select 1dlw613,model 1dlw and id 613
select 1dlw645,model 1dlw and id 645
distance 1dlw613-1dlw645, 1dlw613, 1dlw645
color 70_0_184, 1dlw613-1dlw645
