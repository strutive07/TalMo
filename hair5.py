import numpy
import random
import matplotlib.pyplot as plt


# 머리카락_개수 = 50000
머리카락_개수 = 500
테스트케이스_개수 = 100
머리다시안날확률 = 99



result = numpy.zeros((100, 300))
result2 = result.copy()



# 100살 산다고 가정할떄
# 1일씩 반복
# TC : 2만명


for 머리다시안날확률 in range(75, 101):
    title = "hair loss Percent : " + str(100 - 머리다시안날확률)
    print(title)
    for TC in range(0, 테스트케이스_개수):
        print("TC : ", TC)
        머리카락 = numpy.zeros((310, 머리카락_개수))


        cnt = numpy.zeros((1, 머리카락_개수))
        머리카락_자랄수있는_최대_횟수 = numpy.zeros((1, 머리카락_개수))

        #기저 사례. 처음 랜덤한 수명을 가진 머리카락들
        for j in range(0, 머리카락_개수 - 1):
            머리카락[0][j] = random.randrange(1, 5)
            머리카락_자랄수있는_최대_횟수[0][j] = random.randrange(15, 21)

        모낭 = 머리카락.copy()
        머리카락_나온_횟수 = cnt.copy()

        for i in range(1, 300):
            # print(i/3, " 살")

            # 5만개의 머리카락에 대해서
            정상머리카락개수 = 머리카락_개수

            for j in range(0, 머리카락_개수-2):
                # 머리카락이 20번 이상 자라면 더이상 못자람

                if(머리카락_나온_횟수[0][j] >= 머리카락_자랄수있는_최대_횟수[0][j]):
                    모낭[i][j] = -1
                if (머리카락_나온_횟수[0][j-1] >= 머리카락_자랄수있는_최대_횟수[0][j-1]):
                    모낭[i][j-1] = -1
                if (머리카락_나온_횟수[0][j+1] >= 머리카락_자랄수있는_최대_횟수[0][j+1]):
                    모낭[i][j+1] = -1
                if (머리카락_나온_횟수[0][j+2] >= 머리카락_자랄수있는_최대_횟수[0][j+2]):
                    모낭[i][j+2] = -1
                if (머리카락_나온_횟수[0][j-2] >= 머리카락_자랄수있는_최대_횟수[0][j-2]):
                    모낭[i][j-2] = -1

                if(모낭[i][j] == -1 and 모낭[i][j-1] == -1 and 모낭[i][j+1] == -1 and 모낭[i][j+2] == -1 and 모낭[i][j-2] == -1):
                    정상머리카락개수 = 정상머리카락개수 - 1
                else:
                    if(모낭[i][j] != -1):
                        모낭[i][j] = 모낭[i-1][j] + 0.2
                    if (모낭[i][j-1] != -1):
                        모낭[i][j-1] = 모낭[i - 1][j-1] + 0.2
                    if (모낭[i][j+1] != -1):
                        모낭[i][j+1] = 모낭[i - 1][j+1] + 0.2
                    if (모낭[i][j+2] != -1):
                        모낭[i][j+2] = 모낭[i - 1][j+2] + 0.2
                    if (모낭[i][j-2] != -1):
                        모낭[i][j-2] = 모낭[i - 1][j-2] + 0.2

                    if(모낭[i][j] >= 24):
                        percent = random.randrange(0, 101)
                        if(percent <= 20):
                            모낭[i][j] = 0;
                            머리카락_나온_횟수[0][j] = 머리카락_나온_횟수[0][j] + 1

                            TALMOpercent = random.randrange(0, 101)
                            if(TALMOpercent >= 머리다시안날확률):
                                모낭[i][j] = -1;
                                머리카락_나온_횟수[0][j] = 30

                    if (모낭[i][j-1] >= 24):
                        percent = random.randrange(0, 101)
                        if (percent <= 20):
                            모낭[i][j-1] = 0;
                            머리카락_나온_횟수[0][j-1] = 머리카락_나온_횟수[0][j-1] + 1

                            TALMOpercent = random.randrange(0, 101)
                            if (TALMOpercent >= 머리다시안날확률):
                                모낭[i][j-1] = -1;
                                머리카락_나온_횟수[0][j-1] = 30

                    if (모낭[i][j+1] >= 24):
                        percent = random.randrange(0, 101)
                        if (percent <= 20):
                            모낭[i][j+1] = 0;
                            머리카락_나온_횟수[0][j+1] = 머리카락_나온_횟수[0][j+1] + 1

                            TALMOpercent = random.randrange(0, 101)
                            if (TALMOpercent >= 머리다시안날확률):
                                모낭[i][j+1] = -1;
                                머리카락_나온_횟수[0][j+1] = 30

                    if (모낭[i][j+2] >= 24):
                        percent = random.randrange(0, 101)
                        if (percent <= 20):
                            모낭[i][j+2] = 0;
                            머리카락_나온_횟수[0][j+2] = 머리카락_나온_횟수[0][j+2] + 1

                            TALMOpercent = random.randrange(0, 101)
                            if (TALMOpercent >= 머리다시안날확률):
                                모낭[i][j+2] = -1;
                                머리카락_나온_횟수[0][j+2] = 30

                    if (모낭[i][j-2] >= 24):
                        percent = random.randrange(0, 101)
                        if (percent <= 20):
                            모낭[i][j-2] = 0;
                            머리카락_나온_횟수[0][j-2] = 머리카락_나온_횟수[0][j-2] + 1

                            TALMOpercent = random.randrange(0, 101)
                            if (TALMOpercent >= 머리다시안날확률):
                                모낭[i][j-2] = -1;
                                머리카락_나온_횟수[0][j-2] = 30

                if(cnt[0][j] >= 머리카락_자랄수있는_최대_횟수[0][j]):
                    머리카락[i][j] = -1
                else:
                    #머리카락 자라기
                    머리카락[i][j] = 머리카락[i - 1][j] + 1
                    if 머리카락[i][j] >= 28:
                        머리카락[i][j] = 0
                        cnt[0][j] = cnt[0][j] + 1
                if(머리카락[i-1][j] >= 24):
                    percent = random.randrange(0,101)
                    if(percent >= 80):
                        머리카락[i][j] = 0
                        cnt[0][j] = cnt[0][j] + 1
                        TalMo_Percent = random.randrange(0,101)
                        if(TalMo_Percent >= 머리다시안날확률):
                            cnt[0][j] = 30
            talmo_cnt = 0
            for k in 머리카락[i]:
                if(k != -1):
                    talmo_cnt = talmo_cnt + 1

            result[머리다시안날확률][i] = result[머리다시안날확률][i] + talmo_cnt


            result2[머리다시안날확률][i] = result2[머리다시안날확률][i] + 정상머리카락개수
            # print("정상 모공 개수 : ", result[머리다시안날확률][i])

    x_result = []
    for i in range(0, 300):
        result[머리다시안날확률][i] = result[머리다시안날확률][i] / 테스트케이스_개수
        result2[머리다시안날확률][i] = result2[머리다시안날확률][i] / 테스트케이스_개수
        x_result.append(i)

    plt.plot(x_result, result[머리다시안날확률], x_result, result2[머리다시안날확률])

    plt.title(title)
    xlabel = "Normal hair cnt"
    ylabel = "age * 3"
    plt.xlabel(ylabel)
    plt.ylabel(xlabel)
    filename = "Percent" + str(100 - 머리다시안날확률) + ".png"
    plt.savefig(filename)
    plt.show()








