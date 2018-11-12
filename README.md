## The Cancer Genome Atlas (TCGA) Cancer Data Analysis and Prediction

The Cancer Genome Atlas (TCGA) is a project where the raw cancer genomic data is gathered from
different research institutes. However, it is difficult to understand and analyze these data. Therefore,
the goal of this research project is to use machine learning and data mining techniques to interpret
these data, so it can be accessible to any research group. In order to do this research, data inspection
was been performed. The data comprises 9,037 patients from 36 different types of cancers.
However, while scrutinizing the data set, it has been detected that some patients’ data overlapped
among some tumors. Moreover, another interesting feature has been identified - some tumors are
clustered together and formed new classes. Based on the preliminary data analysis, 22255 mutated
genes were identified which were mutated in 22 different ways. Initially, 1357856 mutations has
been detected for 9,037 patients for 36 cancer types; but after removing the duplicate patients from
9 different tumors, the number of mutations were reduced to 1068351 for 7120 unique patients of
27 tumor types. Through the overall process, the “Silent” mutation has been overlooked. During the
descriptive mining phase, the presence of most frequent genes in each tumor has been identified.
Also, the presence of these genes in other 26 different types of tumors has been correlated.
Furthermore, the most frequent genes in all 27 tumors have been identified. Further analysis was
continued in the predictive mining stage, where different machine-learning algorithms were applied
which included: Naive Bayes classifier, Decision Trees (J48), Rule-based classification (PART) and
Multiclass approach (27-class based classification). Using these algorithms, it has been evaluated
that Naïve Bayes classifier is very effective which accuracy rate was 50.4287 %, and the Multiclass
approach classification performs least with 41.04% accuracy rate. All prediction tasks have been
accomplished by using Waikato Environment for Knowledge Analysis (Weka version-3.8.0).
