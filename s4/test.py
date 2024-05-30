import unittest

from models import User, Product, Comment
from store import Store
from datetime import datetime, timedelta


class TestAll(unittest.TestCase):
    def setUp(self):
        self.store1 = Store()

        self.user1 = User("ali")
        self.user2 = User("reza")

        self.product1 = Product("iphone_S15", 800, "mobile")
        self.product2 = Product("hp_elite", 1500, "laptop")

        self.comment1 = Comment("your iphone was bad", self.user1)
        self.comment2 = Comment("your hp was good", self.user1)
        self.comment3 = Comment("The iphone is cheap", self.user2)

        self.product1.add_review(self.comment1)
        self.product2.add_review(self.comment2)
        self.product1.add_review(self.comment3)

        self.store1.add_product(self.product1, 10)
        self.store1.add_product(self.product2, 2)

        self.store1.users.append(self.user1)
        self.store1.users.append(self.user2)

        self.total_asset = 10 * 800 + 2 * 1500

    def test_remove_product_correct_number_of_removing(self):
        # test1 the correctness of removing number of items
        self.store1.remove_product(self.product1, 5)
        result = self.store1.products[self.product1]
        self.assertEqual(result, 5)

    def test_remove_product_for_negative_amount(self):
        # test2 removing more than existing amount
        self.assertRaises(Exception, self.store1.remove_product, self.product1, 20)

    def test_remove_product_exception_message(self):
        # test3 checks the output message of raised exception
        try:
            self.store1.remove_product(self.product1, 20)
        except Exception as e:
            self.assertEqual(str(e), "Not Enough Products")

    def test_remove_product_calling_unavailabel_product(self):
        # test4 checks if unavailable product is searched
        self.store1.remove_product(self.product1, 10)
        self.assertRaises(KeyError, lambda x: self.store1.products[x], self.product1)

    def test_add_user_check_the_returned_name(self):
        # test 5 checks the output of the add_user method
        name = "NewUser1"
        result = self.store1.add_user(name)
        self.assertEqual(result, name)

    def test_add_user_check_the_returned_name_if_user_already_exists(self):
        # test 6 checks if add_user method returns None if the user already exists
        self.store1.add_user("NewUser1")
        self.assertIsNone(self.store1.add_user("NewUser1"))

    def test_get_total_asset(self):
        # test 7 checks if the correct number is returned by get_total_asset_method
        self.assertEqual(self.store1.get_total_asset(), self.total_asset)

    def test_get_total_profit(self):
        # test 8 checks that the method return a corrrect value for the two sold products costing 2300
        self.store1.sell_product(self.user1, self.product1)
        self.store1.sell_product(self.user2, self.product2)
        total_profit = 800 + 1500
        self.assertEqual(self.store1.get_total_profit(), total_profit)

    def test_get_comments_by_user(self):
        # test 9 checks that a correct list of comment is returend by the method
        resultlist = set(self.store1.get_comments_by_user(self.user1))
        expected_output = set([self.comment1.text, self.comment2.text])
        self.assertEqual(resultlist, expected_output)

    def test_get_inflation_affected_product_names(self):
        # test 10 checks that if the method correctly returns a list after inflation and before inflation
        self.assertEqual(self.store1.get_inflation_affected_product_names(), [])
        self.store1.add_product(Product("iphone_S15", 500, "mobile"))
        self.assertEqual(
            self.store1.get_inflation_affected_product_names(), ["iphone_S15"]
        )

    def test_clean_old_comments(self):
        # test 11 checks that comments are kept and deleted by method correctly
        old_comments = self.store1.get_comments_by_user(self.user1)
        old_time = datetime(2020, 1, 1)
        self.store1.clean_old_comments(old_time)
        self.assertEqual(self.store1.get_comments_by_user(self.user1), old_comments)

        new_time = datetime.now() + timedelta(minutes=10)
        self.store1.clean_old_comments(new_time)
        self.assertEqual(self.store1.get_comments_by_user(self.user1), [])

    def test_get_comments_by_bought_users(self):
        # test 12 checks that correct comments are returned by the method before and after
        # selling a item
        expected_result = self.store1.get_comments_by_user(self.user2)
        result_befor_buying = self.store1.get_comments_by_bought_users(self.product1)
        self.assertEqual(result_befor_buying, [])

        self.store1.sell_product(self.user2, self.product1)
        result_after_buying = self.store1.get_comments_by_bought_users(self.product1)
        self.assertEqual(result_after_buying, expected_result)


if __name__ == "__main__":
    unittest.main()
