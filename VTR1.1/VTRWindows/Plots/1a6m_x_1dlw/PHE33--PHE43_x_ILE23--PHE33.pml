load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mPHE33,model 1a6m_rotate and resi 33
select 1a6mPHE43,model 1a6m_rotate and resi 43
show sticks, 1a6mPHE33 1a6mPHE43
select 1dlwILE23,model 1dlw and resi 23
select 1dlwPHE33,model 1dlw and resi 33
show sticks, 1dlwILE23 1dlwPHE33
sele resn HOH
hide (sele)
set_color 7_0_247, [7,0,247]
select 1a6m282,model 1a6m_rotate and id 282
select 1a6m374,model 1a6m_rotate and id 374
distance 1a6m282-1a6m374, 1a6m282, 1a6m374
color 7_0_247, 1a6m282-1a6m374
select 1dlw170,model 1dlw and id 170
select 1dlw242,model 1dlw and id 242
distance 1dlw170-1dlw242, 1dlw170, 1dlw242
color 7_0_247, 1dlw170-1dlw242
