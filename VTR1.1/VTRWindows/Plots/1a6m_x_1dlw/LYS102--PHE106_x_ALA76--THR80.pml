load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLYS102,model 1a6m_rotate and resi 102
select 1a6mPHE106,model 1a6m_rotate and resi 106
show sticks, 1a6mLYS102 1a6mPHE106
select 1dlwALA76,model 1dlw and resi 76
select 1dlwTHR80,model 1dlw and resi 80
show sticks, 1dlwALA76 1dlwTHR80
sele resn HOH
hide (sele)
set_color 57_0_197, [57,0,197]
select 1a6m871,model 1a6m_rotate and id 871
select 1a6m914,model 1a6m_rotate and id 914
distance 1a6m871-1a6m914, 1a6m871, 1a6m914
color 57_0_197, 1a6m871-1a6m914
select 1dlw555,model 1dlw and id 555
select 1dlw589,model 1dlw and id 589
distance 1dlw555-1dlw589, 1dlw555, 1dlw589
color 57_0_197, 1dlw555-1dlw589
