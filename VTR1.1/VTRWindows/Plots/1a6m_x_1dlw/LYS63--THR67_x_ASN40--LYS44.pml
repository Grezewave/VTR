load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLYS63,model 1a6m_rotate and resi 63
select 1a6mTHR67,model 1a6m_rotate and resi 67
show sticks, 1a6mLYS63 1a6mTHR67
select 1dlwASN40,model 1dlw and resi 40
select 1dlwLYS44,model 1dlw and resi 44
show sticks, 1dlwASN40 1dlwLYS44
sele resn HOH
hide (sele)
set_color 37_0_217, [37,0,217]
select 1a6m552,model 1a6m_rotate and id 552
select 1a6m590,model 1a6m_rotate and id 590
distance 1a6m552-1a6m590, 1a6m552, 1a6m590
color 37_0_217, 1a6m552-1a6m590
select 1dlw293,model 1dlw and id 293
select 1dlw322,model 1dlw and id 322
distance 1dlw293-1dlw322, 1dlw293, 1dlw322
color 37_0_217, 1dlw293-1dlw322
