import numpy as np
from PIL import Image

originalImg=np.array(Image.open("cc.jpg").convert('L'))
originalImg=originalImg.astype('float')

depth=10
grad=np.gradient(originalImg)
grad_x,grad_y=grad
grad_x=grad_x*depth/100
grad_y=grad_y*depth/100
a=np.sqrt(grad_x**2+grad_y**2+1.)
uni_x=grad_x/a
uni_y=grad_y/a
uni_z=1./a

# 考虑光源的影响
vec_el=np.pi/2.2 #光源的俯视角度 弧度
vec_az=np.pi/4.#光源的方位角度，弧度
dx=np.cos(vec_el)*np.cos(vec_az)
dy=np.cos(vec_el)*np.sin(vec_az)
dz=np.sin(vec_el)

b=255*(dx*uni_x+dy*uni_y+dz*uni_z)
b=b.clip(0,255)

im=Image.fromarray(b.astype('uint8'))
im.show()
