from django.test import TestCase
from .models import Item, Reviews, CartItems
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class ItemModelTest(TestCase):

    def setUp(self):
        item = Item()
        item.title = 'Potato'
        item.price = 25.00
        item.slug = "item_name"
        item.save()

        Item.objects.create(title='Onion', price=30.00, slug="vegetables-slug")

    def test_title_label(self):
        item = Item.objects.get(slug="item_name")
        print("Printing the item name here----------->", item)
        self.assertEqual(item.title.lower(), "Potato".lower())

    def test_item_exists(self):
        count = Item.objects.all().count()
        self.assertEqual(count, 2)

    def test_price_amount(self):
        item = Item.objects.get(slug="item_name")
        self.assertEqual(item.price, 250.00)

    def test_get_items_with_equal_price(self):
        count = Item.objects.filter(price=250.00).count()
        self.assertEqual(count, 2)

    def test_get_items_default_value(self):
        items = Item.objects.all()
        for item in items:
            self.assertEqual(item.pieces, 6)

    def test_get_absolute_url(self):
        url = reverse("main:dishes", kwargs={"slug": "item_name"})
        self.assertEqual("/dishes/item_name/", url)

    def test_get_add_to_cart_url(self):
        url = reverse("main:add-to-cart", kwargs={"slug": "item_name"})
        self.assertEqual("/add-to-cart/item_name/", url)

    def test_get_item_delete_url(self):
        url = reverse("main:item-delete", kwargs={"slug": "item_name"})
        self.assertEqual("/item-delete/item_name/", url)

    def test_get_update_item_url(self):
        return reverse("main:item-update", kwargs={"slug": "item_name"})
        self.assertEqual("/item-update/item_name/", url)


class TestReviewsModels(TestCase):
    def setUp(self):
        user = User()
        user.username = "admin"
        user.email = "admin111@gmail.com"
        user.is_member = True
        user.is_superuser = True
        user.set_password("123456")
        user.save()

        item = Item()
        item.title = 'Potato'
        item.price = 250.00
        item.slug = "item_name"
        item.save()

        add_reviews = Reviews()
        add_reviews.review = "Product is good"
        add_reviews.user = user
        add_reviews.item = item
        add_reviews.save()

    def test_review_exist(self):
        count_reviews = Reviews.objects.all().count()
        self.assertEqual(count_reviews, 1)


class TestCartItemsModels(TestCase):
    def setUp(self):
        user = User()
        user.username = "admin"
        user.email = "admin111@gmail.com"
        user.is_member = True
        user.is_superuser = True
        user.set_password("123456")
        user.save()

        item = Item()
        item.title = 'Onion'
        item.price = 250.00
        item.slug = "item_name"
        item.save()

        new_cart_item = CartItems()
        new_cart_item.status = "Active"
        new_cart_item.user = user
        new_cart_item.item = item
        new_cart_item.save()

    def test_cart_item_exist(self):
        count_cart_items = CartItems.objects.all().count()
        self.assertEqual(count_cart_items, 1)

    def test_get_remove_from_cart_url(self):
        url = reverse("main:remove-from-cart", kwargs={"pk": "1"})
        self.assertEqual("/remove-from-cart/1/", url)

    def test_update_status_url(self):
        url = reverse("main:update_status", kwargs={"pk": "0"})
        self.assertEqual("/update_status/0/", url)
