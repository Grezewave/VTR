load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mTHR70,model 1a6m_rotate and resi 70
select 1a6mALA74,model 1a6m_rotate and resi 74
show sticks, 1a6mTHR70 1a6mALA74
select 1dlwALA47,model 1dlw and resi 47
select 1dlwALA51,model 1dlw and resi 51
show sticks, 1dlwALA47 1dlwALA51
sele resn HOH
hide (sele)
set_color 23_0_231, [23,0,231]
select 1a6m615,model 1a6m_rotate and id 615
select 1a6m636,model 1a6m_rotate and id 636
distance 1a6m615-1a6m636, 1a6m615, 1a6m636
color 23_0_231, 1a6m615-1a6m636
select 1dlw346,model 1dlw and id 346
select 1dlw373,model 1dlw and id 373
distance 1dlw346-1dlw373, 1dlw346, 1dlw373
color 23_0_231, 1dlw346-1dlw373
