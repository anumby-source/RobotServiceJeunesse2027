os.chdir('/Users/Gilles/Dropbox/Informatique/Anumby/RSJ2026/M5Stack UnitV')

fd = open('img_0019.dat', 'rb')
b = fd.read()
fd.close()

img=np.empty((320,240), dtype=np.uint8)


for n in range(len(b)):
    img[n%320,n//320]=b[n]

plt.xticks([])
plt.yticks([])
plt.imshow(img, cmap='gray')