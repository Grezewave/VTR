load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mILE107,model 1a6m_rotate and resi 107
select 1a6mALA110,model 1a6m_rotate and resi 110
show sticks, 1a6mILE107 1a6mALA110
select 1dlwVAL81,model 1dlw and resi 81
select 1dlwHIS84,model 1dlw and resi 84
show sticks, 1dlwVAL81 1dlwHIS84
sele resn HOH
hide (sele)
set_color 35_0_219, [35,0,219]
select 1a6m918,model 1a6m_rotate and id 918
select 1a6m943,model 1a6m_rotate and id 943
distance 1a6m918-1a6m943, 1a6m918, 1a6m943
color 35_0_219, 1a6m918-1a6m943
select 1dlw594,model 1dlw and id 594
select 1dlw610,model 1dlw and id 610
distance 1dlw594-1dlw610, 1dlw594, 1dlw610
color 35_0_219, 1dlw594-1dlw610
