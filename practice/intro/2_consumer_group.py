from confluent_kafka import Consumer


# Настройка консьюмера
conf = {
    "bootstrap.servers": "localhost:9094",  # Адрес брокера Kafka
    "group.id": "consumer-group",           # Уникальный идентификатор группы
    "auto.offset.reset": "earliest",        # Начало чтения с самого начала
    "enable.auto.commit": False,             # Автоматический коммит смещений
    "session.timeout.ms": 6_000,            # Время ожидания активности от консьюмера
}
consumer = Consumer(conf)

consumer.subscribe(["test1"])

try:
    while True:
        msg = consumer.poll(0.1)

        if msg is None:
            continue
        if msg.error():
            print(f"Ошибка: {msg.error()}")
            continue

        key = msg.key().decode("utf-8")
        value = msg.value().decode("utf-8")
        print(
            f"Получено сообщение: {key=}, {value=}, "
            f"partition={msg.partition()}, offset={msg.offset()}"
        )
finally:
    consumer.close()
