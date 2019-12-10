load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mGLN26,model 1a6m_rotate and resi 26
select 1a6mILE30,model 1a6m_rotate and resi 30
show sticks, 1a6mGLN26 1a6mILE30
select 1dlwALA17,model 1dlw and resi 17
select 1dlwALA21,model 1dlw and resi 21
show sticks, 1dlwALA17 1dlwALA21
sele resn HOH
hide (sele)
set_color 65_0_189, [65,0,189]
select 1a6m207,model 1a6m_rotate and id 207
select 1a6m242,model 1a6m_rotate and id 242
distance 1a6m207-1a6m242, 1a6m207, 1a6m242
color 65_0_189, 1a6m207-1a6m242
select 1dlw117,model 1dlw and id 117
select 1dlw151,model 1dlw and id 151
distance 1dlw117-1dlw151, 1dlw117, 1dlw151
color 65_0_189, 1dlw117-1dlw151
