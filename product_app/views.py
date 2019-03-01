from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Product
from .models import Invoice
from .models import Invoice_Product

def create(request):
    if request.method == "POST":
        p= Product(product_name=request.POST['product.product_name'] , price=request.POST['product.price'])
        p.save()
        return HttpResponseRedirect('/products')

    return render(request, 'product_app/create.html')

def index(request):
    latest_product_list = Product.objects.all()
    context = {'latest_product_list': latest_product_list}
    return render(request, 'product_app/index.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_app/detail.html', {'product': product})

def results(request, product_id):
    response = "You're looking at the results of product %s."
    return HttpResponse(response % product_id)


def invoice_index(request):
    latest_invoice_list = Invoice.objects.all()
    context = {'latest_invoice_list': latest_invoice_list}
    return render(request, 'product_app/invoice_index.html', context)

def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    invoice_products = invoice.invoice_product_set.all()
    total_price_products = 0
    for product in invoice_products:
        total_price_products = total_price_products + product.price
    product_list = Product.objects.all()

    return render(request, 'product_app/invoice_detail.html', {
        'invoice': invoice,
        'invoice_products': invoice_products,
        'product_count': len(invoice_products),
        'total_price_products': total_price_products,
        'product_list': product_list
        
    })

def invoice_create(request):
    if request.method == "POST":
        p= Invoice(purchase_date=request.POST['invoice.purchase_date'] , total_invoice=request.POST['invoice.total_invoice'] )
        p.save()
        return HttpResponseRedirect('/products/invoices')

    return render(request, 'product_app/invoice_create.html')

def invoice_create_product(request, invoice_id):
    if request.method == "POST":
        invoice = Invoice.objects.get(pk=invoice_id)
        product_id=request.POST['select_product']
        product= Product.objects.get(pk=product_id)
        ip = Invoice_Product(
            invoice= invoice, 
            product= product, 
            price= request.POST['price'], 
            quantity= request.POST['quantity'])
        ip.save()
        return HttpResponseRedirect('/products/invoice_detail/'+str(invoice_id))

def delete_invoice_product(request, invoice_product_id):
    invoice_product= Invoice_Product.objects.get(pk=invoice_product_id)
    invoice_id = invoice_product.invoice.id
    invoice_product.delete()
    return HttpResponseRedirect('/products/invoice_detail/'+str(invoice_id))

def delete_invoice(request, invoice_id):
    invoice = Invoice.objects.get(pk=invoice_id)
    invoice_id = invoice.id
    invoice.delete()
    return HttpResponseRedirect('/products/invoices')

def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product_id = product.id
    product.delete()
    return HttpResponseRedirect('/products')

def dashboard(request):
    latest_invoice_list = Invoice.objects.all().order_by('-purchase_date')[:5]
    context = {'latest_invoice_list': latest_invoice_list}
    return render(request, 'product_app/dashboard.html', context)
