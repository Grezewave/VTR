load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLEU61,model 1a6m_rotate and resi 61
select 1a6mGLY65,model 1a6m_rotate and resi 65
show sticks, 1a6mLEU61 1a6mGLY65
select 1dlwMET38,model 1dlw and resi 38
select 1dlwTHR42,model 1dlw and resi 42
show sticks, 1dlwMET38 1dlwTHR42
sele resn HOH
hide (sele)
set_color 84_0_170, [84,0,170]
select 1a6m531,model 1a6m_rotate and id 531
select 1a6m579,model 1a6m_rotate and id 579
distance 1a6m531-1a6m579, 1a6m531, 1a6m579
color 84_0_170, 1a6m531-1a6m579
select 1dlw278,model 1dlw and id 278
select 1dlw307,model 1dlw and id 307
distance 1dlw278-1dlw307, 1dlw278, 1dlw307
color 84_0_170, 1dlw278-1dlw307
