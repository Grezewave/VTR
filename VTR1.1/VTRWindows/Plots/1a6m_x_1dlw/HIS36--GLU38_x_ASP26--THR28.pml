load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mHIS36,model 1a6m_rotate and resi 36
select 1a6mGLU38,model 1a6m_rotate and resi 38
show sticks, 1a6mHIS36 1a6mGLU38
select 1dlwASP26,model 1dlw and resi 26
select 1dlwTHR28,model 1dlw and resi 28
show sticks, 1dlwASP26 1dlwTHR28
sele resn HOH
hide (sele)
load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mHIS36,model 1a6m_rotate and resi 36
select 1a6mGLU38,model 1a6m_rotate and resi 38
show sticks, 1a6mHIS36 1a6mGLU38
select 1dlwASP26,model 1dlw and resi 26
select 1dlwTHR28,model 1dlw and resi 28
show sticks, 1dlwASP26 1dlwTHR28
sele resn HOH
hide (sele)
set_color 35_0_219, [35,0,219]
select 1a6m305,model 1a6m_rotate and id 305
select 1a6m319,model 1a6m_rotate and id 319
distance 1a6m305-1a6m319, 1a6m305, 1a6m319
color 35_0_219, 1a6m305-1a6m319
select 1dlw189,model 1dlw and id 189
select 1dlw199,model 1dlw and id 199
distance 1dlw189-1dlw199, 1dlw189, 1dlw199
color 35_0_219, 1dlw189-1dlw199
set_color 3_0_251, [3,0,251]
select 1a6m308,model 1a6m_rotate and id 308
select 1a6m327,model 1a6m_rotate and id 327
distance 1a6m308-1a6m327, 1a6m308, 1a6m327
color 3_0_251, 1a6m308-1a6m327
select 1dlw193,model 1dlw and id 193
select 1dlw204,model 1dlw and id 204
distance 1dlw193-1dlw204, 1dlw193, 1dlw204
color 3_0_251, 1dlw193-1dlw204
