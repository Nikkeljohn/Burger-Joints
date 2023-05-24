from django.test import TestCase
from django.test import TestCase
from .models import Contact, Category, Team, Dish, Profile, Order
from django.contrib.auth.models import User


class ModelTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_contact_model(self):
        contact = Contact.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            subject='Test Subject',
            message='Test Message'
        )
        self.assertEqual(contact.name, 'John Doe')
        self.assertEqual(contact.email, 'johndoe@example.com')
        self.assertEqual(contact.subject, 'Test Subject')
        self.assertEqual(contact.message, 'Test Message')

    def test_category_model(self):
        category = Category.objects.create(
            name='Test Category',
            description='Test Description'
        )
        self.assertEqual(category.name, 'Test Category')
        self.assertEqual(category.description, 'Test Description')

    def test_team_model(self):
        team = Team.objects.create(
            name='Test Team',
            designation='Test Designation'
        )
        self.assertEqual(team.name, 'Test Team')
        self.assertEqual(team.designation, 'Test Designation')

    def test_dish_model(self):
        category = Category.objects.create(
            name='Test Category',
            description='Test Description'
        )
        dish = Dish.objects.create(
            name='Test Dish',
            category=category,
            price=10.99
        )
        self.assertEqual(dish.name, 'Test Dish')
        self.assertEqual(dish.category, category)
        self.assertEqual(dish.price, 10.99)

    def test_profile_model(self):
        profile = Profile.objects.create(
            user=self.user,
            contact_number='1234567890',
            address='Test Address'
        )
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.contact_number, '1234567890')
        self.assertEqual(profile.address, 'Test Address')

    def test_order_model(self):
        category = Category.objects.create(
            name='Test Category',
            description='Test Description'
        )
        dish = Dish.objects.create(
            name='Test Dish',
            category=category,
            price=10.99
        )
        profile = Profile.objects.create(
            user=self.user,
            contact_number='1234567890',
            address='Test Address'
        )
        order = Order.objects.create(
            customer=profile,
            item=dish
        )
        self.assertEqual(order.customer, profile)
        self.assertEqual(order.item, dish)

