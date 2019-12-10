load ../../Data/1a6mx1dlw_align/1a6m_rotate.pdb
load ../../Data/1dlw.pdb
hide all
select 1a6mLEU29,model 1a6m_rotate and resi 29
select 1a6mPHE33,model 1a6m_rotate and resi 33
show sticks, 1a6mLEU29 1a6mPHE33
select 1dlwTYR20,model 1dlw and resi 20
select 1dlwGLN24,model 1dlw and resi 24
show sticks, 1dlwTYR20 1dlwGLN24
sele resn HOH
hide (sele)
set_color 76_0_178, [76,0,178]
select 1a6m237,model 1a6m_rotate and id 237
select 1a6m276,model 1a6m_rotate and id 276
distance 1a6m237-1a6m276, 1a6m237, 1a6m276
color 76_0_178, 1a6m237-1a6m276
select 1dlw142,model 1dlw and id 142
select 1dlw172,model 1dlw and id 172
distance 1dlw142-1dlw172, 1dlw142, 1dlw172
color 76_0_178, 1dlw142-1dlw172
