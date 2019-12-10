load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mASP27,model 1a6m_rotate and resi 27
select 1a6mARG31,model 1a6m_rotate and resi 31
show sticks, 1a6mASP27 1a6mARG31
select 1dlwGLN18,model 1dlw and resi 18
select 1dlwASN22,model 1dlw and resi 22
show sticks, 1dlwGLN18 1dlwASN22
sele resn HOH
hide (sele)
set_color 155_0_99, [155,0,99]
select 1a6m221,model 1a6m_rotate and id 221
select 1a6m250,model 1a6m_rotate and id 250
distance 1a6m221-1a6m250, 1a6m221, 1a6m250
color 155_0_99, 1a6m221-1a6m250
select 1dlw122,model 1dlw and id 122
select 1dlw156,model 1dlw and id 156
distance 1dlw122-1dlw156, 1dlw122, 1dlw156
color 155_0_99, 1dlw122-1dlw156
