import openpyxl
import json


class fish_data():
    wb = openpyxl.load_workbook('staticfiles/통합_식품영양성분DB_수산물_20221011.xlsx')
    sheet1 = wb['20220920']
    rows = sheet1['A2':'CE1366']

    for row in rows:
        fish_dict = {}
        fish_dict['NO'] = row[0].value
        fish_dict['SAMPLE_ID'] = row[1].value
        fish_dict['식품코드'] = row[2].value
        fish_dict['DB군'] = row[3].value
        fish_dict['상용제품'] = row[4].value
        fish_dict['식품명'] = row[5].value
        fish_dict['연도'] = row[6].value
        fish_dict['지역/제조사'] = row[7].value
        fish_dict['채취시기'] = row[8].value
        fish_dict['식품대분류'] = row[9].value
        fish_dict['식품상세분류'] = row[10].value
        fish_dict['1회제공량'] = row[11].value
        fish_dict['내용량_단위'] = row[12].value
        fish_dict['에너지(㎉)'] = row[13].value
        fish_dict['수분(g)'] = row[14].value
        fish_dict['수분(%)'] = row[15].value
        fish_dict['단백질(g)'] = row[16].value
        fish_dict['지방(g)'] = row[17].value
        fish_dict['지질-가식부(100g당)'] = row[18].value
        fish_dict['탄수화물(g)'] = row[19].value
        fish_dict['총 식이섬유(g)'] = row[20].value
        fish_dict['총 식이섬유(%)'] = row[21].value
        fish_dict['셀룰로오스(%)'] = row[22].value
        fish_dict['리그닌(%)'] = row[23].value
        fish_dict['칼슘(㎎)'] = row[24].value
        fish_dict['철(㎎)'] = row[25].value
        fish_dict['마그네슘(㎎)'] = row[26].value
        fish_dict['인(㎎)'] = row[27].value
        fish_dict['셀레늄(㎍)'] = row[28].value
        fish_dict['레티놀(㎍)'] = row[29].value
        fish_dict['레티놀A효능'] = row[30].value
        fish_dict['비타민 B1(㎎)'] = row[31].value
        fish_dict['비타민 B2(㎎)'] = row[32].value
        fish_dict['나이아신(㎎)'] = row[33].value
        fish_dict['비타민 C(㎎)'] = row[34].value
        fish_dict['총 아미노산(g)'] = row[35].value
        fish_dict['이소류신(㎎)'] = row[36].value
        fish_dict['류신(㎎)'] = row[37].value
        fish_dict['라이신(㎎)'] = row[38].value
        fish_dict['메티오닌(㎎)'] = row[39].value
        fish_dict['페닐알라닌(㎎)'] = row[40].value
        fish_dict['트레오닌(㎎)'] = row[41].value
        fish_dict['트립토판(㎎)'] = row[42].value
        fish_dict['발린(㎎)'] = row[43].value
        fish_dict['히스티딘(㎎)'] = row[44].value
        fish_dict['아르기닌(㎎)'] = row[45].value
        fish_dict['티로신(㎎)'] = row[46].value
        fish_dict['시스테인(㎎)'] = row[47].value
        fish_dict['알라닌(㎎)'] = row[48].value
        fish_dict['아스파르트산(㎎)'] = row[49].value
        fish_dict['글루탐산(㎎)'] = row[50].value
        fish_dict['글리신(㎎)'] = row[51].value
        fish_dict['프롤린(㎎)'] = row[52].value
        fish_dict['세린(㎎)'] = row[53].value
        fish_dict['타우린(㎎)'] = row[54].value
        fish_dict['글리신 베타인(㎎)'] = row[55].value
        fish_dict['호마린(㎎)'] = row[56].value
        fish_dict['트리고넬린(㎎)'] = row[57].value
        fish_dict['리보핵산(㎎)'] = row[58].value
        fish_dict['데옥시리보핵산(㎎)'] = row[59].value
        fish_dict['총 포화 지방산(%)'] = row[60].value
        fish_dict['라우르산(12:0)(%)'] = row[61].value
        fish_dict['미리스트산(14:0)(%)'] = row[62].value
        fish_dict['스테아르산(18:0)(%)'] = row[63].value
        fish_dict['아라키드산(20:0)(%)'] = row[64].value
        fish_dict['총 단일 불포화지방산(%)'] = row[65].value
        fish_dict['미리스톨레산(14:1)(%)'] = row[66].value
        fish_dict['팔미톨레산(16:1)(%)'] = row[67].value
        fish_dict['올레산(18:1(n-9))(%)'] = row[68].value
        fish_dict['에루크산(22:1)(%)'] = row[69].value
        fish_dict['총 다중 불포화지방산(%)'] = row[70].value
        fish_dict['리놀레산(18:2(n-6)c)(%)'] = row[71].value
        fish_dict['알파 리놀렌산(18:3(n-3))(%)'] = row[72].value
        fish_dict['스테아리돈산(18:4)(%)'] = row[73].value
        fish_dict['아라키돈산(20:4(n-6))(%)'] = row[74].value
        fish_dict['에이코사펜타에노산(20:5(n-3))(%)'] = row[75].value
        fish_dict['도코사헥사에노산(22:6(n-3))(%)'] = row[76].value
        fish_dict['냉산가용성물질(㎎)'] = row[77].value
        fish_dict['회분(g)'] = row[78].value
        fish_dict['가식부(%)'] = row[79].value
        fish_dict['산가용성물질(%)'] = row[80].value
        fish_dict['성분표출처'] = row[81].value
        fish_dict['발행기관'] = row[82].value
        fish_object = json.dumps(fish_dict, ensure_ascii=False)
    
