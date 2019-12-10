load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mGLY124,model 1a6m_rotate and resi 124
select 1a6mGLN128,model 1a6m_rotate and resi 128
show sticks, 1a6mGLY124 1a6mGLN128
select 1dlwALA95,model 1dlw and resi 95
select 1dlwVAL99,model 1dlw and resi 99
show sticks, 1dlwALA95 1dlwVAL99
sele resn HOH
hide (sele)
set_color 15_0_239, [15,0,239]
select 1a6m1078,model 1a6m_rotate and id 1078
select 1a6m1101,model 1a6m_rotate and id 1101
distance 1a6m1078-1a6m1101, 1a6m1078, 1a6m1101
color 15_0_239, 1a6m1078-1a6m1101
select 1dlw688,model 1dlw and id 688
select 1dlw708,model 1dlw and id 708
distance 1dlw688-1dlw708, 1dlw688, 1dlw708
color 15_0_239, 1dlw688-1dlw708
