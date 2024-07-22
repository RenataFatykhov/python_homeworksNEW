from address import Address
from mailing import Mailing

# Создаем адреса
to_address = Address("123456", "Москва", "Тверская", "10", "15")
from_address = Address("654321", "Санкт-Петербург", "Невский проспект", "20", "5")

# Создаем почтовое отправление
mailing = Mailing(to_address, from_address, 150.0, "ABC123456789")

# Печатаем информацию об отправлении
print(mailing)