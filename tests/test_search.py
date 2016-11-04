from django.core.management import call_command
from haystack.forms import SearchForm

from saleor.product.models import Product
from saleor.search.utils import update_product


def test_update_product(index, product_in_stock):
    product_in_stock.name = 'Test 1'
    update_product(product_in_stock)
    call_command('rebuild_index', interactive=False)
    form = SearchForm(data={'q': ""}, load_all=True)
    assert form.is_valid()
    results = form.search()
    print(results)
    print(results.count())
    # print(results[0])
    assert results == []