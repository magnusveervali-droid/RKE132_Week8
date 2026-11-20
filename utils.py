def clean_my_list(some_list):

        cleaned_list = []

        for element in some_list:
            cleaned_element = element.strip()
            cleaned_list.append(cleaned_element)

        return cleaned_list