from django.conf.urls import url
from myapp import views
#配置路由
urlpatterns = [
# url("show_admin/",views.show_admin,name="show_admin"),
url("show/",views.show,name="show"),
url("gl/",views.gl,name="gl"),
url("xy/",views.xy,name="xy"),
url("hh/",views.hh,name="hh"),
url("predict1/",views.predict1,name="predict1"),
url("zhunbei_predict/",views.zhunbei_predict,name="zhunbei_predict")

]

