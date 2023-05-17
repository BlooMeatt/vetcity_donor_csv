import csv
import os

# pyinstaller --onefile vcc_csv_parser.py --specpath EXE\ --distpath .\ --workpath EXE/build

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

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        # next(f)
        reader = csv.DictReader(f,delimiter=',')
        for line in reader:

            out_file = f'.\Output\Анкета_донора_{line["pet_name"]}_{line["name"]}.html'
            output = f'''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Анкета_донора_{line["pet_name"]}_{line["name"]}</title>
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
                                    <li>{line["name"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Адрес проживания</b>
                                <ul>
                                    <li>{line["address"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Номер телефона</b>
                                <ul>
                                    <li>{line["phone"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Email</b>
                                <ul>
                                    <li>{line["e-mail"]}</li>
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
                                    <li>{line["pet_name"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Возраст питомца на момент приобретения</b>
                                <ul>
                                    <li>{line["age_priobretenie"]}</li>
                                </ul>
                            </li>                            
                            <li>
                                <b>Вид (кошка/собака)</b>
                                <ul>
                                    <li>{line["pet_type"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Порода</b>
                                <ul>
                                    <li>{line["poroda"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Пол</b>
                                <ul>
                                    <li>{line["sex"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Возраст (полных лет)</b>
                                <ul>
                                    <li>{line["pet_age"]}</li>
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
                                    <li>{line["gemotransfusia"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Была ли кастрация / стерилизация?</b>
                                <ul>
                                    <li>{line["kastracia"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Если самка не стерилизована, были ли беременность / роды за последние 6 мес.?</b>
                                <ul>
                                    <li>{line["beremennost"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Была ли операция по удалению селезенки?</b>
                                <ul>
                                    <li>{line["splenektomia"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Было ли медикаментозное или хирургическое лечение за последне 6 месяцев?</b>
                                <ul>
                                    <li>{line["lechenie"]}</li>
                                    <li>{line["lechenie_utochnenie"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Диагностировано аутоиммунное гематологическое заболевание или новообразование?</b>
                                <ul>
                                    <li>{line["autoimmunnoe"]}</li>
                                    <li>{line["autoimmunnoe_utochnenie"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Есть ли хроническое заболевание, требующее постоянного лечения?</b>
                                <ul>
                                    <li>{line["hronicheskoe"]}</li>
                                    <li>{line["hronicheskoe_utochnenie"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Прием на постоянной основе медицинских препаратов или добавок</b>
                                <ul>
                                    <li>{line["preparati"]}</li>
                                    <li>{line["preparati_utochnenie"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Был ли контакт с животными, у которых подтверждено или подозревается инфекционное заболевание?</b>
                                <ul>
                                    <li>{line["infection_contact"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Выезд питомца за пределы региона проживания?</b>
                                <ul>
                                    <li>{line["vivoz_pitomca"]}</li>
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
                                    <li>{line["agressia_k_ludyam"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Агрессия к животным</b>
                                <ul>
                                    <li>{line["agressia_k_zhivotnim"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Наличие в рационе сырых продуктов</b>
                                <ul>
                                    <li>{line["siroe_v_racione"]}</li>
                                    <li>{line["siroe_utochnenie"]}</li>
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
                                    <li>Дата обработки: {line["vakcinacia"]}</li>
                                    <li>Дата следующей обработки: {line["vakcinacia_next_date"]}</li>
                                    <li>Препарат: {line["vakcina"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Дирофиляриоз</b>
                                <ul>
                                    <li>Дата обработки: {line["dirofilarioz_date"]}</li>
                                    <li>Дата следующей обработки: {line["diro_next_date"]}</li>
                                    <li>Препарат: {line["diro_preparat"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Эктопаразиты</b>
                                <ul>
                                    <li>Дата обработки: {line["ecto_date"]}</li>
                                    <li>Дата следующей обработки: {line["ecto_next_date"]}</li>
                                    <li>Препарат: {line["ecto_preparat"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Дегельминтизация</b>
                                <ul>
                                    <li>Дата обработки: {line["gelmint_date"]}</li>
                                    <li>Дата следующей обработки: {line["gelmint_next_date"]}</li>
                                    <li>Препарат: {line["gelmint_preparat"]}</li>
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
                                    <li>{line["soglasen_na_sedaciu"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Я даю согласие на выбривание шерсти в области яремной вены у питомца</b>
                                <ul>
                                    <li>{line["soglasen_na_vibrivanie"]}</li>
                                </ul>
                            </li>
                            <li>
                                <b>Я подтверждаю участие в донорской программе минимум на 2 года</b>
                                <ul>
                                    <li>{line["soglasen_na_2_goda"]}</li>
                                </ul>
                            </li>
                        </ol>
                    </ul>
                    <ul>
                        <li><b>Дата:</b> {line["sent"]}</li>
                    </ul>
                </body>
                </html>            
                '''
            with open(out_file,'w',encoding='utf-8') as of:
                of.write(output)
                of.close()
        f.close()
