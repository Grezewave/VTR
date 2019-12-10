load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLEU104,model 1a6m_rotate and resi 104
select 1a6mSER108,model 1a6m_rotate and resi 108
show sticks, 1a6mLEU104 1a6mSER108
select 1dlwPHE78,model 1dlw and resi 78
select 1dlwILE82,model 1dlw and resi 82
show sticks, 1dlwPHE78 1dlwILE82
sele resn HOH
hide (sele)
set_color 7_0_247, [7,0,247]
select 1a6m890,model 1a6m_rotate and id 890
select 1a6m928,model 1a6m_rotate and id 928
distance 1a6m890-1a6m928, 1a6m890, 1a6m928
color 7_0_247, 1a6m890-1a6m928
select 1dlw575,model 1dlw and id 575
select 1dlw605,model 1dlw and id 605
distance 1dlw575-1dlw605, 1dlw575, 1dlw605
color 7_0_247, 1dlw575-1dlw605
