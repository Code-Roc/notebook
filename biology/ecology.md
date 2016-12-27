#��̬���ݴ���ʹ��QIIME

# ��ҵҪ��

1. De-novo OTU picking�Լ�OTU table������
2. alpha�����Է�����������(>5%/10%)��Relative Abundance�ֲ�ͼ��Rarefaction Curve( Shannon, Simpson, Observed species)
3. beta�����Է����� Unweighted/Weighted Unifrac PCoA����
4. Ⱥ���Է�����NMDS����--R
   ���������Adonis��ANOSIM��MRPP��--R

----

# ������� Obtaining the data

��Ⱥ�������ص������ļ�����飺

## BF_Map.txt 5.10KB

���Ƕ�ԭʼ����fna�ļ�����������ԭʼ����

|SampleID|BarcodeSequence|LinkerPrimerSequence|Treatment|Plate|Description|
| --------   | -----:  | :----:  |
|����ID|������������������|����ʱ���ϵ�����|�����Ĵ���Control��Warming||��������TagA,TagB,TagC|

## otu_table_F.txt 23.9MB

OTU������������ѧ������Ϊ����ķ��൥λ

����ó���OTU Table

ÿ��һ��OTU�����ƥ�䵽���ݿ�����΢��������ַ������ݣ��Լ�ÿ�������Ƿ�������OTU--����Ϊ1��������Ϊ0

## otus_BF.rar 36.7MB

�ں�otus_BF�ļ��У�Ϊ**De novo OTU picking**��������ɽ��

# ��ͷ��ʼ��OTU��װ De novo OTU picking

����ȱ��ԭʼ�ļ����������޷����֣�������Ϊ������otus_BF.rar

�˲���������**rep_set.tre**��ʹ��**FigTree**������в鿴��

![](http://api.chenyuan.me/fangcloud/4cf9ea4acb452aa8e0df0fe0fd)

## �鿴������OTU Table

[summarize.txt](http://api.chenyuan.me/fangcloud/9c76ee31266efbf411e51c8388)

һ����50�����������ո�����ԭʼBF_Map.txt��72����������
�������е�F.TagA.3C.12��F.TagA.3C.13��Count��̫С���Ժ��ԣ��Ƚ������ļ�����**IDΪTagA�Ķ�û�г����ڸ�����OTU Table��**

����Point:��Excel�Ƚ�������ͬԪ��http://jingyan.baidu.com/article/c843ea0b7a2a7477921e4a47.html

## Make an OTU network

�˼�˵Ҫ��Cytoscape���д��о�

���ɵ�otu_network�ļ���[����������](http://api.chenyuan.me/fangcloud/a8c63020d9a7d1426cf05a7a77)


# ���ַ���ͳ�� Summarize communities by taxonomic composition

[���ɵ�taxa_summary�ļ���,��������](http://api.chenyuan.me/fangcloud/cff3d489af54eaea157838719c)

> �������ص�

��taxa_summary/taxa_summary_plots�ļ��У�������������ҳ��

��ҳ�򿪺�5��ͼ��ÿ��ͼ�ĺ����궼��50�����������ϵ��·����ԪԽ��Խϸ

ѡ����߲�ε�����barͼ�ɣ�

![](http://api.chenyuan.me/fangcloud/312423426ec71e733de254fbfe)

��ѹѹ���������ҳ������긧������ͼ���Կ���������Ϣ

���º�ɫ�����ģ���Other

������Ŀ��������ϱߵĺ�ɫ�ģ�Proteobacteria

## ������ͼMake a taxonomy heatmap

![](http://api.chenyuan.me/fangcloud/c8d28241ed373bd3901a2d848a)

----

#����alpha������

[���ɵ�arare�ļ��д�������](http://api.chenyuan.me/fangcloud/c07dc497e5679ca505967eb9a5)

alpha�����Եļ�������arare/alpha_div_collated�У�������

* shannon.txt
* simpson.txt
* observed_otus.txt �����PPTҪ���Observed species

ÿһ����һ������

ÿһ������ȡ����С+����������

> rarefaction_##_#.txt: the first set of numbers represents the number of sequences sampled, and the last number represents the iteration number

�ò�ͬ�Ĳ�����С���Եõ���ͬ����ֵ���Ϳ��Ի���������Щͼ

## ��alphaϡ��ͼ

�����˽����Ǹ�ʲô���� [Wikipedia](https://en.wikipedia.org/wiki/Rarefaction_(ecology))

![shannon.png](http://api.chenyuan.me/fangcloud/f4be696682a9f7941f7f0afd64)

![simpson.png](http://api.chenyuan.me/fangcloud/69404575b5438324d08f0dbc0f)

![observed_otus.png](http://api.chenyuan.me/fangcloud/30bad21c580339cc18fb44a299)


���⣺���ʹ��Category:Treatment, �����Ϻܶ�NaN����������ͬ����������Բ���

----

# ����beta������ Compute beta diversity and generate ordination plots

[bdiv_even146.zip��������](http://api.chenyuan.me/fangcloud/ba56a4a459ee7238a8af6c3d3b)

## Unweighted

> ��ɫControl
> ��ɫWarming

![unweighted1.jpg](http://api.chenyuan.me/fangcloud/8c4f7c22f6db3f0a54151c01e4)

![unweighted2.jpg](http://api.chenyuan.me/fangcloud/95708ac65084d85de8a76e517c)

Treatment��û������������

��ʲô���������������أ�

�ֹ�������ɫ��

��ɫ TagC_13
��ɫ TagB_13
��ɫ TagC_12
��ɫ TagB_12

![unweighted_my.jpg](http://api.chenyuan.me/fangcloud/6ff9f674acdb65c53e1cf08021)

����**�������ı��12��13������������������Դ**��

## Weighted

![weighted.jpg](http://api.chenyuan.me/fangcloud/06dcc48950634f7915733ed093)

ͬ����Treatment��û�������Բ���