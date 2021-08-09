def designerPdfViewer(h, word):
    # Write your code here
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
    l2 = []


    for i in range(0, len(word)):
        l2.append(l.index(word[i]))
    print(l2)
    l3=[h[j] for j in l2]
    max1=max(l3)
    return max1*len(word)

h=[1 ,3 ,1 ,3 ,1 ,4 ,1 ,3 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5, 5, 5 ,7]
w="zaba"
print(designerPdfViewer(h,w))