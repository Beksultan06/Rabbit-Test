from pika import ConnectionParameters, BlockingConnection

connetc = ConnectionParameters(
    host="localhost",
    port=5672
) # подключение к брокеру сообщение

def main():
    with BlockingConnection(connetc) as conn: # используем with для того чтобы все граматтно отключилось
        with conn.channel() as ch: # подключаемся к каналу
            ch.queue_declare(queue="messages") # создаеться очередь

            ch.basic_publish(
                exchange="", # используем дефольный Exchange
                routing_key="messages", # он передает историю в messages
                body="Hello Rabbit!"
            ) # публикуем какое либо сообщение
            print("Сообшение отправлена")

if __name__=="__main__":
    main()

# В данный момент все сообщение храняться в RabbitMQ,
# и для того что бы отправить их в пользователя мы
# должны написать наш consumer.