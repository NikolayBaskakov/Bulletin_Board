from django.utils.text import slugify
def make_slug(string, model):
    trans_str = str(string).translate(str.maketrans("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                                                  "abvgdeejziyklmnoprstufhzcss_y_euaabvgdeejziyklmnoprstufhzcss_y_eua"))
    slug = slugify(trans_str)
    if model.objects.filter(slug=slug).exists():
        slug += '-1'
        add_num = 2
        while model.objects.filter(slug=slug).exists():
            slug = slug[:len(slug)-1] + str(add_num)
            add_num += 1
        return slug
    else:
        return slug
