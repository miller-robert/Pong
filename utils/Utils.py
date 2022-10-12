import os,pygame

def load_image(img):
    #path = os.path.join("../sprites",img)
    path = img
    try:
        image = pygame.image.load(path)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except Exception as e:
        print(f"Failed to load in the image {img}")
        print(e)
        exit()
    return image, image.get_rect()