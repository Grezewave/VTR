load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mPRO88,model 1a6m_rotate and resi 88
select 1a6mSER92,model 1a6m_rotate and resi 92
show sticks, 1a6mPRO88 1a6mSER92
select 1dlwASN63,model 1dlw and resi 63
select 1dlwVAL67,model 1dlw and resi 67
show sticks, 1dlwASN63 1dlwVAL67
sele resn HOH
hide (sele)
set_color 58_0_196, [58,0,196]
select 1a6m751,model 1a6m_rotate and id 751
select 1a6m782,model 1a6m_rotate and id 782
distance 1a6m751-1a6m782, 1a6m751, 1a6m782
color 58_0_196, 1a6m751-1a6m782
select 1dlw458,model 1dlw and id 458
select 1dlw489,model 1dlw and id 489
distance 1dlw458-1dlw489, 1dlw458, 1dlw489
color 58_0_196, 1dlw458-1dlw489
