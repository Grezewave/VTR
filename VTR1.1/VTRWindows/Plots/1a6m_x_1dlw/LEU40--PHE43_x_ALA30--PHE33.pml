load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLEU40,model 1a6m_rotate and resi 40
select 1a6mPHE43,model 1a6m_rotate and resi 43
show sticks, 1a6mLEU40 1a6mPHE43
select 1dlwALA30,model 1dlw and resi 30
select 1dlwPHE33,model 1dlw and resi 33
show sticks, 1dlwALA30 1dlwPHE33
sele resn HOH
hide (sele)
set_color 18_0_236, [18,0,236]
select 1a6m338,model 1a6m_rotate and id 338
select 1a6m366,model 1a6m_rotate and id 366
distance 1a6m338-1a6m366, 1a6m338, 1a6m366
color 18_0_236, 1a6m338-1a6m366
select 1dlw216,model 1dlw and id 216
select 1dlw236,model 1dlw and id 236
distance 1dlw216-1dlw236, 1dlw216, 1dlw236
color 18_0_236, 1dlw216-1dlw236
