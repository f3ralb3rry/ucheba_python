# TODO Найдите количество книг, которое можно разместить на дискете
disk_mb = 1.44
book_str = 100
stroki = 50
symb_stroki = 25
one_symb = 4
disk_byte = disk_mb * 1024 * 1024
book_size = book_str * stroki * symb_stroki * one_symb
num_book = disk_byte // book_size
print("Количество книг, помещающихся на дискету:", num_book)
