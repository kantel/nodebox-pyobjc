print "The Pictures folder with paths:"

myimages = filelist( "/Library/Desktop Pictures")

# for the choice later.
myimages = list(myimages)

for f in myimages:
    print f

# display a random image
image(choice(myimages), 30,200)