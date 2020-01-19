def cat_dog_years(human_years):
    first_year = 15
    second_year = first_year + 9
    if human_years == 1:
        cat_years = dog_years = first_year
    if human_years == 2:
        cat_years = dog_years =  second_year
    if human_years > 2:
        cat_years = (human_years -2) *4 + second_year
        dog_years = (human_years-2) *5 + second_year
    return [human_years, cat_years, dog_years]