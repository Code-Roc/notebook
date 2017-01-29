/*
 * ������������������޹ص�Special Judge���룬����OnlineJudge
 * ԭ��Ϊ�ѱ�׼��д������У��Ȱѱ�׼�𰸺��û��𰸶�qsort����������бȽ�
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define AC 0
#define WA 1
#define ERROR -1

#define LINES 100 //��һ����100��
#define LINELEN 15 //���������ֵ�Դ���ÿ�������
char truelines[][LINELEN]={/*�����Ǳ�׼�𰸣�˳���޹أ�һ��LINES�У�ÿ���LINELEN-1���ַ�*/}

int compare(const void* a,const void* b){
	return strcmp((const char*)a,(const char*)b);
}

int spj(FILE *input, FILE *user_output);

void close_file(FILE *f){
    if(f != NULL){
        fclose(f);
    }
}

int main(int argc, char *args[]){
    FILE *input = NULL, *user_output = NULL;
    int result;
    if(argc != 3){
        printf("Usage: spj x.in x.out\n");
        return ERROR;
    }
    input = fopen(args[1], "r");
    user_output = fopen(args[2], "r");
    if(input == NULL || user_output == NULL){
        printf("Failed to open output file\n");
        close_file(input);
        close_file(user_output);
        return ERROR;
    }
    result = spj(input, user_output);
    printf("result: %d\n", result);
    close_file(input);
    close_file(user_output);
    return result;
}
int spj(FILE *input, FILE *user_output){
    /*����û��𰸴��󣬷���WA�����򷵻�AC*/
	int i;char *tmp,userlines[LINES][LINELEN];
	for(i=0;i<LINES;i++){
		tmp=fgets(userlines[i],LINELEN,user_output);
		userlines[i][strlen(userlines[i])-1]=0;//fgets��õ�\n����Ҫɾ��
	}
	qsort(truelines,LINES,LINELEN,compare);
	qsort(userlines,LINES,LINELEN,compare);
	for(i=0;i<LINES;i++){
		//printf("%s,%s\n",truelines[i],userlines[i]);
		if(strcmp(truelines[i],userlines[i])!=0) return WA;
	}
	return AC;
}

