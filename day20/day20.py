import sys
import numpy as np 

np.set_printoptions(threshold=sys.maxsize)

algo = open('input_algorithm.txt','r')
algo_list = np.array(['.#'.index(y) for x in algo for y in x.strip('\n')])

image = open('input_image.txt','r')
image_list = np.array([[0 if y == '.' else 1 for y in x.strip('\n')] for x in image])

def new_pixel(x, y, image):

    bin_str = (str(int(image[y-1][x-1])) + str(int(image[y-1][x])) + str(int(image[y-1][x+1])) + 
               str(int(image[y][x-1]))   + str(int(image[y][x]))   + str(int(image[y][x+1]))   + 
               str(int(image[y+1][x-1])) + str(int(image[y+1][x])) + str(int(image[y+1][x+1]))  )
    idx = int(bin_str, 2)
    
    return algo_list[idx]

def enhance(image_list, times):
    
    padded_image = np.pad(image_list, times + 2, mode = 'constant')
    height, width = padded_image.shape

    for t in range(int(times/2) - 1 , -1 , -1):

        image1 = np.zeros((width,height))
        image2 = np.zeros((width,height))

        for y in range((2*t + 1), height - (2*t + 1)):
            for x in range((2*t + 1) , width - (2*t + 1)):
                if new_pixel(x, y, padded_image):
                    image1[y][x] = 1

        for y in range((2*t + 2), height - (2*t + 2)):
            for x in range((2*t + 2) , width - (2*t + 2)):
                if new_pixel(x, y, image1):
                    image2[y][x] = 1

        padded_image = image2.copy()

    return sum([sum(x) for x in padded_image.tolist()])


# Part 1
print(enhance(image_list, 2))

# Part 2
print(enhance(image_list, 50))