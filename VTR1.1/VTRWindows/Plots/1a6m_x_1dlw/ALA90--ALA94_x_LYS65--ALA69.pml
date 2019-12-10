load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mALA90,model 1a6m_rotate and resi 90
select 1a6mALA94,model 1a6m_rotate and resi 94
show sticks, 1a6mALA90 1a6mALA94
select 1dlwLYS65,model 1dlw and resi 65
select 1dlwALA69,model 1dlw and resi 69
show sticks, 1dlwLYS65 1dlwALA69
sele resn HOH
hide (sele)
set_color 5_0_249, [5,0,249]
select 1a6m766,model 1a6m_rotate and id 766
select 1a6m798,model 1a6m_rotate and id 798
distance 1a6m766-1a6m798, 1a6m766, 1a6m798
color 5_0_249, 1a6m766-1a6m798
select 1dlw474,model 1dlw and id 474
select 1dlw506,model 1dlw and id 506
distance 1dlw474-1dlw506, 1dlw474, 1dlw506
color 5_0_249, 1dlw474-1dlw506
