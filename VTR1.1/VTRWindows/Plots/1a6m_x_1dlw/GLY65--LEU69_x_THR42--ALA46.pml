load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mGLY65,model 1a6m_rotate and resi 65
select 1a6mLEU69,model 1a6m_rotate and resi 69
show sticks, 1a6mGLY65 1a6mLEU69
select 1dlwTHR42,model 1dlw and resi 42
select 1dlwALA46,model 1dlw and resi 46
show sticks, 1dlwTHR42 1dlwALA46
sele resn HOH
hide (sele)
set_color 55_0_199, [55,0,199]
select 1a6m582,model 1a6m_rotate and id 582
select 1a6m604,model 1a6m_rotate and id 604
distance 1a6m582-1a6m604, 1a6m582, 1a6m604
color 55_0_199, 1a6m582-1a6m604
select 1dlw310,model 1dlw and id 310
select 1dlw338,model 1dlw and id 338
distance 1dlw310-1dlw338, 1dlw310, 1dlw338
color 55_0_199, 1dlw310-1dlw338
