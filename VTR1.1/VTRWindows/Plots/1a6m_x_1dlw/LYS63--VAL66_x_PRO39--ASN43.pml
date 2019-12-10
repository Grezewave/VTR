load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLYS63,model 1a6m_rotate and resi 63
select 1a6mVAL66,model 1a6m_rotate and resi 66
show sticks, 1a6mLYS63 1a6mVAL66
select 1dlwPRO39,model 1dlw and resi 39
select 1dlwASN43,model 1dlw and resi 43
show sticks, 1dlwPRO39 1dlwASN43
sele resn HOH
hide (sele)
set_color 81_0_173, [81,0,173]
select 1a6m552,model 1a6m_rotate and id 552
select 1a6m583,model 1a6m_rotate and id 583
distance 1a6m552-1a6m583, 1a6m552, 1a6m583
color 81_0_173, 1a6m552-1a6m583
select 1dlw286,model 1dlw and id 286
select 1dlw314,model 1dlw and id 314
distance 1dlw286-1dlw314, 1dlw286, 1dlw314
color 81_0_173, 1dlw286-1dlw314
