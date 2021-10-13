#!/bin/python3
import pika
import sys
connection=pika.BlockingConnection(
pika.ConnectionParameters(
    host="10.144.124.131",
    port=5672,
    virtual_host="testHost",
    credentials=pika.PlainCredentials(
        username="test",
        password="test",
    ),
)
)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')


path = "/home/danny/Projects/dummy/dummy.txt"
file = open(path, "r")
exe = file.read()
file.close()





#try:
 #   inputNum = int(input(" input a number"))
#except Exception as e:

  #  print (e)
 #   exe = str(e)


#message = ' '.join(sys.argv[1:]) or "info: Hello World!"
message = exe
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close