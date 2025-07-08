from django.urls import path
from . import views
app_name = 'xlsmaker' 
urlpatterns = [
    # path('', views.login, name='login' ),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('generate', views.generate_spreadsheet_view, name='generate-spreadsheet'),
    path('download/', views.download_spreadsheet_view, name='download-spreadsheet'),
    path('clear-preview/', views.clear_preview, name='clear-preview'),
    path('validacao/', views.validacao, name='validacao'),
    path('logout/', views.logout_view, name='logout'),  
    path('historico/', views.historico_solicitacoes, name='historico_solicitacoes'), 
    path('upload-planilha/', views.upload_planilha, name='upload_planilha'), 
    path('download-planilha/', views.download_planilha, name='download_planilha'),
    path('generate-dashboard/', views.generate_dashboard_view, name='generate-dashboard'),
]
