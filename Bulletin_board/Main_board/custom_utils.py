from django.utils.text import slugify

def make_slug(string):
    res_str = str(string).translate(str.maketrans("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                                                  "abvgdeejziyklmnoprstufhzcss_y_euaabvgdeejziyklmnoprstufhzcss_y_eua"))
    return slugify(res_str)
