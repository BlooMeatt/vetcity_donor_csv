import csv
import time
import os

# pyinstaller --onefile main.py --specpath EXE\ --distpath EXE/dist --workpath EXE/build

def folder_exists():
    path = '.\Output'
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        print('Создание папки для выходных файлов')


def csv_finder():
    dir_list = os.listdir()
    file_list = []
    for file in dir_list:
        if file.endswith(".csv"):
            file_list.append(file)
    print("Найдены следующие файлы csv:")
    for file in file_list:
        print(file)
    return file_list


folder_exists()
files = csv_finder()

# template =

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        next(f)
        reader = csv.reader(f, delimiter=',')
        raw_count: int = 0
        for line in reader:
            raw_count += 1
            out_file = f'.\Output\Анкета_донора_{line[4]}_{line[0]}.html'
            output = f'''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Анкета_донора_{line[4]}_{line[0]}</title>
                    <style>
                        p {{
                            font-size: 20px;
                            text-align: center;
                            font-weight: bold;
                        }}
                    </style>
                </head>
                <body>
                    <p>Данные владельца</p>
                    <ul class="group1">
                        <ol>
                            <li>
                                <b>ФИО</b>
                                <ul>
                                    <li>{line[0]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Адрес проживания</b>
                                <ul>
                                    <li>{line[1]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Номер телефона</b>
                                <ul>
                                    <li>{line[2]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Email</b>
                                <ul>
                                    <li>{line[3]}</li>
                                </ul>
                            </li>
                        </ol>
                    </ul>
                    <p>Данные питомца</p>
                    <ul class="group1">
                        <ol>
                            <li>
                                <b>Кличка питомца</b>
                                <ul>
                                    <li>{line[4]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Вид (кошка/собака)</b>
                                <ul>
                                    <li>{line[5]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Порода</b>
                                <ul>
                                    <li>{line[6]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Пол</b>
                                <ul>
                                    <li>{line[7]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Возраст (полных лет)</b>
                                <ul>
                                    <li>{line[8]}</li>
                                </ul>
                            </li>
                        </ol>
                    </ul>
                    <p>Анамнез</p>
                    <ul class="group1">
                        <ol>
                            <li>
                                <b>Переливали ли питомцу кровь ранее?</b>
                                <ul>
                                    <li>{line[9]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Была ли кастрация / стерилизация?</b>
                                <ul>
                                    <li>{line[10]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Если самка не стерилизована, были ли беременность / роды за последние 6 мес.?</b>
                                <ul>
                                    <li>{line[11]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Была ли операция по удалению селезенки?</b>
                                <ul>
                                    <li>{line[12]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Было ли медикаментозное или хирургическое лечение за последне 6 месяцев?</b>
                                <ul>
                                    <li>{line[13]}</li>
                                    <li>{line[14]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Диагностировано аутоиммунное гематологическое заболевание или новообразование?</b>
                                <ul>
                                    <li>{line[15]}</li>
                                    <li>{line[16]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Есть ли хроническое заболевание, требующее постоянного лечения?</b>
                                <ul>
                                    <li>{line[17]}</li>
                                    <li>{line[18]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Прием на постоянной основе медицинских препаратов или добавок</b>
                                <ul>
                                    <li>{line[19]}</li>
                                    <li>{line[20]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Был ли контакт с животными, у которых подтверждено или подозревается инфекционное заболевание?</b>
                                <ul>
                                    <li>{line[21]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Выезд питомца за пределы региона проживания?</b>
                                <ul>
                                    <li>{line[22]}</li>
                                </ul>
                            </li>
                        </ol>
                    </ul>
                    <p>Поведение и привычки</p>
                    <ul class="group1">
                        <ol>
                            <li>
                                <b>Агрессия к людям</b>
                                <ul>
                                    <li>{line[23]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Агрессия к животным</b>
                                <ul>
                                    <li>{line[24]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Наличие в рационе сырых продуктов</b>
                                <ul>
                                    <li>{line[25]}</li>
                                    <li>{line[26]}</li>
                                </ul>
                            </li>
                        </ol>
                    </ul>
                    <p>Вакцинация и обработка</p>
                    <ul class="group1">
                        <ol>
                            <li>
                                <b>Ежегодная комплексная вакцинация</b>
                                <ul>
                                    <li>Дата обработки: {line[27]}</li>
                                    <li>Дата следующей обработки: {line[28]}</li>
                                    <li>Препарат: {line[29]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Дирофиляриоз</b>
                                <ul>
                                    <li>Дата обработки: {line[30]}</li>
                                    <li>Дата следующей обработки: {line[31]}</li>
                                    <li>Препарат: {line[32]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Эктопаразиты</b>
                                <ul>
                                    <li>Дата обработки: {line[33]}</li>
                                    <li>Дата следующей обработки: {line[34]}</li>
                                    <li>Препарат: {line[35]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Дегельминтизация</b>
                                <ul>
                                    <li>Дата обработки: {line[36]}</li>
                                    <li>Дата следующей обработки: {line[37]}</li>
                                    <li>Препарат: {line[38]}</li>
                                </ul>
                            </li>
                        </ol>
                    </ul>
                    <p>Согласие</p>
                    <ul class="group1">
                        <ol>
                            <li>
                                <b>Я даю согласие на седацию / анестезию</b>
                                <ul>
                                    <li>{line[39]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Я даю согласие на выбривание шерсти в области яремной вены у питомца</b>
                                <ul>
                                    <li>{line[40]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Я подтверждаю участие в донорской программе минимум на 2 года</b>
                                <ul>
                                    <li>{line[41]}</li>
                                </ul>
                            </li>
                        </ol>
                    </ul>
                </body>
                </html>            
                '''
            with open(out_file,'w',encoding='utf-8') as of:
                of.write(output)
                of.close()
        f.close()
