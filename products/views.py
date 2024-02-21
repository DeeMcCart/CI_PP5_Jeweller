from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Cat6, Review, StockType
from .forms import ProductForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def all_products(request):
    """ This is the engine of searching, sorting and filtering """
    """ A view to show all products, including sorting and search queries """
    """ DMcC 14/02/24 Products with hide_display =True will not be returned"""

    products = Product.objects.all()
    products = products.filter(hide_display=False)
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        # sort by name/ category in order asc/desc
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # filter by category, e.g. ring, pendant, earrings
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # search using the wildcard search field
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                stringy = "You didn't enter any search criteria!"
                messages.error(request, stringy)
                return redirect(reverse('products'))
            query1 = Q(name__icontains=query)
            queries = query1 | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def maint_categories(request):
    """ This is a sysadmin view to show all products,
    and allow the sysadmin to edit/delete """
    print('In view maint_categories')
    categories = Category.objects.all()
    sources = Cat6.objects.all()
    source_lead_times = StockType.objects.all

    context = {
        'categories': categories,
        'sources': sources,
        'source_lead_times': source_lead_times,
    }

    return render(request, 'products/maint_categories.html', context)


def maint_products(request):
    """ This is a sysadmin view to show all products,
    and allow the sysadmin to edit/delete """
    print('In view maint_products')
    products = Product.objects.all()

    # sort by SKU in order asc/desc
    products = products.order_by('sku')
    context = {
        'products': products,
    }

    return render(request, 'products/maint_products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    num_reviews = 0
    avg_rating = 0

    # getting all reviews
    reviews = Review.objects.filter(product=product_id)
    if (reviews):
        # calculate average rating
        avg_rating = 0
        #    avg_rating = Avg('reviews__rating')

        product.rating = avg_rating
        num_reviews = reviews.count()

    context = {
        'product': product,
        'reviews': reviews,
        'num_reviews': num_reviews,
    }

    return render(request, 'products/product_detail.html', context)


# DMcC 09/02/24 Add @login_required decorator to ensure user logged in
# before executing the view (otherwise redirects them to login)
@login_required
def add_product(request):
    """ Sysadmin:  Add a product to the store """
    # If not a superuser kick user out of function
    if not request.user.is_superuser:
        messages.error(request, 'Restricted: Must have SysAdmin rights'
                       + ' to Add Products!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            stringy = f'Successfully added product SKU { product.sku },'
            + f'{ product.name }.'
            messages.success(request, stringy)

            # return redirect(reverse('add_product'))
            # go to the new product detail - sysadmin can check result
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product.'
                           + ' Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# DMcC 09/02/24 Add @login_required decorator to ensure user logged in
@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    # If not a superuser kick user out of function
    if not request.user.is_superuser:
        messages.error(request, 'Restricted: Must have SysAdmin rights '
                       + 'to edit Products!')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            stringy = f'Successfully updated SKU{product.sku }, {product.name}'
            messages.success(request, stringy)
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.'
                           + ' Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_confirm(request, product_id):
    """ Confirm the (admin) user definitely wishes to """
    """ Delete a product from the store """
    # If not a superuser kick user out of function
    if not request.user.is_superuser:
        messages.error(request, 'Restricted: Must have SysAdmin rights'
                       + ' to Delete Products!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    template = 'products/delete_confirm.html'
    context = {
        'product': product,
    }
    return render(request, template, context)


# DMcC 09/02/24 Add @login_required decorator to ensure user logged in
@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    # If not a superuser kick user out of function
    if not request.user.is_superuser:
        messages.error(request, 'Restricted: Must have SysAdmin rights'
                       + ' to Delete Products!')

        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Product { product.sku },'
                              + ' {product.name} deleted!')

    return redirect(reverse('products'))


@login_required
def review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        print(review_form)
        if review_form.is_valid():
            print(review_form)
            review_form.save()
            messages.success(request, 'Successfully reviewed product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                Please check the form data is correct')
    else:
        review_form = ReviewForm()
        print(review_form)

    template = 'shop/product_detail.html'
    context = {
        'review_form': review_form,
    }

    return render(request, template, context)
