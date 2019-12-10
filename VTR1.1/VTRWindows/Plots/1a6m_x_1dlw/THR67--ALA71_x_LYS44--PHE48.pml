load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mTHR67,model 1a6m_rotate and resi 67
select 1a6mALA71,model 1a6m_rotate and resi 71
show sticks, 1a6mTHR67 1a6mALA71
select 1dlwLYS44,model 1dlw and resi 44
select 1dlwPHE48,model 1dlw and resi 48
show sticks, 1dlwLYS44 1dlwPHE48
sele resn HOH
hide (sele)
set_color 42_0_212, [42,0,212]
select 1a6m593,model 1a6m_rotate and id 593
select 1a6m619,model 1a6m_rotate and id 619
distance 1a6m593-1a6m619, 1a6m593, 1a6m619
color 42_0_212, 1a6m593-1a6m619
select 1dlw325,model 1dlw and id 325
select 1dlw348,model 1dlw and id 348
distance 1dlw325-1dlw348, 1dlw325, 1dlw348
color 42_0_212, 1dlw325-1dlw348
