def prettify_course_name(course_name):
    if not course_name:
        return "Нет информации"
    else:
        return course_name


def prettify_course_weeks_count(course_week_count):
    if not course_week_count:
        return "Нет информации"
    if course_week_count >= 5:
        return "{} недель".format(course_week_count)
    elif course_week_count == 1:
        return "1 неделя"
    else:
        return "{} недели".format(course_week_count)


def prettify_course_languages(course_language):
    if not course_language:
        return "Нет информации"
    if course_language['Subtitles']:
        return "{}, Субтитры: {}".format(course_language['Languages'], course_language['Subtitles'])
    else:
        return course_language['Languages']


def prettify_course_rating(course_rating):
    if not course_rating:
        return "Нет информации"
    else:
        return "{} из 5".format(course_rating)
