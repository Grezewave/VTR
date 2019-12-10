load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLEU89,model 1a6m_rotate and resi 89
select 1a6mHIS93,model 1a6m_rotate and resi 93
show sticks, 1a6mLEU89 1a6mHIS93
select 1dlwLEU64,model 1dlw and resi 64
select 1dlwHIS68,model 1dlw and resi 68
show sticks, 1dlwLEU64 1dlwHIS68
sele resn HOH
hide (sele)
load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLEU89,model 1a6m_rotate and resi 89
select 1a6mHIS93,model 1a6m_rotate and resi 93
show sticks, 1a6mLEU89 1a6mHIS93
select 1dlwLEU64,model 1dlw and resi 64
select 1dlwHIS68,model 1dlw and resi 68
show sticks, 1dlwLEU64 1dlwHIS68
sele resn HOH
hide (sele)
set_color 166_0_88, [166,0,88]
select 1a6m758,model 1a6m_rotate and id 758
select 1a6m788,model 1a6m_rotate and id 788
distance 1a6m758-1a6m788, 1a6m758, 1a6m788
color 166_0_88, 1a6m758-1a6m788
select 1dlw466,model 1dlw and id 466
select 1dlw496,model 1dlw and id 496
distance 1dlw466-1dlw496, 1dlw466, 1dlw496
color 166_0_88, 1dlw466-1dlw496
set_color 150_0_104, [150,0,104]
select 1a6m758,model 1a6m_rotate and id 758
select 1a6m794,model 1a6m_rotate and id 794
distance 1a6m758-1a6m794, 1a6m758, 1a6m794
color 150_0_104, 1a6m758-1a6m794
select 1dlw466,model 1dlw and id 466
select 1dlw502,model 1dlw and id 502
distance 1dlw466-1dlw502, 1dlw466, 1dlw502
color 150_0_104, 1dlw466-1dlw502
