#!/usr/bin/python3
import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="**.***.***.***",
    port=5672,
    virtual_host="********",
    credentials=pika.PlainCredentials(
        username="****",
        password="****",
    ),
)
)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)


print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)
    #path = "/Projects/rabbitmqphp_example/testlog.txt"
    #sys.stdout = open(path, "a") as myfile:
        #myfile.write("hi")
    with open("testlog.txt", "a") as myfile:
        myfile.write(" [x] %r" % body + " \n")

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()