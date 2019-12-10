load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLEU61,model 1a6m_rotate and resi 61
select 1a6mHIS64,model 1a6m_rotate and resi 64
show sticks, 1a6mLEU61 1a6mHIS64
select 1dlwMET38,model 1dlw and resi 38
select 1dlwGLN41,model 1dlw and resi 41
show sticks, 1dlwMET38 1dlwGLN41
sele resn HOH
hide (sele)
set_color 34_0_220, [34,0,220]
select 1a6m531,model 1a6m_rotate and id 531
select 1a6m563,model 1a6m_rotate and id 563
distance 1a6m531-1a6m563, 1a6m531, 1a6m563
color 34_0_220, 1a6m531-1a6m563
select 1dlw278,model 1dlw and id 278
select 1dlw298,model 1dlw and id 298
distance 1dlw278-1dlw298, 1dlw278, 1dlw298
color 34_0_220, 1dlw278-1dlw298
