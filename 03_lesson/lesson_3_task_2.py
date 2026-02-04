from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 14", "+79161234567"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79263457890"))
catalog.append(Smartphone("Xiaomi", "Mi 13", "+79374561234"))
catalog.append(Smartphone("Google", "Pixel 7", "+79485672345"))
catalog.append(Smartphone("Huawei", "P60 Pro", "+79596783456"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
