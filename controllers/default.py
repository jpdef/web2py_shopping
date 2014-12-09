import datetime

@auth.requires_login()
def index():
    products = db().select(db.product.ALL)
    orders = db().select(db.orders.ALL)
    return dict(mess='Customer:  ' + auth.user.first_name,products=products,orders=orders,
      user_id= auth.user_id)

def get_price():
    rows = db(db.product).select() 
    for row in rows.find(lambda row: row.name==request.vars.choosen):
           return row.price
    
def add_item():
    vars = request.post_vars
    db.lineitems.insert(user_id=auth.user_id,
                      productname=vars.newitem,
                      quantity=vars.numitem,
                      totalprice=vars.totalprice,
                      order_id= vars.ordernum);
def add_order():
    now = datetime.datetime.today();
    order=db.orders.insert(time=now,user_id=auth.user_id);
    return order.id;

def complete_order():
    vars = request.post_vars
    db(db.orders.id == vars.ordernum).update(total=vars.ordertotal)
    order = db.orders(vars.ordernum)
    lineitems = db(db.lineitems).select()
    for lineitem in lineitems.find(lambda lineitem: lineitem.order_id==order.id):
        return order.time;
    return "fail"
def user():
    return dict(form=auth())
