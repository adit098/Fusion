from django.urls import path
from . import views

app_name = 'hostelmanagement'

urlpatterns = [
    path('', views.hostel_view, name="hostel_view"),
    path('notice_form/', views.notice_board, name="notice_board"),
    path('edit_schedule/', views.staff_edit_schedule, name='staff_edit_schedule'),
    path('delete_schedule/', views.staff_delete_schedule, name='staff_delete_schedule'),
    path('worker_report/', views.generate_worker_report, name='workerreport'),
    path('edit_student/',views.edit_student_room,name="edit_student_room"),
    path('pdf/', views.GeneratePDF.as_view(), name="pdf"),
    path("<str:hall_num>", views.get_hall_num, name="get_hall_num"),
]