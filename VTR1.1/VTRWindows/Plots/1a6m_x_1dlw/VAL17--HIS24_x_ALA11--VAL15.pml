load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mVAL17,model 1a6m_rotate and resi 17
select 1a6mHIS24,model 1a6m_rotate and resi 24
show sticks, 1a6mVAL17 1a6mHIS24
select 1dlwALA11,model 1dlw and resi 11
select 1dlwVAL15,model 1dlw and resi 15
show sticks, 1dlwALA11 1dlwVAL15
sele resn HOH
hide (sele)
set_color 17_0_237, [17,0,237]
select 1a6m151,model 1a6m_rotate and id 151
select 1a6m197,model 1a6m_rotate and id 197
distance 1a6m151-1a6m197, 1a6m151, 1a6m197
color 17_0_237, 1a6m151-1a6m197
select 1dlw77,model 1dlw and id 77
select 1dlw100,model 1dlw and id 100
distance 1dlw77-1dlw100, 1dlw77, 1dlw100
color 17_0_237, 1dlw77-1dlw100
