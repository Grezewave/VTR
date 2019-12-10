load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLEU40,model 1a6m_rotate and resi 40
select 1a6mLYS42,model 1a6m_rotate and resi 42
show sticks, 1a6mLEU40 1a6mLYS42
select 1dlwALA30,model 1dlw and resi 30
select 1dlwPHE32,model 1dlw and resi 32
show sticks, 1dlwALA30 1dlwPHE32
sele resn HOH
hide (sele)
set_color 69_0_185, [69,0,185]
select 1a6m338,model 1a6m_rotate and id 338
select 1a6m357,model 1a6m_rotate and id 357
distance 1a6m338-1a6m357, 1a6m338, 1a6m357
color 69_0_185, 1a6m338-1a6m357
select 1dlw216,model 1dlw and id 216
select 1dlw225,model 1dlw and id 225
distance 1dlw216-1dlw225, 1dlw216, 1dlw225
color 69_0_185, 1dlw216-1dlw225
