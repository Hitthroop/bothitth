сData = {}

#инфа по специальностям
сData["ball_1"] = "Информация по направлению «Картография и геоинформатика»:\nПроходной балл: 189\nКоличество бюджетных мест: 26"
сData["ball_2"] = "Информация по направлению «Экология и природопользование»:\nПроходной балл: 203\nKоличество бюджетных мест: 23"
сData["ball_3"] = "Информация по направлению «Информационные системы и технологии»:\nПроходной балл: 202\nKоличество бюджетных мест: 67"
сData["ball_4"] = "Информация по направлению «Информационная безопасность»:\nПроходной балл: 190\nKоличество бюджетных мест: 39"
сData["ball_5"] = "Информация по направлению «Приборостроение»:\nПроходной балл: 162\nKоличество бюджетных мест: 16"
сData["ball_6"] = "Информация по направлению «Оптотехника»:\nПроходной балл: 148\nKоличество бюджетных мест: 16"
сData["ball_7"] = "Информация по направлению «Землеустройство и кадастры»:\nПроходной балл: 182\nKоличество бюджетных мест: 60"
сData["ball_8"] = "Информация по направлению «Геодезия и дистанционное зондирование»:\nПроходной балл: 164\nKоличество бюджетных мест: 69"
сData["ball_9"] = "Информация по направлению «Стандартизация и метрология»:\nПроходной балл: 147\nKоличество бюджетных мест: 18"
сData["ball_10"] = "Информация по направлению «Инноватика»:\nПроходной балл: 188\nKоличество бюджетных мест: 20"
сData["ball_11"] = "Информация по направлению «Прикладная геодезия»:\nПроходной балл: 184\nKоличество бюджетных мест: 31"
сData["ball_12"] = "Информация по направлению «Горное дело»:\nПроходной балл: 173\nKоличество бюджетных мест: 30"

def CallbackMsg(call, bot):
    try:
        if call.message:
            if сData[call.data]:
                bot.send_message(call.message.chat.id, сData[call.data])


            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Я не понимаю!")

    except Exception as e:
        print(repr(e))