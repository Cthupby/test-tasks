from django.db import models, Q
from django.http import JsonResponse


class Product(models.Model):
    categories = models.ManyToManyField(Category,
                                        related_name='products',
                                        blank=True, verbose_name=u"категории")
    related_products = models.ManyToManyField('Product',
                                              blank=True,
                                              verbose_name="связанные продукты")

    sku = models.CharField(u'артикул', max_length=128, validators=[validators.check_bad_symbols], unique=True)

    price = models.DecimalField(u'цена', max_digits=12, decimal_places=4)

    slug = models.SlugField(u'slug', max_length=80, db_index=True, unique=True)

    name = models.CharField(u'название', max_length=128)
    title = models.CharField(u'заголовок страницы (<title>)', max_length=256, blank=True)
    description = models.TextField(u'описание', blank=True)


def live_search(request):
    q = request.GET.get("q", "")
    ''' To store serialized query set '''
    serialized_query_set = []
    if q:
        ''' Finding model fields using the Q object '''
        query_set = Product.objects.filter(
            Q(sku__icontains=q) |
            Q(name__icontains=q) |
            Q(description__icontains=q)
        )
        ''' Iteration for serialized query set '''
        for query in query_set:
            serialized_query_set.append({
                "Sku": query.sku,
                "Name": query.name,
                "Description": query.description
            })
    else:
        empty_query = JsonResponse({'response': 'Not found'})
        return empty_query
    data = {
        'response': serialized_query_set
    }
    return JsonResponse(data)
