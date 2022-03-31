Аннотация генома по эпигенетическим состояниям была проведена для астроцитов NH-A (т.к. не было файлов для GM23248).

Все команды были выполнены в терминале linux. Текст этого - в папке proof. Скриншоты с разных стадий выполением задания - в папке screenshots. Вся выдача ChromHMM - в папке ChromHMM_out (за исключением NH-A_10_dense.bed, размер которого > 25 Мб).

Ниже представлен файл cellmarkfiletable.txt, переведённый в таблицу (с добавлением заголовков).

|Тип клеток|Метка|Файл с данными|Контроль| 
|---|---|---|---| 
|NH-A|H3k4me3|H3K4me3StdAlnRep1.bam|ControlStdAlnRep1.bam|
|NH-A|H3k4me1|H3K4me1StdAlnRep1.bam|ControlStdAlnRep1.bam|
|NH-A|H3k27ac|H3K27acStdAlnRep1.bam|ControlStdAlnRep1.bam|
|NH-A|H3k36me3|H3K36me3StdAlnRep1.bam|ControlStdAlnRep1.bam|
|NH-A|H3k27me3|H3K27me3StdAlnRep1.bam|ControlStdAlnRep1.bam|
|NH-A|H3k79me2|H3K79me2StdAlnRep1.bam|ControlStdAlnRep1.bam|
|NH-A|H3k9me3|H3K9me3StdAlnRep1.bam|ControlStdAlnRep1.bam|
|NH-A|H3k4me2|H3K4Me2StdAlnRep1.bam|ControlStdAlnRep1.bam|
|NH-A|H3k9ac|H3K9acStdAlnRep1.bam|ControlStdAlnRep1.bam|
|NH-A|H4k20me1|H4K20me1StdAlnRep1.bam|ControlStdAlnRep1.bam|

Определение паттернов состояний было основано на этих двух графиках:

![emissions_10](https://user-images.githubusercontent.com/60808642/161118736-35671ce5-560e-439a-b603-3a98419fbecc.png)
![NH-A_10_overlap](https://user-images.githubusercontent.com/60808642/161118743-e85be7c5-8053-42ee-a79f-d21066e7840d.png)

А также на основе локализации генов и гистоновых меток из UCSC Genome Browser:

![10](https://user-images.githubusercontent.com/60808642/161123041-3e5ecb6e-3b0c-4ac1-ac2d-7c43133d12b5.png)
