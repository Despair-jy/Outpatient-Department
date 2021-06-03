from django.shortcuts import render
import re
# Create your views here.
from collections import namedtuple
from django.db import connections, connection
from collections import namedtuple
from django.db import connection
from myapp import models
def show(request):
    with connection.cursor() as cursor:



        cursor.execute("SELECT DISTINCT(data) from section_year")
        result1 = namedtuplefetchall(cursor)
        data=[]
        for i in result1:
            data.append(i[0])

        cursor.execute("SELECT treatment_section_name,count from section_year where data like '2017' and  treatment_section_name not like '其他科室' LIMIT 15")
        result2=namedtuplefetchall(cursor)
        count1=[]
        treatment_section_name1=[]
        for i in result2:
            count1.append(i[1])
            treatment_section_name1.append(i[0])

        cursor.execute(
            "SELECT treatment_section_name,count from section_year where data like '2018' and  treatment_section_name not like '其他科室' LIMIT 15")
        result3 = namedtuplefetchall(cursor)
        count2 = []
        treatment_section_name2 = []
        for i in result3:
            count2.append(i[1])
            treatment_section_name2.append(i[0])

        cursor.execute(
            "SELECT treatment_section_name,count from section_year where data like '2019' and  treatment_section_name not like '其他科室' LIMIT 15")
        result4 = namedtuplefetchall(cursor)
        count3 = []
        treatment_section_name3 = []
        for i in result4:
            count3.append(i[1])
            treatment_section_name3.append(i[0])

        cursor.execute(
            "SELECT treatment_section_name,count from section_year where data like '2017' and org_name like '济南市儿童医院' LIMIT 15")
        result5 = namedtuplefetchall(cursor)
        count4 = []
        treatment_section_name4 = []
        for i in result5:
            count4.append(i[1])
            treatment_section_name4.append(i[0])

        cursor.execute(
            "SELECT treatment_section_name,count from section_year where data like '2018' and org_name like '济南市儿童医院' LIMIT 15")
        result6 = namedtuplefetchall(cursor)
        count5 = []
        treatment_section_name5 = []
        for i in result6:
            count5.append(i[1])
            treatment_section_name5.append(i[0])

        cursor.execute(
            "SELECT treatment_section_name,count from section_year where data like '2019' and org_name like '济南市儿童医院' LIMIT 15")
        result7 = namedtuplefetchall(cursor)
        count6 = []
        treatment_section_name6 = []
        for i in result7:
            count6.append(i[1])
            treatment_section_name6.append(i[0])

        # count_year={e:count1[i] for i, e in enumerate(data)}
        # print(count_year)

        cursor.execute("SELECT cnt FROM org_name_2017 where org_name='济南市儿童医院'")
        a1 = namedtuplefetchall(cursor)
        cursor.execute("SELECT cnt FROM org_name_2018 where org_name='济南市儿童医院'")
        a2 = namedtuplefetchall(cursor)
        cursor.execute("SELECT cnt FROM org_name_2019 where org_name='济南市儿童医院'")
        a3 = namedtuplefetchall(cursor)
        cnt1=[]
        cnt2=[]
        cnt3=[]
        for i in a1:
            cnt1.append(i[0])
        for i in a2:
            cnt2.append(i[0])
        for i in a3:
            cnt3.append(i[0])
        cnt_c=[]
        cnt_c.append(cnt1[0])
        cnt_c.append(cnt2[0])
        cnt_c.append(cnt3[0])
        # print(cnt_c)

        cursor.execute("SELECT cnt FROM org_name_2017 where org_name='济南市第四人民医院'")
        a4 = namedtuplefetchall(cursor)
        cursor.execute("SELECT cnt FROM org_name_2018 where org_name='济南市第四人民医院'")
        a5 = namedtuplefetchall(cursor)
        cursor.execute("SELECT cnt FROM org_name_2019 where org_name='济南市第四人民医院'")
        a6 = namedtuplefetchall(cursor)
        cnt4=[]
        cnt5=[]
        cnt6=[]
        for i in a4:
            cnt4.append(i[0])
        for i in a5:
            cnt5.append(i[0])
        for i in a6:
            cnt6.append(i[0])
        cnt_p=[]
        cnt_p.append(cnt4[0])
        cnt_p.append(cnt5[0])
        cnt_p.append(cnt6[0])

        cursor.execute("SELECT treatment_section_name,doc FROM doc_2018 where org_name='济南市儿童医院' GROUP BY doc desc limit 5")
        b1 = namedtuplefetchall(cursor)
        cursor.execute("SELECT treatment_section_name,doc FROM doc_2018 where org_name='济南市第四人民医院' GROUP BY doc desc limit 5 ")
        b2 = namedtuplefetchall(cursor)
        section_doc1 = []
        section_doc2 = []
        doc1=[]
        doc2=[]
        for i in b1 :
            section_doc1.append(i[0])
            doc1.append((i[1]))
        for i in b2 :
            section_doc2.append(i[0])
            doc2.append((i[1]))

        doc_c=[]
        for i in range(len(section_doc1)):
            doc={}
            doc["name"]=section_doc1[i]
            doc["value"]=doc1[i]
            doc_c.append(doc)

        # print(doc_c)
        doc_p = []
        for i in range(len(section_doc2)):
            doc = {}
            doc["name"] = section_doc2[i]
            doc["value"] = doc2[i]
            doc_p.append(doc)

        # print(doc_p)
        cursor.execute(
            "SELECT treatment_section_name,cost from cost_2017 where org_name='济南市儿童医院' ")
        c1 = namedtuplefetchall(cursor)
        cursor.execute(
            "SELECT treatment_section_name,cost from cost_2017 where org_name='济南市第四人民医院' ")
        c2 = namedtuplefetchall(cursor)
        section_doc3 = []
        section_doc4 = []
        cost1=[]
        cost2=[]
        for i in c1 :
            section_doc3.append(i[0])
            cost1.append((i[1]))
        for i in c2 :
            section_doc4.append(i[0])
            cost2.append((i[1]))

        cost_c=[]
        for i in range(len(section_doc3)):
            cost = {}
            cost["name"] = section_doc3[i]
            cost["value"] = cost1[i]
            cost_c.append(cost)
        cost_p = []
        for i in range(len(section_doc4)):
            cost = {}
            cost["name"] = section_doc4[i]
            cost["value"] = cost2[i]
            cost_p.append(cost)
        # count_year={e:count1[i] for i, e in enumerate(data)}
        section_cost1={e:section_doc3[i] for i ,e in enumerate(section_doc3)}
        section_cost2={e:section_doc4[i] for i ,e in enumerate(section_doc4)}
        section_cost={}
        section_cost.update(section_cost1)
        section_cost.update(section_cost2)








    return render(request,"medical/index.html",{"treatment_section_name1":treatment_section_name1,"data":data,"count1":count1,"treatment_section_name2":treatment_section_name2,"treatment_section_name3":treatment_section_name3,
                                               "count2":count2,"count3":count3,"count4":count4,"count5":count5,"count6":count6,"treatment_section_name4":treatment_section_name4,"treatment_section_name5":treatment_section_name5,"treatment_section_name6":treatment_section_name6,
                                               "cnt_c":cnt_c,"cnt_p":cnt_p,"doc_c":doc_c,"doc_p":doc_p,"cost_c":cost_c,"cost_p":cost_p,"section_cost":section_cost})




def gl(request):
    with connection.cursor() as cursor:
        cursor.execute("select admin_illness_name,SUM(count) as count from disease_year WHERE date like '%%01%%' or date like '%%02%%' or date  like '%%03%%' GROUP BY admin_illness_name ORDER BY count DESC")
        a1 = namedtuplefetchall(cursor)
        cursor.execute("select admin_illness_name,SUM(count) as count from disease_year WHERE date like '%%04%%' or date like '%%05%%' or date  like '%%06%%' GROUP BY admin_illness_name ORDER BY count DESC")
        a2= namedtuplefetchall(cursor)
        cursor.execute("select admin_illness_name,SUM(count) as count from disease_year WHERE date like '%%07%%' or date like '%%08%%' or date  like '%%09%%' GROUP BY admin_illness_name ORDER BY count DESC")
        a3=namedtuplefetchall(cursor)
        cursor.execute("select admin_illness_name,SUM(count) as count from disease_year WHERE date like '%%10%%' or date like '%%11%%' or date  like '%%12%%' GROUP BY admin_illness_name ORDER BY count DESC")
        a4=namedtuplefetchall(cursor)
        illness=[]
        illness1 = []
        illness2 = []
        illness3 = []
        illness4 = []
        illness5 = []

        count1 = []
        count2 = []
        count3 = []
        count4 = []
        count5=[]
        count6=[]
        count7=[]
        count8=[]
        count9=[]

        for i in a1:
            illness.append(i[0])
            count1.append(i[1])
        for i in a2:
            count2.append(i[1])
        for i in a3:
            count3.append(i[1])
        for i in a4:
            count4.append(i[1])

        for i in range(len(count1)):
            if i==0:
                count5.append(count1[i])
                illness1.append(illness[i])
            elif i==1:
                count6.append(count1[i])
                illness2.append(illness[i])
            elif i==2:
                count7.append(count1[i])
                illness3.append(illness[i])
            elif i==3:
                count8.append(count1[i])
                illness4.append(illness[i])
            elif i==5:
                count9.append(count1[i])
                illness5.append(illness[i])

        for i in range(len(count2)):
            if i == 0:
                count5.append(count2[i])
            elif i == 1:
                count6.append(count2[i])

            elif i == 2:
                count7.append(count2[i])

            elif i == 3:
                count8.append(count2[i])

            elif i == 6:
                count9.append(count2[i])

        for i in range(len(count3)):
            if i == 0:
                count5.append(count3[i])
            elif i == 1:
                count6.append(count3[i])

            elif i == 4:
                count7.append(count3[i])

            elif i == 3:
                count8.append(count3[i])

            elif i == 8:
                count9.append(count3[i])

        for i in range(len(count4)):
            if i == 1:
                count5.append(count4[i])
            elif i == 0:
                count6.append(count4[i])

            elif i == 2:
                count7.append(count4[i])

            elif i == 3:
                count8.append(count4[i])

            elif i == 5:
                count9.append(count4[i])
        global hospital_2017_name, hospital_2017_value, hospital_2018_value, hospital_2018_name
        with connection.cursor() as cursor:
            # 再复杂的sql也不怕
            cursor.execute(
                "select admin_illness_name,count(admin_illness_name) as count from train_2017 GROUP BY admin_illness_name ORDER BY count DESC")
            # 返回列表
            cursor.close()
            result1 = namedtuplefetchall(cursor)
        year_disease = []
        for i in result1:
            dict = {}
            dict["name"] = i[0]
            dict["value"] = i[1]
            year_disease.append(dict)
        # print(year_disease)
        with connection.cursor() as cursor:
            # 再复杂的sql也不怕
            cursor.execute(
                "select admin_illness_name,count(admin_illness_name) as count from train_2018 GROUP BY admin_illness_name ORDER BY count DESC")
            # 返回列表
            cursor.close()
            result2 = namedtuplefetchall(cursor)
        for i in result2:
            dict = {}
            dict["name"] = i[0]
            dict["value"] = i[1]
            year_disease.append(dict)

        # # 绘制每个医院看病top10
        # name1 = request.POST.get("name", '')
        # if name1 == "济南市儿童医院":
        #     with connection.cursor() as cursor:
        #         # 再复杂的sql也不怕
        #         cursor.execute(
        #             "SELECT admin_illness_name ,count from hospital_disease where org_name='济南市儿童医院' and treatment_date LIKE '2017%%'  ORDER BY count DESC LIMIT 6")
        #         # 返回列表
        #         cursor.close()
        #         hospital_2017 = namedtuplefetchall(cursor)
        #     hospital_2017_name = []
        #     hospital_2017_value = []
        #     for i in hospital_2017:
        #         hospital_2017_name.append(i[0])
        #         hospital_2017_value.append(i[1])
        #     hospital_2017_name.reverse()
        #     hospital_2017_value.reverse()
        #     # print(jinan_2017_name)
        #     # print(jinan_2017_value)
        #     with connection.cursor() as cursor:
        #         # 再复杂的sql也不怕
        #         cursor.execute(
        #             "SELECT admin_illness_name ,count from hospital_disease where org_name='济南市儿童医院' and treatment_date LIKE '2018%%'  ORDER BY count desc LIMIT 6")
        #         # 返回列表
        #         cursor.close()
        #         hospital_2018 = namedtuplefetchall(cursor)
        #     hospital_2018_name = []
        #     hospital_2018_value = []
        #     for i in hospital_2018:
        #         hospital_2018_name.append(i[0])
        #         hospital_2018_value.append(i[1])
        #     hospital_2018_name.reverse()
        #     hospital_2018_value.reverse()
        #     # print(jinan_2018_name)
        #     # print(jinan_2018_value)
        # elif name1 == "济南市第四人民医院":
        #     with connection.cursor() as cursor:
        #         # 再复杂的sql也不怕
        #         cursor.execute(
        #             "SELECT admin_illness_name ,count from hospital_disease where org_name='济南市第四人民医院' and treatment_date LIKE '2017%%'  ORDER BY count DESC LIMIT 6")
        #         # 返回列表
        #         cursor.close()
        #         hospital_2017 = namedtuplefetchall(cursor)
        #     hospital_2017_name = []
        #     hospital_2017_value = []
        #     for i in hospital_2017:
        #         hospital_2017_name.append(i[0])
        #         hospital_2017_value.append(i[1])
        #     hospital_2017_name.reverse()
        #     hospital_2017_value.reverse()
        #     # print(jinan_2017_name)
        #     # print(jinan_2017_value)
        #     with connection.cursor() as cursor:
        #         # 再复杂的sql也不怕
        #         cursor.execute(
        #             "SELECT admin_illness_name ,count from hospital_disease where org_name='济南市第四人民医院' and treatment_date LIKE '2018%%'  ORDER BY count desc LIMIT 6")
        #         # 返回列表
        #         cursor.close()
        #         hospital_2018 = namedtuplefetchall(cursor)
        #     hospital_2018_name = []
        #     hospital_2018_value = []
        #     for i in hospital_2018:
        #         hospital_2018_name.append(i[0])
        #         hospital_2018_value.append(i[1])
        #     hospital_2018_name.reverse()
        #     hospital_2018_value.reverse()
        # elif name1 == "":
        #     with connection.cursor() as cursor:
        #         # 再复杂的sql也不怕
        #         cursor.execute(
        #             "SELECT admin_illness_name ,count from hospital_disease where org_name='济南市儿童医院' and treatment_date LIKE '2017%%'  ORDER BY count DESC LIMIT 6")
        #         # 返回列表
        #         cursor.close()
        #         hospital_2017 = namedtuplefetchall(cursor)
        #     hospital_2017_name = []
        #     hospital_2017_value = []
        #     for i in hospital_2017:
        #         hospital_2017_name.append(i[0])
        #         hospital_2017_value.append(i[1])
        #     hospital_2017_name.reverse()
        #     hospital_2017_value.reverse()
        #     # print(jinan_2017_name)
        #     # print(jinan_2017_value)
        #     with connection.cursor() as cursor:
        #         # 再复杂的sql也不怕
        #         cursor.execute(
        #             "SELECT admin_illness_name ,count from hospital_disease where org_name='济南市儿童医院' and treatment_date LIKE '2018%%'  ORDER BY count desc LIMIT 6")
        #         # 返回列表
        #         hospital_2018 = namedtuplefetchall(cursor)
        #         cursor.close()
        #     hospital_2018_name = []
        #     hospital_2018_value = []
        #     for i in hospital_2018:
        #         hospital_2018_name.append(i[0])
        #         hospital_2018_value.append(i[1])
        #     hospital_2018_name.reverse()
        #     hospital_2018_value.reverse()

        # 绘制每年每月的疾病top10
        year = request.POST.get("year", '')
        month = request.POST.get("month", '')
        name = []
        value = []
        if year != '' and month != '':
            year = re.match("\d+", year).group()
            month = re.match("\d+", month).group()
            a = '0'
            if int(month) <= 9:
                year_month = year + a + month
            else:
                year_month = year + month
            # print(year_month)
            a = models.DiseaseYear1.objects.filter(date=year_month).order_by("-count")[0:10]
            for i in a:
                name.append(i.admin_illness_name)
                value.append(i.count)
        else:
            b = models.DiseaseYear1.objects.filter(date="201701").order_by("-count")[0:10]
            # print(b)
            for i in b:
                name.append(i.admin_illness_name)
                value.append(i.count)

        # 慢性病近几年发病趋势
        gaoxueya_value = []
        tang_value = []
        xuezhi_value = []
        naogeng = []
        chronicDiseases = models.ChronicDiseases.objects.filter(admin_illness_name='高血压').order_by("date").values_list()
        for i in chronicDiseases:
            gaoxueya_value.append(i[2])
        chronicDiseases1 = models.ChronicDiseases.objects.filter(admin_illness_name='糖尿病').order_by(
            "date").values_list()
        for i in chronicDiseases1:
            tang_value.append(i[2])
        chronicDiseases2 = models.ChronicDiseases.objects.filter(admin_illness_name='高脂血症').order_by(
            "date").values_list()
        for i in chronicDiseases2:
            xuezhi_value.append(i[2])
        chronicDiseases3 = models.ChronicDiseases.objects.filter(admin_illness_name='脑梗死').order_by(
            "date").values_list()
        for i in chronicDiseases3:
            naogeng.append(i[2])

    # ,
    # "hospital_2017_name": hospital_2017_name, "hospital_2017_value": hospital_2017_value, "hospital_2018_name": hospital_2018_name,
    # "hospital_2018_value": hospital_2018_value, "year": year, "month": month, "name1": name1
    return render(request,"medical/index1.html",{"count5":count5,"count6":count6,"count7":count7,"count8":count8,"count9":count9,"year_disease":year_disease,"name":name,"value":value,
    "gaoxueya_value":gaoxueya_value,"tang_value":tang_value,"xuezhi_value":xuezhi_value,"naogeng":naogeng})




def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

# def index2017(request):
#     objs = NewCount2017.objects.all()
#     return render(request, 'count_2017.html', locals())
#
# def index2018(request):
#     objs1 = NewCount2018.objects.all()
#     return render(request,'count_2018.html',locals())
#
# def map(request):
#     return render(request,"jinan_map.html")
#
# def top_2017(request):
#     top_2017=Top202017.objects.all()
#     return render(request, "top10_2017.html", locals())

def xy(request):
    return render(request, "medical/index3.html")


def hh(request):
    # 绘制每个医院看病top10
    name1 = request.POST.get("name", '')
    if name1 == "济南市儿童医院":
        with connection.cursor() as cursor:
            # 再复杂的sql也不怕
            cursor.execute(
                "SELECT admin_illness_name ,count from hospital_disease where org_name='济南市儿童医院' and treatment_date LIKE '2017%%'  ORDER BY count DESC LIMIT 4")
            # 返回列表
            cursor.close()
            hospital_2017 = namedtuplefetchall(cursor)
        hospital_2017_name = []
        hospital_2017_value = []
        for i in hospital_2017:
            hospital_2017_name.append(i[0])
            hospital_2017_value.append(i[1])
        hospital_2017_name.reverse()
        hospital_2017_value.reverse()
        # print(jinan_2017_name)
        # print(jinan_2017_value)
        with connection.cursor() as cursor:
            # 再复杂的sql也不怕
            cursor.execute(
                "SELECT admin_illness_name ,count from hospital_disease where org_name='济南市儿童医院' and treatment_date LIKE '2018%%'  ORDER BY count desc LIMIT 4")
            # 返回列表
            cursor.close()
            hospital_2018 = namedtuplefetchall(cursor)
        hospital_2018_name = []
        hospital_2018_value = []
        for i in hospital_2018:
            hospital_2018_name.append(i[0])
            hospital_2018_value.append(i[1])
        hospital_2018_name.reverse()
        hospital_2018_value.reverse()
        # print(jinan_2018_name)
        # print(jinan_2018_value)
    elif name1 == "济南市第四人民医院":
        with connection.cursor() as cursor:
            # 再复杂的sql也不怕
            cursor.execute(
                "SELECT admin_illness_name ,count from hospital_disease where org_name='济南市第四人民医院' and treatment_date LIKE '2017%%'  ORDER BY count DESC LIMIT 4")
            # 返回列表
            cursor.close()
            hospital_2017 = namedtuplefetchall(cursor)
        hospital_2017_name = []
        hospital_2017_value = []
        for i in hospital_2017:
            hospital_2017_name.append(i[0])
            hospital_2017_value.append(i[1])
        hospital_2017_name.reverse()
        hospital_2017_value.reverse()
        # print(jinan_2017_name)
        # print(jinan_2017_value)
        with connection.cursor() as cursor:
            # 再复杂的sql也不怕
            cursor.execute(
                "SELECT admin_illness_name ,count from hospital_disease where org_name='济南市第四人民医院' and treatment_date LIKE '2018%%'  ORDER BY count desc LIMIT 4")
            # 返回列表
            cursor.close()
            hospital_2018 = namedtuplefetchall(cursor)
        hospital_2018_name = []
        hospital_2018_value = []
        for i in hospital_2018:
            hospital_2018_name.append(i[0])
            hospital_2018_value.append(i[1])
        hospital_2018_name.reverse()
        hospital_2018_value.reverse()
    elif name1 == "":
        with connection.cursor() as cursor:
            # 再复杂的sql也不怕
            cursor.execute(
                "SELECT admin_illness_name ,count from hospital_disease where org_name='济南市儿童医院' and treatment_date LIKE '2017%%' ORDER BY count DESC LIMIT 4")
            # 返回列表
            cursor.close()
            hospital_2017 = namedtuplefetchall(cursor)
        hospital_2017_name = []
        hospital_2017_value = []
        for i in hospital_2017:
            hospital_2017_name.append(i[0])
            hospital_2017_value.append(i[1])
        hospital_2017_name.reverse()
        hospital_2017_value.reverse()
        # print(jinan_2017_name)
        # print(jinan_2017_value)
        with connection.cursor() as cursor:
            # 再复杂的sql也不怕
            cursor.execute(
                "SELECT admin_illness_name ,count from hospital_disease where org_name='济南市儿童医院' and treatment_date LIKE '2018%%'  ORDER BY count desc LIMIT 4")
            # 返回列表
            hospital_2018 = namedtuplefetchall(cursor)
            cursor.close()
        hospital_2018_name = []
        hospital_2018_value = []
        for i in hospital_2018:
            hospital_2018_name.append(i[0])
            hospital_2018_value.append(i[1])
        hospital_2018_name.reverse()
        hospital_2018_value.reverse()

    # 绘制2020年疾病花费前三

    with connection.cursor() as cursor:
        # 再复杂的sql也不怕
        cursor.execute(
            "select name,data from cost_total2020  ORDER BY data DESC LIMIT 10")
        # 返回列表
        cursor.close()
        a=namedtuplefetchall(cursor)
    ss=[]
    for i in a:
        dict = {}
        dict["name"]=i[0]
        dict["value"]=i[1]
        ss.append(dict)

    name=[]
    for i in a:
        name.append(i[0])

    return render(request,'medical/index2.html',{"hospital_2017_name":hospital_2017_name,"hospital_2017_value":hospital_2017_value,"hospital_2018_name":hospital_2018_name,
                                                    "hospital_2018_value":hospital_2018_value,"name1":name1,"ss":ss,"name":name})


def zhunbei_predict(request):
    return render(request,'medical/index5.html')


# 接收预测的数据进行处理
def predict1(request):
    id = request.POST.get("id")
    date = request.POST.get("date")
    hospital_name = request.POST.get("hospital_name")
    disease_name = request.POST.get("disease_name")
    treatment_name = request.POST.get("treatment_name")
    treatment_code = request.POST.get("treatment_code")
    district_code = request.POST.get("district_code")
    price = request.POST.get("price")
    print(type(id))
    print(id)
    if id!='' and date!='' and hospital_name!='' and disease_name!='' and treatment_name!='' and treatment_code!='' and district_code!='' and price!='':
        from pypmml import Model
        model = Model.fromFile(r"mml/test")
        zhuang_huan=[disease_name,hospital_name,treatment_code,treatment_name]
        print(zhuang_huan)
        import numpy as np
        zhuang_huan= np.array(zhuang_huan)
        from sklearn.preprocessing import LabelEncoder
        encoder = LabelEncoder()
        zhuang_huan = encoder.fit_transform(zhuang_huan)
        zhuang_huan=list(zhuang_huan)
        print(zhuang_huan)
        zhuang_huan.insert(0,id)
        zhuang_huan.insert(2,price)
        zhuang_huan.append(date)
        zhuang_huan.append(district_code)
        print(zhuang_huan)
        # predict_results = list(map(eval, zhuang_huan))
        # print(predict_results)
        # result=[id,disease_name,price,hospital_name,treatment_code,treatment_name,date,district_code]

        # 需求将医院,病种，科室名称，科室编码转换成特征值
        # data = [[4.0, 1687.0, 293.64401349999997, 0.0, 34.0, 37.0, 20190201, 370104.0]]
        result = np.array(zhuang_huan)
        y_predict = model.predict(result)
        print("预测结果：", y_predict)
        if int(y_predict[0])==0:
            a="不需要复诊"
        elif int(y_predict[0])==1:
            a="需要复诊"
    else:
        return 0

    return render(request,"medical/index5.html" , {"predict": a})
