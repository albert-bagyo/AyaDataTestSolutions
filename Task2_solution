import os
images = os.listdir('./mask-images/masks')
try:
    os.mkdir('human')
    os.mkdir('background')
except:
    print("Couldn't create folder")

for image in images:
    if image.endswith('00000.png'):
        os.rename(f'./mask-images/masks/{image}',f'./background/{image}')
    else:
        os.rename(f'./mask-images/masks/{image}',f'./human/{image}')
