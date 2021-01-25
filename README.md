# Лаборатория Django-разработки от школы Thinknetica

Приветствуем вас в Лаборатории Django-разработки. Это ваш репозиторий, в котором вы будете работать над проектом.

# Проект

### Выбранный проект - Аренда и покупка недвижимости

Во время Лаборатории вы будете работать над проектом маркетплейса, тематику вы можете выбрать сами из этого списка:

- Торговая площадка, где поставщики продают свои товары конечным клиентам (примеры: [ozon.ru](http://ozon.ru/) или [amazon.com](http://amazon.com/))
- Сайт объявлений (пример: [avito.ru](http://avito.ru/))
- Сайт поиска работы (пример: [hh.ru](http://hh.ru/))
- Аренда и покупка недвижимости (примеры: [Cian.ru](http://cian.ru/) или [AirBnB.com](http://airbnb.com/))
- Бронирование отелей (пример: [booking.com](http://booking.com/))

Задачи в проекте у вас будут ставиться универсальные, подходящие под
любую из выбранных тематик, но в некоторых случаях вам нужно будет
выбирать более подходящие названия сущностей. Например, для торгового
маркетплейса для описания сущности товара вполне подойдет название Goods
(товар), а для сайта поиска работы, это уже будет Vacancy (вакансия) и
т.п.

**Выбранную тематику вашего маркетплейса нужно указать в вашем репозитории, добавив информацию об этом в секцию About вашего репозитория (нажать на шестеренку и заполнить поле Description).**

Мы будем работать в условиях приближенных к реальной разработке, поэтому в качестве трекера мы будем использовать Github и его фичи, такие как issues, pull requests и projects. Это то, с чем вам придется сталкиваться в реальной разработке практически ежедневно.

Для каждого участника мы уже подготовили и настроили отдельный репозиторий. Давайте подробнее разберемся, что там есть и как с этим работать.

# Задачи (Issues)

Все задачи, которые вам нужно будет сделать, оформляются как issues на Github. Вы можете посмотреть их на вкладке Issues своего репозитория, но большую часть времени вы будете работать через Project Board (вкладка Projects), где задачи представлены в более удобном и наглядном виде (об этом ниже).

![Issues__thinknetica_test_student_repo.png](https://user-images.githubusercontent.com/968537/104715110-2295ea00-5737-11eb-9b61-34832b969f03.png)

Все задачи в рамках проекта объединены в тематические модули, которые на гитхабе представлены в виде milestones.

Всего в проекте 14 модулей, по 2 модуля на каждую неделю. Сейчас вы можете увидеть задачи на первую неделю (т.е. 2 первых milestones или модуля), каждый понедельник у вас в репозитории будут **автоматически** появляться задачи на новую неделю.

Каждая задача имеет метку вида 1.1, 1.2 и т.д., где первая цифра - номер модуля (milestone), а вторая - порядковый номер задачи в модуле.

**Важно! Задачи нужно выполнять последовательно, согласно нумерации, т.к. они зависят друг от друга!**

Вы можете посмотреть список завершенных и доступных модулей на вкладке milestones, там же можно видеть прогресс по каждому модулю и задачи внутри конкретного модуля.

# Projects

Задачи удобнее смотреть не через вкладку Issues, а через вкладку Projects, там уже есть подготовленный проект. Здесь же вы увидите список задач и этапы работы над ними:

![Django_Lab_01.png](https://user-images.githubusercontent.com/968537/104715642-dac39280-5737-11eb-8e9f-7b262c90afb0.png)

В проекте есть несколько колонок:

- **ToDo** - сюда попадают все вновь добавленные задачи. Обратите внимание, что задачи здесь не упорядочены, поэтому при их выполнении, ориентируйтесь на метки задач. Нажав на название задачи вы можете ознакомиться с ее описанием и материалами для выполнения. Здесь задачи будут появляться автоматически каждую неделю.
- **In Progress** - как только вы начинаете работать над задачей, перетащите ее в эту колонку из колонки ToDo
- **Review in progress** - здесь вы видите список Pull Requests (скоращенно PR, это ваш код, оформленный для проверки наставником), ожидающего проверки наставника, а также PR для которых наставник оставил комментарии и запросил изменения в коде. Сюда задачи попадают автоматически, когда вы запрашиваете проверку вашего PR. Пока задача на проверке, вы можете взять в работу следующую задачу из ToDo.
- **Reviewer approved** - cюда попадают те PR, которые принял наставник. Это значит, что вы можете сливать PR в основную ветку (делать merge). При слиянии PR в основную ветку, этот PR автоматически закрывается и попадает в следующую колонку.
- **Done** - сюда попадают закрытые (завершенные) задачи и PR. Если PR и задача связаны (см. ниже), то при слиянии PR с основной веткой проекта, задача и PR закроются автоматически и сразу попадут в эту колонку.

Большая часть действий по переносу задач и PR между колонками автоматизирована средствами гитхаба, но чтобы это правильно работало, нужно правильно оформлять Pull Requests  и следовать четкому процессу (который, кстати, такой же, как в реальной разработке).

# Процесс работы над проектом

## Первые шаги

Прежде всего, вам нужно склонировать ваш репозиторий на локальную машину, где вы будете вести разработку.

Это делается командой  git clone  с указанием адреса вашего репозитория, например:

```jsx
git clone git@github.com:thinknetica/test_student_repo.git
```

Далее разработку вы будете вести внутри той директории, куда склонировали проект.

## Работа над задачей и сдача на проверку

1. Вы берете задачу в работу из колонки ToDo и перетаскиваете ее в колонку In Progress, что означает, что вы взяли ее в работу.  **Важно!**  **Выполняйте задачи последовательно, в соответствии с  номером лейбла** (например, 1.1, 1.2 и т.д.).

    ![Django_Lab_01%201.png](https://user-images.githubusercontent.com/968537/104715736-f9c22480-5737-11eb-8f34-87064afddc92.png)

2. Локально, в директории с проектом, создайте ветку для работы над задачей. **Для каждой задачи - отдельная ветка!** Это делается командой `git checkout -b <branch name>` Например:

    ```bash
    git checkout -b 1_2_edit_static_pages
    ```

    **В имени ветки указывайте порядковый номер задачи, в соответствии с лейблом**, также рекомендуется указать имя, соответствующее сути задачи, можно кратко.

3. Выполняете работу над задачей в этой ветке. В процессе старайтесь делать больше коммитов. В процессе работы, а также в конце работы над задачей, старайтесь протестировать работу выполненной фичи вручную (даже при наличии автотестов).

    **Не сдавайте незаконченную задачу или задачу с багами!**

4. Когда вы закончили работу над задачей и планируете сдать ее на проверку, вам нужно отправить ветку с задачей на гитхаб командой `git push -u origin <branch name>` Например:

    ```bash
    git push -u origin 1_2_edit_static_pages
    ```

    Флаг `-u` означает, что у вас создается связь между локальной и удаленной ветками и если вам нужно будет внести изменения в локальной ветке и снова их отправить в репозиторий в удаленную ветку, достаточно будет выполнить просто `git push`, без дополнительных параметров.

5. Далее, вам нужно создать Pull Request через интерфейс на Github, для этого:
    1. Заходите во вкладку Pull Requests:
    2. Нажимаете кнопку "New Pull Request"
    3. Выбираете ветки для создания PR. В `base` у вас всегда `main`, в `compare`выбираете ветку с кодом задачи
    4. Нажимаете Create Pull Request

        ![Comparing_main___1_1_basic_template__thinknetica_test_student_repo.png](https://user-images.githubusercontent.com/968537/104715849-21b18800-5738-11eb-95b7-741e29117ddd.png)

6. Теперь нужно правильно оформить PR, чтобы он связался с задачей и проектом, а также назначить проверяющего (Reviewer). Для этого нужно при создании PR указать:

1. В описании PR написать "Closes #<номер issue>", например, Closes #2 или Closes #5. **Обратите внимание: указывать нужно номер issue, а не номер label**. Номер issue можно всегда посмотреть в списке issues. Альтернативный вариант: выбрать нужный issue в меню справа в разделе Linked issues
2. В меню справа в разделе Reviewers выбрать вашего наставника (если этого не сделать, он не увидит ваше задание на проверке)
3. В том же меню в разделе Project выбрать проект (в списке только один проект, так что выбрать нужно его).
4. После всего этого нажать на кнопку Create Pull Request

![Comparing_main___second_branch__thinknetica_test_student_repo.png](https://user-images.githubusercontent.com/968537/104715983-486fbe80-5738-11eb-8905-eba5640a487c.png)

7. Если вы все сделали правильно, то задача попадет на проверку наставнику, а внутри проекта на гитхабе, этот PR будет также отображаться в колонке "Review in progress" с меткой "on review" (**метка** **добавляется автоматически, но это может занять до пары минут**), что означает, что PR ожидает проверки наставником. При этом, вы должны увидеть, что сама задача(issue) связана с этим PR, о чем будет гласить подпись под карточкой задачи:

![Django_Lab_01%202.png](https://user-images.githubusercontent.com/968537/104716116-7fde6b00-5738-11eb-8523-9639a2a02c22.png)

**По наличию/отсутствию метки "on review" можно понимать, ожидает PR проверки или уже проверен**

## Проверка кода и внесение исправлений

После того, как вы сдали PR на проверку, наставник проведет code review в течение 48 часов (возможно, гораздо быстрее, это максимальный срок).

Если наставник отклонил ваш PR, то вы увидите карточку с PR в колонке Review in progress с пометкой "Сhanges requestes", при этом исчезнет метка "on review", что означает, что наставник завершил проверку. Также вам придет уведомление на почту и на гитхабе о том, что запрошены изменения.

![Django_Lab_01%203.png](https://user-images.githubusercontent.com/968537/104716172-997fb280-5738-11eb-9723-2f57bd08226a.png)

В этом случае вам нужно зайти в PR и прочитать комментарии наставника, вы также можете задать вопросы в комментариях к PR.

Далее вам нужно внести изменения, согласно этим замечаниям.

**Чтобы внести изменения нужно сделать следующее:**

1. Локально переключиться в ветку с нужной задачей
2. Внести необходимые исправления в код, обязательно закоммитить их (коммитов может быть несколько)
3. Сделать пуш изменений на Github командой `git push`
4. Зайти в тот же самый PR (**Важно! Новый PR создавать НЕ нужно, существующий PR "подхватит" все изменения**), что был отклонен и повторно запросить проверку  у наставника, нажав на кнопку c двумя стрелками справа от его имени:

    ![Pull_Request__7__thinknetica_test_student_repo.png](https://user-images.githubusercontent.com/968537/104716242-b5835400-5738-11eb-9e5b-cdd8c0515191.png)

После этих действий, PR вновь попадет на проверку наставнику, при этом в проекте PR останется также в колонке Review in Progress, но у него вновь добавится метка "on review".

**Если наставник принял ваш PR**, то он окажется в колонке Reviewer approved (сама задача будет по-прежнему в колонке In Progress) и у него появится подпись "Changes approved":

![Django_Lab_01%204.png](https://user-images.githubusercontent.com/968537/104716284-cc29ab00-5738-11eb-9ced-069175cbf9f2.png)

**После этого, вам нужно слить эту ветку в основную ветку**. Это можно сделать двумя способами:

1. Локально командой git merge (не забудьте после этого сделать git push в основную ветку репозитория)
2. Через интерфейс PR, нажав на зеленую кнопку "Merge Pull Request" (будет доступна, если нет конфликтов и Github может выполнить автоматическое слияние).

После того, как PR (ветка) будут слиты, PR и связанная с ним задача (issue) автоматически закроются и попадут в колонку Done:

![Django_Lab_01%205.png](https://user-images.githubusercontent.com/968537/104716334-de0b4e00-5738-11eb-8980-160b7554ddbf.png)

Теперь можно приступать к следующей задаче и повторить весь процесс.