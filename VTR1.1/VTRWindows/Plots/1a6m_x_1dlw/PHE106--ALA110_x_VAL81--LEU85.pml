load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mPHE106,model 1a6m_rotate and resi 106
select 1a6mALA110,model 1a6m_rotate and resi 110
show sticks, 1a6mPHE106 1a6mALA110
select 1dlwVAL81,model 1dlw and resi 81
select 1dlwLEU85,model 1dlw and resi 85
show sticks, 1dlwVAL81 1dlwLEU85
sele resn HOH
hide (sele)
set_color 57_0_197, [57,0,197]
select 1a6m907,model 1a6m_rotate and id 907
select 1a6m943,model 1a6m_rotate and id 943
distance 1a6m907-1a6m943, 1a6m907, 1a6m943
color 57_0_197, 1a6m907-1a6m943
select 1dlw594,model 1dlw and id 594
select 1dlw620,model 1dlw and id 620
distance 1dlw594-1dlw620, 1dlw594, 1dlw620
color 57_0_197, 1dlw594-1dlw620
