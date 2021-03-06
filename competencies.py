from rutermextract import TermExtractor

_in = """ПК-1 ^ способность демонстрации общенаучных базовых знаний естественных наук, математики иинформатики, понимание основных фактов, концепций, принципов теорий, связанных с прикладной математикой и информатикой 
ПК-2 ^ способность приобретать новые научные и профессиональные знания, используя современные образовательные и информационные технологии 
ПК-3 ^ способность понимать и применять в исследовательской и прикладной деятельности современный математический аппарат 
ПК-4 ^ способность в составе научно-исследовательского и производственного коллектива решать задачи профессиональной деятельности 
ПК-5 ^ способность критически переосмысливать накопленный опыт, изменять при необходимости вид и характер своей профессиональной деятельности 
ПК-6 ^ способность осуществлять целенаправленный поиск информации о новейших научных и технологических достижениях в сети Интернет и из других источников 
ПК-7 ^ способность собирать, обрабатывать и интерпретировать данные современных научных исследований, необходимые для формирования выводов по соответствующим научным, профессиональным, социальным и этическим проблемам 
ПК-8 ^ способность формировать суждения о значении и последствиях своей профессиональной деятельности с учетом социальных, профессиональных и этических позиций 
ПК-9 ^ способность решать задачи производственной и технологической деятельности на профессиональном уровне, включая: разработку алгоритмических и программных решений в области системного и прикладного программирования 
ПК-10 ^ способность применять в профессиональной деятельности современные языки программирования и языки баз данных, операционные системы, электронные библиотеки и пакеты программ, сетевые технологии 
ПК-11 ^ способность приобретать и использовать организационно-управленческие навыки в профессиональной и социальной деятельности 
ПК-12 ^ способность составлять и контролировать план выполняемой работы, планировать необходимые для выполнения работы ресурсы, оценивать результаты собственной работы 
ПК-13 ^ способность использовать основы защиты производственного персонала и населения от возможных последствий аварий, катастроф, стихийных бедствий и применения современных средств поражения, основных мер по ликвидации их последствий, способность к общей оценке условий безопасности жизнедеятельности 
ПК-14 ^ способность владеть методикой преподавания учебных дисциплин 
ПК-15 ^ способность применять на практике современные методы педагогики и средства обучения 
ПК-16 ^ способность использования основ защиты производственного персонала и населения от возможных последствий аварий, катастроф, стихийных бедствий и применения современных средств поражения, основных мер по ликвидации их последствий, способность к общей оценке условий безопасности жизнедеятельности 
ПК-17 ^ способность реализации решений, направленных на поддержку социально-значимых проектов, на повышение электронной грамотности населения, обеспечения общедоступности информационных услуг 
ПК-18 ^ умение публично представить собственные и известные научные результаты 
ПК-19 ^ владение методом алгоритмического моделирования при анализе постановок прикладных задач 
ПК-20 ^ владение методами математического и алгоритмического моделирования при решении прикладных и инженерно-технических задач 
ПК-21 ^ умение грамотно использовать программные комплексы при решении задач механики 
ПК-22 ^ понимание того, что фундаментальное математическое знание является главным инструментом механики 
ПК-23 ^ владение методами математического и алгоритмического моделирования при решении задач механики 
ПК-24 ^ владение проблемно-задачной формой представления задач механики 
ПК-25 ^ владение методом физического моделирования при анализе проблем механики 
ПК-26 ^ владение проблемно-задачнойформойпредставленияматематических знаний 
ПК-27 ^ владение проблемно-задачной формой представления естественнонаучных знаний 
ПК-28 ^ умение самостоятельно математически корректно ставить инженерно-физические задачи 
ПК-29 ^ глубокое понимание роли экспериментальных исследований в механике 
ПК-30 ^ умение самостоятельно математически корректно ставить задачи механики 
ПК-31 ^ способность передавать результат проведенных физико-математических и прикладных исследований в виде конкретных рекомендаций, выраженных в терминах предметной области изучавшегося явления 
ПК-32 ^ умение точно представить фундаментальные знания в устной форме 
ПК-33 ^ владение основами педагогического мастерства 
ПК-34 ^ умение точно представлять математические знания в устной форме
ОПК-1 ^ Способность использовать основные законы естественнонаучных дисциплин в профессиональной деятельности, применять методы математического анализа и математического (компьютерного) моделирования, теоретического и экспериментального исследования
ОПК-2 ^ Способность выявить естественнонаучную сущность проблем, возникающих в ходе профессиональной деятельности, привлечь их для решения соответствующий физико-математический аппарат
ОПК-3 ^ Владение основными законами геометрического формирования, построения и взаимного пересечения моделей плоскости и пространства, необходимыми для выполнения и чтения чертежей зданий, сооружений, конструкций, составления конструкторской документации и деталей
ОПК-4 ^ Владение эффективными правилами, методами и средствами сбора, обмена, хранения и обработки информации, навыками работы с компьютером как средством управления информацией
ОПК-5 ^ Владение основными методами защиты производственного персонала и населения от возможных последствий аварий, катастроф, стихийных бедствий
ОПК-6 ^ Способность осуществлять поиск, хранение, обработку и анализ информации из различных источников и баз данных, представлять ее в требуемом формате с использованием информационных, компьютерных и сетевых технологий
ОПК-7 ^ Готовностью к работе в коллективе, способность осуществлять руководство коллективом, подготавливать документацию для создания системы менеджмента качества производственного подразделения
ОПК-8 ^ Умение использовать нормативные правовые документы в профессиональной деятельности
ОПК-9 ^ Владение одним из иностранных языков на уровне профессионального общения и письменного перевода"""


_in = """ОПК.3 ^ Способен разрабатывать алгоритмические и программные решения применяя математические модели, методы и современные средства проектирования информационных и автоматизированных систем; создавать информационные ресурсы прикладных баз данных, тестов и средств тестирования систем и средств на соответствие стандартам и исходным требованиям ^ Применяет теоретические методы анализа и средства информационного моделирования для теоретического и экспериментального исследования и дальнейшего проектирования информационных и автоматизированных систем
ОПК.5 ^ Способен инсталлировать и сопровождать программное обеспечение информационных систем и баз данных с учетом информационной безопасности ^ Выполняет инсталляцию и настройку программного обеспечения
ПК.2 ^ Способность выполнять работы и управлять работами по созданию (модификации) и сопровождению информационных систем автоматизирующих задачи организационного управления и бизнес-процессы ^ Выполняет работы по проектированию и сопровождению информационных систем; управляет работами по модификации и управлению ИТ-инфраструктурой
ПК.3 ^ Способность применять языки, системы и инструментальные средства программирования, работать с программными средствами прикладного, системного и специализированного назначения ^ Работает с программными средствами прикладного, системного и специализированного назначения
ПК.4 ^ Способность применять методы и технологии конфигурирования информационных систем, сетевых технологий и платформенных окружений ^ Использует методы и технологии конфигурирования информационных систем, сетевых технологий и платформенных окружений; этапы внедрения, адаптации и настройки информационных систем Выполняет адаптацию и локализует программное обеспечение, проводит сборку и администрирование информационной системы Исправляет дефекты и несоответствия установки, интеграции и настройки системного и прикладного программного обеспечения; выполняет комплекс работ сопровождения и реинжиниринга
ПК.1 ^ Способность взаимодействовать и сотрудничать с профессиональными сетевыми сообществами, отслеживать динамику развития выбранных направлений области информационных технологий ^  
ПК.12 ^ способность разрабатывать, оценивать и реализовывать процессы жизненного цикла информационных систем, программного обеспечения, сервисов информационных технологий, а также реализовывать методы и механизмы оценки и анализа функционирования средств информационных технологий  ^ """
competencies = {}
te = TermExtractor()
for line in _in.split("\n"):
    code, text, context = [ _.strip() for _ in line.split('^') ]
    terms = tuple([ str(t) for t in te(text + context) if str(t).count(" ") > 0 ])
    competencies.update({terms:{"code":code, "text":text}})