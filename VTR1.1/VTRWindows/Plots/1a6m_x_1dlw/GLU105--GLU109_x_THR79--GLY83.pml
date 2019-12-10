load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mGLU105,model 1a6m_rotate and resi 105
select 1a6mGLU109,model 1a6m_rotate and resi 109
show sticks, 1a6mGLU105 1a6mGLU109
select 1dlwTHR79,model 1dlw and resi 79
select 1dlwGLY83,model 1dlw and resi 83
show sticks, 1dlwTHR79 1dlwGLY83
sele resn HOH
hide (sele)
set_color 21_0_233, [21,0,233]
select 1a6m898,model 1a6m_rotate and id 898
select 1a6m929,model 1a6m_rotate and id 929
distance 1a6m898-1a6m929, 1a6m898, 1a6m929
color 21_0_233, 1a6m898-1a6m929
select 1dlw580,model 1dlw and id 580
select 1dlw606,model 1dlw and id 606
distance 1dlw580-1dlw606, 1dlw580, 1dlw606
color 21_0_233, 1dlw580-1dlw606
