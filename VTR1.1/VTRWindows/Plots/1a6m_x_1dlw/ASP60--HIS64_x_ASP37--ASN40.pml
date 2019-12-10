load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mASP60,model 1a6m_rotate and resi 60
select 1a6mHIS64,model 1a6m_rotate and resi 64
show sticks, 1a6mASP60 1a6mHIS64
select 1dlwASP37,model 1dlw and resi 37
select 1dlwASN40,model 1dlw and resi 40
show sticks, 1dlwASP37 1dlwASN40
sele resn HOH
hide (sele)
set_color 47_0_207, [47,0,207]
select 1a6m523,model 1a6m_rotate and id 523
select 1a6m563,model 1a6m_rotate and id 563
distance 1a6m523-1a6m563, 1a6m523, 1a6m563
color 47_0_207, 1a6m523-1a6m563
select 1dlw273,model 1dlw and id 273
select 1dlw290,model 1dlw and id 290
distance 1dlw273-1dlw290, 1dlw273, 1dlw290
color 47_0_207, 1dlw273-1dlw290
