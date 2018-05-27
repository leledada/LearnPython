from PIL import Image


# fill_image 方法把原图转换成正方形，方便计算切割九宫格
def fill_image(image):
    width, height = image.size
    new_len = max(width, height)

    # 将新图片是正方形，长度为原宽高中最长的，color="white"代表底色是白色，发朋友圈的话，建议white
    new_image = Image.new(image.mode, (new_len, new_len), color='white')

    # 根据两种不同的情况，将原图片放入新建的空白图片中部
    if width > height:
        new_image.paste(image, (0, int((new_len - height) / 2)))
    else:
        new_image.paste(image, (int((new_len - width) / 2), 0))
    return new_image


def cut_image(image):
    width, height = image.size
    print('原图的尺寸', width, height)
    item_width = int(width / 3)
    item_height = int(height / 3)

    # 保存每一个小切图的区域
    box_list = []

    for i in range(3):
        for j in range(3):
            # 切图区域是矩形，位置由对角线的两个点(左上和右下)确定
            # 去掉fill_image 精确切分成9块，但是朋友圈九宫格缩略图都是正方形，整体看起来就不完整，不推荐这种方法。
            # box = (j * item_width, i * item_height, (j + 1) * item_width, (i + 1) * item_height)
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)

    # print('box_list', box_list)

    image_list = [image.crop(box) for box in box_list]
    return image_list


def save_images(image_list, out_dir):
    for (index, image) in enumerate(image_list, start=1):
        # 用enumerate制造序列号，方便按序号保存图片
        image.save("{out_dir}_{index}.png".format(out_dir=out_dir, index=index), "PNG")


def to9imgs(file_path, out_dir='./'):
    image = Image.open(file_path)
    image1 = fill_image(image)
    image_list = cut_image(image1)
    print('image_list--->', image_list)
    pic_name = file_path.split('.')[0]
    out_dir = out_dir+ r'/'+pic_name
    save_images(image_list, out_dir)


if __name__ == '__main__':
    # to9imgs('IMG_0192.jpg')
    to9imgs('happy.png')
