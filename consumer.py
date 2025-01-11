from pika import ConnectionParameters, BlockingConnection

connetc = ConnectionParameters(
    host="localhost",
    port=5672
) # подключение к брокеру сообщение

def callback(ch, method, properties, body):
    print(f"Получил сообщение: {body.decode()}")
    try:
        x = 1/0   #если ошибка не критично можно сказать кролику чтобы он продолжил обрабатывать сообщение,
        # если же ошибка серезьное то нужно фиксить ошибку, в данном случай ошибка простая и я его обрабатываю с помощью
        # исключени
    except:
        pass

    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    with BlockingConnection(connetc) as conn: #используем with для того чтобы все граматтно отключилось
        with conn.channel() as ch: # подключаемся к каналу
            ch.queue_declare(queue="messages") # создаеться очередь

            ch.basic_consume( # потребление сообщений
                queue="messages", #название нашего очереди
                on_message_callback=callback, # этот параметр отвечает за, когда получим сообщение оно будет вызываться
                # auto_ack=True, # 1)способ: говорим кролику что мы получило сообщение, кролик удалить сообщение
                # этот плохой метод для обработкив сообщений
            )
            print("Жду сообщений")
            ch.start_consuming() # Запускаем, чтобы было постоянное потребление


if __name__=="__main__":
    main( )