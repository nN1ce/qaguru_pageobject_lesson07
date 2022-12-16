from demoqa_tests.model import app
from demoqa_tests.model.pages import registration_form

from tests.test_data.users import student

def test_submit_student_registration_form():

    app.registration_form.given_opened()

    # WHEN

    registration_form.set_field('#firstName', student.name)
    registration_form.set_field('#lastName', student.last_name)
    registration_form.set_field('#userEmail', student.email)

    registration_form.set_gender(student.gender.value)

    '''
    # OR
    gender_male = browser.element('[for=gender-radio-1]')
    gender_male.click()
    # OR
    gender_male = browser.element('[for=gender-radio-1]')
    gender_male.click()
    # OR
    browser.element('[id^=gender-radio][value=Male]').perform(command.js.click)
    browser.element('[id^=gender-radio][value=Male]').element(
        './following-sibling::*'
    ).click()
    # OR better:
    browser.element('[id^=gender-radio][value=Male]').element('..').click()
    # OR
    browser.all('[id^=gender-radio]').element_by(have.value('Male')).element('..').click()
    browser.all('[id^=gender-radio]').by(have.value('Male')).first.element('..').click()
    '''
    registration_form.set_field('#userNumber', student.user_number)

    registration_form.set_birth_date(student.birth_month, student.birth_year, student.birth_day)
    '''
    # OR something like
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('28 Mar 1995').press_enter()
    '''

    registration_form.add_subjects(student.subjects)

    registration_form.set_hobbies(student.hobbies)

    registration_form.send_file(student.picture_file)

    registration_form.set_field('#currentAddress', student.current_address)

    registration_form.scroll_to_bottom()

    registration_form.set_state(student.state)
    registration_form.set_city(student.city)

    registration_form.submit()

    # THEN

    registration_form.should_have_submitted(
        [
            ('Student Name', f'{student.name} {student.last_name}'),
            ('Student Email', student.email),
            ('Gender', student.gender.value),
        ],
    )
