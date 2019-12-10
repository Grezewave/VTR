load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mILE28,model 1a6m_rotate and resi 28
select 1a6mLEU32,model 1a6m_rotate and resi 32
show sticks, 1a6mILE28 1a6mLEU32
select 1dlwPHE19,model 1dlw and resi 19
select 1dlwILE23,model 1dlw and resi 23
show sticks, 1dlwPHE19 1dlwILE23
sele resn HOH
hide (sele)
set_color 145_0_109, [145,0,109]
select 1a6m229,model 1a6m_rotate and id 229
select 1a6m268,model 1a6m_rotate and id 268
distance 1a6m229-1a6m268, 1a6m229, 1a6m268
color 145_0_109, 1a6m229-1a6m268
select 1dlw131,model 1dlw and id 131
select 1dlw164,model 1dlw and id 164
distance 1dlw131-1dlw164, 1dlw131, 1dlw164
color 145_0_109, 1dlw131-1dlw164
