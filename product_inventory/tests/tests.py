import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from product_inventory.models import Product, Category, Enterprise
from datetime import time


@pytest.mark.django_db
def test_product_list_api_view():
    category = Category.objects.create(name='Test Category')
    enterprise = Enterprise.objects.create(
        name='Test Enterprise',
        description='Test Description',
        start_of_workday=time(hour=9, minute=0),  # Assuming start of workday is 9:00 AM
        end_of_workday=time(hour=17, minute=0),  # Assuming end of workday is 5:00 PM
        address='Test Address'
    )

    client = APIClient()

    product_1 = {
        'name': 'Test Product 1',
        'description': 'Test Description 1',
        'price': 10.50,
        'stock_quantity': 100,
        'category': category.id,
        'enterprise': enterprise.id
    }

    product_2 = {
        'name': 'Test Product 2',
        'description': 'Test Description 2',
        'price': 20.75,
        'stock_quantity': 200,
        'category': category.id,
        'enterprise': enterprise.id
    }

    response = client.post(reverse('create_product'), product_1, format='json')
    assert response.status_code == 201

    response = client.post(reverse('create_product'), product_2, format='json')
    assert response.status_code == 201

    response = client.get(reverse('product_list'))
    assert response.status_code == 200
    assert len(response.data) == 2

    # Access individual products from list
    assert response.data[0]['name'] == product_1['name']
    assert response.data[1]['name'] == product_2['name']


@pytest.mark.django_db
def test_create_product():
    # Create test data for category and enterprise
    category = Category.objects.create(name='Test Category')
    enterprise = Enterprise.objects.create(
        name='Test Enterprise',
        description='Test Description',
        start_of_workday=time(hour=9, minute=0),
        end_of_workday=time(hour=17, minute=0),
        address='Test Address'
    )

    # Creating products with invalid values
    invalid_product_1 = {
        'name': 'Invalid Product 1',
        'description': 'Test Description 1',
        'price': -10.50,
        'stock_quantity': 100,
        'category': category.id,
        'enterprise': enterprise.id
    }

    invalid_product_2 = {
        'name': 'Invalid Product 2',
        'description': 'Test Description 2',
        'price': 20.75,
        'stock_quantity': -200,
        'category': category.id,
        'enterprise': enterprise.id
    }

    client = APIClient()

    # Attempt to create products with invalid values
    response = client.post(reverse('create_product'), invalid_product_1, format='json')
    assert response.status_code == 400  # Expecting a Bad Request response
    assert 'non_field_errors' in response.data
    assert 'Price cannot be negative' in response.data['non_field_errors']

    response = client.post(reverse('create_product'), invalid_product_2, format='json')
    assert response.status_code == 400  # Expecting a Bad Request response
    assert 'non_field_errors' in response.data
    assert 'Stock quantity cannot be negative' in response.data['non_field_errors']

    # Create data for a new product
    new_product_data = {
        'name': 'New Test Product',
        'description': 'Test Description',
        'price': 10.50,
        'stock_quantity': 100,
        'category': category.id,
        'enterprise': enterprise.id
    }

    # Create a POST request to create a new product
    response = client.post(reverse('create_product'), new_product_data, format='json')
    assert response.status_code == 201  # Expecting a successful response


@pytest.mark.django_db
class TestProductUpdateDeleteAPIView:

    @pytest.fixture
    def sample_product(self):

        """Fixture to create a sample product."""
        # Create test data for category and enterprise
        category = Category.objects.create(name='Test Category')
        enterprise = Enterprise.objects.create(
            name='Test Enterprise',
            description='Test Description',
            start_of_workday=time(hour=9, minute=0),
            end_of_workday=time(hour=17, minute=0),
            address='Test Address'
        )

        return Product.objects.create(
            name='Sample Product',
            description='Sample Description',
            price=20.00,
            stock_quantity=50,
            category=category,
            enterprise=enterprise
        )

    def test_update_product(self, sample_product):
        # Define updated data for the product
        updated_data = {
            'name': 'Updated Product',
            'description': 'Updated Description',
            'price': '25.00',
            'stock_quantity': 75,
            'category': sample_product.category.id,
            'enterprise': sample_product.enterprise.id
        }

        client = APIClient()

        # Make a PUT request to update the product
        url = reverse('product', kwargs={'pk': sample_product.pk})
        response = client.put(url, updated_data, format='json')

        # Check if the product was updated successfully
        assert response.status_code == 200
        assert response.data['name'] == updated_data['name']
        assert response.data['description'] == updated_data['description']
        assert response.data['price'] == updated_data['price']
        assert response.data['stock_quantity'] == updated_data['stock_quantity']

    def test_delete_product(self, sample_product):
        # Make a DELETE request to delete the product
        client = APIClient()
        url = reverse('product', kwargs={'pk': sample_product.pk})
        response = client.delete(url)

        # Check if the product was deleted successfully
        assert response.status_code == 204
        assert not Product.objects.filter(pk=sample_product.pk).exists()


@pytest.mark.django_db
def test_enterprise_list_api_view():
    client = APIClient()

    enterprise_1 = {
        'name': 'Test Enterprise 1',
        'description': 'Test Description 1',
        'start_of_workday': '09:00',
        'end_of_workday': '18:00',
        'address': 'Test Address 1',
    }

    enterprise_2 = {
        'name': 'Test Enterprise 2',
        'description': 'Test Description 2',
        'start_of_workday': '10:00',
        'end_of_workday': '17:00',
        'address': 'Test Address 2',
    }

    response = client.post(reverse('create_enterprise'), enterprise_1, format='json')
    assert response.status_code == 201

    response = client.post(reverse('create_enterprise'), enterprise_2, format='json')
    assert response.status_code == 201

    response = client.get(reverse('enterprise_list'))
    assert response.status_code == 200
    assert len(response.data) == 2

    # Access individual enterprises from list
    assert response.data[0]['name'] == enterprise_1['name']
    assert response.data[1]['name'] == enterprise_2['name']


@pytest.mark.django_db
def test_create_enterprise():

    # Creating enterprises with invalid values
    invalid_enterprise_1 = {
        'name': '',
        'description': 'Test Description 1',
        'start_of_workday': '09:00',
        'end_of_workday': '18:00',
        'address': 'Test Address 1',
    }

    invalid_enterprise_2 = {
        'name': 'Test Name 1',
        'description': 'Test Description 1',
        'start_of_workday': '-09:00',
        'end_of_workday': '18:00',
        'address': 'Test Address 1',
    }

    client = APIClient()

    # Attempt to create enterprises with invalid values
    response = client.post(reverse('create_enterprise'), invalid_enterprise_1, format='json')
    assert response.status_code == 400
    assert 'name' in response.data
    assert 'This field may not be blank.' in response.data['name']

    response = client.post(reverse('create_enterprise'), invalid_enterprise_2, format='json')
    assert response.status_code == 400
    assert 'start_of_workday' in response.data
    assert ('Time has wrong format. Use one of these formats instead: hh:mm[:ss[.uuuuuu]].'
            in response.data['start_of_workday'])

    # Create data for a new enterprise
    new_enterprise_data = {
        'name': 'Test Name 1',
        'description': 'Test Description 1',
        'start_of_workday': '09:00',
        'end_of_workday': '18:00',
        'address': 'Test Address 1',
    }

    # Create a POST request to create a new enterprise
    response = client.post(reverse('create_enterprise'), new_enterprise_data, format='json')
    assert response.status_code == 201  # Expecting a successful response


@pytest.mark.django_db
class TestEnterpriseUpdateDeleteAPIView:
    @pytest.fixture
    def sample_enterprise(self):

        return Enterprise.objects.create(
            name='Sample Product',
            description='Sample Description',
            start_of_workday='11:00',
            end_of_workday='19:00',
            address='Test Address 1',
        )

    def test_update_enterprise(self, sample_enterprise):
        # Define updated data for the enterprise
        updated_data = {
            'name': 'Updated Product',
            'description': 'Updated Description',
            'start_of_workday': '10:00',
            'end_of_workday': '18:00',
            'address': 'Updated Address'
        }

        client = APIClient()

        # Make a PUT request to update the enterprise
        url = reverse('enterprise', kwargs={'pk': sample_enterprise.pk})
        response = client.put(url, updated_data, format='json')

        # Check if the enterprise was updated successfully
        assert response.status_code == 200
        assert response.data['name'] == updated_data['name']
        assert response.data['description'] == updated_data['description']
        assert response.data['start_of_workday'] == updated_data['start_of_workday']
        assert response.data['end_of_workday'] == updated_data['end_of_workday']
        assert response.data['address'] == updated_data['address']

    def test_delete_enterprise(self, sample_enterprise):
        # Make a DELETE request to delete the enterprise
        client = APIClient()
        url = reverse('enterprise', kwargs={'pk': sample_enterprise.pk})
        response = client.delete(url)

        # Check if the enterprise was deleted successfully
        assert response.status_code == 204
        assert not Product.objects.filter(pk=sample_enterprise.pk).exists()


@pytest.mark.django_db
def test_category_list_api_view():
    client = APIClient()

    category_1 = {
        'name': 'Test Category 1',
    }

    category_2 = {
        'name': 'Test Category 2',
    }

    response = client.post(reverse('create_category'), category_1, format='json')
    assert response.status_code == 201

    response = client.post(reverse('create_category'), category_2, format='json')
    assert response.status_code == 201

    response = client.get(reverse('category_list'))
    assert response.status_code == 200
    assert len(response.data) == 2

    # Access individual categories from list
    assert response.data[0]['name'] == category_1['name']
    assert response.data[1]['name'] == category_2['name']


@pytest.mark.django_db
def test_category():

    # Creating category with invalid values
    invalid_category = {
        'name': ''
    }

    client = APIClient()

    # Attempt to create category with invalid values
    response = client.post(reverse('create_category'), invalid_category, format='json')
    assert response.status_code == 400
    assert 'name' in response.data
    assert 'This field may not be blank.' in response.data['name']

    # Create data for a new category
    new_enterprise_data = {
        'name': 'Test Name',
    }

    # Create a POST request to create a new category
    response = client.post(reverse('create_category'), new_enterprise_data, format='json')
    assert response.status_code == 201  # Expecting a successful response


@pytest.mark.django_db
class TestCategoryUpdateDeleteAPIView:
    @pytest.fixture
    def sample_category(self):

        return Category.objects.create(
            name='Sample Product',
        )

    def test_update_category(self, sample_category):
        client = APIClient()

        updated_data = {
            'name': 'Updated Product',
        }

        # Make a PUT request to update the category
        url = reverse('category', kwargs={'pk': sample_category.pk})
        response = client.put(url, updated_data, format='json')

        # Check if the category was updated successfully
        assert response.status_code == 200
        assert response.data['name'] == updated_data['name']

    def test_delete_category(self, sample_category):
        # Make a DELETE request to delete the category
        client = APIClient()
        url = reverse('category', kwargs={'pk': sample_category.pk})
        response = client.delete(url)

        # Check if the category was deleted successfully
        assert response.status_code == 204
        assert not Product.objects.filter(pk=sample_category.pk).exists()
