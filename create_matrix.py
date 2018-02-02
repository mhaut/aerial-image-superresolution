import numpy as np
from PIL import Image
from os import listdir
from os.path import isdir, join
import matplotlib.pyplot as plt

#directories = [f for f in listdir("images") if isdir(join("images", f))]
directories = [['harbor', 'intersection', 'parking', 'road'], ['agricultural2', 'agricultural', 'airplane', 'residential'], ['circular_farmland', 'baseball', 'bridge', 'industry']]


mosaic = np.zeros((12,256,256,3), dtype=np.uint8)
i=0
for rowimage in directories:
	for dirim in rowimage:
		for image in listdir("images" + "/" + dirim):
			imagepath = "images" + "/" + dirim + "/" + image
			if "hr" in imagepath:
				try:
					mosaic[i,:,:,:] = np.array(Image.open(imagepath).convert('RGB'))
				except: #images of 96x96
					mosaic[i,:,:,:] = np.array(Image.open(imagepath).convert('RGB').resize((256,256), Image.ANTIALIAS))
				i += 1

(np.hstack((mosaic[8,:,:,:], mosaic[9,:,:,:], mosaic[10,:,:,:], mosaic[11,:,:,:])))
#exit()

final_mosaic = np.vstack((
						np.hstack((mosaic[0,:,:,:], mosaic[1,:,:,:],  mosaic[2,:,:,:],  mosaic[3,:,:,:])), \
						np.hstack((mosaic[4,:,:,:], mosaic[5,:,:,:],  mosaic[6,:,:,:],  mosaic[7,:,:,:])), \
						np.hstack((mosaic[8,:,:,:], mosaic[9,:,:,:], mosaic[10,:,:,:], mosaic[11,:,:,:]))
					))


fig = plt.imshow(final_mosaic)
plt.axis('off')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.savefig("mosaic.png", bbox_inches='tight', pad_inches = 0)
plt.show()
