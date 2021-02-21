import scrapy

class CoursesSpider(scrapy.Spider):
    name = "courses"

    def start_requests(self):
        url = 'http://courseap.itc.ntnu.edu.tw/acadmOpenCourse/CofopdlCtrl'
        
        courseQuery = {
            "acadmYear": "109",
            "acadmTerm": "2",
            "chn":'',
            "engTeach": "N",
            "moocs": "N",
            "remoteCourse": "N",
            "digital": "N",
            "adsl": "N",
            "deptCode": "",
            "zuDept":'',
            "classCode":'',
            "kind":'',
            "generalCore":'',
            "teacher":'',
            "serial_number":'',
            "course_code":'',
            "language": "chinese",
            "action": "showGrid",
            "start": "0",
            "limit": "99999",
            "page": "1",
        }
        yield scrapy.FormRequest(url=url, method='GET', callback=self.parse, formdata=courseQuery)

    def parse(self, response):
        filename = f'courses_new.json'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')