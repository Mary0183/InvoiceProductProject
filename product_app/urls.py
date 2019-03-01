from django.urls import path


from . import views

app_name = 'product_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('invoices', views.invoice_index, name='invoices'),
    path('invoice_detail/<int:invoice_id>', views.invoice_detail, name='invoice_detail'),
    path('invoice_create', views.invoice_create, name='invoice_create'),
    path('invoice_create_product/<int:invoice_id>', views.invoice_create_product, name='invoice_create_product'),
    path('delete_invoice_product/<int:invoice_product_id>', views.delete_invoice_product, name='delete_invoice_product'),
    path('delete_invoice/<int:invoice_id>', views.delete_invoice, name='delete_invoice'),
    path('delete_product/<int:product_id>', views.delete_product, name='delete_product'),
    path('dashboard', views.dashboard, name='dashboard')
    ]

