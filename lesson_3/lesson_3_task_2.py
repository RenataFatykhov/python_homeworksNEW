from smartphone import Smartphone

catalog = []

catalog.append(Smartphone(brand="Apple", model="iPhone 15", phone_number="+79123456789"))
catalog.append(Smartphone(brand="Samsung", model="Galaxy S21", phone_number="+79234567890"))
catalog.append(Smartphone(brand="Google", model="Pixel 6", phone_number="+79345678901"))
catalog.append(Smartphone(brand="OnePlus", model="9 Pro", phone_number="+79456789012"))
catalog.append(Smartphone(brand="Xiaomi", model="Mi 11", phone_number="+79567890123"))

# Печатаем весь каталог в формате <марка> - <модель>. <номер телефона>
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")