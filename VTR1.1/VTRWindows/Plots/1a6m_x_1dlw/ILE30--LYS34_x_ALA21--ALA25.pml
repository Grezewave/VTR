load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mILE30,model 1a6m_rotate and resi 30
select 1a6mLYS34,model 1a6m_rotate and resi 34
show sticks, 1a6mILE30 1a6mLYS34
select 1dlwALA21,model 1dlw and resi 21
select 1dlwALA25,model 1dlw and resi 25
show sticks, 1dlwALA21 1dlwALA25
sele resn HOH
hide (sele)
set_color 92_0_162, [92,0,162]
select 1a6m245,model 1a6m_rotate and id 245
select 1a6m287,model 1a6m_rotate and id 287
distance 1a6m245-1a6m287, 1a6m245, 1a6m287
color 92_0_162, 1a6m245-1a6m287
select 1dlw154,model 1dlw and id 154
select 1dlw181,model 1dlw and id 181
distance 1dlw154-1dlw181, 1dlw154, 1dlw181
color 92_0_162, 1dlw154-1dlw181
