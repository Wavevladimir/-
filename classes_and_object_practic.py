class Image:
    def __init__(self, resolution, title, extention):
        self.resolution = resolution
        self.title = title
        self.extention = extention
    def resize(self, new_resolution):
        self.resolution = new_resolution
    
    def __str__(self):
        return f"{self.title}.{self.extention}"
first_img = Image('1920x1080', "My dog", 'jpg')

print(first_img.resolution)
print(first_img.title)
print(first_img.extention)

first_img.resize('4000x3000')

print(first_img.resolution)

second_img = Image('8000x5000', "My cat", 'png')
print(first_img)