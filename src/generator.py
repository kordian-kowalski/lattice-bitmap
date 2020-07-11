from PIL import Image


def generate(width, height, wallsize, gapsize, border):
    total_size = wallsize + gapsize

    h_offset = (width % total_size) / 2 + 1
    v_offset = (height % total_size) / 2 + 1

    im = Image.new('1', (width, height), color=0)
    px = im.load()

    for x in range(width):
        for y in range(height):
            px[x, y] = x < border \
                       or y < border \
                       or x >= width - border \
                       or y >= height - border \
                       or ((x + h_offset) % total_size < wallsize) \
                       or ((y + v_offset) % total_size < wallsize)

    return im
