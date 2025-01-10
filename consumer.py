from pika import ConnectionParameters, BlockingConnection


connetc = ConnectionParameters(
    host="localhost",
    port=5672
) # подключение к брокеру сообщение


def callback(ch, method, properties, body):
    print(f"Получил сообщение: {body.decode()}")

def main():
    with BlockingConnection(connetc) as conn: #используем with для того чтобы все граматтно отключилось
        with conn.channel() as ch: # подключаемся к каналу
            ch.queue_declare(queue="messages") # создаеться очередь

            ch.basic_consume( # потребление сообщений
                queue="messages", #название нашего очереди
                on_message_callback=callback, # этот параметр отвечает за, когда получим сообщение оно будет вызываться
            )
            print("Жду сообщений")
            ch.start_consuming() # Запускаем, чтобы было постоянное потребление


if __name__=="__main__":
    main( )