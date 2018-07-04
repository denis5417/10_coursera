from bs4 import BeautifulSoup, NavigableString


def get_courses_list(xml):
    xml_soup = BeautifulSoup(xml, features="lxml-xml")
    return [course.contents[0] for course in xml_soup.find_all("loc")]


def agregate_course_info(html):
    html_soup = BeautifulSoup(html, features="lxml")
    return {
        'Name': get_course_name(html_soup),
        'Languages': get_course_languages(html_soup),
        'Weeks': get_course_weeks_count(html_soup),
        'Rating': get_course_average_rating(html_soup)
    }


def get_course_name(html_soup):
    course_name = html_soup.find("h1")
    if not course_name:
        return None
    return course_name.contents[0].encode('raw-unicode-escape').decode('utf-8-sig')


def get_course_languages(html_soup):
    lang = html_soup.find('div', attrs={'class': 'rc-Language'})
    lang_no_subtitles_len = 3
    if not lang:
        return None
    if len(lang) == lang_no_subtitles_len:  # course has no subtitles
        return {"Languages": lang.contents[1], "Subtitles": None}
    else:  # course has got subtitles
        return {"Languages": lang.contents[1], "Subtitles": lang.contents[3].contents[3]}


def get_course_average_rating(html_soup):
    rating = html_soup.find('div', attrs={'class': 'ratings-text'})
    if not rating:
        return None
    if type(rating.contents[0]) == NavigableString:  # first type of rating string like "4.9 stars"
        return rating.contents[0][:3]  # get only number from string
    else:  # other type of rating string like "Rated 4.9 out of 5"
        return rating.contents[0].contents[1][6:9]  # get only number from string


def get_course_weeks_count(html_soup):
    weeks = html_soup.find('div', attrs={'class': 'rc-WeekView'})
    if not weeks:
        return None
    return len(weeks)
