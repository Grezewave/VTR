load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mVAL114,model 1a6m_rotate and resi 114
select 1a6mSER117,model 1a6m_rotate and resi 117
show sticks, 1a6mVAL114 1a6mSER117
select 1dlwALA88,model 1dlw and resi 88
select 1dlwALA92,model 1dlw and resi 92
show sticks, 1dlwALA88 1dlwALA92
sele resn HOH
hide (sele)
set_color 70_0_184, [70,0,184]
select 1a6m977,model 1a6m_rotate and id 977
select 1a6m1009,model 1a6m_rotate and id 1009
distance 1a6m977-1a6m1009, 1a6m977, 1a6m1009
color 70_0_184, 1a6m977-1a6m1009
select 1dlw648,model 1dlw and id 648
select 1dlw669,model 1dlw and id 669
distance 1dlw648-1dlw669, 1dlw648, 1dlw669
color 70_0_184, 1dlw648-1dlw669
