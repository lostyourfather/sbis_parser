import requests
import json


companies = {}
region = '68'
cnt = 0
while True:
    req_str = '{"jsonrpc":"2.0","protocol":6,"method":"Contractor.ListCompany","params":{"Фильтр":{"d":[["-62","-63"],[null],true,true,["' + region +'"],[1]],"s":[{"t":{"n":"Массив","t":"Строка"},"n":"Category"},{"t":{"n":"Массив","t":"Строка"},"n":"KindMan"},{"t":"Логическое","n":"MatchedFields"},{"t":"Логическое","n":"Misspelling"},{"t":{"n":"Массив","t":"Строка"},"n":"Region"},{"t":{"n":"Массив","t":"Число целое"},"n":"State"}],"_type":"record","f":0},"Сортировка":{"d":[[false,"Выручка",true]],"s":[{"t":"Логическое","n":"l"},{"t":"Строка","n":"n"},{"t":"Логическое","n":"o"}],"_type":"recordset","f":0},"Навигация":{"d":[true,100,' + str(
        cnt) + '],"s":[{"t":"Логическое","n":"ЕстьЕще"},{"t":"Число целое","n":"РазмерСтраницы"},{"t":"Число целое","n":"Страница"}],"_type":"record","f":0},"ДопПоля":[]},"id":1}'
    req_json = json.loads(req_str)
    header = {
            'cookie': 'lang=ru-RU; CpsUserId=f7b67558-dcd8-4ce5-b142-0583843bd554; did=d6480d01-cc14-4f26-9b0d-8a36ea17c53f; s3sid-online-daab=004643aa-00d17fe3-00ba-3fced8cd42ce535a; s3su=004643aa-00d17fe3; s3tok-daab=__D6Ld79tDqttjHTntl8aOJsYGIZLU4t4ym90wZGximOhwQ8IdgY2gYrIJPCYlLEX1rNszOYu0N2Fo23ZkwDffMNkGoePPAwfnilwiF5OcSOkCKPe9uytqNT; sid=004643aa-00d17fe3-00ba-3fced8cd42ce535a; tz=-180; s3ds=1920%7C1080%7C1880%7C406%7C1920%7C1040',
            'content-type': 'application/json; charset=UTF-8'
        }
    list_employers = requests.post('https://online.saby.ru/service/?x_version=21.1239-162.1', headers=header,
                                       json=req_json)
    list_employers = list_employers.text
    company = ''
    for employer in json.loads(list_employers)['result']['d']:
        if company == employer[1]:
            break
        print(company, employer[2])
        company = employer[1]
        companies[company] = employer[4]
    cnt += 1
    print(cnt)
    if company == '':
        break
data_json = {'number_of_employers_all': len(companies), 'number_of_employers_less_150': len([i for i in companies.values() if i is not None and float(i)<150000000]), 'companies': companies}
with open('employers_cities/tambov.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data_json, ensure_ascii=False))
print(len(companies))
print(companies.items())
'''money_json = json.loads('{"jsonrpc":"2.0","protocol":6,"method":"АБ.ПрочитатьАнализСПП","params":{"ИдОрганизации":15885196,"Тип":"ФинАнализ"},"id":1}')
data2 = requests.post('https://online.saby.ru/service/?x_version=21.1241-69', headers=header, json=money_json)
data2 = json.loads(data2.text)
print(data2['result']['data']['2020'])'''