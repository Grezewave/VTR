load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mILE75,model 1a6m_rotate and resi 75
select 1a6mLEU86,model 1a6m_rotate and resi 86
show sticks, 1a6mILE75 1a6mLEU86
select 1dlwPHE48,model 1dlw and resi 48
select 1dlwVAL109,model 1dlw and resi 109
show sticks, 1dlwPHE48 1dlwVAL109
sele resn HOH
hide (sele)
set_color 55_0_199, [55,0,199]
select 1a6m648,model 1a6m_rotate and id 648
select 1a6m738,model 1a6m_rotate and id 738
distance 1a6m648-1a6m738, 1a6m648, 1a6m738
color 55_0_199, 1a6m648-1a6m738
select 1dlw358,model 1dlw and id 358
select 1dlw785,model 1dlw and id 785
distance 1dlw358-1dlw785, 1dlw358, 1dlw785
color 55_0_199, 1dlw358-1dlw785
