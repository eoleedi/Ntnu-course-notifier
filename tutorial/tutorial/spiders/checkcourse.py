import os,requests
import time, json, random



def course_query(courseQuery):
    rs = requests.session()
    url = "http://courseap.itc.ntnu.edu.tw/acadmOpenCourse/CofopdlCtrl"
    return rs.get(url, params=courseQuery)
    

if __name__=="__main__":
    courseQuery = {
        "acadmYear": 109,
        "acadmTerm": 2,
        "chn":'',
        "engTeach": "N",
        "moocs": "N",
        "remoteCourse": "N",
        "digital": "N",
        "adsl": "N",
        "deptCode": "GU",
        "zuDept":'',
        "classCode":'',
        "kind":'',
        "generalCore":'',
        "teacher":'',
        "serial_number":'',
        "course_code":'',
        "language": "chinese",
        "action": "showGrid",
        "start": 0,
        "limit": 99999,
        "page": 1,
    }
    parsed = json.loads(course_query(courseQuery).text)
    print(json.dumps(parsed, indent=4, ensure_ascii=False))