load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mGLY25,model 1a6m_rotate and resi 25
select 1a6mLEU29,model 1a6m_rotate and resi 29
show sticks, 1a6mGLY25 1a6mLEU29
select 1dlwTHR16,model 1dlw and resi 16
select 1dlwTYR20,model 1dlw and resi 20
show sticks, 1dlwTHR16 1dlwTYR20
sele resn HOH
hide (sele)
set_color 58_0_196, [58,0,196]
select 1a6m203,model 1a6m_rotate and id 203
select 1a6m234,model 1a6m_rotate and id 234
distance 1a6m203-1a6m234, 1a6m203, 1a6m234
color 58_0_196, 1a6m203-1a6m234
select 1dlw110,model 1dlw and id 110
select 1dlw139,model 1dlw and id 139
distance 1dlw110-1dlw139, 1dlw110, 1dlw139
color 58_0_196, 1dlw110-1dlw139
