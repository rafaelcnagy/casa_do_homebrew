from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.pdf_list, name='pdf_list'),
    path('create', views.create_pdf, name='create_pdf'),
    path('', views.PdfList.as_view(template_name='taverna_dos_pdfs/pdf_list.html'), name='pdf_list'),
    path('pdf/<int:pk>', views.PdfDetail.as_view(template_name='taverna_dos_pdfs/pdf_view.html'), name='pdf_view'),
    path('pdf/<int:pk>/update', views.PdfUpdate.as_view(template_name='taverna_dos_pdfs/pdf_update.html'), name='pdf_update'),
    path('pdf/<int:pk>/delete', views.PdfDelete.as_view(template_name='taverna_dos_pdfs/pdf_delete.html'), name='pdf_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
