from os import *
import gzip
import pickle
# print(getcwd())
chdir("""D:/Downloads""")
# ob=open('D:/Downloads/AI/train-images.idx3-ubyte',0)
# 
# print(ob)


# with gzip.open('train-images-idx3-ubyte.gz', 'rb') as f:
#     train_set, valid_set, test_set = pickle.load(f)


# pkl() (
#   python -c 'import pickle,sys;d=pickle.load(open(sys.argv[1],"rb"));print(d)' "$1"
# )
# pkl my.pkl
from mnist import MNIST
# mndata.gz = True
mndata = MNIST('D:\Downloads\AI')
images, labels = mndata.load_training()

import matplotlib.cm as cm
import matplotlib.pyplot as plt


plt.imshow(images[0], cmap=cm.Greys_r)
plt.show()