car_brands = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet."
print(car_brands.split(","))
print(f"There are {len(car_brands.split(","))} car brands in this list")
car_brands_reverse = sorted(car_brands.split(","), reverse=True)
print(car_brands_reverse)
car_brands_list = [brand.strip(" .") for brand in car_brands.split(",")]
print(car_brands_list)
brands_with_o = [brand for brand in car_brands_list if "o" in brand.lower()]
print(f"There are {len(brands_with_o)} car brands with the letter 'o'.")
brands_without_i = [brand for brand in car_brands_list if "i" not in brand.lower()]
print(f"There are {len(brands_without_i)} car brands without the letter 'i'.")

# Bonus 1