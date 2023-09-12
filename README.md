# Annotation of the human genome into different types of epigenetic states.

[This README in russian](README.ru.md)

The annotation was done based on histone modifications data.  
This data was taken from the [ENCODE project](https://www.encodeproject.org/).  
So, reads obtained from ChIP-seq experiments were aligned to the human genome (version hg19).  
And the resulting .bam files were taken for this annotation.

Automatic annotation of the genome into epigenetic types was carried out using the ChromHMM program.
As a result of the iterative procedure (Baum-Welsh algorithm), the program determines the combination of histone marks that are typical for each of the N different epigenetic types.
The biological aim of this annotation was to manually assign a possible biological function to each of the N epigenetic types based on indirect independent observations.

The annotation by type was performed for NH-A astrocytes (as there were no files for GM23248).

All commands were executed in the Linux terminal.  
The text of this is in the proof folder.  
Screenshots from different stages of the task are in the screenshots folder.  
All ChromHMM output is in the ChromHMM_out folder (with the exception of NH-A_10_dense.bed, the size of which is > 25 MB).

Below is the cellmarkfiletable.txt file with headers added.

|Cell type|Histone mark|Data file|Control| 
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

The definition of state patterns was based on these two graphs:

![emissions_10](https://user-images.githubusercontent.com/60808642/161118736-35671ce5-560e-439a-b603-3a98419fbecc.png)
![NH-A_10_overlap](https://user-images.githubusercontent.com/60808642/161118743-e85be7c5-8053-42ee-a79f-d21066e7840d.png)

As well as using gene localization and histone marks from the UCSC Genome Browser:

![10](https://user-images.githubusercontent.com/60808642/161123041-3e5ecb6e-3b0c-4ac1-ac2d-7c43133d12b5.png)

|Type|Typical marks|Typical features|Label| 
|---|---|---|---| 
|1|H3k9me3, H3k27me3, H3k4me2|CpG islands, reference exons, transcription termination reference sites, nuclear lamina associated domains|Weak promoter|
|2|-|A significant part of the genome, nuclear lamina associated domains|Repressed heterochromatin|
|3|H3k20me1, H3k36me3|Reference genes, transcription termination reference sites|Transcription start regions|
|4|H3k79me2, H4k20me1, H3k36me3|Reference exons, reference genes, transcription termination reference sites|Transcription elongation region|
|5|H3k79me2, H4k20me1|Reference genes|Regions repressed by polycomb proteins|
|6|H3k79me2|Reference genes|Introns|
|7|H3k4me3, H3k9ac, H3k4me2, H3k27a, H3k4me1, H3k79me2, H4k20me1|Reference exons, reference genes, transcription termination reference sites, regions spaced 2 kilobases from transcription start sites|Strong enhancer|
|8|H3k4me2, H3k4me1|Transcription termination reference sites, nuclear lamina associated domains|Weak enhancer|
|9|H3k9ac, H3k4me2, H3k27ac, H3k4me1|Reference genes, transcription termination reference sites, nuclear lamina associated domains|Insulator|
|10|H3k4me3, H3k9ac, H3k4me2|CpG islands, reference exons, reference genes, transcription termination reference sites, transcription start reference sites, regions spaced 2 kilobases from transcription start sites|Active promoter|

To modify the .bed file and display these types, a script was written in python (src folder). Unfortunately, the resulting .bed file is still too large, so there is only a screenshot of it.

The resulting diagram in the UCSC Genome browser looks like:

![13](https://user-images.githubusercontent.com/60808642/161148019-f6395f2f-aff2-4992-a88f-4d478fe423ee.png)
