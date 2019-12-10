load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLYS102,model 1a6m_rotate and resi 102
select 1a6mPHE106,model 1a6m_rotate and resi 106
show sticks, 1a6mLYS102 1a6mPHE106
select 1dlwGLN77,model 1dlw and resi 77
select 1dlwVAL81,model 1dlw and resi 81
show sticks, 1dlwGLN77 1dlwVAL81
sele resn HOH
hide (sele)
set_color 58_0_196, [58,0,196]
select 1a6m869,model 1a6m_rotate and id 869
select 1a6m904,model 1a6m_rotate and id 904
distance 1a6m869-1a6m904, 1a6m869, 1a6m904
color 58_0_196, 1a6m869-1a6m904
select 1dlw560,model 1dlw and id 560
select 1dlw591,model 1dlw and id 591
distance 1dlw560-1dlw591, 1dlw560, 1dlw591
color 58_0_196, 1dlw560-1dlw591
