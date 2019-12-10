load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mASP20,model 1a6m_rotate and resi 20
select 1a6mHIS24,model 1a6m_rotate and resi 24
show sticks, 1a6mASP20 1a6mHIS24
select 1dlwALA10,model 1dlw and resi 10
select 1dlwALA14,model 1dlw and resi 14
show sticks, 1dlwALA10 1dlwALA14
sele resn HOH
hide (sele)
set_color 0_0_254, [0,0,254]
select 1a6m169,model 1a6m_rotate and id 169
select 1a6m196,model 1a6m_rotate and id 196
distance 1a6m169-1a6m196, 1a6m169, 1a6m196
color 0_0_254, 1a6m169-1a6m196
select 1dlw72,model 1dlw and id 72
select 1dlw95,model 1dlw and id 95
distance 1dlw72-1dlw95, 1dlw72, 1dlw95
color 0_0_254, 1dlw72-1dlw95
