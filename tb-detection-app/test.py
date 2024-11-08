import os
def get_image_options(path):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    total_path = os.path.join(script_directory, path)

    image_extensions = ['jpg', 'jpeg', 'png']
    image_files = [f for f in os.listdir(total_path) if f.split('.')[-1].lower() in image_extensions]
    return image_files

x= get_image_options('examples')
print(x)