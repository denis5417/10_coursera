from parse_args import parse_args
from fetch_webpage import fetch_webpage
import xlsx_output as xout
import courses_data_get as cdg


if __name__ == '__main__':
    coursera_xml_feed_url = "https://www.coursera.org/sitemap~www~courses.xml"
    xout.output_courses_info_to_xlsx(parse_args().output,
                                     cdg.get_courses_list(fetch_webpage(coursera_xml_feed_url))[:parse_args().quantity])
