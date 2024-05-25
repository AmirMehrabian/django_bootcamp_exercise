from models import Product, User

class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount
        print(f'we have {self.products.get(product) } of {product.name}')

    def remove_product(self, product, amount=1):
        num_items = self.products.get(product) 
        if num_items:
            if num_items < amount:
                raise Exception("Not Enough Products")
                
            elif num_items == amount:
                self.products.pop(product)

            else:
                self.products[product] -= amount
        print(f'we have {self.products.get(product) } of {product.name}')
        

    def add_user(self, username):
        new_user = User(username)
        print(f'number of users are {len(self.users)}')
        
        if len(self.users) == 0:
            self.users.append(new_user)
            return username
            
            
        match_list = list(filter(lambda x: x == new_user, self.users))
        if len(match_list) :
            return None

        
        self.users.append(new_user)
        return username

    
    def get_total_asset(self):
        return sum([ ii.price * self.products[ii]   for ii in self.products])
        

    def get_total_profit(self):
        total_profit = 0 
        for user in self.users:
           total_profit = total_profit + sum(list(map(lambda x: x.price, user.bought_products)))

        return total_profit


    def get_comments_by_user(self, user):
        all_comments= []
        for prod in self.products:
            for comment in prod.comments:
               # print(prod.name, comment.text, comment.user.username)
                if comment.user == user:
                    all_comments.append(comment.text)
        
        return all_comments

    
    def get_inflation_affected_product_names(self):
        inflated_products = set()
        for ii in self.products:
            count = 0
            for jj in self.products:
                
                if ii.name == jj.name:
                  
                  count += 1
                 
                  if count > 1 :
                     inflated_products.add(ii.name)
                
        return list(inflated_products)
    

    def clean_old_comments(self, date):
        
        for prod in self.products:

            new_comments = []
            for comment in prod.comments:
               # print(prod.name, comment.text, comment.user.username)
                if comment.date_added > date:
                    new_comments.append(comment)
            prod.comments = new_comments

    def get_comments_by_bought_users(self, product):
         
        
        comments_by_buyers = list()
       
                
        for comment in  product.comments:
         
            for bought_prod in comment.user.bought_products:
                if bought_prod.name == product.name:
                     comments_by_buyers.append(comment.text)
                
        return comments_by_buyers
