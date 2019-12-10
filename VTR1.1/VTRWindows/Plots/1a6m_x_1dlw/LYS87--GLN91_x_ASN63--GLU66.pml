load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLYS87,model 1a6m_rotate and resi 87
select 1a6mGLN91,model 1a6m_rotate and resi 91
show sticks, 1a6mLYS87 1a6mGLN91
select 1dlwASN63,model 1dlw and resi 63
select 1dlwGLU66,model 1dlw and resi 66
show sticks, 1dlwASN63 1dlwGLU66
sele resn HOH
hide (sele)
set_color 59_0_195, [59,0,195]
select 1a6m742,model 1a6m_rotate and id 742
select 1a6m768,model 1a6m_rotate and id 768
distance 1a6m742-1a6m768, 1a6m742, 1a6m768
color 59_0_195, 1a6m742-1a6m768
select 1dlw461,model 1dlw and id 461
select 1dlw480,model 1dlw and id 480
distance 1dlw461-1dlw480, 1dlw461, 1dlw480
color 59_0_195, 1dlw461-1dlw480
