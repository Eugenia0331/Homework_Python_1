from address import Address
from mailing import Mailing

from_address = Address("101000", "Москва", "Тверская", "1", "10")
to_address = Address("190000", "Санкт-Петербург", "Невский проспект", "25", "45")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350.5,
    track="RU123456789"
)

print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)