import requests
import json
import time
import csv


workdir = './'


CATEGORY_IT_ALL = [
  10,
  342,
  383,
  366,
  390,
  349,
  370,
  351,
  393,
  352,
  386,
  361,
  341,
  388,
  343,
  371,
  385,
  350,
  355,
  384,
  338,
  364,
  381,
  340,
  391,
  347,
  382,
  359,
  344,
  336,
  369,
  354,
  348,
  353,
  345,
  394,
  387,
  365,
  396,
  368,
  362,
  363,
  392,
  1083,
  1084,
  1088,
  358,
  1062,
  1056,
  1081,
  1082,
  1061,
  1054,
  1055,
  1063,
  1064,
  1065,
  1066,
  1070,
  1069,
  1071,
  1072,
  1073,
  1074,
  1068,
  1067,
  1079,
  1080,
  1060,
  1057,
  1058,
  1059,
  1078,
  1077,
  1075,
  1076
]


def validate(item):
    item = str(item)
    item = item.replace(',', '.')
    return item


def get_page(i, category):
    cookies = 'lang=ru-RU; s3ps=612971c8-982b-4196-8a86-485a0335249d-7793991; hrVacanciesSortListState=date; hrVacanciesCommonFilterSet={"region":["52","5200000100000"],"category":[10,342,383,366,390]}; did=d6480d01-cc14-4f26-9b0d-8a36ea17c53f; CpsUserId=566357fe-9ae6-4bfa-bee0-8bdbac42cc1d; s3sid-online-daab=0076ed47-011274b7-00ac-8e695fe3ae3b44cb; s3su=0076ed47-011274b7; s3tok-daab=__Dkhga8fmSLkRcrPLbfHyJir5jOobDCqvOTivWSBz5MA6ZY99SRqbigHACuKazXIKmaijYYzHF8mMT8i5HckBIj9VPosaUnOSCVKC0OPugkiweQjNk5d8H0; sid=0076ed47-011274b7-00ac-8e695fe3ae3b44cb; tz=-180; hrVacanciesCommonFilterState={"region":["52"],"category":[10,342,383,366,390,349,370,351,393,352,386,361,341,388,343,371,385,350,355,384,338,364,381,340,391,347,382,359,344,336,369,354,348,353,345,394,387,365,396,368,362,363,392,1083,1084,1088,358,1062,1056,1081,1082,1061,1054,1055,1063,1064,1065,1066,1070,1069,1071,1072,1073,1074,1068,1067,1079,1080,1060,1057,1058,1059,1078,1077,1075,1076],"is_active":false}; s3ds=1920|1080|1880|391|1920|1040'
    api_url = "https://online.sbis.ru/hr/service/?x_version=20.7104-76"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "authority": "online.sbis.ru",
        "method": "POST",
        "path": "/hr/service/?x_version=20.7104-76",
        "scheme": "https",
        "accept": "application/json, text/javascript, */*; q=0.01",

        "accept-language": "ru-RU;q=0.8,en-US;q=0.5,en;q=0.3",
        "content-length": "1029",
        "content-type": "application/json; charset=UTF-8",
        "cookie": cookies,
        "origin": "https://online.sbis.ru",
        "referer": "https://online.sbis.ru/hr.html?region_left=hr",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-calledmethod": "hr.GetVacancyList",
        "x-originalmethodname": "aHIuR2V0VmFjYW5jeUxpc3Q=",
        "x-requested-with": "XMLHttpRequest",
        "x-requestuuid": "4803b614-c6d7-1f49-71c7-26a9df226bc3",
        "x-uniq-id": "a3eaecb4-f86b-e8a3-e1f7-0d50d2d0ef82"
    }
    data_count = 20 # кол-во вакансий в одном запросе

    region = [[region_number]]

    json_r = {"jsonrpc": "2.0", "protocol": 6,
              "method": "hr.GetVacancyList",
              "params": {"Фильтр": {"d": [{"d": [
                  {"d": category, "s": [{"t": {"n": "Массив", "t": "Число целое"}, "n": "value"}], "_type": "record",
                   "f": 2},
                  {"d": region, "s": [{"t": {"n": "Массив", "t": "Строка"}, "n": "value"}], "_type": "record",
                   "f": 3}], "s": [{"t": "Запись", "n": "category"}, {"t": "Запись", "n": "region"}], "_type": "record",
                  "f": 1},
                  False, None, None],
                  "s": [{"t": "Запись", "n": "dict_filters"}, {"t": "Логическое", "n": "is_active"},
                        {"t": "Строка", "n": "salary_from"}, {"t": "Строка", "n": "salary_to"}], "_type": "record",
                  "f": 0},
                  "Сортировка": {"d": [[False, "relevance", True], [False, "updated_at", True]],
                                 "s": [{"t": "Логическое", "n": "l"}, {"t": "Строка", "n": "n"},
                                       {"t": "Логическое", "n": "o"}], "_type": "recordset", "f": 0},
                  "Навигация": {"d": [True, data_count, i],
                                "s": [{"t": "Логическое", "n": "ЕстьЕще"}, {"t": "Число целое", "n": "РазмерСтраницы"},
                                      {"t": "Число целое", "n": "Страница"}], "_type": "record", "f": 0},
                  "ДопПоля": []},
              "id": 1
              }

    r = requests.post(api_url, headers=headers, json=json_r, )
    # r.encoding = 'utf-8'


    json_data = json.loads(r.text)
    if 'result' not in json_data:
        return 0, 0
    if len(json_data['result']['d']) < 20:
        return 0, 0
    if not 'result' in json_data:
        return 3000, 3000
    print(json_data['result']['d'][1][28].split('-')[0])
    start = json_data['result']['d'][1][28].split('-')[0]
    end = json_data['result']['d'][-1][28].split('-')[0]
    return start, end


if __name__ == '__main__':
    regions = {
        'orel': '57', 'rysan': '62', 'smolensk': '67', 'tambov': '68'
    }
    for name, id in regions.items():
        region_number = id#input('Type the number of region from SBIS: ')
        region_name = name#input('Type the name of region: ')
        categories = CATEGORY_IT_ALL
        i = 0
        year2020 = 0
        year2019 = 0
        flag = False
        while True:
            try:
                start, end = get_page(i, [CATEGORY_IT_ALL])
            except:
                time.sleep(3)
                start, end = get_page(i, [CATEGORY_IT_ALL])
            finally:
                time.sleep(10)
                start, end = get_page(i, [CATEGORY_IT_ALL])
            if start == 0 and end == 0:
                if year2020 < 500:
                    year2020 = (i - year2020) * 20
                if year2019 > 0:
                    year2019 = (i - year2019) * 20
                break
            i += 1
            if int(start) < 2021 and year2020 == 0:
                print(f'Start: {i}')
                year2020 = i
            if int(start) < 2020 and flag == False:
                print(f'End 2020: {i}')
                year2020 = (i - year2020) * 20
                year2019 = i
                flag = True
            if int(end) < 2019:
                print(f'End: {i}')
                year2019 = (i - year2019) * 20
                break
            time.sleep(2)
            if i > 1000:
                break
        with open(f'{region_name}.json', 'w') as fw:
            fw.write(json.dumps({'2020': year2020, '2019': year2019, 'Sum': year2020+year2019}))
        time.sleep(90)