from models import User


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()
        self.total_profit = 0

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        try:
            if self.products[product] < amount:
                raise Exception("Not Enough Products")
            self.products[product] -= amount
            if self.products[product] == 0:
                self.products.pop(product)
        except KeyError:
            raise Exception("Not Enough Products")

    def does_username_exist(self, username):
        for user in self.users:
            if user.username == username:
                return True
        return False

    def add_user(self, username):
        if not self.does_username_exist(username):
            self.users.append(User(username))
            return username
        else:
            return None

    def get_total_asset(self):
        asset = 0
        for product, amount in self.products.items():
            asset += product.price * amount
        return asset

    def get_total_profit(self):
        return self.total_profit

    def sell_product(self, user, product, quantity=1):
        if product in self.products and self.products[product] >= quantity:
            self.remove_product(product, quantity)
            self.total_profit += product.price * quantity
            user.bought_products.extend([product] * quantity)
            return True
        else:
            return False

    def get_comments_by_user(self, user):
        comments = []
        for product in self.products.keys():
            for comment in product.comments:
                if comment.user == user:
                    comments.append(comment.text)
        return comments

    def _is_inflation_affected(self, product):
        for product_ in self.products.keys():
            if product_.price < product.price:
                return True
        return False

    def get_inflation_affected_product_names(self):
        changed_price = {}
        ret = set()
        for x in self.products:
            if x.name in changed_price and x.price != changed_price[x.name]:
                ret.add(x.name)
            changed_price[x.name] = x.price
        return list(ret)

    def clean_old_comments(self, date):
        for product in self.products.keys():
            for comment in reversed(product.comments):
                if comment.date_added < date:
                    product.comments.remove(comment)

    def get_comments_by_bought_users(self, product):
        comments = []
        for comment in product.comments:
            if product in comment.user.bought_products:
                comments.append(comment.text)
        return comments
