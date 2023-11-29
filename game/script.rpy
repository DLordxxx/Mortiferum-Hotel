# Определение персонажей игры

define gg = Character('???', color="#5a11ad") #фиол


define ch = Character('Чревоугодие', color="#FF6600") #оранж


define le = Character('Лень', color="#00bfff") #голуб


define jad = Character('Жадность', color="#ccff00") #шартрез


define pox = Character('Похоть', color="#c4149b") #роза


define gn = Character('Гнев', color="#bf0d0d") #крас


define gor = Character('Гордыня', color="#FEb7F0") #цвет испуганой нимфы+b


define zav = Character('Зависть', color="#5353ec") #лазурь
define dvor = Character('Дворецкий', color="#5353ec")

#Запоминающие действия
define beryshi = False
define snova = False
define vajno1 = False

# Музыка и звуки
define audio.glazaout = "music/glazaout.ogg"
define audio.sbil = "sound/sbil.ogg"
define audio.fon = "music/fon.mp3"
define audio.doroga = "music/doroga.mp3"
define audio.fon2 = "music/fon2.mp3"

# Задаётся изначальная позиция персонажей
init:
    $ left = Position(xalign=0.2)
    $ right = Position(xalign=0.75)
init-1:
    $ menu_timer_onoff=False

# Заставка
label splashscreen:
    screen black
    scene zastavka with fade
    pause(2)
    scene black with fade
    pause(0.5)
    scene zastavka2 with fade
    pause(2)
    scene black with fade
    return

# Игра начинается здесь:
label start:

# ЗНАКОМСТВО
    stop music fadeout 1
    scene bg lift
    with fade
    play music fon
    dvor '''
    Приветствую вас в нашем отеле «Peccatum Mortale»!

    Мы рады каждому гостю, ведь именно он подарит незабываемые эмоции, которые вы запомните навсегда!

    Какой этаж желаете?
    '''
#здесь нужен силует гг

    gg '''
    Что простите?

    Куда я попал?
    '''
#пропадает гг - говорит двор

    dvor '''
    Ох, так вы один из новых постояльцев?

    Позвольте мне немного вас просветить. Этот отель по своей сути необычный – люди, прибывшие сюда могут очиститься как физически, так и духовно
    '''
    stop music fadeout 1
#(гудок от фуры) (флешка)
    play music glazaout
    scene black with off
    pause 1.0
    scene bg machine with onn
    stop music fadeout 3

    play music doroga

    '''
    Всплывают резкие воспоминания…

    Яркий свет фар и громкий шум от гудка надвигающейся фуры, которую уже ничто не остановит.
    '''
    stop music fadeout 1
    play sound sbil
    '''
    Удар.

    Слышно лишь тёплую кровь, капающую на белоснежную дорогу.
    '''
#затемнение-кружок
    play music glazaout
    scene black with off
    pause 1.0
    scene bg lift with onn
    stop music fadeout 3
    play music fon
    dvor '''
    Советую посетить первый этаж, там можно отведать вкуснейшие блюда.

    Думаю, и вы найдёте что-нибудь себе по вкусу, заранее желаю приятного аппетита!
    '''
    gg "Спасибо… *в недоумении*"

    '''Лифт поднимается с цокольного на первый'''

# РЕЦЕПЦИЯ
    stop music fadeout 1
    scene bg recheznia
    with fade
    play music fon2

    gg '''
    Здесь кто-нибудь есть?

    Хм, а что это?
    '''
    "*Найден листочек*"
    menu:
        gg "Занятно…"

        "Взять":
            #Сцена с листочек-чек (порядок блюд)
            scene bg chek
            with fade
            gg "Интересно, к чему бы это?"
            scene black
            with fade
            "Взяв листочек, он направился в ресторан"

        "Оставить":
            scene black
            with fade
            "Оставив листочек, он направился в ресторан"

#первый этаж, ЧРЕВОУГОДИЕ
    stop music fadeout 1
    scene bg restaurant
    with fade

    ch '''
    Не желаете ли что-нибудь отведать?
    '''

label restaurant:
    #ВЫБРАТЬ ПРАВИЛЬНЫЙ ПОРЯДОК (2413)=(ГРЕХ)
    menu:
        ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

        #ПОРЯДОК "Е"
        "Ежевичный чизкейк":
            menu:
                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                #ПОРЯДОК "ЕГ"
                "Гребешки в сливочном соусе":
                    menu:
                        ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ЕГХ"
                        "Хинкали с шампиньонами":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ЕГХР"
                                "Ризотто с песто":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "ЕГР"
                        "Ризотто с песто":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ЕГРХ"
                                "Хинкали с шампиньонами":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant
                #ПОРЯДОК "ЕХ"
                "Хинкали с шампиньонами":
                    menu:
                        ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ЕХГ"
                        "Гребешки в сливочном соусе":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ЕХГР"
                                "Ризотто с песто":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant
                        #ПОРЯДОК "ЕХР"
                        "Ризотто с песто":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ЕХРГ"
                                "Гребешки в сливочном соусе":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant
                #ПОРЯДОК "ЕР"
                "Ризотто с песто":
                    menu:
                        ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ЕРГ"
                        "Гребешки в сливочном соусе":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ЕРГX"
                                "Хинкали с шампиньонами":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "ЕРХ"
                        "Хинкали с шампиньонами":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ЕРХГ"
                                "Гребешки в сливочном соусе":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

        #ПОРЯДОК "Г"
        "Гребешки в сливочном соусе":
            menu:
                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                #ПОРЯДОК "ГЕ"
                "Ежевичный чизкейк":
                    menu:
                        ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ГЕХ"
                        "Хинкали с шампиньонами":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ГЕХР"
                                "Ризотто с песто":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "ГЕР"
                        "Ризотто с песто":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ГЕРХ"
                                "Хинкали с шампиньонами":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                #ПОРЯДОК "ГХ"
                "Хинкали с шампиньонами":
                    menu:
                        ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ГХЕ"
                        "Ежевичный чизкейк":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                "Ризотто с песто":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "ГХР"
                        "Ризотто с песто":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ГХРЕ"
                                "Ежевичный чизкейк":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                #ПОРЯДОК "ГР"
                "Ризотто с песто":
                    menu:
                        ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ГРЕ"
                        "Ежевичный чизкейк":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ГРЕХ"
                                "Хинкали с шампиньонами":
                                    ch "Надеюсь вам понравились наши блюда и вы вернетесь к нам еще раз!"
                                    jump skip1

                        #ПОРЯДОК "ГРХ"
                        "Хинкали с шампиньонами":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ГРХЕ"
                                "Ежевичный чизкейк":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

        #ПОРЯДОК "Х"
        "Хинкали с шампиньонами":
            menu:
                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                #ПОРЯДОК "ХЕ"
                "Ежевичный чизкейк":
                    menu:
                        ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ХЕГ"
                        "Гребешки в сливочном соусе":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ХЕГР"
                                "Ризотто с песто":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "ХЕР"
                        "Ризотто с песто":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ХЕРГ"
                                "Гребешки в сливочном соусе":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                #ПОРЯДОК "ХГ"
                "Гребешки в сливочном соусе":
                    menu:
                        ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ХГЕ"
                        "Ежевичный чизкейк":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                "Ризотто с песто":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "ХГР"
                        "Ризотто с песто":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ХГРЕ"
                                "Ежевичный чизкейк":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                #ПОРЯДОК "ХР"
                "Ризотто с песто":
                    menu:
                        ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "ХРЕ"
                        "Ежевичный чизкейк":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ХРЕГ"
                                "Гребешки в сливочном соусе":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "ХРГ"
                        "Гребешки в сливочном соусе":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "ХРГЕ"
                                "Ежевичный чизкейк":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

        #ПОРЯДОК "Р"
        "Ризотто с песто":
            menu:
                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                #ПОРЯДОК "РЕ"
                "Ежевичный чизкейк":
                    menu:
                        ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "РЕГ"
                        "Гребешки в сливочном соусе":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "РЕГХ"
                                "Хинкали с шампиньонами":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "РЕХ"
                        "Хинкали с шампиньонами":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "РЕХГ"
                                "Гребешки в сливочном соусе":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                #ПОРЯДОК "РГ"
                "Гребешки в сливочном соусе":
                    menu:
                        ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "РГЕ"
                        "Ежевичный чизкейк":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "РГЕХ"
                                "Хинкали с шампиньонами":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "РГХ"
                        "Хинкали с шампиньонами":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "РГХЕ"
                                "Ежевичный чизкейк":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                #ПОРЯДОК "РХ"
                "Хинкали с шампиньонами":
                    menu:
                        ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                        #ПОРЯДОК "РХЕ"
                        "Ежевичный чизкейк":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "РХЕГ"
                                "Гребешки в сливочном соусе":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

                        #ПОРЯДОК "РХГ"
                        "Гребешки в сливочном соусе":
                            menu:
                                ch "Нашим поварам под силу приготовить любое блюдо, которое вы пожелаете"

                                #ПОРЯДОК "РХГЕ"
                                "Ежевичный чизкейк":
                                    ch "Вы уверены, что съедите все?"
                                    jump restaurant

#ЛИФТ-РАЗГОВОРЫ
label skip1:
    scene black
    with fade
    "Возвращается к лифту"

    if snova:
        scene bg lenb
        with fade
        le "Снова вы? Ну как, выспались?"
        jump yshel

    play music fon
    scene bg lift
    with fade
    gg "Тот молодой господин, в ресторане, был несколько странным. Вы знакомы с ним?"
    dvor '''
    Вряд ли. *небольшая улыбка на лице*

    Желаете продолжить обзор нашего отеля?
    '''
    gg '''
    Чертовщина какая-то.

    Мне надо поскорее отсюда выбраться... *шепотом*
    '''
    scene black
    with fade
    "Лифт поднимается на второй этаж"

#второй этаж, ЛЕНЬ
label lenb:
    stop music fadeout 1
    scene bg lenb
    with fade
    '''
    Фойе представляет собой небольшое пространство с тусклым светом, который едва ли освещает дюжину картин на стене.

    Чуть ниже красовались оливковые диванчики и, судя по их виду, простояли они здесь больше века.

    На одном из них расположился джентльмен, не отводящий взгляда от вычурных произведений искусства.
    '''
    le "Неужели вам хочется бегать, словно тушканчик, по этажам?"
    gg "Что вы имеете в виду?"
    le '''
    Чуточку отдыха никому не помешает.

    Я сижу здесь порядка двух сотен лет, избегая всякую суету.

    Вы в самом деле думаете, что я несчастен?
    '''
    '''Мужчина откидывается назад, отчего пролежни дивана под ним становятся гораздо заметнее.'''
    gg "Прошу прощения, но мне пора идти, я хочу осмотреть все этажи отеля."
    le "Бросьте, милостивый. Разве вам здесь не нравится?"
    menu:
        le "Вечное спокойствие, тишина, не надо никуда лишний раз бегать…"

        "Попытаться уйти":
            jump skip2

        "Остаться":
            jump skip2

#ИЛЛЮЗИЯ ВЫБОРА
label skip2:
    le "Вы не понимаете, что теряете!"
    '''Лицо мужчины вмиг стало мрачным

    Его слабые и дрожащие руки едва ли могли меня удержать, но я все равно не способен был сделать и шага в сторону лифта.
    '''
    gg "Пустите!"
    le "Таких удобств вам более нигде не отыскать, поверьте на слово!"
    menu:
        gg "Не смейте меня задерживать! Я не собираюсь здесь больше оставаться!"

        "Попытаться уйти":
            jump yshel

        "Не сопротивляться":
            jump ostalsa

#НЕ ПОДДАЛСЯ РЕЧАМ ЛЕНИ
label yshel:
    le "*вздох* Смею предположить, что вам претит моя компания."
    gg "..."
    le '''
    В любом случае мне было приятно с вами повстречаться.

    Примите небольшой презент в знак признательности за наше мимолетное знакомство.
    '''
    "Мужчина протянул небольшую коробочку."
    gg "Что там?"
    le "В отеле всегда царит шум, но на моем этаже целыми сутками тишина, потому возьми с собой эти беруши. Уверен, позже они тебе понадобятся."
    gg "Вы крайне добры."

    #ЗАПОМИНАЮЩЕЕ ДЕЙСТВИЕ
    $ beryshi = True
    jump skip3

#Решил полежать
label ostalsa:
    gg "И вправду, думаю, отдых мне не помешает"
    scene black
    with fade
    gg "Кажется, где-то это я уже слышал"

    #ЗАПОМИНАЮЩЕЕ ДЕЙСТВИЕ
    $ snova = True
    scene bg restaurant
    with fade
    jump restaurant

#ЛИФТ-РАЗГОВОРЫ
label skip3:
    scene bg lift
    with fade
    play music fon
    dvor "Ох, вы уже здесь… Не захотелось составить компанию нашему замечательному постояльцу со второго этажа? "
    gg "Нет, он несколько странный."
    dvor "Вероятно, вы правы. *хмурится*"
    gg "Будьте любезны, на третий."
    dvor "Как вам будет угодно."

#третий этаж, ЖАДНОСТЬ

label jadnostb:
    stop music fadeout 1
    scene bg test
    with fade
    '''Громкая музыка из дальнего проигрывателя сильно бьет по ушам

    Над ним склонился мужчина, отчаянно пытаясь починить его, но, кажется, все безнадежно
    '''
    gg "Здравс…"
    jad "Черт побери, заткнись! Я не спал уже восемь ночей!"
    gg "Я подумал вам нужна помощь..."
    jad "Себе помоги, мальчонка!"
    gg "Почему вы мне грубите? Я ведь к вам с добрыми намерениями"
    jad "Ну и с чем ты мне поможешь?"
    # Развилка
    menu:
        "*достает беруши*"

        "Отдать":
            jump otdal

        "Оставить себе":
            jump sebe

label otdal:
    gg "Кажется, они вам нужнее"
    jad "Почему делишься со мной столь “дорогой” вещью?"
    gg "Мне по нраву шумные места"
    $ vajno1 = True

    jump skip4

label sebe:
    "*замечает молоток*"
    gg "Кажется, у меня есть решение"
    "*начинает замахиваться*"
    # звук поломки
    "*хрусь*"
    jad "Хм, интересно, почему я раньше до этого не догадался"
    jump skip4

label skip4:
    jad "Спасибо тебе, теперь я наконец-то смогу проводить свое время в тишине и спокойствии у себя в логове"

    scene bg lift
    with fade
    play music fon
    gg "Так приятно вновь оказаться в тишине."
    dvor "Безусловно, мы ведь стараемся обеспечить комфорт каждому гостю."
    "*свет становится явно тусклее*"
    gg "Вам еще есть над чем поработать."
    "*нажимает на кнопку четвертого этажа*"

#четвертый этаж, ПОХОТЬ

label pohotb:
    stop music fadeout 1
    scene bg pohot
    with fade
    "*комната усыпана свечами и лепестками роз на полу*"
    gg '''Романтично…

    Интересно, для кого такая атмосфера сделана?
    '''
    pox '''Давненько я не встречала настолько обворожительных джентльменов в отеле.

    Вы здесь недавно?
    '''
    "*на лице девушки кроткая улыбка*"
    gg "Приятно слышать *смущенно*"
    pox "Присаживайся ко мне на диванчик, красавчик"
    "*присел на край дивана*"
#БЕЗ РАЗЛИВОК
    menu:
        pox "Вам понравился мой прием?"

        "Сказать правду":
            jump true

        "Солгать":
            jump false

#СКАЗАЛ ПРАВДУ
label true:
    gg '''Да…

    Но к чему такое большое внимание ко мне?
    '''
    pox "Что вы, не льстите себе"
    jump dialog1

#СКАЗАЛ ЛОЖЬ
label false:
    gg "Нет, мне не нравится ваша навязчивость"
    pox "Значит мне нужно узнать тебя поближе…"
    jump dialog1

label dialog1:
    "*девушка подсела ближе и нежно опустила руку на колено*"
    menu:
        pox "У такого мужчины как вы, должно быть, есть девушка?"

        "Да":
            gg "Поэтому мне не нужно долго задерживаться, иначе она будет переживать за меня"
            pox "Если ты “задержишься”, то у нас будет больше времени, чтобы раскрыть наши отношения"
            gg "Наши?"
            "*проскользнула ухмылка на ее лице*"
            pox '''Разве тебе не хочется жить в большом доме с личным дворецким

            Будешь наслаждаться жизнью припеваючи: в достатке, тепле, уюте и окутанный любовью
            '''
            jump dialog2

        "Нет":
            jump dialog2

label dialog2:
    gg "Я не совсем понимаю, к чему вы клоните"
    pox "Как вы смотрите на то, чтобы провести незабываемый вечер в компании юной дамы"
    gg "..."
# label test:
#     "бла бла"
#     if beryshi:
#         "Один предмет есть"
#     else:
#         "Пропустил LOL"




# Объявляется таймер
#     $ timez = 100
#     $ time_range = 100
#     $ marker = "no_choice"
#     $ menu_timer_onoff=True
#
#     menu:
#         ch "Выбор?"
#
#         "1":
#             "Вы выбрали первый вариант"
#
#             jump final1
#         "2":
#             "Вы выбрали второй вариант"
#
#             jump final2
#
# label final1:
#     gg "Поздравляю, вы открыли первую концовку!"
#
#     jump start
#
# label final2:
#     gg "Поздравляю, вы открыли вторую концовку!"
#
#     return
#
# label no_choice:
#     "Неудача"

    return
