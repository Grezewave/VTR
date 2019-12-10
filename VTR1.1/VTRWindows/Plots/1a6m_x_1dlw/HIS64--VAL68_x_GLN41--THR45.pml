load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mHIS64,model 1a6m_rotate and resi 64
select 1a6mVAL68,model 1a6m_rotate and resi 68
show sticks, 1a6mHIS64 1a6mVAL68
select 1dlwGLN41,model 1dlw and resi 41
select 1dlwTHR45,model 1dlw and resi 45
show sticks, 1dlwGLN41 1dlwTHR45
sele resn HOH
hide (sele)
set_color 51_0_203, [51,0,203]
select 1a6m566,model 1a6m_rotate and id 566
select 1a6m597,model 1a6m_rotate and id 597
distance 1a6m566-1a6m597, 1a6m566, 1a6m597
color 51_0_203, 1a6m566-1a6m597
select 1dlw301,model 1dlw and id 301
select 1dlw331,model 1dlw and id 331
distance 1dlw301-1dlw331, 1dlw301, 1dlw331
color 51_0_203, 1dlw301-1dlw331
