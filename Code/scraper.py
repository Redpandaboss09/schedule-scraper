from playwright.sync_api import sync_playwright, Page
from configparser import ConfigParser

config = ConfigParser()
config.read('../configs/pdf_config.ini')

# A parent function that calls all the other functions and logs into the website
def login(page: Page, username: str = config['LOGIN']['username'], password: str = config['LOGIN']['password']):
    page.goto("https://stjohnsprep.myschoolapp.com/app/student#studentmyday/progress")
    page.goto("https://stjohnsprep.myschoolapp.com/app/student#login")
    page.get_by_label("Username or Email").click()
    page.get_by_label("Username or Email").fill(username)
    page.get_by_role("button", name="Next").click()
    page.get_by_placeholder("username@stjohnsprep.org").click()
    page.get_by_placeholder("username@stjohnsprep.org").fill(username)
    page.get_by_placeholder("username@stjohnsprep.org").press("Enter")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(password)
    page.get_by_placeholder("Password").press("Enter")
    page.get_by_role("button", name="No").click()
    page.get_by_role("link", name="Progress").click()

    return final_joining(page)

# Scrape the class number
def get_class_number(page: Page):
    page.wait_for_selector('#coursesContainer')

    # Get the course elements
    course_elements = page.query_selector_all('.row')

    # Extract class numbers
    class_numbers = []
    for course_element in course_elements:
        col_elements = course_element.query_selector_all('.col-md-3')

        if col_elements:
            class_number = col_elements[0].query_selector('h5').inner_text()
            class_number = class_number.split(' | ')[0]
            class_numbers.append(class_number)

    return delete_duplicates(class_numbers)

# Scrape the instructor names
def get_instructor_names(page: Page):
    page.wait_for_selector('#coursesContainer')

    # Get the course elements
    course_elements = page.query_selector_all('.row')

    # Extract instructor names
    instructor_names = []
    for course_element in course_elements:
        h4_element = course_element.query_selector('.group-owner-name')
        if h4_element:
            instructor_name = h4_element.inner_text()
            instructor_names.append(instructor_name)

    return delete_duplicates(instructor_names)

# Join the course names, instructor names, and class numbers
def join_elements(page: Page, course_names: dict(), instructor_names: list(), class_numbers: list()):
    joined_elements = {}

    for key in course_names.keys():
        joined_elements[key] = [course_names[key], instructor_names[int(key[4:])], class_numbers[int(key[4:])]]

    return joined_elements

# Scrape the unedited course names
def course_names(page: Page):
    page.wait_for_selector('#coursesContainer')

    # Get the course elements
    course_elements = page.query_selector_all('.row')

    # Extract course names
    course_names = []
    for course_element in course_elements:
        link_element = course_element.query_selector('a')
        if link_element:
            h3_element = link_element.query_selector('h3')
            if h3_element:
                course_name = h3_element.inner_text()
                course_names.append(course_name)

    return delete_values(course_names)

# The final course names that are fully edited
def final_course_names(page: Page):
    unedited_course_names = course_names(page)[0]
    courses = {}

    for course in unedited_course_names.values():
        key = course[course.find('(') + 1 : course.find(')')]

        courses[key] = [course.split(" - ")[0]]

    sorted_courses = dict(sorted(courses.items()))
    return sorted_courses

# Final joining of values
def final_joining(page: Page):
    joined = join_elements(page, course_names(page)[0], get_instructor_names(page), get_class_number(page))
    courses_final = final_course_names(page)

    for value in joined.values():
        key = value[0][value[0].find('(') + 1 : value[0].find(')')]

        if key in courses_final.keys():
            courses_final[key].append(value[1])
            courses_final[key].append(value[2])

    return courses_final


# Delete values that are not classes (Ambigous values)
def delete_values(group: list()):
    removed = {}
    filtered = {}

    group = delete_duplicates(group)

    # Filter the keys based on assumption that classes have (LETTER)
    i = 0
    for value in group:
        start_index = value.find('(')
        end_index = value.find(')')

        if start_index != -1 and end_index != -1:
            substring = value[start_index + 1: end_index]

            if len(substring) == 1 and substring.isalpha():
                filtered['temp' + str(i)] = value
            else:
                removed['temp' + str(i)] = value
        else:
            removed['temp' + str(i)] = value

        i += 1

    return filtered, removed

# Delete duplicate values
def delete_duplicates(group: list()):
    new_group = []

    for value in group:
        if value not in new_group:
            new_group.append(value)

    return new_group

def caller():
    needed_values = None

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        needed_values = login(page)

    return needed_values