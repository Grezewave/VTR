load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mHIS36,model 1a6m_rotate and resi 36
select 1a6mTHR39,model 1a6m_rotate and resi 39
show sticks, 1a6mHIS36 1a6mTHR39
select 1dlwASP26,model 1dlw and resi 26
select 1dlwVAL29,model 1dlw and resi 29
show sticks, 1dlwASP26 1dlwVAL29
sele resn HOH
hide (sele)
set_color 53_0_201, [53,0,201]
select 1a6m305,model 1a6m_rotate and id 305
select 1a6m328,model 1a6m_rotate and id 328
distance 1a6m305-1a6m328, 1a6m305, 1a6m328
color 53_0_201, 1a6m305-1a6m328
select 1dlw189,model 1dlw and id 189
select 1dlw206,model 1dlw and id 206
distance 1dlw189-1dlw206, 1dlw189, 1dlw206
color 53_0_201, 1dlw189-1dlw206
