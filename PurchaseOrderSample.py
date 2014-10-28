import btcchina

access_key = "<YOUR PAYMENT ACCESS KEY>"
secret_key = "<YOUR PAYMENT SECRET KEY>"
 
bc = btcchina.BTCChina(access_key, secret_key)
result = bc.create_purchase_order(0.5, "CNY", "<YOUR SERVER URL to PROCESS CALLBACK>","http://www.baidu.com","demo001","A notebook maybe","13500000001",0);
#result = bc.create_purchase_order(0.0004, "BTC", "http://<YOUR SERVER URL to PROCESS CALLBACK>","<RETURN URL>","demo002","A notebook maybe","13500000001",0);
print result

#result = bc.get_purchase_order(1)
#print result

#get the last 5 orders
#result = bc.get_purchase_orders(5) 
#print result
