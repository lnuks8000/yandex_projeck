async def task2():
    while datetime.weekday() != 0 and str(datetime.now().strftime('%H:%M:%S')) != '04:00:00':
        pass
    bot.send_message(1370770852, 'начало плановой перестройки')
    try:
        os.rename("ned0", "ned")
        os.rename("ned1", "ned0")
        os.rename("ned", "ned1")
        for i in range(1, 8):
            u = open(f'ned1/{i}.txt', 'w')
            u.close()
        bot.send_message(1370770852, 'перенастройка прошла успешно!')
    except:
        bot.send_message(1370770852, 'ой, ой, что-то пошло не так')


async def main():
    await asyncio.gather(task2(), task2())

asyncio.run(main())