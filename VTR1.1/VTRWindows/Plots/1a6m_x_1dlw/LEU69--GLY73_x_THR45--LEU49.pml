load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLEU69,model 1a6m_rotate and resi 69
select 1a6mGLY73,model 1a6m_rotate and resi 73
show sticks, 1a6mLEU69 1a6mGLY73
select 1dlwTHR45,model 1dlw and resi 45
select 1dlwLEU49,model 1dlw and resi 49
show sticks, 1dlwTHR45 1dlwLEU49
sele resn HOH
hide (sele)
set_color 103_0_151, [103,0,151]
select 1a6m607,model 1a6m_rotate and id 607
select 1a6m632,model 1a6m_rotate and id 632
distance 1a6m607-1a6m632, 1a6m607, 1a6m632
color 103_0_151, 1a6m607-1a6m632
select 1dlw334,model 1dlw and id 334
select 1dlw359,model 1dlw and id 359
distance 1dlw334-1dlw359, 1dlw334, 1dlw359
color 103_0_151, 1dlw334-1dlw359
