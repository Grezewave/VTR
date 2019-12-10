load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mILE111,model 1a6m_rotate and resi 111
select 1a6mLEU115,model 1a6m_rotate and resi 115
show sticks, 1a6mILE111 1a6mLEU115
select 1dlwLEU85,model 1dlw and resi 85
select 1dlwLEU89,model 1dlw and resi 89
show sticks, 1dlwLEU85 1dlwLEU89
sele resn HOH
hide (sele)
set_color 46_0_208, [46,0,208]
select 1a6m951,model 1a6m_rotate and id 951
select 1a6m981,model 1a6m_rotate and id 981
distance 1a6m951-1a6m981, 1a6m951, 1a6m981
color 46_0_208, 1a6m951-1a6m981
select 1dlw623,model 1dlw and id 623
select 1dlw650,model 1dlw and id 650
distance 1dlw623-1dlw650, 1dlw623, 1dlw650
color 46_0_208, 1dlw623-1dlw650
