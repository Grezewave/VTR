load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLEU72,model 1a6m_rotate and resi 72
select 1a6mLEU76,model 1a6m_rotate and resi 76
show sticks, 1a6mLEU72 1a6mLEU76
select 1dlwPHE48,model 1dlw and resi 48
select 1dlwALA52,model 1dlw and resi 52
show sticks, 1dlwPHE48 1dlwALA52
sele resn HOH
hide (sele)
set_color 7_0_247, [7,0,247]
select 1a6m627,model 1a6m_rotate and id 627
select 1a6m649,model 1a6m_rotate and id 649
distance 1a6m627-1a6m649, 1a6m627, 1a6m649
color 7_0_247, 1a6m627-1a6m649
select 1dlw351,model 1dlw and id 351
select 1dlw378,model 1dlw and id 378
distance 1dlw351-1dlw378, 1dlw351, 1dlw378
color 7_0_247, 1dlw351-1dlw378
