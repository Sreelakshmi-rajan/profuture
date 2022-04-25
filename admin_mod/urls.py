from django.contrib import admin
from django.urls import re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^admin_login_page$',views.admin_login_page,name='admin_login_page'),
    re_path(r'^admin_login$',views.admin_login,name='admin_login'),
    re_path(r'^register_page$',views.register_page,name='register_page'),
    re_path(r'^admin_register$',views.admin_register,name='admin_register'),
    re_path(r'^base_ext$',views.base_ext,name='base_ext'),
    re_path(r'^add_pro_form$',views.add_pro_form,name='add_pro_form'),
    re_path(r'^add_pro$',views.add_pro,name='add_pro'),
    re_path(r'^add_project_show$',views.add_project_show,name='add_project_show'),
    re_path(r'^edit/<int:projectid>$',views.add_pro_edit,name='add_pro_edit'),
    re_path(r'^update/<int:projectid>$',views.update,name='update'),
    re_path(r'^add_platform_show$',views.add_platform_show,name='add_platform_show'),
    re_path(r'^add_platform_form$',views.add_platform_form,name='add_platform_form'),
    re_path(r'^add_platform$',views.add_platform,name='add_platform'),
    re_path(r'^platformedit/<int:platformid>$',views.add_platform_edit,name='add_platform_edit'),
    re_path(r'^platformupdate/<int:platformid>$',views.platform_update,name='platform_update'),
    re_path(r'^project_delete/<int:projectid>$',views.project_delete,name='project_delete'),
    re_path(r'^platform_delete/<int:platformid>$',views.platform_delete,name='platform_delete'),
    re_path(r'^project_view$',views.project_view,name='project_view'),
    re_path(r'^add_mcq$',views.add_mcq,name='add_mcq'),
    re_path(r'^add_mcq_form$',views.add_mcq_form,name='add_mcq_form'),
    re_path(r'^mcq_form$',views.mcq_form,name='mcq_form'),
    re_path(r'^mcqedit/<int:mcqid>$',views.add_mcq_edit,name='add_mcq_edit'),
    re_path(r'^mcqupdate/<int:mcqid>$',views.mcq_update,name='mcq_update'),
    re_path(r'^mcq_delete/<int:mcqid>$',views.mcq_delete,name='mcq_delete'),
    re_path(r'^course$',views.course,name='course'),
    
    
]
    
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)