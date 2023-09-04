# input
human_age = float(input("Enter the human age: "))

#1 to 7 ratio for dog age
dog_age = human_age * 7

#Result
print(f"{human_age} human years is equal to {dog_age} dog years")

#Dog age in years
dog_age_years= int(human_age * 7)

#remaining months
remaining_months = (human_age * 7 - dog_age_years) * 12

#remaining days
remaining_days = int(remaining_months * 30.44)

#number of months
dog_age_months = remaining_months - (remaining_days / 30.44)

#result
if remaining_days ==0:
	print(f"An age {human_age} human should be {dog_age_years} years in dog's age.")
else:
	print(f"An age {human_age} human should be {dog_age_years} years, {int(dog_age_months)} months, and {remaining_days} days in dog's age.")

#cat to human ratio
cat_age = human_age / 9

#cat age result
cat_age_years = int(cat_age)

#remaining months for cat
remaining_months_cat = (cat_age - cat_age_years) *12

#remaining days for cat
remaining_days_cat = int(remaining_months_cat * 30.44)

if remaining_days_cat ==0:
	print(f"An age {human_age} human should be {cat_age_years} years in cat's age.")
else:
	print(f"An age {human_age} human should be {cat_age_years} years, {int(remaining_months_cat)} months, and {remaining_days_cat} days in cat's age.")

#horse age to human
horse_age = 3 * ((human_age **2) / 47 + 12)

#horse years
horse_age_years = int(horse_age)

#remaining months for horse
remaining_months_horse = (horse_age - horse_age_years) * 12

#remaining horse days
remaining_days_horse = int(remaining_months_horse * 30.44)

if remaining_days_horse == 0:
	print(f"An age {human_age} human should be {horse_age_years} in horse age.")
else:
	print(f"An age {human_age} human should be {horse_age_years} years, {int(remaining_months_horse)} months, and {remaining_days_horse} days in horse age.")
