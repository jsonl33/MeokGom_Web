# Generated by Django 4.1.2 on 2022-11-03 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0003_fooddb_delete_groceries'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SAMPLE_ID', models.CharField(max_length=100, verbose_name='SAMPLE_ID')),
                ('식품코드', models.CharField(max_length=100, verbose_name='식품코드')),
                ('DB군', models.CharField(max_length=100, verbose_name='DB군')),
                ('상용제품', models.CharField(max_length=100, verbose_name='상용제품')),
                ('식품명', models.CharField(max_length=100, verbose_name='식품명')),
                ('연도', models.IntegerField(verbose_name='연도')),
                ('지역_제조사', models.CharField(max_length=100, verbose_name='지역_제조사')),
                ('채취시기', models.CharField(max_length=100, verbose_name='채취시기')),
                ('식품대분류', models.CharField(max_length=100, verbose_name='식품대분류')),
                ('식품상세분류', models.CharField(max_length=100, verbose_name='식품상세분류')),
                ('_1회제공량', models.IntegerField(verbose_name='1회제공량')),
                ('내용량_단위', models.CharField(max_length=100, verbose_name='내용량_단위')),
                ('총내용량_g', models.FloatField(verbose_name='총내용량(g)')),
                ('총내용량_mL', models.FloatField(verbose_name='총내용량(mL)')),
                ('에너지', models.FloatField(verbose_name='에너지(㎉)')),
                ('수분', models.FloatField(verbose_name='수분(g)')),
                ('단백질', models.FloatField(verbose_name='단백질(g)')),
                ('지방', models.FloatField(verbose_name='지방(g)')),
                ('탄수화물', models.FloatField(verbose_name='탄수화물(g)')),
                ('총당류', models.FloatField(verbose_name='총당류(g)')),
                ('자당', models.FloatField(verbose_name='자당(g)')),
                ('포도당', models.FloatField(verbose_name='포도당(g)')),
                ('과당', models.FloatField(verbose_name='과당(g)')),
                ('유당', models.FloatField(verbose_name='유당(g)')),
                ('맥아당', models.FloatField(verbose_name='맥아당(g)')),
                ('총_식이섬유', models.FloatField(verbose_name='총 식이섬유(g)')),
                ('칼슘', models.FloatField(verbose_name='칼슘(㎎)')),
                ('철_mg', models.FloatField(verbose_name='철(㎎)')),
                ('철_ug', models.FloatField(verbose_name='철(㎍)')),
                ('마그네슘', models.FloatField(verbose_name='마그네슘(㎎)')),
                ('인', models.FloatField(verbose_name='인(㎎)')),
                ('칼륨', models.FloatField(verbose_name='칼륨(㎎)')),
                ('나트륨', models.FloatField(verbose_name='나트륨(㎎)')),
                ('아연', models.FloatField(verbose_name='아연(㎎)')),
                ('구리', models.FloatField(verbose_name='구리(㎎)')),
                ('망간', models.FloatField(verbose_name='망간(㎎)')),
                ('셀레늄', models.FloatField(verbose_name='셀레늄(㎍)')),
                ('레티놀', models.FloatField(verbose_name='레티놀(㎍)')),
                ('베타카로틴', models.FloatField(verbose_name='베타카로틴(㎍)')),
                ('비타민_D3', models.FloatField(verbose_name='비타민 D3(㎍)')),
                ('토코페롤', models.FloatField(verbose_name='토코페롤(㎎)')),
                ('토코트리에놀', models.FloatField(verbose_name='토코트리에놀(㎎)')),
                ('비타민_B1', models.FloatField(verbose_name='비타민 B1(㎎)')),
                ('비타민_B2', models.FloatField(verbose_name='비타민 B2(㎎)')),
                ('나이아신', models.FloatField(verbose_name='나이아신(㎎)')),
                ('엽산', models.FloatField(verbose_name='엽산(DFE)(㎍)')),
                ('비타민_B12', models.FloatField(verbose_name='비타민 B12(㎍)')),
                ('비타민_C', models.FloatField(verbose_name='비타민 C(㎎)')),
                ('총_아미노산', models.FloatField(verbose_name='총 아미노산(㎎)')),
                ('이소류신', models.FloatField(verbose_name='이소류신(㎎)')),
                ('류신', models.FloatField(verbose_name='류신(㎎)')),
                ('라이신', models.FloatField(verbose_name='라이신(㎎)')),
                ('메티오닌', models.FloatField(verbose_name='메티오닌(㎎)')),
                ('페닐알라닌', models.FloatField(verbose_name='페닐알라닌(㎎)')),
                ('트레오닌', models.FloatField(verbose_name='트레오닌(㎎)')),
                ('발린', models.FloatField(verbose_name='발린(㎎)')),
                ('히스티딘', models.FloatField(verbose_name='히스티딘(㎎)')),
                ('아르기닌', models.FloatField(verbose_name='아르기닌(㎎)')),
                ('티로신', models.FloatField(verbose_name='티로신(㎎)')),
                ('시스테인', models.FloatField(verbose_name='시스테인(㎎)')),
                ('알라닌', models.FloatField(verbose_name='알라닌(㎎)')),
                ('아스파르트산', models.FloatField(verbose_name='아스파르트산(㎎)')),
                ('글루탐산', models.FloatField(verbose_name='글루탐산(㎎)')),
                ('글리신', models.FloatField(verbose_name='글리신(㎎)')),
                ('프롤린', models.FloatField(verbose_name='프롤린(㎎)')),
                ('세린', models.FloatField(verbose_name='세린(㎎)')),
                ('콜레스테롤', models.FloatField(verbose_name='콜레스테롤(㎎)')),
                ('총_포화_지방산', models.FloatField(verbose_name='총 포화 지방산(g)')),
                ('부티르산', models.FloatField(verbose_name='부티르산(4:0)(g)')),
                ('카프로산', models.FloatField(verbose_name='카프로산(6:0)(g)')),
                ('카프릴산', models.FloatField(verbose_name='카프릴산(8:0)(g)')),
                ('카프르산', models.FloatField(verbose_name='카프르산(10:0)(g)')),
                ('라우르산', models.FloatField(verbose_name='라우르산(12:0)(g)')),
                ('미리스트산', models.FloatField(verbose_name='미리스트산(14:0)(g)')),
                ('팔미트산', models.FloatField(verbose_name='팔미트산(16:0)(g)')),
                ('스테아르산', models.FloatField(verbose_name='스테아르산(18:0)(g)')),
                ('아라키드산', models.FloatField(verbose_name='아라키드산(20:0)(g)')),
                ('미리스톨레산', models.FloatField(verbose_name='미리스톨레산(14:1)(g)')),
                ('팔미톨레산', models.FloatField(verbose_name='팔미톨레산(16:1)(g)')),
                ('올레산', models.FloatField(verbose_name='올레산(18:1(n-9))(g)')),
                ('박센산', models.FloatField(verbose_name='박센산(18:1(n-7))(g)')),
                ('가돌레산', models.FloatField(verbose_name='가돌레산(20:1)(g)')),
                ('리놀레산', models.FloatField(verbose_name='리놀레산(18:2(n-6)c)(g)')),
                ('알파_리놀렌산', models.FloatField(verbose_name='알파 리놀렌산(18:3(n-3))(g)')),
                ('감마_리놀렌산', models.FloatField(verbose_name='감마 리놀렌산(18:3(n-6))(g)')),
                ('에이코사디에노산', models.FloatField(verbose_name='에이코사디에노산(20:2(n-6))(g)')),
                ('에이코사트리에노산', models.FloatField(verbose_name='에이코사트리에노산(20:3(n-6))(g)')),
                ('아라키돈산', models.FloatField(verbose_name='아라키돈산(20:4(n-6))(g)')),
                ('에이코사펜타에노산', models.FloatField(verbose_name='에이코사펜타에노산(20:5(n-3))(g)')),
                ('도코사펜타에노산', models.FloatField(verbose_name='도코사펜타에노산(22:5(n-3))(g)')),
                ('도코사헥사에노산', models.FloatField(verbose_name='도코사헥사에노산(22:6(n-3))(g)')),
                ('트랜스_지방산', models.FloatField(verbose_name='트랜스 지방산(g)')),
                ('트랜스_올레산', models.FloatField(verbose_name='트랜스 올레산(18:1(n-9)t)(g)')),
                ('트랜스_리놀레산', models.FloatField(verbose_name='트랜스 리놀레산 (18:2t)(g)')),
                ('트랜스_리놀렌산', models.FloatField(verbose_name='트랜스 리놀렌산(18:3t)(g)')),
                ('회분', models.FloatField(verbose_name='회분(g)')),
                ('카페인', models.FloatField(verbose_name='카페인(㎎)')),
                ('성분표출처', models.CharField(max_length=100, verbose_name='성분표출처')),
                ('발행기관', models.CharField(max_length=100, verbose_name='발행기관')),
            ],
        ),
        migrations.DeleteModel(
            name='FoodDB',
        ),
    ]